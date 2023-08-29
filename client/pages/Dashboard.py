import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

st.header("Data Dashboard")
st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Download link for the sample CSV file
sample_data = """
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,output
63,1,3,145,233,1,0,150,0,2.3,0,0,1,1
37,1,2,130,250,0,1,187,0,3.5,0,0,2,1
41,0,1,130,204,0,0,172,0,1.4,2,0,2,1
68,1,0,144,193,1,1,141,0,3.4,1,2,3,0
57,1,0,130,131,0,1,115,1,1.2,1,1,3,0
57,0,1,130,236,0,0,174,0,0,1,1,2,0
"""

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Scatter Plot: Age vs Cholesterol")
    fig = go.Figure(data=go.Scatter(x=df['age'], y=df['chol'], mode='markers'))
    fig.update_layout(title='Age vs Cholesterol', xaxis=dict(title='Age'), yaxis=dict(title='Cholesterol'))
    st.plotly_chart(fig)
    
    # Histogram: Age Distribution
    st.subheader("Histogram: Age Distribution")
    hist_fig = px.histogram(df, x='age', nbins=10, title='Age Distribution')
    st.plotly_chart(hist_fig)

    # Bar Chart: Chest Pain Types
    st.subheader("Bar Chart: Chest Pain Types")
    cp_counts = df['cp'].value_counts().reset_index()
    cp_counts.columns = ['Chest Pain Type', 'Count']
    bar_fig = px.bar(cp_counts, x='Chest Pain Type', y='Count', title='Chest Pain Types')
    st.plotly_chart(bar_fig)

    # Box Plot: Age vs Cholesterol by Gender
    st.subheader("Box Plot: Age vs Cholesterol by Gender")
    box_fig = px.box(df, x='sex', y='chol', color='sex', points='all', title='Age vs Cholesterol by Gender')
    st.plotly_chart(box_fig)

    # Correlation Heatmap
    st.subheader("Correlation Heatmap")
    corr = df.corr()
    heatmap_fig = px.imshow(corr, labels=dict(x="Feature", y="Feature", color="Correlation"))
    st.plotly_chart(heatmap_fig)
else:
    st.sidebar.info("Want to visualize your data, Upload csv file with below data \n")
    #st.sidebar.write("Got your own data,")
    st.sidebar.write("Download [sample CSV file](https://docs.google.com/spreadsheets/d/1SxQNJIU2xzhBqENgBWstN8k-MBPGbQ9ZoyhHfY0Jx2U/edit?usp=sharing), to upload your data")
    st.sidebar.download_button("Download Sample CSV", data=sample_data, file_name="sample.csv")
    st.sidebar.warning("Do not delete row 1 containing column headings. Feel free to update other rows with your data", icon="⚠️")
    # df = pd.read_csv('../../app/data/data.csv')  # Make sure 'data.csv' exist or correct file path
