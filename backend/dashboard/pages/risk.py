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
.stMetric {
    border-radius: 18px;
    background-color: #ffffff;
    border: 1px solid #e5d9db !important;
}
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

st.markdown(
    "<div style='padding: 22px; border-radius: 24px; background: linear-gradient(135deg, #7f2437, #45131d); color:#f9ede8;'>"
    "<h1 style='margin:0;'>Risk Metrics</h1>"
    "<p style='margin:8px 0 0 0; color:#dac8c9;'>Volatility, downside exposure and factor risk in one clean view.</p>"
    "</div>",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4, gap='large')
col1.metric("Volatility", "18%")
col2.metric("Beta", "1.12")
col3.metric("Alpha", "0.09")
col4.metric("Sortino Ratio", "1.44")

risk_factors = pd.DataFrame({
    "Category": ["Market", "Credit", "Liquidity", "Event", "Currency"],
    "Exposure": [72, 54, 38, 45, 28],
})

fig = px.bar(
    risk_factors,
    x="Exposure",
    y="Category",
    orientation="h",
    title="Risk Factor Exposure",
    template="plotly_white",
    color_discrete_sequence=["#a23851"],
)
fig.update_layout(
    plot_bgcolor="#f6eef0",
    paper_bgcolor="#f6eef0",
    font_color="#2a1f25",
    title_font_color="#2a1f25",
)

st.plotly_chart(fig, use_container_width=True)

