#!/usr/bin/env python3
"""Detect module-level overlap between active plans."""
import re
from collections import defaultdict
from pathlib import Path

ACTIVE = {'approved', 'executing', 'review', 'in-review'}


def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    return m.group(1) if m else ""


def modules(fm):
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


def get(fm, key):
    m = re.search(rf'^{key}\s*:\s*(.+?)$', fm, re.MULTILINE)
    return m.group(1).strip() if m else None


def main():
    plans = [
        p for p in Path('.ai/plans').glob('*.md')
        if not any(p.name.endswith(s) for s in
                   ('.brief.md', '.review.md', '.redteam.md'))
        and p.name != 'INDEX.md'
    ]
    by_module = defaultdict(list)
    for p in plans:
        fm = parse_fm(p.read_text())
        status = get(fm, 'status')
        if status not in ACTIVE:
            continue
        pid = get(fm, 'id') or p.stem
        for m in modules(fm):
            by_module[m].append(pid)
    overlaps = {m: ids for m, ids in by_module.items() if len(ids) > 1}
    if not overlaps:
        print("No overlaps among active plans.")
        return
    print("OVERLAPS:")
    for m, ids in overlaps.items():
        print(f"  {m}: plans {', '.join(ids)}")


if __name__ == '__main__':
    main()
