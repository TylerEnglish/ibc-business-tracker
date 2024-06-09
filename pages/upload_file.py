import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload Excel File Here")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    df = pd.read_excel(uploaded_file)
