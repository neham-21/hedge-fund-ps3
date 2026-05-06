import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Hedge Fund Dashboard",
    layout="wide",
)

PAGE_CSS = """
<style>
body {
    background-color: #f2edf1;
    color: #1a1a1a;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #3b1420 0%, #551f2e 100%);
    color: #f9ede8;
}
.css-18e3th9, .css-1d391kg {
    background-color: #f2edf1;
}
.stButton>button, button[kind="secondary"] {
    background-color: #7e2432;
    color: #f9ede8;
    border: 1px solid #5e1624;
    border-radius: 12px;
}
.stMetric {
    border-radius: 18px;
    background-color: #ffffff;
    border: 1px solid #e5d9db !important;
}
hr {
    border-color: rgba(0,0,0,0.08);
}
</style>
"""

st.markdown(PAGE_CSS, unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        "<div style='padding: 24px; border-radius: 24px; background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12);'>"
        "<h2 style='margin:0; color:#f9ede8;'>Hedge Dash</h2>"
        "<p style='margin:6px 0 0 0; color:#e9d2d8;'>Analytics, risk, trades and signals in one place.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["Overview", "Analytics", "Risk", "Trades", "Signals"],
        index=0,
    )
    st.markdown("---")
    st.markdown("### Filters")
    st.selectbox("Year", ["All", "2025", "2024"])
    st.selectbox("Country", ["All", "USA", "UK", "Japan", "India"])
    st.selectbox("Fund Status", ["All", "Active", "Closed"])
    st.markdown("---")
    st.markdown(
        "<div style='padding:12px; border-radius:18px; background:#471b28; color:#f8efe6;'>"
        "<strong>Pro Tip:</strong> Use the left menu to switch pages and review the latest portfolio metrics.</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    "<div style='padding: 24px; border-radius: 24px; background: linear-gradient(135deg, #7a2030, #38131d); margin-bottom:24px;'>"
    "<div style='display:flex; justify-content:space-between; align-items:center;'>"
    "<div><h1 style='margin:0; color:#f9ede8;'>Viewer Demographics</h1>"
    "<p style='margin:6px 0 0 0; color:#dac8c9;'>High-level portfolio and risk monitoring tailored for a hedge fund dashboard.</p></div>"
    "<div style='display:flex; gap:10px;'>"
    "<div style='background:#f9ede8; padding:12px 18px; border-radius:16px; color:#33131a; font-weight:600;'>Search</div>"
    "<div style='background:#5a1a2a; padding:12px 18px; border-radius:16px; color:#f9ede8;'>⚙️</div>"
    "</div>"
    "</div>"
    "</div>",
    unsafe_allow_html=True,
)

summary = pd.DataFrame({
    "Metric": ["Total Sales", "Total Orders", "Total Customers"],
    "Value": ["$59,690", "4,865", "2,245"],
    "Change": ["+12.4%", "+8.9%", "+13.4%"],
})

st.markdown("### Quick Snapshot")
st.dataframe(summary, use_container_width=True)

if page == "Overview":
    st.markdown("## Overview")
    st.markdown("---")
    st.write("A polished breakout of benchmark returns, AUM and NAV analytics.")
elif page == "Analytics":
    st.markdown("## Analytics")
    st.markdown("---")
    st.write("Portfolio growth, revenue trends, and strategy comparisons.")
elif page == "Risk":
    st.markdown("## Risk")
    st.markdown("---")
    st.write("Volatility, downside risk, and factor exposures.")
elif page == "Trades":
    st.markdown("## Trades")
    st.markdown("---")
    st.write("Newest trade activity and transaction performance.")
else:
    st.markdown("## Signals")
    st.markdown("---")
    st.write("Live buy/sell signals with confidence metrics.")
