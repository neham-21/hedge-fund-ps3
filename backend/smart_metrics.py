import pandas as pd
import numpy as np

# =========================
# Load Dataset
# =========================

df = pd.read_csv("data/processed/smart_portfolio_results.csv")

# Remove missing values
df.dropna(inplace=True)

# =========================
# Sharpe Ratio
# =========================

sharpe_ratio = (
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
    df["Portfolio_Value"] - rolling_max
) / rolling_max

max_drawdown = drawdown.min() * 100

# =========================
# Total Return
# =========================

initial_value = df["Portfolio_Value"].iloc[0]

final_value = df["Portfolio_Value"].iloc[-1]

total_return = (
    (final_value - initial_value)
    / initial_value
) * 100

# =========================
# Win Rate
# =========================

wins = (df["Portfolio_Returns"] > 0).sum()

losses = (df["Portfolio_Returns"] < 0).sum()

win_rate = (
    wins / (wins + losses)
) * 100

# =========================
# Print Metrics
# =========================

print("\n===== SMART PORTFOLIO METRICS =====\n")

print(f"Total Return: {total_return:.2f}%")

print(f"Sharpe Ratio: {sharpe_ratio:.2f}")

print(f"Volatility: {volatility:.4f}")

print(f"Max Drawdown: {max_drawdown:.2f}%")

print(f"Win Rate: {win_rate:.2f}%")