import pandas as pd

# =========================
# Load Dataset
# =========================

df = pd.read_csv("signals_nifty.csv")

# =========================
# Initial Settings
# =========================

initial_capital = 100000

cash = initial_capital

position = 0

portfolio_values = []

trade_log = []

# =========================
# Backtesting Loop
# =========================

for i in range(len(df)):

    signal = df.loc[i, "Signal"]

    price = df.loc[i, "Close"]

    datetime = df.loc[i, "Datetime"]

    # =====================
    # BUY
    # =====================

    if signal == 1 and position == 0:

        position = cash / price

        trade_log.append(
            f"BUY at {price:.2f} on {datetime}"
        )

        cash = 0

    # =====================
    # SELL
    # =====================

    elif signal == -1 and position > 0:

        cash = position * price

        trade_log.append(
            f"SELL at {price:.2f} on {datetime}"
        )

        position = 0

    # =====================
    # Portfolio Value
    # =====================

    portfolio_value = cash + (position * price)

    portfolio_values.append(portfolio_value)

# =========================
# Store Results
# =========================

df["Portfolio_Value"] = portfolio_values

# =========================
# Performance Metrics
# =========================

final_value = df["Portfolio_Value"].iloc[-1]

total_return = (
    (final_value - initial_capital)
    / initial_capital
) * 100

# =========================
# Print Results
# =========================

print(f"\nInitial Capital: ₹{initial_capital}")

print(f"Final Portfolio Value: ₹{final_value:.2f}")

print(f"Total Return: {total_return:.2f}%")

print("\nTrade Log:")

for trade in trade_log[:10]:
    print(trade)

# =========================
# Save Dataset
# =========================

df.to_csv("backtested_nifty.csv", index=False)