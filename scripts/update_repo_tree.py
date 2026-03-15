from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
INSTRUCTIONS_PATH = ROOT / ".github" / "instructions" / "copilot.instructions.md"
START_MARKER = "<!-- repo-tree:start -->"
END_MARKER = "<!-- repo-tree:end -->"
TREE_COMMAND = [
    "tree",
    "-a",
    "-I",
    ".git|node_modules|.venv|__pycache__",
    "-L",
    "3",
]


def get_tree_output() -> str:
    try:
        result = subprocess.run(
            TREE_COMMAND,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise SystemExit(
            "`tree` is not installed. Install it with `brew install tree` and rerun."
        ) from exc
    except subprocess.CalledProcessError as exc:
        raise SystemExit(exc.stderr.strip() or exc.stdout.strip() or str(exc)) from exc

    return result.stdout.rstrip()


def update_instructions(tree_output: str) -> None:
    content = INSTRUCTIONS_PATH.read_text()

    if START_MARKER not in content or END_MARKER not in content:
        raise SystemExit("Tree markers were not found in copilot.instructions.md")

    before, remainder = content.split(START_MARKER, maxsplit=1)
    _, after = remainder.split(END_MARKER, maxsplit=1)
    replacement = f"{START_MARKER}\n```text\n{tree_output}\n```\n{END_MARKER}"
    INSTRUCTIONS_PATH.write_text(before + replacement + after)


def main() -> int:
    tree_output = get_tree_output()
    update_instructions(tree_output)
    print(f"Updated {INSTRUCTIONS_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())