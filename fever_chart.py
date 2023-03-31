import pandas as pd
import plotly.express as px
import plotly.io as pio
import webbrowser

# Read data from CSV file
df = pd.read_csv('data2.csv')

# Create fever chart showing the number of products by type and name
fig = px.treemap(df, path=['product_type', 'product_name'], values='product_id')

# Set chart layout
fig.update_layout(
    height=600,
    margin=dict(l=20, r=20, t=40, b=20),
    font=dict(size=18)
)

# Generate HTML code for dashboard
html = pio.to_html(fig, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('fever_chart.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('fever_chart.html')