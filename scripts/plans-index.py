#!/usr/bin/env python3
"""Generate .ai/plans/INDEX.md from front matter of all plan files."""
import re
from pathlib import Path


def parse_fm(text):
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ':' in line and not line.startswith(' '):
            k, v = line.split(':', 1)
            out[k.strip()] = v.strip()
    return out


def main():
    plans_dir = Path('.ai/plans')
    plans = sorted([
        p for p in plans_dir.glob('*.md')
        if not any(p.name.endswith(s) for s in
                   ('.brief.md', '.review.md', '.redteam.md'))
        and p.name != 'INDEX.md'
    ])
    rows = []
    for p in plans:
        fm = parse_fm(p.read_text())
        rows.append({
            'id': fm.get('id', '?'),
            'slug': fm.get('slug', p.stem),
            'status': fm.get('status', '?'),
            'tier': fm.get('tier', '?'),
            'phase': f"{fm.get('current_phase', '?')}/{fm.get('total_phases', '?')}",
        })
    out = ['# Plans Index', '',
           '| ID | Slug | Status | Tier | Phase |',
           '|----|------|--------|------|-------|']
    for r in rows:
        out.append(f"| {r['id']} | {r['slug']} | {r['status']} | {r['tier']} | {r['phase']} |")
    (plans_dir / 'INDEX.md').write_text('\n'.join(out) + '\n')
    print(f"Wrote INDEX.md with {len(rows)} plans.")


if __name__ == '__main__':
    main()
