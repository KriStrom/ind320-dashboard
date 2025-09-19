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
df_meteo_jan
