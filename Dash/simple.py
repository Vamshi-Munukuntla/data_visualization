from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

file_path = r'C:\Users\vamsh\PycharmProjects\data_visualization'
src_file = file_path + r'\Data\EPA_fuel_economy_summary.csv'
df = pd.read_csv(src_file)

fig = px.histogram(
    df,
    x='fuelCost08',
    color='class_summary',
    labels={'fuelCost08':'Annual Fuel Cost'},
    nbins=40,
    title='Fuel Cost Distribution'
)

app.layout = html.Div(children=[
    html.H1('Simple Histogram'),
    html.Div('Annual Fuel Cost Plot'),
    dcc.Graph(id='example-histogram', figure=fig),
])

if __name__ == '__main__':
    app.run_server(debug=True)

