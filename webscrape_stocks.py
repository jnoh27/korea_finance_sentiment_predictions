import os
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# By industry
symbols = ['153130.KS',  # KODEX IT (Technology Sector)
           '091170.KS',  # KODEX Bank (Finance Sector)
           '143860.KS',  # KODEX Healthcare (Healthcare Sector)
           '266360.KS',  # KODEX Media & Entertainment (Entertainment Sector)
           '117460.KS',  # KODEX Energy & Chemicals (Energy Sector)
           '091180.KS',  # KODEX Automobiles (Automobile Sector)
           '244580.KS',  # KODEX Bio (Bio Sector)
           '266410.KS',  # KODEX Consumer Staples (Consumer Staples sector)
           '117700.KS',  # KODEX Construction (Construction Sector)
           ]

# Date range
start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')

# Fetch the data using yfinance
for symbol in symbols:
    data = yf.download(symbol, start=start_date, end=end_date)
    filename = os.path.join("Stock Sector Datas", f"{symbol}_sector_data.csv")
    data.to_csv(filename)
    print(f"Data for {symbol} saved to '{filename}'")

if __name__ == "__main__":
    for symbol in symbols:
        file_path = os.path.join("Stock Sector Datas", f"{symbol}_sector_data.csv")
        kospi_df = pd.read_csv(file_path)

        # Display the first few rows of the data
        print(f"Data from {symbol}_sector_data.csv:")
        print(kospi_df.head(), end='\n\n')

        # Display basic statistics of the data
        # print(kospi_df.describe())
