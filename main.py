from pathlib import Path
from subprocess import run
from sys import argv

finder_path = Path(__file__).parent / "find.py"

# https://learn.microsoft.com/en-us/windows/terminal/command-line-arguments
run(["wt", "-F", "python", finder_path, argv[1]])
