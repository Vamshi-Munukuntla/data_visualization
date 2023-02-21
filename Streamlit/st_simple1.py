import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import streamlit as st

src_file = 'EPA_fuel_economy_summary.csv'
df = pd.read_csv(src_file)

fig = px.histogram(
    df,
    x='fuelCost08',
    color='class_summary',
    labels={'fuelCost08':'Annual Fuel Cost'},
    nbins=40,
    title='Fuel Cost Distribution'
)

st.title('Simple Example')
st.write(fig)


