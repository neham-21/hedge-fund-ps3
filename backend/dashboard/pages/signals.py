import streamlit as st
import pandas as pd
import plotly.express as px

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
    "<h1 style='margin:0;'>Trading Signals</h1>"
    "<p style='margin:8px 0 0 0; color:#dac8c9;'>Live buy/sell signals and confidence measures for portfolio strategies.</p>"
    "</div>",
    unsafe_allow_html=True,
)

signals = pd.DataFrame({
    "Date": ["2025-05-01", "2025-05-02", "2025-05-03", "2025-05-04"],
    "Asset": ["AAPL", "TSLA", "MSFT", "AMZN"],
    "Signal": ["BUY", "SELL", "BUY", "SELL"],
    "Price": [180, 250, 320, 145],
    "Confidence": ["High", "Medium", "High", "Low"],
})

st.dataframe(signals, use_container_width=True)

fig = px.scatter(
    signals,
    x="Date",
    y="Price",
    color="Signal",
    size=[15, 15, 15, 15],
    template="plotly_white",
)
fig.update_traces(marker=dict(line=dict(width=1, color='#4a1322')))
fig.update_layout(
    plot_bgcolor="#f6eef0",
    paper_bgcolor="#f6eef0",
    font_color="#2a1f25",
    title_font_color="#2a1f25",
)

st.plotly_chart(fig, use_container_width=True)

