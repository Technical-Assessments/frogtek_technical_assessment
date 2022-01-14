import sys
sys.path.append('/FROGTEK_TECHNICAL_ASSESSMENT')
from src.data_wrangling import csv_to_df
import sqlite3


if __name__ == "__main__":

    table_name = "yellowtaxis"
    year = 2020
    taxis_color = "Yellow"
    months = ("January",)
    year_html = None #########

    df = csv_to_df(year, taxis_color, *months)
    print(df)

    # name = "2020_yellow_jan_feb_mar.csv"
    # yellowtaxis_2020.to_csv(name, index=False)

    conn = sqlite3.connect("../taxis.db")
    df.to_sql('yellowtaxis', conn, if_exists='replace', index=False)