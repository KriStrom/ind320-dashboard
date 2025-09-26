import pandas as pd
import streamlit as st

# Adding plotly backend to pandas
pd.options.plotting.backend = "plotly"


# csv to dataframe
@st.cache_data
def get_csv_data(path):
    return pd.read_csv(path)