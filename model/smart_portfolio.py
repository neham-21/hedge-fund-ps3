import pandas as pd
import numpy as np

df = pd.read_csv("multi_asset_dataset.csv")

# =========================
# Calculate Returns
# =========================

df["Bond_Returns"] = df["Bonds"].pct_change()

# Remove NaN
df.dropna(inplace=True)

# =========================
# Rolling Volatility
# =========================

window = 30

oil_vol = df["Oil_Returns"].rolling(window).std()

gold_vol = df["Gold_Returns"].rolling(window).std()

bond_vol = df["Bond_Returns"].rolling(window).std()

# =========================
# Inverse Volatility Weights
# =========================

inv_oil = 1 / oil_vol

inv_gold = 1 / gold_vol

inv_bond = 1 / bond_vol

total = inv_oil + inv_gold + inv_bond

df["Oil_Weight"] = inv_oil / total

df["Gold_Weight"] = inv_gold / total

df["Bond_Weight"] = inv_bond / total

# =========================
# Weight Limits
# =========================

df["Oil_Weight"] = df["Oil_Weight"].clip(0.1, 0.5)

df["Gold_Weight"] = df["Gold_Weight"].clip(0.1, 0.5)

df["Bond_Weight"] = df["Bond_Weight"].clip(0.1, 0.5)

# Normalize weights again

weight_sum = (
    df["Oil_Weight"]
    +
    df["Gold_Weight"]
    +
    df["Bond_Weight"]
)

df["Oil_Weight"] /= weight_sum

df["Gold_Weight"] /= weight_sum

df["Bond_Weight"] /= weight_sum

# =========================
# Portfolio Returns
# =========================

df["Portfolio_Returns"] = (
    df["Oil_Weight"] * df["Oil_Returns"]
    +
    df["Gold_Weight"] * df["Gold_Returns"]
    +
    df["Bond_Weight"] * df["Bond_Returns"]
)

# =========================
# Portfolio Value
# =========================

initial_capital = 100000

df["Portfolio_Value"] = (
    1 + df["Portfolio_Returns"]
).cumprod() * initial_capital

# =========================
# Save
# =========================

df.to_csv("smart_portfolio_results.csv", index=False)

print(df[[
    "Oil_Weight",
    "Gold_Weight",
    "Bond_Weight",
    "Portfolio_Value"
]].tail())

print("\nMin Return:", df["Portfolio_Returns"].min())
print("Max Return:", df["Portfolio_Returns"].max())