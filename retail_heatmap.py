import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Pivot the data to create a table of total sales by country and month
df_pivot = df.pivot_table(index='Country', columns='Month', values='TotalSales', aggfunc='sum')

# Create the heatmap using Seaborn
plt.figure(figsize=(12,8))
sns.heatmap(df_pivot, cmap='YlGnBu')
plt.title('Total Sales by Country and Month')
plt.show()