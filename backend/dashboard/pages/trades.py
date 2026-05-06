import streamlit as st
import pandas as pd

PAGE_CSS = """
<style>
body {
    background-color: #f2edf1;
    color: #1a1a1a;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1420 0%, #551f2e 100%);
}
.stDataFrame table {
    background-color: #ffffff;
}
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

st.markdown(
    "<div style='padding: 22px; border-radius: 24px; background: linear-gradient(135deg, #7f2437, #45131d); color:#f9ede8;'>"
    "<h1 style='margin:0;'>Trade Logs</h1>"
    "<p style='margin:8px 0 0 0; color:#dac8c9;'>Recent transactions, order status and profit/loss performance.</p>"
    "</div>",
    unsafe_allow_html=True,
)

trade_filter = st.selectbox("Filter by Asset", ["All", "AAPL", "TSLA", "MSFT", "AMZN"], index=0)

trades = pd.DataFrame({
    "Date": ["2025-05-01", "2025-05-02", "2025-05-03", "2025-05-04"],
    "Asset": ["AAPL", "TSLA", "MSFT", "AAPL"],
    "Action": ["BUY", "SELL", "BUY", "SELL"],
    "Price": [180, 250, 320, 185],
    "Quantity": [10, 5, 8, 12],
    "PnL": [200, -50, 120, 75],
    "Status": ["Completed", "Pending", "Completed", "Closed"],
})

if trade_filter != "All":
    trades = trades[trades["Asset"] == trade_filter]

st.dataframe(trades, use_container_width=True)

