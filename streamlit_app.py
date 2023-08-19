import requests
import streamlit as st

API_URL = "http://localhost:8000"  # Replace with your FastAPI server URL

st.title("Heart Attack Prediction")

age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.selectbox("Fasting Blood Sugar", [0, 1])
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved")
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise")
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy")
thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

if st.button("Predict"):
    data = {
        "age": age,
        "sex": int(sex == "Male"),
        "cp": cp,
        "trestbps": trestbps,
        "chol": chol,
        "fbs": fbs,
        "restecg": restecg,
        "thalach": thalach,
        "exang": exang,
        "oldpeak": oldpeak,
        "slope": slope,
        "ca": ca,
        "thal": thal
    }
    
    response = requests.post(f"{API_URL}/predict", json=data)
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.write("Prediction:", prediction)
    else:
        st.error("Failed to get prediction. Please try again.")