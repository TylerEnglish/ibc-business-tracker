import streamlit as st
import pandas as pd

def app():
    st.title('📊 Sales Data')

    if 'uploaded_file' in st.session_state:
        uploaded_file = st.session_state.uploaded_file
        
        # Load data
        df = pd.read_excel(uploaded_file, sheet_name=["Sales", "Daily Business Hours", "Inventory"])
        dbh_df = df["Daily Business Hours"]
        inv_df = df["Inventory"]
        sale_df = df["Sales"]

        st.subheader('Sales Data from Uploaded File')
        
        # Display DataFrame
        st.dataframe(sale_df)

        st.subheader("Inventory")
        st.dataframe(inv_df)

        st.subheader("Daily Business Hours")
        st.dataframe(dbh_df)
        
    else:
        st.info("Please upload an Excel file on the Home page to get started")
