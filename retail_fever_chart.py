import pandas as pd
import numpy as np
import plotly.express as px

# Load the data from the CSV file
df = pd.read_csv("OnlineRetail.csv")

# Convert the InvoiceDate column to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create a new column to represent the month of each transaction
df['Month'] = df['InvoiceDate'].dt.strftime('%Y-%m')

# Convert the Quantity and UnitPrice columns to numeric types
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

# Create a new column to represent the total sales for each transaction
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Use the InvoiceNo and Country columns to filter out rows with missing values
df.dropna(subset=['InvoiceNo', 'Country', 'TotalSales'], inplace=True)
df = df[df['TotalSales'] > 0]

# Group the data by month and country and calculate the total sales
df_grouped = df.groupby(['Month', 'Country'], as_index=False)['TotalSales'].sum()

# Create the fever chart using Plotly
fig = px.treemap(df_grouped, path=['Country', 'Month'], values='TotalSales',
                  color='TotalSales', color_continuous_scale='reds',
                  title='Total Sales by Month and Country')
fig.show()