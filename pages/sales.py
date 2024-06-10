import streamlit as st
import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title='Sales Dashboard', page_icon='📊')
st.title('Sales Dashboard')

if 'uploaded_file' in st.session_state:
    uploaded_file = st.session_state.uploaded_file

    dataframe = pd.read_excel(uploaded_file, sheet_name=['Sales'])
    df = dataframe['Sales']

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar filters
st.sidebar.header('Filters')
date_range = st.sidebar.date_input('Date range', value=[df['Date'].min().date(), df['Date'].max().date()])
items = st.sidebar.multiselect('Select Items Sold', options=df['Item Sold'].unique(), default=df['Item Sold'].unique())

# Convert date_range to datetime
date_range = [pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])]

# Filter data
filtered_data = df[(df['Date'] >= date_range[0]) & (df['Date'] <= date_range[1])]
if items:
    filtered_data = filtered_data[filtered_data['Item Sold'].isin(items)]

# Display data
st.header('Filtered Data')
st.dataframe(filtered_data)

# # Sales by Date (Line Chart)
# st.header('Sales by Date')
# sales_by_date = filtered_data.groupby('Date')['Total Sales'].sum()
# fig, ax = plt.subplots()
# ax.plot(sales_by_date.index, sales_by_date.values, marker='o')
# ax.set_xlabel('Date')
# ax.set_ylabel('Total Sales')
# ax.set_title('Sales by Date')
# st.pyplot(fig)

# Sales by Date (Line Chart)
st.header('Sales by Date')
sales_by_date = filtered_data.groupby('Date')['Total Sales'].sum()
fig, ax = plt.subplots()
ax.plot(sales_by_date.index, sales_by_date.values, marker='o')
ax.set_xlabel('Date')
ax.set_ylabel('Total Sales')
ax.set_title('Sales by Date')
ax.tick_params(axis='x', rotation=45)  # Make x-axis labels horizontal
st.pyplot(fig)

# Sales by Item Sold (Bar Chart)
st.header('Sales by Item Sold')
sales_by_item = filtered_data.groupby('Item Sold')['Total Sales'].sum()
fig, ax = plt.subplots()
sales_by_item.plot(kind='bar', ax=ax)
ax.set_xlabel('Item Sold')
ax.set_ylabel('Total Sales')
ax.set_title('Sales by Item Sold')
ax.tick_params(axis='x', rotation=45)
st.pyplot(fig)

# Quantity Sold by Item Sold (Horizontal Bar Chart)
st.header('Quantity Sold by Item Sold')
quantity_by_item = filtered_data.groupby('Item Sold')['Quantity Sold'].sum()
fig, ax = plt.subplots()
quantity_by_item.plot(kind='barh', ax=ax)
ax.set_xlabel('Quantity Sold')
ax.set_ylabel('Item Sold')
ax.set_title('Quantity Sold by Item Sold')
st.pyplot(fig)

# Advanced Chart: Pair Plot of Sales Data
st.header('Pair Plot of Sales Data')
sns.pairplot(filtered_data, diag_kind='kde', markers='+')
st.pyplot(plt.gcf())