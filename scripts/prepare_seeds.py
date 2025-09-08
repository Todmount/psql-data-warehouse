from pathlib import Path
import petl as etl, re

from common.get_project_root import get_project_root

project_root = get_project_root()
erp_path = project_root / 'datasets' / 'source_erp'
crm_path = project_root / 'datasets' / 'source_crm'
seeds_path = project_root / 'seeds'

def normalize(s):
    s = s.strip().lower()
    return re.sub(r'\W+', '_', s)


def copy_rename(src_path: Path, dest: Path, prefix: str) -> None:

    Path(dest).mkdir(parents=True, exist_ok=True)
    counter = []
    for src in src_path.rglob('*.csv'):
        file_name = src.name
        new_file_name = f"{prefix}_{file_name.lower()}"
        table = etl.fromcsv(src, delimiter=',')
        table = etl.rename(table, {h: normalize(h) for h in etl.header(table)})
        etl.tocsv(table, dest/new_file_name)

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