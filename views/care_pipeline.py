import streamlit as st
import plotly.graph_objects as go
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer


load_css()

filtered_df = st.session_state["filtered_df"]
st.title("🔄 Care Pipeline Flow")

# Load Data



# -------------------------
# KPIs
# -------------------------

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Intake",
    f"{total_intake(filtered_df):,.0f}"
)

col2.metric(
    "Total Transfers",
    f"{total_transfers(filtered_df):,.0f}"
)

col3.metric(
    "Total HHS Care",
    f"{total_hhs_population(filtered_df):,.0f}"
)

col4.metric(
    "Total Discharges",
    f"{total_discharges(filtered_df):,.0f}"
)

col5.metric(
    "Pipeline Throughput",
    f"{pipeline_throughput(filtered_df)}%"
)

st.divider()

# -------------------------
# Sankey Data
# -------------------------

intake = total_intake(filtered_df)
transfers = total_transfers(filtered_df)
hhs = total_hhs_population(filtered_df)
discharges = total_discharges(filtered_df)

fig = go.Figure(
    go.Sankey(
        node=dict(
            pad=20,
            thickness=20,
            label=[
                "CBP Intake",
                "CBP Custody",
                "HHS Care",
                "Sponsor Placement"
            ]
        ),

        link=dict(
            source=[0, 1, 2],
            target=[1, 2, 3],
            value=[
                intake,
                transfers,
                discharges
            ]
        )
    )
)

fig.update_layout(
    title="Care Transition Pipeline Flow",
    height=600
)

st.plotly_chart(
    fig,
    width="stretch"
)

st.divider()

# -------------------------
# Flow Summary
# -------------------------

st.subheader("Pipeline Summary")

st.write(f"Total Children Entering System: {intake:,.0f}")

st.write(f"Children Transferred to HHS: {transfers:,.0f}")

st.write(f"Children Discharged from HHS: {discharges:,.0f}")

st.write(
    f"Overall Throughput Rate: "
    f"{pipeline_throughput(filtered_df)}%"
)
show_footer()