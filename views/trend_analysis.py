import streamlit as st
import plotly.express as px
import pandas as pd 
from utils.helpers import load_css
from components.footer import show_footer
from components.kpi_cards import show_kpis

load_css()

filtered_df = st.session_state["filtered_df"]

st.title("📈 Trend Analysis")

# -------------------------
# Calculate Metrics
# -------------------------

filtered_df["Transfer_Efficiency"] = (
    filtered_df["CBP_Transfers"] /
    filtered_df["CBP_Custody"]
) * 100

filtered_df["Discharge_Effectiveness"] = (
    filtered_df["HHS_Discharges"] /
    filtered_df["HHS_Care"]
) * 100

filtered_df["Pipeline_Throughput"] = (
    filtered_df["HHS_Discharges"] /
    filtered_df["CBP_Intake"].replace(0, 1)
) * 100

import numpy as np 
filtered_df.replace([np.inf, -np.inf],0,inplace=True)
df = filtered_df.fillna(0)

# -------------------------
# Monthly Summary
# -------------------------

monthly_df = df.copy()

monthly_df["Date"] = pd.to_datetime(
    monthly_df["Date"],
    errors="coerce"
)

monthly_df["Month"] = (
    monthly_df["Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_summary = (
    monthly_df
    .groupby("Month")
    .agg({
        "Transfer_Efficiency": "mean",
        "Discharge_Effectiveness": "mean",
        "Pipeline_Throughput": "mean"
    })
    .reset_index()
)

# -------------------------
# KPI Section
# -------------------------

avg_transfer = monthly_summary[
    "Transfer_Efficiency"
].mean()

avg_discharge = monthly_summary[
    "Discharge_Effectiveness"
].mean()

best_month = monthly_summary.loc[
    monthly_summary["Transfer_Efficiency"].idxmax(),
    "Month"
]

worst_month = monthly_summary.loc[
    monthly_summary["Transfer_Efficiency"].idxmin(),
    "Month"
]

show_kpis([
    (
        "Avg Transfer Efficiency",
        f"{avg_transfer:.2f}%"
    ),
    (
        "Avg Discharge Effectiveness",
        f"{avg_discharge:.2f}%"
    ),
    (
        "Best Month",
        best_month
    ),
    (
        "Worst Month",
        worst_month
    )
])

# -------------------------
# Chart 1
# -------------------------

fig1 = px.line(
    monthly_summary,
    x="Month",
    y="Transfer_Efficiency",
    title="Monthly Transfer Efficiency Trend"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# -------------------------
# Chart 2
# -------------------------

fig2 = px.line(
    monthly_summary,
    x="Month",
    y="Discharge_Effectiveness",
    title="Monthly Discharge Effectiveness Trend"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# -------------------------
# Chart 3
# -------------------------

fig3 = px.bar(
    monthly_summary,
    x="Month",
    y="Pipeline_Throughput",
    title="Monthly Pipeline Throughput Trend"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

# -------------------------
# Chart 4
# -------------------------

monthly_summary["Moving_Average_3M"] = (
    monthly_summary["Transfer_Efficiency"]
    .rolling(3)
    .mean()
)

fig4 = px.line(
    monthly_summary,
    x="Month",
    y="Moving_Average_3M",
    title="3-Month Moving Average"
)

st.plotly_chart(
    fig4,
    width="stretch"
)

st.divider()

# -------------------------
# Trend Assessment
# -------------------------

st.info(
    f"""
    Trend Analysis evaluates whether care transition
    performance is improving, stable, or declining over time.

    Average Transfer Efficiency: {avg_transfer:.2f}%
    Average Discharge Effectiveness: {avg_discharge:.2f}%
    """
)

first_period = (
    monthly_summary["Transfer_Efficiency"]
    .head(3)
    .mean()
)

last_period = (
    monthly_summary["Transfer_Efficiency"]
    .tail(3)
    .mean()
)

st.subheader("Trend Assessment")

if last_period > first_period:
    st.success(
        "📈 Transfer performance has improved over time."
    )

elif abs(last_period - first_period) < 2:
    st.info(
        "➡️ Transfer performance has remained relatively stable."
    )

else:
    st.warning(
        "📉 Transfer performance has declined over time."
    )

# -------------------------
# Key Findings
# -------------------------

st.subheader("Key Findings")

st.success(
    f"Average Transfer Efficiency: {avg_transfer:.2f}%"
)

st.info(
    f"Average Discharge Effectiveness: {avg_discharge:.2f}%"
)

st.warning(
    f"Average Pipeline Throughput: {monthly_summary['Pipeline_Throughput'].mean():.2f}%"
)

st.success(
    f"Best Performing Month: {best_month}"
)

st.error(
    f"Worst Performing Month: {worst_month}"
)

show_footer()