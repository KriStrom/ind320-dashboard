import streamlit as st
from utils.data_loader import get_csv_data
import pandas as pd

# Page title
st.title("Meteo data for the 1st month of 2025")
 
# Load data
data_meteo = get_csv_data("data/open-meteo-subset.csv")


# Transform the data
data_meteo["time"] = pd.to_datetime(data_meteo["time"])
df_meteo_jan = data_meteo[data_meteo["time"].dt.month == 1]


# Prepare table: each *original column* (except 'time') is a row
rows = []
for col in df_meteo_jan.columns:
    if col != "time":
        rows.append({
            "Parameter": col,
            "Values": df_meteo_jan[col].values  # series of values for January
        })

table_df = pd.DataFrame(rows)


# Display the table with a line chart per row
st.dataframe(
    table_df,
    column_config={
        "Parameter": st.column_config.TextColumn("Parameter"),
        "Values": st.column_config.LineChartColumn(
            "January Data",
            y_min=None,  # auto-scale
            y_max=None
        )
    },
    hide_index=True
)
