import streamlit as st
import plotly.express as px
from utils.metrics import *
from utils.helpers import load_css
from components.kpi_cards import show_kpis
from components.footer import show_footer



load_css()
filtered_df = st.session_state["filtered_df"]

st.title("🚚 Transfer Efficiency Analytics")

# Calculate Efficiency
df = calculate_transfer_efficiency(filtered_df)

# --------------------------
# KPI Section
# --------------------------

col1, col2, col3 = st.columns(3)
show_kpis([
    (
        "Average Efficiency",
        f"{average_transfer_efficiency(df)}%"
    ),
    (
        "Maximum Efficiency",
        f"{max_transfer_efficiency(df)}%"
    ),
    (
        "Minimum Efficiency",
        f"{min_transfer_efficiency(df)}%"
    )
])

# --------------------------
# Daily Trend
# --------------------------

fig1 = px.line(
    df,
    x="Date",
    y="Transfer_Efficiency",
    title="Daily Transfer Efficiency Trend"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# --------------------------
# Rolling Average
# --------------------------

df["Rolling_7_Day"] = (
    df["Transfer_Efficiency"]
    .rolling(7)
    .mean()
)

fig2 = px.line(
    df,
    x="Date",
    y="Rolling_7_Day",
    title="7-Day Rolling Average"
)

st.plotly_chart(
    fig2,
    width="stretch"
)

# --------------------------
# Monthly Analysis
# --------------------------

monthly_df = df.copy()

monthly_df["Month"] = (
    monthly_df["Date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_efficiency = (
    monthly_df
    .groupby("Month")["Transfer_Efficiency"]
    .mean()
    .reset_index()
)

fig3 = px.bar(
    monthly_efficiency,
    x="Month",
    y="Transfer_Efficiency",
    title="Monthly Transfer Efficiency"
)

st.plotly_chart(
    fig3,
    width="stretch"
)

st.divider()

# --------------------------
# Insight Section
# --------------------------

avg_efficiency = average_transfer_efficiency(df)

st.info(
    f"""
    Average Transfer Efficiency: {average_transfer_efficiency(df)}%

    This metric measures how effectively children are transferred
    from CBP custody into HHS care.
    """
)

st.subheader("Transfer Efficiency Assessment")

if avg_efficiency > 90:
    st.success(
        "Excellent transfer performance detected."
    )

elif avg_efficiency > 70:
    st.warning(
        "Transfer performance is acceptable but can improve."
    )

else:
    st.error(
        "Transfer efficiency requires attention."
    )

show_footer()