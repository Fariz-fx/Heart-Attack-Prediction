import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.header("Data Dashboard")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.info("Want to visualize your data, Upload csv file with \n")
    # df = pd.read_csv('../../app/data/data.csv')  # Make sure 'data.csv' exist or correct file path
# fig = go.Figure(data=go.Scatter(x=df['age'], y=df['chol'], mode='markers'))
# fig.update_layout(title='Age vs Cholesterol', xaxis=dict(title='Age'), yaxis=dict(title='Cholesterol'))
# st.plotly_chart(fig)