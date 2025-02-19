import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("DATA SWEEPER")
st.write("Transfrom your files between CSV and Excel formats with built in data cleaning and visualization")

uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files: 
    for file in uploaded_files:
        file_ext = os.path.splittext(file.name)[-1].lower()
