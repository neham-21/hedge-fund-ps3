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
.stDataFrame table {
    background-color: #ffffff;
}
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

st.markdown(
    "<div style='padding: 22px; border-radius: 24px; background: linear-gradient(135deg, #7f2437, #45131d); color:#f9ede8;'>"
    "<h1 style='margin:0;'>Country Analysis</h1>"
    "<p style='margin:8px 0 0 0; color:#dac8c9;'>A polished burgundy dashboard for benchmark returns, AUM, and NAV insights.</p>"
    "</div>",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4, gap='large')
col1.metric("Portfolio Value", "$125.4k")
col2.metric("Sharpe Ratio", "1.82")
col3.metric("Daily Return", "+2.4%")
col4.metric("Max Drawdown", "-8.1%")

st.markdown(
    "<div style='display:flex; gap:20px; flex-wrap:wrap; margin-top:24px;'>"
    "<div style='flex:2; min-width:320px; background:#ffffff; border-radius:22px; padding:22px; border:1px solid #e5d9db;'>"
    "<h3 style='margin:0 0 12px 0; color:#2a1f25;'>Benchmark Return % by Country</h3>"
    "<p style='margin:0; color:#5d4b4e;'>Japan 4.1%, Singapore 4.1%, UK 3.9%, Germany 3.9%.</p>"
    "</div>"
    "<div style='flex:1; min-width:260px; background:#ffffff; border-radius:22px; padding:22px; border:1px solid #e5d9db;'>"
    "<h3 style='margin:0 0 12px 0; color:#2a1f25;'>Filters</h3>"
    "<p style='margin:0; color:#5d4b4e;'>Year, region and fund status available here.</p>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div style='display:grid; grid-template-columns:1.5fr 1fr; gap:20px; margin-top:20px;'>"
    "<div style='background:#ffffff; border-radius:22px; padding:22px; border:1px solid #e5d9db;'>"
    "<h3 style='margin:0 0 18px 0; color:#2a1f25;'>AUM USD by Country</h3>"
    "<div style='height:260px; display:flex; align-items:center; justify-content:center; color:#7d5a61;'>Chart placeholder</div>"
    "</div>"
    "<div style='background:#ffffff; border-radius:22px; padding:22px; border:1px solid #e5d9db;'>"
    "<h3 style='margin:0 0 18px 0; color:#2a1f25;'>NAV USD by Country</h3>"
    "<div style='height:260px; display:flex; align-items:center; justify-content:center; color:#7d5a61;'>Chart placeholder</div>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

