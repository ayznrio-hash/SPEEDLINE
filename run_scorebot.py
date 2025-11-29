import os
import sys
from pathlib import Path
import runpy


def main():
    base_dir = Path(__file__).resolve().parent
    scorebot_dir = base_dir / "src" / "speedline" / "scorebot"

    if not scorebot_dir.exists():
        raise SystemExit(f"ScoreBot folder nahi mila: {scorebot_dir}")

    os.chdir(scorebot_dir)
    sys.path.insert(0, str(scorebot_dir))

    runpy.run_module("app", run_name="__main__")


if __name__ == "__main__":
    main()
