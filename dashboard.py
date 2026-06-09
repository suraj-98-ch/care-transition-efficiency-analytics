import streamlit as st
from utils.helpers import load_css
from utils.data_loader import load_data
from utils.data_cleaning import clean_data
from components.sidebar import get_filtered_data

st.set_page_config(
    page_title="Care Transition Analytics",
    page_icon="📊",
    layout="wide"
)

load_css()

#-----load data -------
df = load_data()
df = clean_data(df)
page, filtered_df = get_filtered_data(df)
st.session_state["filtered_df"] = filtered_df

# =========================
# PAGE ROUTING
# =========================

if page == "Executive Overview":
    exec(open("views/executive_overview.py", encoding="utf-8").read(),globals())

elif page == "Transfer Efficiency":
    exec(open("views/transfer_efficiency.py", encoding="utf-8").read(),globals())

elif page == "Discharge Outcomes":
    exec(open("views/discharge_outcomes.py", encoding="utf-8").read(),globals())

elif page == "Outcome Stability":
    exec(open("views/outcome_stability.py", encoding="utf-8").read(),globals())

elif page == "Trend Analysis":
    exec(open("views/trend_analysis.py", encoding="utf-8").read(),globals())

elif page == "Research Insights":
    exec(open("views/research_insights.py", encoding="utf-8").read(),globals())

elif page == "Executive Summary":
    exec(open("views/executive_summary.py", encoding="utf-8").read(),globals())

elif page == "Bottleneck Detection":
    exec(open("views/bottleneck_detection.py", encoding="utf-8").read(),globals())

elif page == "Care Pipeline":
    exec(open("views/care_pipeline.py", encoding="utf-8").read(),globals())

#-------HOME PAGE ---------

else:

    st.title("📊 Care Transition Efficiency & Placement Outcome Analytics")

    st.markdown("""
    ### Executive Analytics Dashboard

    This dashboard evaluates the efficiency of the UAC care transition pipeline.

    #### Key Focus Areas

    - CBP → HHS Transfer Efficiency
    - Discharge & Placement Outcomes
    - Backlog Detection
    - Outcome Stability
    - Trend Analysis
    - Executive Insights & Recommendations
    """)
    
#---------- Executive KPI Summary----------

    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(
    "Total Intake",
    f"{filtered_df['CBP_Intake'].sum():,.0f}"
    )

    col2.metric(
    "Transfers",
    f"{filtered_df['CBP_Transfers'].sum():,.0f}"
    )

    col3.metric(
    "HHS Care",
    f"{filtered_df['HHS_Care'].sum():,.0f}"
    )

    col4.metric(
    "Discharges",
    f"{filtered_df['HHS_Discharges'].sum():,.0f}"
    )

    st.divider()
    
    #-------------- Dataset Summary -----------
    st.subheader("📂 Dataset Summary")

    st.write(
    f"Records Available: {len(filtered_df):,}"
    )

    st.write(
    f"Start Date: {filtered_df['Date'].min().date()}"
    )

    st.write(
    f"End Date: {filtered_df['Date'].max().date()}"
    )

    st.divider()

    #----- Dashboard Highlights ------

    col1, col2, col3 = st.columns(3)
    col1.info("📈 9 Analytics Modules")
    col2.info("📊 Process Efficiency Monitoring")
    col3.info("🏛 Government Policy Insights")
    st.success("9 Analytics Modules Available • Use the Analytics Control Panel to explore the dashboard.")
