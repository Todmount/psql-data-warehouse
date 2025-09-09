"""
Script to generate dbt sources from provided CSVs (raw data).
By default, will save sources into models/bronze.
"""
import csv
import yaml

from typing import Any
from common.constants import CRM_PATH, ERP_PATH, BRONZE_PATH
from pathlib import Path

# Source: https://gist.github.com/jamescherti/522a99074ae9ad71bbf93f7395b6b90a
def yaml_dump_indent_lists(data: Any, **kwargs):
    """Same as yaml.dump() but with a better indentation for lists and blank lines between top-level objects.

    >>> print(yaml_dump_indent_lists({"list": [1, 2, 3]}))
    ---
    list:
      - 1
      - 2
      - 3
    """

    class YamlDumper(yaml.Dumper):
        # HACK: insert blank lines between top-level objects
        # inspired by https://stackoverflow.com/a/44284819/3786245
        # source: https://github.com/yaml/pyyaml/issues/127#issuecomment-525800484
        def write_line_break(self, data=None):
            super().write_line_break(data)

            if len(self.indents) == 1:
                super().write_line_break()

        def increase_indent(self, flow=False, indentless=False):
            return super().increase_indent(flow, False)

    return yaml.dump(
        data,
        Dumper=YamlDumper,
        # default_flow_style=False,
        indent=2,
        sort_keys=False,
    )


def generate_dbt_yml(csv_file_path: Path, prefix: str) -> None:

    source_name = csv_file_path.stem
    table_name = f"{prefix}_{source_name}"
    output_yml_path = BRONZE_PATH / f"{table_name}.yml"

    with open(csv_file_path, "r") as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

    columns = []
    for header in headers:
        columns.append(
            {
                "name": header,
                "description": f"A column automatically generated from {table_name}.",
                "tests": ["not_null"],
            }
        )

    dbt_yml_content = {
        "version": 2,
        "sources": [
            {
                "name": "bronze",
                "description": "",
                "schema": "bronze",
                "tables": [{"name": table_name, "columns": columns}],
            }
        ],
    }
    with open(output_yml_path, "+x") as yamlfile:
        yaml_string = yaml_dump_indent_lists(dbt_yml_content)
        yamlfile.write(yaml_string)

def main(src_path: Path, prefix: str):
    for src in src_path.glob("*.csv"):
        try:
            generate_dbt_yml(csv_file_path=src, prefix=prefix)
        except FileExistsError:
            print(f"Source for {src.name} exist! Skipping...")
            continue

if __name__ == "__main__":
    main(CRM_PATH, 'crm')
    main(ERP_PATH, 'erp')
