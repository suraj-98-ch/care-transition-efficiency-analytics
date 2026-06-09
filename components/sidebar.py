import streamlit as st
import pandas as pd

def get_filtered_data(df):

    with st.sidebar:

        st.title("📊 Analytics Control Panel")

        page = st.selectbox(
            "📑 Select Analytics Module",[
                "Home",
                "Executive Overview",
                "Transfer Efficiency",
                "Discharge Outcomes",
                "Outcome Stability",
                "Trend Analysis",
                "Research Insights",
                "Executive Summary",
                "Bottleneck Detection",
                "Care Pipeline"
            ]
        )

        st.divider()

        st.subheader("📅 Date Filter")

        start_date = st.date_input(
            "Start Date",
            df["Date"].min()
        )

        end_date = st.date_input(
            "End Date",
            df["Date"].max()
        )

        st.divider()

        # Selected Period

        days = (end_date - start_date).days

        st.subheader("📅 Selected Period")

        st.info(
            f"Analyzing {days} days of data"
        )

        st.divider()

        # Dataset Info

        st.subheader("📂 Dataset Info")

        st.write(
            f"Records: {len(df):,}"
        )

        st.write(
            f"Start: {df['Date'].min().date()}"
        )

        st.write(
            f"End: {df['Date'].max().date()}"
        )

        st.divider()

        # Quick Stats

        st.subheader("⚡ Quick Stats")

        st.metric(
            "Total Intake",
            f"{df['CBP_Intake'].sum():,.0f}"
        )

        st.metric(
            "Total Discharges",
            f"{df['HHS_Discharges'].sum():,.0f}"
        )

        st.divider()

        # Guide

        st.subheader("📖 Dashboard Guide")

        st.caption("""
Executive Overview → Overall KPIs

Transfer Efficiency → Transfer Analytics

Discharge Outcomes → Placement Analytics

Outcome Stability → Stability Tracking

Trend Analysis → Long-Term Trends
""")

    filtered_df = df[
        (df["Date"] >= pd.to_datetime(start_date))
        &
        (df["Date"] <= pd.to_datetime(end_date))
    ].copy()

    if filtered_df.empty:
        st.warning("No data available for the salected date range.")

    return page, filtered_df