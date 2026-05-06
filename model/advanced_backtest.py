import pandas as pd

# Load dataset
df = pd.read_csv("signals_nifty.csv")

# =========================
# Initial Settings
# =========================

initial_capital = 100000

cash = initial_capital

position = 0

buy_price = 0

portfolio_values = []

trade_log = []

# Risk settings
position_size = 0.25

stop_loss_pct = 0.03

take_profit_pct = 0.08

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

        investment = cash * position_size

        position = investment / price

        cash -= investment

        buy_price = price

        trade_log.append(
            f"BUY at {price:.2f} on {datetime}"
        )

    # =====================
    # STOP LOSS / TAKE PROFIT
    # =====================

    if position > 0:

        stop_loss_price = buy_price * (1 - stop_loss_pct)

        take_profit_price = buy_price * (1 + take_profit_pct)

        if price <= stop_loss_price:

            cash += position * price

            trade_log.append(
                f"STOP LOSS SELL at {price:.2f} on {datetime}"
            )

            position = 0

        elif price >= take_profit_price:

            cash += position * price

            trade_log.append(
                f"TAKE PROFIT SELL at {price:.2f} on {datetime}"
            )

            position = 0

    # =====================
    # NORMAL SELL
    # =====================

    elif signal == -1 and position > 0:

        cash += position * price

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
# Final Metrics
# =========================

final_value = df["Portfolio_Value"].iloc[-1]

total_return = (
    (final_value - initial_capital)
    / initial_capital
) * 100

print(f"\nFinal Portfolio Value: ₹{final_value:.2f}")

print(f"Total Return: {total_return:.2f}%")

print("\nTrade Samples:\n")

for trade in trade_log[:15]:
    print(trade)

# Save dataset
df.to_csv("advanced_backtest.csv", index=False)