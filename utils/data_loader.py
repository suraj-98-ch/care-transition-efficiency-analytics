import pandas as pd
import streamlit as st


@st.cache_data
def load_data():

    df = pd.read_csv("data/raw/uac_dataset.csv")

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"],errors="coerce")

    df = df.dropna(subset=["Date"])

    # Rename columns
    df = df.rename(
        columns={
            "Children apprehended and placed in CBP custody*": "CBP_Intake",
            "Children in CBP custody": "CBP_Custody",
            "Children transferred out of CBP custody": "CBP_Transfers",
            "Children in HHS Care": "HHS_Care",
            "Children discharged from HHS Care": "HHS_Discharges"
        }
    )

    numeric_cols = [
        "CBP_Intake",
        "CBP_Custody",
        "CBP_Transfers",
        "HHS_Care",
        "HHS_Discharges"
    ]
    for col in numeric_cols:
        df[col] = (
            df[col].astype(str).str.replace(",", "", regex=False)
        )
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )
        df[numeric_cols] = (
            df[numeric_cols].fillna(0)
        )
        df = df.sort_values("Date")

        df = df.reset_index(drop=True)

    return df