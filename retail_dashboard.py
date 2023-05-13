import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# Load the Online Retail dataset as a CSV file
df = pd.read_csv("OnlineRetail.csv", encoding='latin-1')
# Remove rows with missing values
df = df.dropna()

# Convert the InvoiceDate column to a datetime object
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Add a column for the total sales amount
df['TotalSales'] = df['Quantity'] * df['UnitPrice']

# Create a new dataframe with monthly sales data
monthly_sales = df.groupby(pd.Grouper(key='InvoiceDate', freq='M')).sum(numeric_only=
                                                                        True)
monthly_sales.reset_index(inplace=True)

# Create a new dataframe with top 10 most popular products
top_products = df.groupby('Description').sum(numeric_only=True).sort_values('Quantity', 
                                                                            ascending=False).head(10)
top_products.reset_index(inplace=True)

# Create a new dataframe with top 10 customers by total sales
top_customers = df.groupby('Customer').sum(numeric_only=True).sort_values('TotalSales'
                                                                            , ascending=
                                                                            False).head(10)
top_customers.reset_index(inplace=True)

# Create a subplot with two charts: monthly sales and top 10 products
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'bar'}, {'type': 'pie'}]])

# Add the monthly sales bar chart to the subplot
fig.add_trace(go.Bar(x=monthly_sales['InvoiceDate'], y=monthly_sales['TotalSales'], name
                     ='Monthly Sales'), row=1, col=1)

# Add the top 10 products pie chart to the subplot
fig.add_trace(go.Pie(labels=top_products['Description'], values=top_products['Quantity']
                     , name='Top 10 Products'), row=1, col=2)

# Update the subplot layout
fig.update_layout(title='Online Retail Dashboard')

# Show the dashboard
fig.show()

# Create a new dataframe with customer lifetime value and recency
clv = df.groupby('Customer').agg({'TotalSales': sum, 'InvoiceDate': max}).reset_index()
clv.rename(columns={'InvoiceDate': 'LastPurchaseDate'}, inplace=True)
clv['Recency'] = (pd.to_datetime('today') - clv['LastPurchaseDate']).dt.days
clv['CustomerLifetimeValue'] = clv['TotalSales'] * 0.2 / 0.8
clv = clv[['Customer', 'Recency', 'CustomerLifetimeValue']]

# Create a scatter plot of customer lifetime value by recency
fig = px.scatter(clv, x='Recency', y='CustomerLifetimeValue', color='Customer')

# Add labels and title
fig.update_layout(title='Customer Lifetime Value by Recency', xaxis_title=
                  'Recency (days)',
                  yaxis_title='Customer Lifetime Value ($)')

# Show the scatter plot
fig.show()