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
    "<h1 style='margin:0;'>Strategy Analytics</h1>"
    "<p style='margin:8px 0 0 0; color:#dac8c9;'>Portfolio performance and country-level analytics in a refined burgundy layout.</p>"
    "</div>",
    unsafe_allow_html=True,
)

timeline = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Portfolio": [100000, 108000, 105000, 120000, 125000],
})

allocation = pd.DataFrame({
    "Country": ["Japan", "Singapore", "UK", "Germany", "USA", "India"],
    "AUM": [55, 49, 46, 46, 45, 41],
})

fig1 = px.line(
    timeline,
    x="Month",
    y="Portfolio",
    markers=True,
    title="Portfolio Growth",
    template="plotly_white",
)
fig1.update_traces(line_color="#7b2540", marker_color="#9f3b58")
fig1.update_layout(
    plot_bgcolor="#f6eef0",
    paper_bgcolor="#f6eef0",
    font_color="#2a1f25",
    title_font_color="#2a1f25",
)

fig2 = px.bar(
    allocation,
    x="Country",
    y="AUM",
    title="AUM USD by Country",
    template="plotly_white",
    color_discrete_sequence=["#a23851"],
)
fig2.update_layout(
    plot_bgcolor="#f6eef0",
    paper_bgcolor="#f6eef0",
    font_color="#2a1f25",
    title_font_color="#2a1f25",
)

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

