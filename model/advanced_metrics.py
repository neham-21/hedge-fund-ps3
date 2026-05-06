import pandas as pd
import numpy as np

df = pd.read_csv("advanced_backtest.csv")

# Portfolio returns
df["Returns"] = df["Portfolio_Value"].pct_change()

df.dropna(inplace=True)

# Sharpe Ratio
sharpe = (
    df["Returns"].mean()
    /
    df["Returns"].std()
) * np.sqrt(252)

# Volatility
volatility = (
    df["Returns"].std()
    * np.sqrt(252)
)

# Drawdown
rolling_max = df["Portfolio_Value"].cummax()

drawdown = (
    df["Portfolio_Value"] - rolling_max
) / rolling_max

max_drawdown = drawdown.min() * 100

# Win/Loss
wins = (df["Returns"] > 0).sum()

losses = (df["Returns"] < 0).sum()

win_rate = wins / (wins + losses) * 100

# Print metrics
print("\n===== ADVANCED METRICS =====\n")

print(f"Sharpe Ratio: {sharpe:.2f}")

print(f"Volatility: {volatility:.4f}")

print(f"Max Drawdown: {max_drawdown:.2f}%")

print(f"Win Rate: {win_rate:.2f}%")