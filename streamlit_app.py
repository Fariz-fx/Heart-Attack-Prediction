import logging
import requests
import streamlit as st

API_URL = "http://localhost:8000"  # Replace with your FastAPI server URL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

st.title("Heart Attack Prediction")

age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3]) ##  0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic
trestbps = st.number_input("Resting Blood Pressure [mm Hg]", min_value=0, max_value=300) 
chol = st.number_input("Cholesterol [mg/dl]", min_value=0, max_value=1000)
fbs = st.selectbox("Fasting Blood Sugar", [0, 1]) ## fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2]) ## 0 = Normal, 1 = ST-T wave normality, 2 = Left ventricular hypertrophy
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300)
exang = st.selectbox("Exercise Induced Angina", [0, 1]) ## (1 = yes; 0 = no)
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4)
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
    
    try:
        response = requests.post(f"{API_URL}/predict", json=data)
        if response.status_code == 200:
            prediction = response.json().get("prediction")
            st.write("Prediction:", prediction)
        else:
            st.error("Failed to get prediction. Please try again.")
            logger.error(f"Prediction request failed with status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to the server. Please try again later.")
        logger.error(f"Server connection error: {str(e)}")
    except Exception as e:
        st.error("An error occurred. Please try again.")
        logger.error(f"Error occurred: {str(e)}")