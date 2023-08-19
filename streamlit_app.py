import logging
import requests
import streamlit as st

API_URL = "http://localhost:8000"  # Replace with your FastAPI server URL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

st.title("Heart Attack Prediction")

def log_analytics(cp, trestbps, chol, fbs):
    logger.info(f"CP: {cp}")
    logger.info(f"Trestbps: {trestbps}")
    logger.info(f"Chol: {chol}")
    logger.info(f"FBS: {fbs}")

def make_prediction(data):
    try:
        response = requests.post(f"{API_URL}/predict", json=data)
        if response.status_code == 200:
            if prediction := response.json().get("prediction"):
                st.write("Prediction:", prediction)
            else:
                st.warning("Unable to provide a prediction. Please check the input values.")
        else:
            st.error("Failed to get prediction. Please try again.")
            logger.error(f"Prediction request failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to the server. Please try again later.")
        logger.error(f"Server connection error: {str(e)}")
    except Exception as e:
        st.error("An error occurred. Please try again.")
        logger.error(f"Error occurred: {str(e)}")

age = st.number_input("Age", min_value=1, max_value=100, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp_options = {
    0: "Typical Angina",
    1: "Atypical Angina",
    2: "Non-anginal Pain",
    3: "Asymptomatic"
}
cp = st.selectbox("Chest Pain Type",options=list(cp_options.keys()),format_func=lambda x:cp_options[x])## [0, 1, 2, 3]) ##  0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic
trestbps = st.number_input("Resting Blood Pressure [mm Hg]", min_value=0, max_value=300,value=150)
chol = st.number_input("Cholesterol [mg/dl]", min_value=0, max_value=1000,value=500)
fbs_options = {
    0: "No",
    1: "Yes"
}
fbs = st.selectbox("Fasting Blood Sugar", options=list(fbs_options.keys()), format_func=lambda x: fbs_options[x],help="If > 120 mg/dl, select Yes")
#fbs = st.selectbox("Fasting Blood Sugar", [0, 1]) ## fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
restecg_options = {
    0: "Normal",
    1: "ST-T Wave Normality",
    2: "Left Ventricular Hypertrophy"
}
restecg = st.selectbox("Resting Electrocardiographic Results", options=list(restecg_options.keys()), format_func=lambda x: restecg_options[x])
#restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2]) ## 0 = Normal, 1 = ST-T wave normality, 2 = Left ventricular hypertrophy
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300,value=150)
exang_options = {
    0: "No",
    1: "Yes"
}
exang = st.selectbox("Exercise Induced Angina", options=list(exang_options.keys()), format_func=lambda x: exang_options[x])
#exang = st.selectbox("Exercise Induced Angina", [0, 1]) ## (1 = yes; 0 = no)
oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0,value=5.0)
slope_options = {
    0: "Upsloping",
    1: "Flat",
    2: "Downsloping"
}
slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=list(slope_options.keys()), format_func=lambda x: slope_options[x])
#slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=4,value=4)
thal_options = {
    0: "Normal",
    1: "Fixed Defect",
    2: "Reversible Defect",
    3: "Unknown"
}
thal = st.selectbox("Thalassemia", options=list(thal_options.keys()), format_func=lambda x: thal_options[x])
#thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Add the toggle button/checkbox
enable_analytics = st.checkbox("Enable Analytics", value=True, help="This will collect basic data to improve application performance")

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

    if enable_analytics:
        log_analytics(cp_options[cp], trestbps, chol, fbs)

    make_prediction(data)