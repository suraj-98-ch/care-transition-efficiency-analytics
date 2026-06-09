import streamlit as st
import plotly.express as px
from utils.metrics import *
from utils.helpers import load_css
from components.footer import show_footer
from components.kpi_cards import show_kpis


load_css()

filtered_df = st.session_state["filtered_df"]

st.title("📊 Outcome Stability Analytics")

df = calculate_outcome_stability(filtered_df)

# -------------------------
# KPI Section
# -------------------------

show_kpis([
    (
        "Stability Score",
        f"{stability_score(df)}"
    ),
    (
        "Average Discharge Rate",
        f"{average_discharge_rate(df)}%"
    ),
    (
        "Volatility",
        f"{discharge_volatility(df)}"
    )
])

# -------------------------
# Daily Stability Trend
# -------------------------

fig1 = px.line(
    df,
    x="Date",
    y="Discharge_Effectiveness",
    title="Daily Outcome Performance"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# -------------------------
# Rolling Volatility
# -------------------------

df["Rolling_Volatility"] = (
    df["Discharge_Effectiveness"]
    .rolling(14)
    .std()
)

fig2 = px.line(
    df,
    x="Date",
    y="Rolling_Volatility",
    title="14-Day Rolling Volatility"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# -------------------------
# Monthly Stability
# -------------------------

monthly_df = df.copy()

monthly_df["Month"] = (
    monthly_df["Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_stability = (
    monthly_df
    .groupby("Month")["Discharge_Effectiveness"]
    .std()
    .reset_index()
)

fig3 = px.bar(
    monthly_stability,
    x="Month",
    y="Discharge_Effectiveness",
    title="Monthly Outcome Volatility"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

st.divider()

# -------------------------
# Assessment
# -------------------------

score = stability_score(df)

st.info(
    f"""
    Stability Score: {stability_score(df)}

    This analysis measures consistency in discharge
    outcomes and placement performance over time.
    Higher scores indicate more reliable reunification outcomes.
    """
)

st.subheader("Outcome Stability Assessment")

if score >= 90:
    st.success(
        "Highly stable placement outcomes."
    )

elif score >= 75:
    st.warning(
        "Moderately stable outcomes with some variability."
    )

else:
    st.error(
        "Outcome performance shows significant volatility."
    )

# -------------------------
# Key Findings
# -------------------------

st.subheader("Key Findings")

st.success(
    f"Stability Score: {score}"
)

st.info(
    f"Average Discharge Rate: {average_discharge_rate(df)}%"
)

st.warning(
    f"Observed Volatility: {discharge_volatility(df)}"
)

show_footer()