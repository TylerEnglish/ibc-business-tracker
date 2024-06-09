import streamlit as st
import pandas as pd

def app():
    st.title('📊 IBC Data Explorer Dashboard')

    with st.expander('About this app'):
        st.markdown('**What can this app do?**')
        st.markdown('**How to use the app?**')
        st.warning('To engage with the app:\n'
                   '1. Upload your excel sheet\n'
                   '2. Explore the dashboard')
        

    st.header("Introduction")

    st.header("Upload Actual Data")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

    if uploaded_file is not None:
        # Store the file in session state
        st.session_state.uploaded_file = uploaded_file
        
    else:
        st.info("Please upload an Excel file to get started")


    st.header("Demo")
    st.write("Example on Dummy Data")

    df = pd.read_excel('data/Student_Business_Test2.xlsx', sheet_name=["Daily Business Hours", "Inventory", "Sales", "Member Actions"])
    dbh_df = df['Daily Business Hours']
    inv_df = df["Inventory"]
    sale_df = df["Sales"]
    member_df = df["Member Actions"]

    st.write("How a Data Frame Looks")
    st.dataframe(dbh_df)

    st.write("Line Chart")


    st.markdown("[GitHub Repository](https://github.com/TylerEnglish/ibc-business-tracker)")
