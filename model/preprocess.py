import pandas as pd

from ta.trend import SMAIndicator, MACD
from ta.momentum import RSIIndicator
from ta.volatility import BollingerBands

# =========================
# Load Dataset
# =========================

df = pd.read_csv("nifty50_hourly.csv")

# Convert datetime column
df["Datetime"] = pd.to_datetime(df["Datetime"])

# Sort values
df = df.sort_values("Datetime")

# Remove missing values
df.dropna(inplace=True)

# =========================
# Technical Indicators
# =========================

# SMA 20
df["SMA20"] = SMAIndicator(
    close=df["Close"],
    window=20
).sma_indicator()

# SMA 50
df["SMA50"] = SMAIndicator(
    close=df["Close"],
    window=50
).sma_indicator()

# RSI
df["RSI"] = RSIIndicator(
    close=df["Close"],
    window=14
).rsi()

# MACD
macd = MACD(close=df["Close"])

df["MACD"] = macd.macd()

df["MACD_SIGNAL"] = macd.macd_signal()

# Bollinger Bands
bb = BollingerBands(close=df["Close"])

df["BB_HIGH"] = bb.bollinger_hband()

df["BB_LOW"] = bb.bollinger_lband()

# Remove NaN rows created by indicators
df.dropna(inplace=True)

# Save processed dataset
df.to_csv("processed_nifty.csv", index=False)

# Print results
print(df.head())

print("\nColumns:")
print(df.columns)
