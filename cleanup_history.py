from pathlib import Path

# TODO shd have history for each search path
# TODO shd backup history, see fzf on PC for that

root = Path("C:\\Users\\jaibe\\OneDrive\\IIT")
history_path = Path(__file__).parent / "history.txt"
out = "\n".join(
    list(
        dict.fromkeys(  # de-duplicate, preserving order
            [
                path
                for path in history_path.read_text().splitlines()
                if (root / Path(path)).exists()  # remove non-existent paths
            ]
        )
    )
)
history_path.write_text(out)
