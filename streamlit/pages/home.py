import streamlit as st

if "data_meteo" not in st.session_state:
    st.session_state.data_meteo = None

st.title("Kristian Strøm's streamlit app for IND320")
