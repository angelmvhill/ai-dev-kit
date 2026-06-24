#!/usr/bin/env python3
"""Bootstrap ai-dev-kit in a project repository.

Usage:
  python init_project.py --project-root PATH --project-name NAME \\
      [--kit-version v0.2.0] [--kit-url URL] [--dry-run] [--force-rule]

Attaches the kit as .ai/kit (git submodule or local junction when AI_DEV_KIT_LOCAL
is set), scaffolds .ai/ artifacts from templates, and writes a Cursor workflow rule.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_KIT_URL = "https://github.com/angelmvhill/ai-dev-kit.git"
DEFAULT_KIT_VERSION = "v0.2.0"
AI_DIRS = ("overrides", "notes", "briefs", "plans", "reviews")
TEMPLATE_MAP = {
    "project.template.md": "PROJECT.md",
    "state.template.md": "STATE.md",
    "followups.template.md": "FOLLOWUPS.md",
}
STUB_FILES = {
    "JOURNAL.md": "# Journal\n",
    "DECISIONS.md": "# Decisions\n",
    "CONVENTIONS.md": (
        "# Project conventions\n\n"
        "Extends `.ai/kit/CONVENTIONS.md`. Add project-local overrides here.\n"
    ),
}


def run(cmd: list[str], *, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise RuntimeError(
            f"Command failed ({result.returncode}): {' '.join(cmd)}\n"
            f"stdout: {result.stdout.strip()}\nstderr: {result.stderr.strip()}"
        )
    return result


def is_git_repo(path: Path) -> bool:
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--git-dir"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def read_kit_version(changelog: Path) -> str:
    if not changelog.is_file():
        return "unknown"
    match = re.search(r"^## v(\d+\.\d+\.\d+)", changelog.read_text(encoding="utf-8"), re.MULTILINE)
    return match.group(1) if match else "unknown"


def resolve_rule_template(explicit: Path | None) -> Path:
    if explicit is not None:
        if not explicit.is_file():
            raise FileNotFoundError(f"Rule template not found: {explicit}")
        return explicit
    candidates = [
        Path(__file__).resolve().parent.parent / "templates" / "ai-dev-kit-workflow.mdc.template",
        Path(__file__).resolve().parent / ".." / "templates" / "ai-dev-kit-workflow.mdc.template",
    ]
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved.is_file():
            return resolved
    raise FileNotFoundError("Could not locate ai-dev-kit-workflow.mdc.template")


def create_junction(link: Path, target: Path) -> None:
    link.parent.mkdir(parents=True, exist_ok=True)
    if link.exists() or link.is_symlink():
        return
    if sys.platform == "win32":
        run(["cmd", "/c", "mklink", "/J", str(link), str(target)])
    else:
        link.symlink_to(target, target_is_directory=True)


def attach_kit_local(ai_root: Path, local_path: Path, *, dry_run: bool) -> str:
    kit_path = ai_root / "kit"
    local_path = local_path.resolve()
    if not local_path.is_dir():
        raise NotADirectoryError(f"AI_DEV_KIT_LOCAL is not a directory: {local_path}")
    if kit_path.exists():
        return "skipped"
    if dry_run:
        return "would_junction"
    ai_root.mkdir(parents=True, exist_ok=True)
    create_junction(kit_path, local_path)
    return "junction"


def attach_kit_submodule(
    project_root: Path,
    ai_root: Path,
    kit_url: str,
    kit_version: str,
    *,
    dry_run: bool,
) -> str:
    kit_path = ai_root / "kit"
    if kit_path.exists():
        return "skipped"
    if dry_run:
        return "would_submodule"
    ai_root.mkdir(parents=True, exist_ok=True)
    run(["git", "submodule", "add", kit_url, str(kit_path.relative_to(project_root))], cwd=project_root)
    run(["git", "-C", str(kit_path), "checkout", kit_version])
    return "submodule"


def pin_kit_version(kit_path: Path, kit_version: str, *, dry_run: bool) -> str:
    if not kit_path.is_dir():
        return "skipped"
    if dry_run:
        return "would_checkout"
    run(["git", "-C", str(kit_path), "fetch", "--tags", "--quiet"], check=False)
    run(["git", "-C", str(kit_path), "checkout", kit_version])
    return "checked_out"


def copy_if_missing(src: Path, dst: Path, *, dry_run: bool) -> str:
    if dst.exists():
        return "skipped"
    if dry_run:
        return "would_create"
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return "created"


def write_if_missing(path: Path, content: str, *, dry_run: bool) -> str:
    if path.exists():
        return "skipped"
    if dry_run:
        return "would_create"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return "created"


def personalize_state(state_path: Path, kit_version: str, *, dry_run: bool) -> None:
    if not state_path.is_file() or dry_run:
        return
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = state_path.read_text(encoding="utf-8")
    replacements = {
        r"^status: .*$": "status: INIT",
        r"^last_updated: .*$": f"last_updated: {today}",
        r"^last_session: .*$": "last_session: bootstrap",
        r"^last_prompt: .*$": "last_prompt: meta/init-project",
        r"^next_action: .*$": "next_action: planning/charter",
        r"^kit_version: .*$": f"kit_version: {kit_version}",
    }
    for pattern, replacement in replacements.items():
        text = re.sub(pattern, replacement, text, count=1, flags=re.MULTILINE)
    state_path.write_text(text, encoding="utf-8")


def personalize_project(project_path: Path, project_name: str, *, dry_run: bool) -> None:
    if not project_path.is_file() or dry_run:
        return
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    text = project_path.read_text(encoding="utf-8")
    text = text.replace("<PROJECT NAME>", project_name)
    text = re.sub(r"^started: .*$", f"started: {today}", text, count=1, flags=re.MULTILINE)
    project_path.write_text(text, encoding="utf-8")


def install_cursor_rule(
    project_root: Path,
    rule_template: Path,
    *,
    dry_run: bool,
    force: bool,
) -> str:
    rule_path = project_root / ".cursor" / "rules" / "ai-dev-kit-workflow.mdc"
    if rule_path.exists() and not force:
        return "skipped"
    if dry_run:
        return "would_create" if not rule_path.exists() else "would_overwrite"
    rule_path.parent.mkdir(parents=True, exist_ok=True)
    rule_path.write_text(rule_template.read_text(encoding="utf-8"), encoding="utf-8")
    return "created" if not force else "overwritten"


def bootstrap(args: argparse.Namespace) -> dict:
    project_root = args.project_root.resolve()
    ai_root = project_root / ".ai"
    kit_path = ai_root / "kit"
    local_kit = os.environ.get("AI_DEV_KIT_LOCAL")

    if not project_root.is_dir():
        raise FileNotFoundError(f"project_root does not exist: {project_root}")
    if not is_git_repo(project_root):
        raise RuntimeError(f"project_root is not a git repository: {project_root}")

    rule_template = resolve_rule_template(args.rule_template)
    summary: dict = {
        "project_root": str(project_root),
        "project_name": args.project_name,
        "dry_run": args.dry_run,
        "kit_attach": None,
        "kit_version": None,
        "next_action": "planning/charter",
        "created": [],
        "skipped": [],
    }

    if local_kit:
        attach_status = attach_kit_local(ai_root, Path(local_kit), dry_run=args.dry_run)
        summary["kit_attach"] = {"mode": "local", "path": local_kit, "status": attach_status}
    else:
        attach_status = attach_kit_submodule(
            project_root,
            ai_root,
            args.kit_url,
            args.kit_version,
            dry_run=args.dry_run,
        )
        summary["kit_attach"] = {"mode": "submodule", "url": args.kit_url, "status": attach_status}

    pending_attach = attach_status in ("would_submodule", "would_junction")
    if kit_path.is_dir() and not pending_attach and not args.dry_run:
        summary["kit_attach"]["pin"] = pin_kit_version(kit_path, args.kit_version, dry_run=False)

    kit_version = read_kit_version(kit_path / "CHANGELOG.md") if kit_path.is_dir() else "unknown"
    summary["kit_version"] = kit_version

    for dirname in AI_DIRS:
        target = ai_root / dirname
        rel = str(target.relative_to(project_root))
        if target.exists():
            summary["skipped"].append(rel)
        elif args.dry_run:
            summary["created"].append(rel)
        else:
            target.mkdir(parents=True, exist_ok=True)
            summary["created"].append(rel)

    templates_dir = kit_path / "templates"
    if not templates_dir.is_dir() and not args.dry_run:
        raise FileNotFoundError(
            f"Kit templates not found at {templates_dir}. Attach .ai/kit first or set AI_DEV_KIT_LOCAL."
        )

    for template_name, dest_name in TEMPLATE_MAP.items():
        src = templates_dir / template_name
        dst = ai_root / dest_name
        rel = str(dst.relative_to(project_root))
        if not src.is_file() and not args.dry_run:
            raise FileNotFoundError(f"Missing kit template: {src}")
        status = copy_if_missing(src, dst, dry_run=args.dry_run)
        (summary["created"] if status != "skipped" else summary["skipped"]).append(rel)
        if dest_name == "STATE.md" and status != "skipped":
            personalize_state(dst, kit_version, dry_run=args.dry_run)
        if dest_name == "PROJECT.md" and status != "skipped":
            personalize_project(dst, args.project_name, dry_run=args.dry_run)

    for filename, content in STUB_FILES.items():
        dst = ai_root / filename
        rel = str(dst.relative_to(project_root))
        status = write_if_missing(dst, content, dry_run=args.dry_run)
        (summary["created"] if status != "skipped" else summary["skipped"]).append(rel)

    rule_rel = ".cursor/rules/ai-dev-kit-workflow.mdc"
    rule_status = install_cursor_rule(
        project_root,
        rule_template,
        dry_run=args.dry_run,
        force=args.force_rule,
    )
    if rule_status == "skipped":
        summary["skipped"].append(rule_rel)
    else:
        summary["created"].append(rule_rel)

    return summary


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Bootstrap ai-dev-kit in a project.")
    parser.add_argument("--project-root", type=Path, required=True, help="Absolute path to git repo root")
    parser.add_argument("--project-name", required=True, help="Project identifier (kebab-case)")
    parser.add_argument("--kit-url", default=DEFAULT_KIT_URL, help="Kit git remote URL")
    parser.add_argument("--kit-version", default=DEFAULT_KIT_VERSION, help="Git tag to pin .ai/kit")
    parser.add_argument("--rule-template", type=Path, default=None, help="Path to Cursor rule template")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without modifying files")
    parser.add_argument("--force-rule", action="store_true", help="Overwrite existing Cursor rule")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    try:
        summary = bootstrap(parse_args(argv))
        print(json.dumps(summary, indent=2))
        return 0
    except (RuntimeError, FileNotFoundError, NotADirectoryError) as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
