import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load the data from the CSV file
df = pd.read_csv("OnlineRetail.csv")

# Convert the InvoiceDate column to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create a new column to represent the date of each transaction
df['Date'] = df['InvoiceDate'].dt.date

# Convert the Quantity and UnitPrice columns to numeric types
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')

# Create a new column to represent the total sales for each transaction
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Use the InvoiceNo and Country columns to filter out rows with missing values
df.dropna(subset=['InvoiceNo', 'Country', 'TotalSales'], inplace=True)
df = df[df['TotalSales'] > 0]

# Group the data by date and calculate the total sales
df_grouped = df.groupby(['Date'], as_index=False)['TotalSales'].sum()

# Create a calendar fever chart using Plotly
fig = go.Figure(data=go.Heatmap(
        x=df_grouped['Date'],
        y=['Sales'],
        z=[df_grouped['TotalSales']],
        colorscale='Reds'
))

# Set the axis labels and title
fig.update_layout(
    title='Total Sales by Date',
    title_x=0.5,
    xaxis=dict(
        title='Date',
        tickformat='%Y-%m-%d'
    ),
    yaxis=dict(
        visible=False
    )
)

fig.show()