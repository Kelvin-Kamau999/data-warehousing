import plotly.graph_objs as go
import plotly.colors as colors
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
import webbrowser

# Read data from CSV file
df = pd.read_csv('data2.csv')

# Create bar chart showing the number of products by type
bar_fig = go.Figure(go.Bar(
    x=df['product_type'].unique(),
    y=df.groupby('product_type').count()['product_id'],
    marker_color=colors.qualitative.Plotly,
    text=df.groupby('product_type').count()['product_id'],
    textposition='auto',
    name='Number of Products by Type'
))

# Create scatter plot showing the number of products by name
scatter_fig = go.Figure(go.Scatter(
    x=df['product_name'].unique(),
    y=df.groupby('product_name').count()['product_id'],
    mode='markers',
    marker=dict(
        color=df.groupby('product_name').count()['product_id'],
        colorscale='Viridis',
        size=15,
        sizemode='diameter',
        sizeref=0.1
    ),
    text=df.groupby('product_name').count()['product_id'],
    name='Number of Products by Name'
))

# Create dashboard with two rows and one column
dashboard = make_subplots(rows=2, cols=1, vertical_spacing=0.15)

# Add charts to dashboard
dashboard.add_trace(bar_fig.data[0], row=1, col=1)
dashboard.add_trace(scatter_fig.data[0], row=2, col=1)

# Update dashboard layout
dashboard.update_layout(
    title='Product Analysis Dashboard',
    height=800,
    showlegend=True,
    margin=dict(l=50, r=50, t=50, b=50)
)

# Generate HTML code for dashboard
html = pio.to_html(dashboard, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('dashboard.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('dashboard.html')