import os
import sys
import runpy
from pathlib import Path


def main():
    # Find the ScoreBot directory
    base_dir = Path(__file__).resolve().parent
    scorebot_dir = base_dir / "src" / "speedline" / "scorebot"

    # Change working directory so imports like `from bot import ...` keep working
    os.chdir(scorebot_dir)

    # Ensure scorebot_dir is on sys.path
    sys.path.insert(0, str(scorebot_dir))

    # Run app.py as if it was executed directly
    runpy.run_module("app", run_name="__main__")


if __name__ == "__main__":
    main()
