import pandas as pd
import numpy as np

df = pd.read_csv("portfolio_results.csv")

# Remove NaN
df.dropna(inplace=True)

# =========================
# Sharpe Ratio
# =========================

sharpe = (
    df["Portfolio_Returns"].mean()
    /
    df["Portfolio_Returns"].std()
) * np.sqrt(252)

# =========================
# Volatility
# =========================

volatility = (
    df["Portfolio_Returns"].std()
    * np.sqrt(252)
)

# =========================
# Max Drawdown
# =========================

rolling_max = df["Portfolio_Value"].cummax()

drawdown = (
    df["Portfolio_Value"]
    - rolling_max
) / rolling_max

max_drawdown = drawdown.min() * 100

# =========================
# Total Return
# =========================

initial = df["Portfolio_Value"].iloc[0]

final = df["Portfolio_Value"].iloc[-1]

total_return = (
    (final - initial)
    / initial
) * 100

# =========================
# Print Results
# =========================

print("\n===== PORTFOLIO METRICS =====\n")

print(f"Total Return: {total_return:.2f}%")

print(f"Sharpe Ratio: {sharpe:.2f}")

print(f"Volatility: {volatility:.4f}")

print(f"Max Drawdown: {max_drawdown:.2f}%")