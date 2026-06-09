import numpy as np

def total_intake(df):
    return df["CBP_Intake"].sum()


def total_transfers(df):
    return df["CBP_Transfers"].sum()


def total_hhs_population(df):
    return df["HHS_Care"].sum()


def total_discharges(df):
    return df["HHS_Discharges"].sum()


def transfer_efficiency_ratio(df):

    transfers = total_transfers(df)
    custody = df["CBP_Custody"].sum()

    if custody == 0:
        return 0

    return round((transfers / custody) * 100, 2)


def discharge_effectiveness(df):

    discharges = total_discharges(df)
    hhs = total_hhs_population(df)

    if hhs == 0:
        return 0

    return round((discharges / hhs) * 100, 2)


def backlog_rate(df):

    intake = total_intake(df)
    discharges = total_discharges(df)

    return intake - discharges

def pipeline_throughput(df):

    entries = total_intake(df)

    exits = total_discharges(df)

    if entries == 0:
        return 0

    return round((exits / entries) * 100, 2)

def calculate_transfer_efficiency(df):

    temp_df = df.copy()

    temp_df["Transfer_Efficiency"] = (
        temp_df["CBP_Transfers"] /
        temp_df["CBP_Custody"]
    ) * 100

    temp_df["Transfer_Efficiency"] = (
        temp_df["Transfer_Efficiency"]
        .fillna(0)
        .replace([float("inf"), float("-inf")], 0)
    )

    return temp_df


def average_transfer_efficiency(df):

    df = calculate_transfer_efficiency(df)

    return round(
        df["Transfer_Efficiency"].mean(),
        2
    )


def max_transfer_efficiency(df):

    df = calculate_transfer_efficiency(df)

    return round(
        df["Transfer_Efficiency"].max(),
        2
    )


def min_transfer_efficiency(df):

    df = calculate_transfer_efficiency(df)

    return round(
        df["Transfer_Efficiency"].min(),
        2
    )

def calculate_discharge_effectiveness(df):

    temp_df = df.copy()

    temp_df["Discharge_Effectiveness"] = (
        temp_df["HHS_Discharges"] /
        temp_df["HHS_Care"]
    ) * 100

    temp_df["Discharge_Effectiveness"] = (
        temp_df["Discharge_Effectiveness"]
        .fillna(0)
        .replace([float("inf"), float("-inf")], 0)
    )

    return temp_df


def average_discharge_effectiveness(df):

    df = calculate_discharge_effectiveness(df)

    return round(
        df["Discharge_Effectiveness"].mean(),
        2
    )


def max_discharge_effectiveness(df):

    df = calculate_discharge_effectiveness(df)

    return round(
        df["Discharge_Effectiveness"].max(),
        2
    )


def min_discharge_effectiveness(df):

    df = calculate_discharge_effectiveness(df)

    return round(
        df["Discharge_Effectiveness"].min(),
        2
    )

def calculate_backlog(df):

    temp_df = df.copy()

    temp_df["Backlog"] = (
        temp_df["CBP_Intake"]
        - temp_df["HHS_Discharges"]
    )

    return temp_df


def average_backlog(df):

    df = calculate_backlog(df)

    return round(
        df["Backlog"].mean(),
        2
    )


def max_backlog(df):

    df = calculate_backlog(df)

    return round(
        df["Backlog"].max(),
        2
    )

def min_backlog(df):

    df = calculate_backlog(df)

    return round(
        df["Backlog"].min(),
        2
    )

import numpy as np


def calculate_outcome_stability(df):

    temp_df = df.copy()

    temp_df["Discharge_Effectiveness"] = (
        temp_df["HHS_Discharges"] /
        temp_df["HHS_Care"]
    ) * 100

    temp_df["Discharge_Effectiveness"] = (
        temp_df["Discharge_Effectiveness"]
        .fillna(0)
        .replace([float("inf"), float("-inf")], 0)
    )

    return temp_df


def stability_score(df):

    df = calculate_outcome_stability(df)

    std = df["Discharge_Effectiveness"].std()

    score = max(0, 100 - std * 10)

    return round(score, 2)


def average_discharge_rate(df):

    df = calculate_outcome_stability(df)

    return round(
        df["Discharge_Effectiveness"].mean(),
        2
    )


def discharge_volatility(df):

    df = calculate_outcome_stability(df)

    return round(
        df["Discharge_Effectiveness"].std(),
        2
    )