import plotly.graph_objs as go
import plotly.colors as colors
import pandas as pd
import plotly.io as pio
import webbrowser
import seaborn as sns

# Load the Iris dataset from seaborn
iris = sns.load_dataset('iris')

# Create dial gauge showing the number of samples by species
dial_fig = go.Figure(go.Indicator(
    mode='gauge+number',
    value=iris.groupby('species').count()['sepal_length'][0],
    title={'text': "Number of Samples by Species"},
    gauge=dict(
        axis=dict(
            range=[0, iris.groupby('species').count()['sepal_length'].max()],
            tickmode='linear',
            tickfont=dict(size=15),
            tickangle=0
        ),
        bar=dict(
            color='darkblue'
        ),
        steps=[
            dict(
                range=[0, iris.groupby('species').count()['sepal_length'].max()*0.2],
                color='lightgray'
            ),
            dict(
                range=[iris.groupby('species').count()['sepal_length'].max()*0.2, iris.groupby('species').count()['sepal_length'].max()*0.6],
                color='gray'
            ),
            dict(
                range=[iris.groupby('species').count()['sepal_length'].max()*0.6, iris.groupby('species').count()['sepal_length'].max()],
                color='black'
            )
        ]
    )
))

# Add labels to the dial gauge
dial_fig.update_layout(
    height=400,
    margin=dict(l=50, r=50, t=50, b=50),
    annotations=[dict(
        x=0.5,
        y=0.5,
        text=str(iris.groupby('species').count()['sepal_length'][0]),
        font=dict(
            size=40
        ),
        showarrow=False
    )]
)

# Generate HTML code for dashboard
html = pio.to_html(dial_fig, include_plotlyjs='cdn')

# Save dashboard to HTML file
with open('dial_gauge.html', 'w') as f:
    f.write(html)

# Open dashboard in default web browser
webbrowser.open('dial_gauge.html')
