"""
Utility script to work with the bronze level of the warehouse.
Serves as simple orchestration; the main work is in SQL files.
Main operations: Recreate DB, Recreate schemas and tables, Load raw data into DB.
"""

import psycopg2
import logging
from dotenv import load_dotenv, find_dotenv
from rich.console import Console
from rich.logging import RichHandler
from logging.handlers import RotatingFileHandler
from rich.traceback import install as traceback_cfg

from common.constants import (
    PROJECT_ROOT,
    DB_HOST,
    DB_NAME,
    DB_USER,
    DB_PASSWORD,
    DB_SUPERNAME,
    DB_SUPERUSER,
    DB_SUPERPASSWORD,
)

load_dotenv(find_dotenv())

QUERY_PATH = PROJECT_ROOT / "scripts" / "bronze" / "sql"
DSN = f"user={DB_USER} password={DB_PASSWORD} host={DB_HOST} dbname={DB_NAME}"
DSN_SUPER = (
    f"user={DB_SUPERUSER} password={DB_SUPERPASSWORD} host={DB_HOST} dbname={DB_SUPERNAME}"
)
FORMAT = "%(message)s"
FORMAT_TO_FILE = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

logging.basicConfig(
    level="INFO",
    format=FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=False)],
)

log = logging.getLogger("rich")
log_to_file = logging.getLogger("to_file")

logfile = RotatingFileHandler(PROJECT_ROOT / 'logs' / 'load_bronze.log', maxBytes=512*1024, backupCount=5)
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(FORMAT_TO_FILE)
log_to_file.propagate = False
log_to_file.addHandler(logfile)

traceback_cfg(
    width=120,
    show_locals=False, # there are passwords
    theme="monokai",
    word_wrap=True
)

console = Console()


def load_query(filename: str) -> str | None:
    """Read a SQL file into a string."""
    path = QUERY_PATH / filename
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        log_to_file.exception("Query failed!")
        console.print_exception()


def run_query(query: str) -> None:
    try:
        conn = psycopg2.connect(DSN)
        with conn, conn.cursor() as curs:
            curs.execute(query)
    except Exception:
        log_to_file.exception("DDL query failed!")
        console.print_exception()
    finally:
        if conn:
            log_to_file.info("Explicitly closing connection...")
            conn.close()


def rebuild_db() -> None:
    """Drop the database and create new"""
    conn = psycopg2.connect(DSN_SUPER)
    conn.autocommit = True

    terminate_backend = load_query(QUERY_PATH / "terminate_backend.sql")
    create_db = load_query(QUERY_PATH / "create_database.sql")

    try:
        log.info("Rebuilding DB from scratch...")
        with conn.cursor() as spr:
            spr.execute(terminate_backend)
            spr.execute(f"DROP DATABASE IF EXISTS {DB_NAME};")
            spr.execute(create_db, [DB_USER])
        conn.close()
    except Exception:
        log_to_file.error("Query failed!", exc_info=True, stack_info=False)
        console.print_exception()


def create_schemas() -> None:
    log.info("Creating schemas...")
    query = load_query(QUERY_PATH / "create_schemas.sql")
    run_query(query)


def ddl_bronze() -> None:
    """Drop existing tables and build a new structure"""
    log.info("Creating tables from scratch...")
    query = load_query(QUERY_PATH / "ddl_bronze.sql")
    run_query(query)


def load_data() -> None:
    log.info("Inserting raw data into DB...")
    query = load_query(QUERY_PATH / "load_bronze.sql")
    run_query(query)


def run_all() -> None:
    # log_to_file.info("-"*40)
    log.info("Starting full bronze pipeline...")
    rebuild_db()
    create_schemas()
    ddl_bronze()
    load_data()


def confirmation() -> None:
    log.warning(f"This will DROP the '{DB_NAME}' database. Proceed with caution!")
    user_input = input(
        "Enter 'yes' to continue or press enter to go to the menu >> "
    )
    if user_input.strip().lower() != "yes":
        log_to_file.info("Aborting operation. Return to menu...")
        main()
    else:
        log_to_file.info("User decided to go on!")


def proceed():
    user_input: str = input("'q' to quit or press enter to continue >> ")
    if user_input.strip().lower() == "q":
        log.info("Exiting...")
        log_to_file.info("END SESSION | "+'='*50)
        raise SystemExit(0)


def main() -> None:
    print(
        "\nBronze Layer Utility\n"
        "1. Drop and create empty database\n"
        "2. Create schemas and empty tables for bronze layer\n"
        "3. Load new batch of data into bronze layer\n"
        "4. Run all\n"
        "q. Exit"
    )
    choice = input("Enter your choice >> ")
    if choice == "q":
        log.info("Exiting...")
        log_to_file.info("END SESSION | "+'='*50)
        raise SystemExit(0)
    elif choice == "1":
        log_to_file.info("Awaiting confirmation for DB drop & rebuild...")
        confirmation()
        rebuild_db()
    elif choice == "2":
        create_schemas()
        ddl_bronze()
    elif choice == "3":
        load_data()
    elif choice == "4":
        log_to_file.info("Awaiting confirmation for initiating full bronze rebuild...")
        confirmation()
        run_all()
    else:
        log.warning("Invalid choice. Try again.")
        return


if __name__ == "__main__":
    log_to_file.info("NEW SESSION | "+'='*50)
    while True:
        try:
            log_to_file.info("Running cycle...")
            main()
            proceed()
        except KeyboardInterrupt:
            log.info("Exiting...")
            log_to_file.info("END SESSION | "+'='*50)
            raise SystemExit(0)
