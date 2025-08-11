from os import walk
from os.path import join
from sys import argv
from pathlib import Path

src = argv[1]
history_path = Path(__file__).parent / "history.txt"

print(history_path.read_text())

for root, dirs, files in walk(src):
    for file in files:
        # make the full path, then remove the prefix
        # + 1 for dir separator
        path = join(root, file)[len(src) + 1 :]

        # TODO shell can't handle unicode characters when piping to fzf?
        # just list.py runs without errors

        # https://stackoverflow.com/a/77374899/17100530
        # cp437 is the default code page for cmd
        # need to decode it again else its bytes

        # flush in case it doesn't pipe in realtime coz of buffering?
        print(path.encode("cp437", errors="ignore").decode("cp437"), flush=True)
