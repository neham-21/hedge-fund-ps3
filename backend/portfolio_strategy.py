import pandas as pd

df = pd.read_csv("multi_asset_dataset.csv")

# =========================
# Bond Returns
# =========================

df["Bond_Returns"] = df["Bonds"].pct_change()

# =========================
# Equal Portfolio Allocation
# =========================

oil_weight = 0.33

gold_weight = 0.33

bond_weight = 0.34

# =========================
# Portfolio Returns
# =========================

df["Portfolio_Returns"] = (
    oil_weight * df["Oil_Returns"]
    +
    gold_weight * df["Gold_Returns"]
    +
    bond_weight * df["Bond_Returns"]
)

# =========================
# Portfolio Value
# =========================

initial_capital = 100000

df["Portfolio_Value"] = (
    1 + df["Portfolio_Returns"]
).cumprod() * initial_capital

# =========================
# Save Dataset
# =========================

df.to_csv("portfolio_results.csv", index=False)

print(df.head())