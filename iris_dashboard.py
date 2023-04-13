import plotly.graph_objs as go
import plotly.colors as colors
from plotly.subplots import make_subplots
import pandas as pd
import plotly.io as pio
import webbrowser
from sklearn.datasets import load_iris

# Load iris dataset
iris = load_iris()

# Create pandas dataframe from iris data
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target_names[iris.target]

# Create scatter plot showing sepal length vs petal length, with different colors for each species
scatter_fig = go.Figure()
for species in iris.target_names:
    df_species = df[df['species'] == species]
    scatter_fig.add_trace(go.Scatter(
        x=df_species['sepal length (cm)'],
        y=df_species['petal length (cm)'],
        mode='markers',
        marker=dict(
            color=colors.qualitative.Plotly[iris.target_names.tolist().index(species)],
            size=10,
            opacity=0.8
        ),
        name=species
    ))

# Create dashboard with one row and one column
dashboard = make_subplots(rows=1, cols=1)

# Add scatter plot to dashboard
for trace in scatter_fig.data:
    dashboard.add_trace(trace, row=1, col=1)

# Update dashboard layout
dashboard.update_layout(
    title='Iris Dataset Analysis Dashboard',
    height=600,
    showlegend=True,
    xaxis_title='Sepal Length (cm)',
    yaxis_title='Petal Length (cm)',
    margin=dict(l=50, r=50, t=50, b=50)
)

# Generate HTML code for dashboard
html = pio.to_html(dashboard, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('iris_dashboard.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('iris_dashboard.html')
