import streamlit as st
import plotly.express as px
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer
from components.kpi_cards import show_kpis


load_css()

filtered_df = st.session_state["filtered_df"]

st.title("🏠 Discharge Outcome Analytics")



# Calculate Metrics
df = calculate_discharge_effectiveness(filtered_df)

# -------------------------
# KPI Section
# -------------------------

show_kpis([
    (
        "Average Discharge Effectiveness",
        f"{average_discharge_effectiveness(df)}%"
    ),
    (
        "Maximum Discharge Rate",
        f"{max_discharge_effectiveness(df)}%"
    ),
    (
        "Minimum Discharge Rate",
        f"{min_discharge_effectiveness(df)}%"
    )
])

# -------------------------
# Daily Trend
# -------------------------

fig1 = px.line(
    df,
    x="Date",
    y="Discharge_Effectiveness",
    title="Daily Discharge Effectiveness"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# -------------------------
# 7-Day Rolling Average
# -------------------------

df["Rolling_Discharge_7D"] = (
    df["Discharge_Effectiveness"]
    .rolling(7)
    .mean()
)

fig2 = px.line(
    df,
    x="Date",
    y="Rolling_Discharge_7D",
    title="7-Day Rolling Discharge Trend"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# -------------------------
# Monthly Performance
# -------------------------

monthly_df = df.copy()

monthly_df["Month"] = (
    monthly_df["Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_perf = (
    monthly_df
    .groupby("Month")["Discharge_Effectiveness"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    monthly_perf,
    x="Month",
    y="Discharge_Effectiveness",
    title="Monthly Placement Performance"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

st.divider()

# -------------------------
# Assessment
# -------------------------

avg_discharge = average_discharge_effectiveness(df)

st.info(
    f"""
    Average Discharge Effectiveness: {average_discharge_effectiveness(df)}%

    This metric evaluates how effectively children
    transition from HHS care to successful sponsor placement.
    """
)

st.subheader("Placement Outcome Assessment")

if avg_discharge > 10:
    st.success(
        "Excellent placement performance detected."
    )

elif avg_discharge > 5:
    st.warning(
        "Placement outcomes are stable but can improve."
    )

else:
    st.error(
        "Placement performance requires attention."
    )

# -------------------------
# Summary
# -------------------------

st.subheader("Key Findings")

st.success(
    f"Average Discharge Effectiveness: {avg_discharge}%"
)

st.info(
    f"Peak Discharge Performance: {max_discharge_effectiveness(df)}%"
)

st.warning(
    f"Lowest Discharge Performance: {min_discharge_effectiveness(df)}%"
)

show_footer()