# Daily update of FX quotes
# peter.gruber@usi.ch, 2024-03

# Requires --  pip install pandas yfinance
import pandas as pd
import yfinance as yf
from datetime import datetime

# Fetch data for EUR/USD currency pair
eur_usd = yf.download("EURUSD=X", period="1d")

# Extract the latest closing price
eur_usd_latest = eur_usd['Close'].iloc[-1]

# Create a DataFrame to store the date and the latest closing price
fx_data = pd.DataFrame({
    'Date': [datetime.now().strftime('%Y-%m-%d')],
    'USD_Latest': [eur_usd_latest]
})

# Append the data to a CSV file, without headers and index
fx_data.to_csv('fx.csv', mode='a', header=False, index=False, sep=",")
