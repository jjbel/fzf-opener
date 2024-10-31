# fzf-opener

Say you want to open C:\Users\me\a\really\long\path\myfile.pdf but don't want to spend hours double clicking through Windows Explorer.

Just run `python main.py C:\`, search quickly for it using [fzf](https://github.com/junegunn/fzf) (eg for the above path, just type `arlypdf`), press enter, and the file will open.

If you use the [autohotkey](https://www.autohotkey.com) script `fzf_opener.ahk`, then just press `Ctrl+Space` and watch the list of files open.
