from sys import argv
from pathlib import Path
from subprocess import run
import os

def list_files_str(src):
    out = ""
    # https://stackoverflow.com/q/50948391
    for root, dirs, files in os.walk(src):
        for file in files:
            # make the full path, then remove the prefix
            # + 1 for dir separator
            out += os.path.join(root, file)[len(src) + 1:] + '\n'
    return out

src_dir = argv[1]

# https://stackoverflow.com/a/165662
# no need to use .decode() since specified encoding
found_path = run(['fzf'], capture_output=True, input=list_files_str(src_dir), encoding='UTF-8').stdout

if len(found_path) == 0:
    print("failed")
else:
    found_path = os.path.join(src_dir, found_path)

    # https://ss64.com/nt/start.html
    # first arg: give a blank title
    run(f'start "" "{found_path}"', shell=True)

# TODO for history
# make separate history file for each query
# data_dir = Path(__file__).parent / 'data'
