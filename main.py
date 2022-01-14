import sys
sys.path.append('/FROGTEK_TECHNICAL_ASSESSMENT')
from src.data_wrangling import csv_to_df
from src.database_mgmt import sqlite_insert_df
import sqlite3


if __name__ == "__main__":

    db_name = "taxis"
    table_name = "yellowtaxis"
    year = 2020
    taxis_color = "Yellow"
    months = ("January",)
    year_html = None

    df = csv_to_df(year, taxis_color, *months)
    print(df)

    sqlite_insert_df(db_name, table_name, df)

    # name = "2020_yellow_jan_feb_mar.csv"
    # yellowtaxis_2020.to_csv(name, index=False)