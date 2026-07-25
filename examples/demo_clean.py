"""Demo: run cmclean against a temporary tree and print comment issues."""
from __future__ import annotations

import tempfile
from pathlib import Path

from cmclean.engine import analyze

DEMO_SNIPPET = """\
# TODO: review before merge
# normal comment
x = 1
"""


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "app.py").write_text(DEMO_SNIPPET, encoding="utf-8")
        issues = analyze(str(root))
        print(f"Found {len(issues)} issue(s) in demo tree:\n")
        for issue in issues:
            print(f"{issue.path}:{issue.line} [{issue.kind}]")
            print(f"  {issue.snippet}")
        print()
        return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
