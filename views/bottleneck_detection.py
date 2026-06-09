import streamlit as st
import plotly.express as px
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer
from components.sidebar import get_filtered_data

load_css()

filtered_df = st.session_state["filtered_df"]

st.title("🚨 Bottleneck Detection Analytics")


# Calculate Backlog
df = calculate_backlog(filtered_df)

# -------------------------
# KPI Section
# -------------------------

col1, col2 = st.columns(2)

col1.metric(
    "Average Daily Backlog",
    f"{average_backlog(df):,.0f}"
)

col2.metric(
    "Maximum Daily Backlog",
    f"{max_backlog(df):,.0f}"
)

st.divider()

# -------------------------
# Backlog Trend
# -------------------------

fig1 = px.line(
    df,
    x="Date",
    y="Backlog",
    title="Daily Backlog Trend"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# -------------------------
# Rolling Backlog
# -------------------------

df["Rolling_Backlog"] = (
    df["Backlog"]
    .rolling(7)
    .mean()
)

fig2 = px.line(
    df,
    x="Date",
    y="Rolling_Backlog",
    title="7-Day Rolling Backlog"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# -------------------------
# High Risk Days
# -------------------------

high_risk = df[
    df["Backlog"] > df["Backlog"].quantile(0.90)
]

st.subheader("High Backlog Days")

st.dataframe(
    high_risk[
        [
            "Date",
            "Backlog"
        ]
    ],
    width="stretch"
)

# -------------------------
# Assessment
# -------------------------

st.subheader("Bottleneck Assessment")

avg_backlog_value = average_backlog(df)

if avg_backlog_value > 0:
    st.warning(
        "Persistent backlog accumulation detected."
    )
else:
    st.success(
        "No significant backlog accumulation detected."
    )

show_footer()