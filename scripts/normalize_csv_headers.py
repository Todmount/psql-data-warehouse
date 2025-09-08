from pathlib import Path
import re
from common.get_project_root import get_project_root

project_folder = get_project_root()
seeds_folder = project_folder / 'seeds' / 'bronze'

def _normalize_header(col: str) -> str:
    col = col.strip().lower()
    col = re.sub(r"\W+", "_", col)
    return col


def norm_headers(folder: Path) -> None:
    for csv_file in folder.glob("*.csv"):
        with open(csv_file, "r", encoding="utf-8") as f_in, \
                open(csv_file.with_suffix(".csv"), "w", encoding="utf-8") as f_out:

            # Read and normalize the header
            header = f_in.readline().strip().split(",")
            new_header = [_normalize_header(c) for c in header]
            f_out.write(",".join(new_header) + "\n")

            # Copy the rest of the file without touching
            for line in f_in:
                f_out.write(line)

        print(f"Normalized headers in {csv_file.name} → {csv_file.stem}.csv")

if __name__ == "__main__":
    norm_headers(seeds_folder)