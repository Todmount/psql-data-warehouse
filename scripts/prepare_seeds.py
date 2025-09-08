from pathlib import Path
from shutil import copy2

from common.get_project_root import get_project_root

project_root = get_project_root()
erp_path = project_root / 'datasets' / 'source_erp'
crm_path = project_root / 'datasets' / 'source_crm'
seeds_path = project_root / 'seeds'


def copy_rename(src_path: Path, dest: Path, prefix: str) -> None:

    Path(dest).mkdir(parents=True, exist_ok=True)
    counter = []
    for src in src_path.rglob('*.csv'):
        file_name = src.name
        # if file_name is None: print('kek')
        new_file_name = f"{prefix}_{file_name.lower()}"
        copy2(src, dest/new_file_name)
        print(f"Successfully copied {new_file_name}")
        counter.append('src')

    if not counter:
        print(f"Nothing to copy in \"{src_path}\"!")


def main() -> None:
    """
    If a file in 'datasets/source_crp/' move it to 'seeds/bronze/'
    And rename it to crp_{file_name}
    """
    dest = seeds_path / 'bronze'

    copy_rename(crm_path, dest, 'crm')
    copy_rename(erp_path, dest, 'erp')

if __name__ == "__main__":
    try:
        main()
    except FileExistsError:
        print("[ERROR] Provided destination is not a folder!")