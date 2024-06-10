import streamlit as st
import pandas as pd

# Page title
st.set_page_config(page_title='Upload Data', page_icon='📊')
st.title('Upload Data')

uploaded_file = st.file_uploader("Upload Excel File Here", type=["xlsx"])
if uploaded_file is not None:
    # Store the file in session state
    st.session_state.uploaded_file = uploaded_file

if 'uploaded_file' in st.session_state:
    df = st.session_state.uploaded_file

print(st.session_state)