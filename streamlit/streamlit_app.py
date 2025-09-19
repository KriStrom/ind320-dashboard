import streamlit as st
import pandas as pd


# --- Page setup ---
page_home = st.Page(
    page="pages/home.py",
    title="Home",
    default=True,
)

page_data_table = st.Page(
    page="pages/data_table.py",
    title="Data table",
)

page_data_advanced = st.Page(
    page="pages/data_advanced.py",
    title="Data table - advanced",
)


# --- Navigation menu ----
pg = st.navigation(pages=[page_home, page_data_table, page_data_advanced])
# Run navigation
pg.run()