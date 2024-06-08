import pandas as pd

# Read Excel file with multiple sheets
xls = pd.read_excel("data/Student_Business_Template_Test.xlsx", sheet_name=['Daily Business Hours', 'Inventory'])

# Access individual sheets using sheet names
sheet1_df = xls['Daily Business Hours']
sheet2_df = xls['Inventory']

sheet1_df
