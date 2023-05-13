import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio

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

# Group the data by country and calculate the total sales
df_grouped = df.groupby('Country', as_index=False)['TotalSales'].sum()

# Sort the dataframe by total sales in descending order
df_grouped = df_grouped.sort_values('TotalSales', ascending=False)

# Create the dial gauge using Plotly
fig = go.Figure()

num_countries = 10  # Set the number of countries to display

fig.add_trace(go.Indicator(
    mode = "gauge+number",
    value = df_grouped['TotalSales'].iloc[0],
    title = {'text': "Total Sales by Country"},
    gauge = {
        'axis': {'range': [0, 2000000], 'tickwidth': 1, 'tickcolor': 'darkblue'},
        'bar': {'color': 'darkblue'},
        'bgcolor': 'white',
        'borderwidth': 2,
        'bordercolor': 'gray',
        'steps': [
            {'range': [0, df_grouped['TotalSales'].quantile(0.10)], 'color': 'lightgray'},
            {'range': [df_grouped['TotalSales'].quantile(0.10),
                       df_grouped['TotalSales'].quantile(0.20)], 'color': 'gray'},
            {'range': [df_grouped['TotalSales'].quantile(0.20), 
                       df_grouped['TotalSales'].quantile(0.30)], 'color': 'lightgray'},
            {'range': [df_grouped['TotalSales'].quantile(0.30), 
                       df_grouped['TotalSales'].quantile(0.40)], 'color': 'gray'},
            {'range': [df_grouped['TotalSales'].quantile(0.40), 
                       df_grouped['TotalSales'].quantile(0.50)], 'color': 'lightgray'},
            {'range': [df_grouped['TotalSales'].quantile(0.50), 
                       df_grouped['TotalSales'].quantile(0.60)], 'color': 'gray'},
            {'range': [df_grouped['TotalSales'].quantile(0.60), 
                       df_grouped['TotalSales'].quantile(0.70)], 'color': 'lightgray'},
            {'range': [df_grouped['TotalSales'].quantile(0.70), 
                       df_grouped['TotalSales'].quantile(0.80)], 'color': 'gray'},
            {'range': [df_grouped['TotalSales'].quantile(0.80), 
                       df_grouped['TotalSales'].quantile(0.90)], 'color': 'lightgray'},
            {'range': [df_grouped['TotalSales'].quantile(0.90), 
                       df_grouped['TotalSales'].max()], 'color': 'gray'}
        ],
        'threshold': {
            'line': {'color': 'red', 'width': 4},
            'thickness': 0.75,
            'value': df_grouped['TotalSales'].quantile(0.60)
        }
    },
    number = {'prefix': "$", 'font': {'size': 30}},
))

# Add annotations for the country names
for i in range(num_countries):
    if i < len(df_grouped):
        fig.add_annotation(x=0.5, y=0.5 - i*0.05, text=df_grouped['Country'].iloc[i], 
                           font=dict(size=20), showarrow=False)

# fig.show()
# Save the visualization as an HTML file
pio.write_html(fig, file='retail_dial_gauge.html', auto_open=True)