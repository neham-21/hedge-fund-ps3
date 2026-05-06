import pandas as pd

# Load processed dataset
df = pd.read_csv("processed_nifty.csv")

# =========================
# Generate Signals
# =========================

df["Signal"] = 0

# BUY CONDITIONS
buy_condition = (
    (df["SMA20"] > df["SMA50"]) &
    (df["RSI"] < 70) &
    (df["MACD"] > df["MACD_SIGNAL"])
)

# SELL CONDITIONS
sell_condition = (
    (df["SMA20"] < df["SMA50"]) &
    (df["RSI"] > 30)
)

# Assign signals
df.loc[buy_condition, "Signal"] = 1

df.loc[sell_condition, "Signal"] = -1

# =========================
# Save Dataset
# =========================

df.to_csv("signals_nifty.csv", index=False)

# =========================
# Show Results
# =========================

print(df[[
    "Datetime",
    "Close",
    "SMA20",
    "SMA50",
    "RSI",
    "MACD",
    "MACD_SIGNAL",
    "Signal"
]].tail(20))
