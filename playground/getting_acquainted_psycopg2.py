import os

import pandas
import psycopg2
import pandas as pd
from dotenv import load_dotenv, find_dotenv
from common.constants import *

load_dotenv(find_dotenv())

def get_column_names(curs) -> list[str]:
    curs.execute("Select * FROM bronze.crm_cust_info LIMIT 0")
    colnames: list[str] = [desc[0] for desc in curs.description]
    print(colnames)
    return colnames

def great_query(curs, colnames) -> None:
    query: str = f"SELECT * FROM bronze.crm_cust_info LIMIT 2"

    curs.execute(query)
    da_table = curs.fetchall()
    for i in da_table:
        print(f"{colnames[0]} {i[0]} ")

def main() -> None:
    dsn: str = (
        f"user={DB_USER} "
        f"password={DB_PASSWORD} "
        f"host={DB_HOST} "
        f"dbname='datawarehouse'"
    )

    with psycopg2.connect(dsn) as conn:
        with conn.cursor() as cursor:
            # great_query(cursor, colnames=get_column_names(cursor))
            # get_column_names(cursor)
            query: str = f"SELECT * FROM bronze.crm_cust_info LIMIT 2"
            # moved to sqlalchemy
            d = pd.read_sql_query(query, conn)
            print(type(d))
            print(pd.DataFrame.head(d))


if __name__ == "__main__":
    try:
        main()
    except psycopg2.OperationalError as e:
        print(f"Error. Could not connect to database. \nReason: {e}")
    except psycopg2.errors.UndefinedTable as e:
        print(f"Error: {e}")
    # except Exception as e:
    #     print(f"Unexpected error: {e}")