import streamlit as st
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer
from components.kpi_cards import show_kpis

load_css()

filtered_df = st.session_state["filtered_df"]

st.title("📋 Executive Summary")

# -------------------------
# Core Metrics
# -------------------------

avg_transfer = average_transfer_efficiency(filtered_df)
avg_discharge = average_discharge_effectiveness(filtered_df)
stability = stability_score(filtered_df)

st.subheader("Executive Dashboard")

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
    Executive Overview

    Transfer Efficiency: {avg_transfer:.2f}%

    Discharge Effectiveness: {avg_discharge:.2f}%

    Outcome Stability: {stability:.2f}

    This dashboard evaluates the efficiency,
    continuity, and reliability of the UAC care
    transition pipeline from intake through placement.
    """
)

# -------------------------
# Project Objective
# -------------------------

st.subheader("Project Objective")

st.write("""
Evaluate the efficiency of the UAC care transition pipeline by
analyzing transfers from CBP custody into HHS care, discharge
performance, backlog accumulation, and overall placement outcomes.
""")

st.divider()

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

st.success(
    f"Outcome Stability Score: {stability:.2f}"
)

st.warning(
    "Transfer performance varies across reporting periods."
)

st.warning(
    "Placement outcomes remain stable but discharge effectiveness is relatively low."
)

st.info(
    "Bottleneck patterns suggest opportunities to improve sponsor placement speed."
)

st.divider()

# -------------------------
# Risks
# -------------------------

st.subheader("Operational Risks")

st.error(
    "Delays in sponsor placement can increase care duration."
)

st.warning(
    "Transfer efficiency below target levels may create system congestion."
)

st.warning(
    "Backlog accumulation can reduce operational responsiveness."
)

st.error(
    "Variability in discharge performance may impact reunification timelines."
)

st.divider()

# -------------------------
# Recommendations
# -------------------------

st.subheader("Recommendations")

st.success(
    "Improve coordination between CBP and HHS transfer operations."
)

st.success(
    "Enhance sponsor verification workflows."
)

st.info(
    "Introduce automated backlog monitoring."
)

st.info(
    "Establish monthly performance reviews."
)

st.success(
    "Create transfer efficiency benchmarks above 80%."
)

st.warning(
    "Expand outcome stability monitoring."
)

st.success(
    "Accelerate discharge processing through workflow optimization."
)

st.divider()

# -------------------------
# Overall Assessment
# -------------------------

st.subheader("Overall Assessment")

if (avg_transfer >= 80 and avg_discharge >= 5 and stability >= 85):
    st.success(
        "The care transition system demonstrates strong operational performance."
    )
else:
    st.warning(
        "The system is functioning but would benefit from targeted process improvements."
    )

st.divider()

# -------------------------
# Conclusion
# -------------------------

st.subheader("Conclusion")

st.write("""
The analysis demonstrates that the UAC care transition pipeline
is generally stable but presents opportunities to improve transfer
efficiency, discharge effectiveness, and placement timelines.

Continuous monitoring of transition performance and outcome stability
can support better operational decision-making and faster reunification outcomes.
""")

show_footer()