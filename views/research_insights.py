import streamlit as st
import pandas as pd
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer
from components.kpi_cards import show_kpis


load_css()

filtered_df = st.session_state["filtered_df"]

st.title("🔍 Research Insights & Recommendations")

# Metrics
avg_transfer = average_transfer_efficiency(filtered_df)
avg_discharge = average_discharge_effectiveness(filtered_df)
stability = stability_score(filtered_df)

st.subheader("Key Performance Indicators")

# -------------------------
# KPI Section
# -------------------------

show_kpis([
    (
        "Transfer Efficiency",
        f"{avg_transfer:.2f}%"
    ),
    (
        "Discharge Effectiveness",
        f"{avg_discharge:.2f}%"
    ),
    (
        "Outcome Stability",
        f"{stability:.2f}"
    )
])

st.divider()

st.info(
    f"""
    Executive Insight

    Average Transfer Efficiency: {avg_transfer:.2f}%

    Average Discharge Effectiveness: {avg_discharge:.2f}%

    Outcome Stability Score: {stability:.2f}

    These indicators collectively measure the effectiveness,
    reliability, and continuity of the care transition pipeline.
    """
)

# -------------------------
# Major Findings
# -------------------------

st.subheader("Major Findings")

if avg_transfer < 80:
    st.warning(
        "Transfer efficiency remains below the desired operational target."
    )
else:
    st.success(
        "Transfer efficiency is operating at a strong level."
    )

if avg_discharge < 5:
    st.error(
        "Discharge effectiveness is low, indicating slower sponsor placement outcomes."
    )
else:
    st.success(
        "Discharge effectiveness is performing well."
    )

if stability > 85:
    st.success(
        "Outcome performance remains relatively stable over time."
    )
else:
    st.warning(
        "Outcome stability shows noticeable variation."
    )

st.divider()

# -------------------------
# Bottleneck Summary
# -------------------------

st.subheader("Bottleneck Summary")

summary_data = {
    "Area": [
        "CBP Intake",
        "Transfer Process",
        "HHS Placement",
        "Outcome Stability"
    ],
    "Status": [
        "Stable",
        "Moderate Risk",
        "High Risk",
        "Stable"
    ]
}

summary_df = pd.DataFrame(summary_data)

st.dataframe(
    summary_df,
    width="stretch",
    hide_index=True
)

st.divider()

# -------------------------
# Recommendations
# -------------------------

st.subheader("Recommendations")

st.success(
    "1. Improve coordination between CBP and HHS transfer teams."
)

st.info(
    "2. Reduce administrative delays in sponsor verification."
)

st.success(
    "3. Implement weekly monitoring of discharge effectiveness."
)

st.warning(
    "4. Establish early-warning alerts for backlog accumulation."
)

st.info(
    "5. Set operational targets for transfer efficiency above 80%."
)

st.success(
    "6. Track outcome stability monthly."
)

st.warning(
    "7. Strengthen case management workflows to accelerate reunification."
)

st.divider()

# -------------------------
# Overall Assessment
# -------------------------

st.subheader("Overall System Health")

if (avg_transfer > 80 and avg_discharge > 5 and stability > 85):
    st.success(
        "Overall system performance is healthy and operating efficiently."
    )
else:
    st.warning(
        "System performance requires targeted operational improvements."
    )

show_footer()