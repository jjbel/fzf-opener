from pathlib import Path
from subprocess import run
from sys import argv
from time import sleep

finder_path = Path(__file__).parent / 'find.py'
windows_terminal_profile = "Command Prompt"

# https://learn.microsoft.com/en-us/windows/terminal/command-line-arguments
run(['wt', '-F', '-p', windows_terminal_profile, 'python', finder_path, argv[1]])

# https://stackoverflow.com/a/3729202
result_path  = Path(__file__).parent / 'path.txt'
result = result_path.read_text()

# terminal command runs async, so check when file updated
while result == 'done':
    result = result_path.read_text()
    # TODO tune this
    sleep(0.1)
result_path.write_text('done')

# https://ss64.com/nt/start.html
# first arg: give a blank title
if result != 'failed':
    run(f'start "" "{result}"', shell=True)
# TODO improve speed: open with okular if pdf
