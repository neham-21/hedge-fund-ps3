import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hedge Fund Dashboard",
    layout="wide"
)

st.title("📈 Hedge Fund Risk Dashboard")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Overview",
        "Analytics",
        "Risk Metrics",
        "Trade Logs"
    ]
)

if page == "Overview":

    st.header("Portfolio Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Portfolio Value", "$12,450")
    col2.metric("Sharpe Ratio", "1.42")
    col3.metric("Max Drawdown", "-8.2%")

elif page == "Analytics":

    st.header("Portfolio Analytics")

    data = {
        "date": ["2024-01", "2024-02", "2024-03", "2024-04"],
        "portfolio_value": [10000, 11000, 10800, 12500]
    }

    df = pd.DataFrame(data)

    fig = px.line(
        df,
        x="date",
        y="portfolio_value",
        title="Portfolio Growth"
    )

    st.plotly_chart(fig, use_container_width=True)

elif page == "Risk Metrics":

    st.header("Risk Analytics")

    st.metric("Volatility", "18%")
    st.metric("Beta", "1.1")
    st.metric("Alpha", "0.09")

elif page == "Trade Logs":

    st.header("Trade Logs")

    trades = pd.DataFrame({
        "Asset": ["AAPL", "TSLA"],
        "Action": ["BUY", "SELL"],
        "Price": [180, 250],
        "Quantity": [10, 5]
    })

    st.dataframe(trades)