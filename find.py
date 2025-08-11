from subprocess import Popen, PIPE, run
from sys import argv
from pathlib import Path

# TODO ensure no trailing slash for list.py
base_path = argv[1].rstrip("/")

finder_path = Path(__file__).parent / "find.py"
history_path = Path(__file__).parent / "history.txt"

p1 = Popen(["python", "list.py", base_path], stdout=PIPE, shell=True)
p2 = Popen(["fzf"], stdin=p1.stdout, stdout=PIPE, shell=True)

# Close p1's stdout in parent to allow fzf to receive EOF properly
p1.stdout.close()

# Read selected result from fzf
out, _ = p2.communicate()

found_path = out.rstrip().decode()


if found_path == "":
    exit()

history_path.write_text(history_path.read_text() + str(found_path) + "\n")
found_path = Path(base_path) / Path(found_path)
# print(found_path)

# https://ss64.com/nt/start.html
# first arg: give a blank title
run(f'start "" "{found_path}"', shell=True)
