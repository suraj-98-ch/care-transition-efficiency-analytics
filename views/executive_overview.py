import streamlit as st
import plotly.express as px
from utils.metrics import *
from utils.helpers import load_css
from components.kpi_cards import show_kpis
from components.footer import show_footer


load_css()

filtered_df = st.session_state["filtered_df"]

st.title("📊 Executive Overview")


# -------------------------
# KPI Cards
# -------------------------

show_kpis([
    (
        "Total Intake",
        f"{total_intake(filtered_df):,.0f}"
    ),
    (
        "Total Transfers",
        f"{total_transfers(filtered_df):,.0f}"
    ),
    (
        "Total HHS Care",
        f"{total_hhs_population(filtered_df):,.0f}"
    ),
    (
        "Total Discharges",
        f"{total_discharges(filtered_df):,.0f}"
    )
])

st.divider()

show_kpis([
    (
        "Transfer Efficiency",
        f"{transfer_efficiency_ratio(filtered_df)}%"
    ),
    (
        "Discharge Effectiveness",
        f"{discharge_effectiveness(filtered_df)}%"
    ),
    (
        "Backlog Rate",
        f"{backlog_rate(filtered_df):,.0f}"
    )
])

st.divider()

# -------------------------
# Trend Charts
# -------------------------

fig1 = px.line(
    filtered_df,
    x="Date",
    y="CBP_Intake",
    title="Intake Trend"
)

st.plotly_chart(fig1, width="stretch")

fig2 = px.line(
    filtered_df,
    x="Date",
    y="CBP_Transfers",
    title="Transfer Trend"
)

st.plotly_chart(fig2, width="stretch")

fig3 = px.line(
    filtered_df,
    x="Date",
    y="HHS_Discharges",
    title="Discharge Trend"
)

st.plotly_chart(fig3, width="stretch")

show_footer()