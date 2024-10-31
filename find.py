from sys import argv
from pathlib import Path
from subprocess import run
from os import walk
import os
from pprint import pprint

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
found_path = run(['fzf'], capture_output=True, input=list_files_str(src_dir), encoding='ascii').stdout
result_path  = Path(__file__).parent / 'path.txt'

if len(found_path) == 0:
    result_path.write_text("failed")
else:
    found_path = os.path.join(src_dir, found_path)
    result_path.write_text(found_path)

# TODO for history
# make separate history file for each query
# data_dir = Path(__file__).parent / 'data'
