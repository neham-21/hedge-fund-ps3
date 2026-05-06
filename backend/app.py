from fastapi import FastAPI
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load dataset
df = pd.read_csv("data/processed/advanced_backtest.csv")

# =========================
# HOME
# =========================

@app.get("/")
def home():

    return {
        "message": "Hedge Fund Trading System API"
    }

# =========================
# METRICS
# =========================

@app.get("/metrics")
def get_metrics():

    initial_value = df["Portfolio_Value"].iloc[0]

    final_value = df["Portfolio_Value"].iloc[-1]

    total_return = (
        (final_value - initial_value)
        / initial_value
    ) * 100

    return {
        "total_return": round(total_return, 2),
        "final_portfolio_value": round(final_value, 2)
    }

# =========================
# SIGNALS
# =========================

@app.get("/signals")
def get_signals():

    signals = df[[
        "Datetime",
        "Close",
        "Signal"
    ]].tail(50)

    return signals.to_dict(orient="records")

# =========================
# PORTFOLIO
# =========================

@app.get("/portfolio")
def get_portfolio():

    portfolio = df[[
        "Datetime",
        "Portfolio_Value"
    ]]

    return portfolio.tail(200).to_dict(orient="records")

@app.get("/trades")
def get_trades():

    trades = df[df["Signal"] != 0][[
        "Datetime",
        "Close",
        "Signal"
    ]]

    return trades.to_dict(orient="records")

@app.get("/risk")
def get_risk_metrics():

    returns = df["Portfolio_Value"].pct_change()

    volatility = returns.std()

    max_drawdown = (
        (
            df["Portfolio_Value"]
            - df["Portfolio_Value"].cummax()
        )
        /
        df["Portfolio_Value"].cummax()
    ).min()

    return {
        "volatility": round(float(volatility), 6),
        "max_drawdown": round(float(max_drawdown), 6)
    }
    
    # =========================
# SMART PORTFOLIO DATA
# =========================

portfolio_df = pd.read_csv(
    "data/processed/smart_portfolio_results.csv"
)

# =========================
# PORTFOLIO METRICS
# =========================

@app.get("/portfolio-metrics")
def portfolio_metrics():

    initial = portfolio_df[
        "Portfolio_Value"
    ].iloc[0]

    final = portfolio_df[
        "Portfolio_Value"
    ].iloc[-1]

    total_return = (
        (final - initial)
        / initial
    ) * 100

    return {
        "final_value": round(float(final), 2),
        "total_return": round(float(total_return), 2)
    }

# =========================
# PORTFOLIO ALLOCATIONS
# =========================

@app.get("/allocations")
def allocations():

    latest = portfolio_df.tail(1)

    return {
        "oil_weight":
            round(
                float(
                    latest["Oil_Weight"].values[0]
                ),
                4
            ),

        "gold_weight":
            round(
                float(
                    latest["Gold_Weight"].values[0]
                ),
                4
            ),

        "bond_weight":
            round(
                float(
                    latest["Bond_Weight"].values[0]
                ),
                4
            )
    }

# =========================
# PORTFOLIO VALUES
# =========================

@app.get("/portfolio-history")
def portfolio_history():

    history = portfolio_df[[
        "Date",
        "Portfolio_Value"
    ]]

    return history.tail(200).to_dict(
        orient="records"
    )