#!/usr/bin/env python3
"""Check that the git diff stays within a phase's allowed scope.

Usage: python deviation-check.py <plan_id> <phase_num>
Exits 1 if files outside scope are touched.
"""
import re
import subprocess
import sys
from pathlib import Path


def parse_front_matter(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return m.group(1) if m else ""


def get_modules_touched(fm):
    paths = []
    in_block = False
    for line in fm.splitlines():
        if re.match(r'^modules_touched\s*:', line):
            in_block = True
            continue
        if in_block:
            m = re.match(r'^\s+-\s+(.+?)\s*$', line)
            if m:
                paths.append(m.group(1))
            elif line.strip() and not line.startswith(' '):
                break
    return paths


def get_phase_files(text, phase_num):
    pattern = rf'###\s+Phase\s+{phase_num}\b.*?(?=\n###|\n##\s|\Z)'
    m = re.search(pattern, text, re.DOTALL)
    if not m:
        return []
    section = m.group(0)
    paths = []
    in_block = False
    for line in section.splitlines():
        if re.match(r'\s*-?\s*files_allowed\s*:', line):
            in_block = True
            continue
        if in_block:
            mm = re.match(r'\s+-\s+(.+?)\s*$', line)
            if mm:
                paths.append(mm.group(1))
            elif line.strip() and not re.match(r'\s+-', line):
                break
    return paths


def is_within(file, allowed):
    for a in allowed:
        a_norm = a.rstrip('/')
        if file == a_norm or file.startswith(a_norm + '/'):
            return True
        # glob-ish match for trailing /*
        if a.endswith('/*') and file.startswith(a[:-1]):
            return True
    return False


def main():
    if len(sys.argv) != 3:
        print("Usage: deviation-check.py <plan_id> <phase_num>")
        sys.exit(2)
    plan_id, phase_num = sys.argv[1], int(sys.argv[2])
    plans_dir = Path('.ai/plans')
    candidates = [
        p for p in plans_dir.glob(f'{plan_id}-*.md')
        if not any(p.name.endswith(s) for s in
                   ('.brief.md', '.review.md', '.redteam.md'))
    ]
    if not candidates:
        print(f"No plan found for id {plan_id}")
        sys.exit(1)
    plan = candidates[0]
    text = plan.read_text()
    fm = parse_front_matter(text)
    allowed = get_modules_touched(fm) + get_phase_files(text, phase_num)
    if not allowed:
        print("WARN: no files_allowed or modules_touched found")
    base = subprocess.check_output(
        ['git', 'merge-base', 'HEAD', 'main']).decode().strip()
    diff = subprocess.check_output(
        ['git', 'diff', '--name-only', f'{base}...HEAD']).decode().splitlines()
    violations = [f for f in diff if f and not is_within(f, allowed)]
    if violations:
        print("DEVIATIONS:")
        for v in violations:
            print(f"  - {v}")
        sys.exit(1)
    print(f"OK: {len(diff)} files changed, all within scope.")


if __name__ == '__main__':
    main()
