import pandas as pd


def clean_data(df):

    # Create copy
    df = df.copy()

    # Remove duplicates
    df = df.drop_duplicates()

    numeric_cols = [
        "CBP_Intake",
        "CBP_Custody",
        "CBP_Transfers",
        "HHS_Care",
        "HHS_Discharges"
    ]

    df[numeric_cols] = df[numeric_cols].fillna(0)

    # Sort by date
    df = df.sort_values("Date")

    df = df.reset_index(drop=True)

    return df