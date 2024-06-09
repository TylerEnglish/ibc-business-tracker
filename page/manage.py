import streamlit as st
import pandas as pd

def app():
    st.title('📊 Manage Data')

    if 'uploaded_file' in st.session_state:
        uploaded_file = st.session_state.uploaded_file
        
        # Load data
        df = pd.read_excel(uploaded_file, sheet_name=["Member Actions"])
        member_df = df["Member Actions"]

        st.subheader('Member Actions Data from Uploaded File')
        st.dataframe(member_df)
        
    else:
        st.info("Please upload an Excel file on the Home page to get started")
