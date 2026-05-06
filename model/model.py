import yfinance as yf

data = yf.download(
    "^NSEI",
    period="730d",
    interval="1h"
)

# Remove multi-level column names
data.columns = data.columns.droplevel(1)

# Save clean CSV
data.to_csv("nifty50.csv")

print(data.head())
