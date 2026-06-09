import streamlit as st

def show_navigation():

    pages = {
        "Executive Overview": "executive_overview",
        "Transfer Efficiency": "transfer_efficiency",
        "Discharge Outcomes": "discharge_outcomes",
        "Outcome Stability": "outcome_stability",
        "Trend Analysis": "trend_analysis",
        "Research Insights": "research_insights",
        "Executive Summary": "executive_summary",
        "Bottleneck Detection": "bottleneck_detection",
        "Care Pipeline": "care_pipeline"
    }

    selected = st.sidebar.selectbox(
        "Select Page",
        list(pages.keys())
    )

    return pages[selected]