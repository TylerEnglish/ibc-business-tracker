import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
    st.title('📊 IBC Data Explorer Dashboard')

    with st.expander('About this app'):
        st.markdown('**What can this app do?**')
        st.markdown('This app allows you to explore and analyze business data from Excel files.')
        st.markdown('**How to use the app?**')
        st.warning('To engage with the app:\n'
                   '1. Upload your Excel sheet\n'
                   '2. Navigate through different sections using the sidebar.\n'
                   '2. Explore the dashboard')

    st.header("Introduction")
    st.write("Welcome to the IBC Data Explorer Dashboard. This tool allows you to upload and analyze business data from Excel files. The app supports various data visualizations and summaries to help you understand your business metrics better.")

    st.header("Upload Actual Data")
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

    def plot_line_chart(df, title):
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=df, x=df["Date"], y=df["Stop Traffic"])
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel('Stop Traffic')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    if uploaded_file is not None:
        # Store the file in session state
        st.session_state.uploaded_file = uploaded_file

        # Read the uploaded file
        df = pd.read_excel(uploaded_file, sheet_name=["Daily Business Hours", "Inventory", "Sales", "Member Actions"])
        dbh_df = df['Daily Business Hours']
        inv_df = df["Inventory"]
        sale_df = df["Sales"]
        member_df = df["Member Actions"]

        st.write("Data from the uploaded file:")
        st.dataframe(dbh_df)

        st.header("Line Chart")
        plot_line_chart(dbh_df, "Daily Business Hours Line Chart")
    else:
        st.header("Demo")
        st.write("Example on Dummy Data")

        # Example with dummy data if no file is uploaded
        df = pd.read_excel('data/Student_Business_Test2.xlsx', sheet_name=["Daily Business Hours", "Inventory", "Sales", "Member Actions"])
        dbh_df = df['Daily Business Hours']
        inv_df = df["Inventory"]
        sale_df = df["Sales"]
        member_df = df["Member Actions"]

        st.write("How a Data Frame Looks")
        st.dataframe(dbh_df)

        st.write("Line Chart")
        plot_line_chart(dbh_df, "Dummy Data Line Chart")

    st.markdown("[GitHub Repository](https://github.com/TylerEnglish/ibc-business-tracker)")

