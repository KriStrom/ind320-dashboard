import streamlit as st
import pandas as pd
import plotly.express as px
import plotly
from utils.data_loader import get_csv_data

st.title("Data table (advanced)")

# Load data
if st.session_state.data_meteo is None:
    data_meteo = get_csv_data("data/open-meteo-subset.csv")
    # Transform the data
    data_meteo["time"] = pd.to_datetime(data_meteo["time"])
    data_meteo = data_meteo.rename(columns={
        'temperature_2m (°C)': 'Temperature',
        'precipitation (mm)': 'Precipitation',
        'wind_speed_10m (m/s)': 'Wind speed',
        'wind_gusts_10m (m/s)': 'Wind gusts',
        'wind_direction_10m (°)': 'Wind direction'
    })

# Drop down menu
selected_drop_down = st.selectbox(label="Select what do display:",
             options=[
                 'Everything',
                 'Temperature',
                 'Precipitation',
                 'Wind speed',
                 'Wind gusts',
                 'Wind direction'
                      ], 
             index=0,
             accept_new_options=False
             )

# Time range selector
months = data_meteo["time"].dt.month.unique()
months = sorted(months)

start_time, end_time = st.select_slider(label="Select a timeframe of months (jan=1, dec=12):",
                 options=months,
                 value=(1, 1))
# Store the filtered data for later use
filtered_data = data_meteo[data_meteo["time"].dt.month.between(start_time, end_time)]




# Display plot depending on the drop down option
if selected_drop_down == 'Everything':
    for col in data_meteo.columns.drop("time"):
        fig = px.line(filtered_data, x="time", y=col, title=col)
        st.plotly_chart(fig)
else:
    fig = px.line(filtered_data, x="time", y=selected_drop_down, title=selected_drop_down)
    st.plotly_chart(fig)


