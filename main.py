from pathlib import Path
from subprocess import run
from sys import argv

finder_path = Path(__file__).parent / 'find.py'
windows_terminal_profile = "Command Prompt"

# https://learn.microsoft.com/en-us/windows/terminal/command-line-arguments
run(['wt', '-F', '-p', windows_terminal_profile, 'python', finder_path, argv[1]])
