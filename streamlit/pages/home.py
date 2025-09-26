import streamlit as st

# --- Initializations ---
# Data variables
if "data_meteo" not in st.session_state:
    st.session_state.data_meteo = None

# --- Frontend ---
st.title("Kristian Strøm's streamlit app for IND320")
st.write("Use the navigation menu to find the content.")
