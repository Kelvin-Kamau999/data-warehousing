import pandas as pd
import plotly.graph_objects as go

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

# Calculate the average unit price by country
df_avg_price = df.groupby(['Country'], as_index=False)['UnitPrice'].mean()

# Create a dial gauge to show the average unit price by country
fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = df_avg_price[df_avg_price['Country']=='United Kingdom']['UnitPrice'].values[0],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Average Unit Price in United Kingdom"},
    gauge = {
        'axis': {'range': [0, 10]},
        'steps' : [
            {'range': [0, 2], 'color': "lightgray"},
            {'range': [2, 4], 'color': "gray"},
            {'range': [4, 6], 'color': "lightgreen"},
            {'range': [6, 8], 'color': "green"},
            {'range': [8, 10], 'color': "darkgreen"}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': df_avg_price['UnitPrice'].mean()}
    }
))

fig.show()