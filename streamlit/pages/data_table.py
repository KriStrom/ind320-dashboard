import streamlit as st
from utils.data_loader import get_csv_data

st.title("Data table (simple)")

data_meteo = get_csv_data("data/open-meteo-subset.csv")
st.dataframe(data_meteo.head())