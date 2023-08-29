import datetime
import logging
import requests
import streamlit as st

API_URL = "http://localhost:8000"  # Replace with your FastAPI server URL

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')

now = datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S')

# Global variable for log status
enable_analytics = False

def make_prediction(data,model_type):
    try:
        if model_type == "ChatGPT":
            if enable_analytics==True:
                logger.info(f"Received a ChatGPT prediction request with the following data: {data}")
            else:
                logger.info("ChatGPT is selected")
            response = requests.post(f"{API_URL}/predict_chatgpt", json=data)
            if response.status_code == 200:
                if prediction := response.json().get("prediction"):
                    prediction_message = f"ChatGPT Prediction: {prediction}"
                    st.info(prediction_message)
                    #st.write("ChatGPT Prediction:", prediction)
                    logger.info(prediction_message)
                else:
                    warning_message="Unable to provide a ChatGPT prediction. Please check the input values."
                    st.warning(warning_message)
                    logger.warning(warning_message)
            else:
                st.error("Failed to get ChatGPT prediction. Please try again.")
                logger.error(f"ChatGPT prediction request failed with status code: {response.status_code}")
        elif model_type == "Custom Model":
            if enable_analytics==True:
                logger.info(f"Received a Custom Model prediction request with the following data: {data}")
            else:
                logger.info("Custom Model is selected")
            response = requests.post(f"{API_URL}/predict_custom_model", json=data)
            #st.write(f"DEBUG: Response: {response.json()}")  # Adding Debug
            if response.status_code == 200:
                # [DEBUG]: Log the result
                logger.info(response.json())
                #prediction = response.json().get("prediction")
                prediction_prob = response.json().get('Prediction_Probability_Percentage', 'N/A')
                message = response.json().get('message', 'N/A')
                if prediction_prob != 'N/A':
                    prediction_results = f"Predicted possibility of Heart Attack in Custom Model: {prediction_prob}%"
                    logger.info(prediction_results)  
                    st.info(message)
                else:
                    warning_message = "Unable to provide a Custom Model prediction. Please check the input values."
                    st.warning(warning_message)

            else:
                st.error("Failed to get Custom Model prediction. Please try again.")
                logger.error(f"Custom Model prediction request failed with status code: {response.status_code}")
        else:
            model_error="Invalid model type selected."
            st.error(model_error)
            logger.critical(model_error)
        # logger.info(f"Making a {model_type} prediction with the following data: {data}")

    except requests.exceptions.RequestException as e:
        st.error("Failed to connect to the server. Please try again later.")
        logger.error(f"Server connection error: {str(e)}")
    except Exception as e:
        st.error("An error occurred. Please try again.")
        logger.error(f"Error occurred: {str(e)}")


st.title("HU-Heart Attack Prediction")
# Document the app functionality
#st.markdown("## App Documentation")
st.write("This app predicts the likelihood of a heart attack based on your inputs.")
st.write("- Choose the prediction model type: Custom Model or ChatGPT.")
st.write("- Adjust the input fields according to your personal information.")
st.write("- Enable analytics to collect data for ML model accuracy.")
st.write("- Click the 'Predict' button to get the prediction result.")
st.write("- The result will be displayed based on the selected model.")
model_type = st.radio("Model Type", ["Custom Model", "ChatGPT"],help="Chatgpt is 70-80% accurate (or) Custom Model trained with the Data is 85% accurate")
#input_style = st.sidebar.radio("Choose Input Style:", ["Slider", "Text Input"])

age = st.slider("Age", min_value=18, max_value=100, value=30, help="Your current age in years")
sex = st.radio("Sex", ["Male", "Female"], help="Your biological sex")
cp_options = {
    3: "No Pain (Asymptomatic)",
    0: "Typical Angina",
    1: "Atypical Angina",
    2: "Non-anginal Pain"
}
cp = st.selectbox("Nature of Chest Pain",options=list(cp_options.keys()),
                  format_func=lambda x:cp_options[x],
                  help="Please select the type of chest pain you experience. 'Typical Angina' is chest pain typically associated with heart disease and is triggered by physical exertion or stress. 'Atypical Angina' refers to chest pain that does not tick all the boxes for typical angina, it might show some symptoms of angina but not all. 'Non-anginal Pain' is chest pain that is not related to the heart. 'No Pain' indicates the lack of chest pain. When in doubt, please consult with your doctor.")## [0, 1, 2, 3]) ##  0 = Typical Angina, 1 = Atypical Angina, 2 = Non-anginal Pain, 3 = Asymptomatic
trestbps = st.slider("Resting Blood Pressure [mm Hg]", min_value=80, max_value=200,value=120, 
                     help="Your blood pressure level in mm Hg while at rest")
chol = st.slider("Cholesterol [mg/dl]", min_value=120, max_value=570,value=200, 
                 help="Your serum cholesterol level in mg/dl")
fbs_options = {
    0: "No (<=120 mg/dl)",
    1: "Yes (>120 mg/dl)"
}
fbs = st.radio("Is Fasting Blood Sugar  > 120 mg/dl?", options=list(fbs_options.keys()), format_func=lambda x: fbs_options[x],help="If > 120 mg/dl, select Yes")
#fbs = st.selectbox("Fasting Blood Sugar", [0, 1]) ## fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
restecg_options = {
    0: "Normal",
    1: "ST-T Wave Normality",
    2: "Left Ventricular Hypertrophy"
}
restecg = st.selectbox("Resting Electrocardiographic Results", options=list(restecg_options.keys()), format_func=lambda x: restecg_options[x],
                       help="These are the outcomes of your electrocardiographic test while at rest")
#restecg = st.selectbox("Resting Electrocardiographic Results", [0, 1, 2]) ## 0 = Normal, 1 = ST-T wave normality, 2 = Left ventricular hypertrophy
thalach = st.slider("Maximum Heart Rate Achieved", min_value=60, max_value=250,value=150,
                    help="This is the highest heart rate one achieves during maximum exercise. Normal resting heart rate for adults ranges from 60 to 100 beats per minute. During strenuous exercise it can go beyond, however, excessively high heart rate during exertion can be a sign of heart disease. Please input the heart rate reached at peak level during exercise. If unavailable, the average adult 'maximum' is typically 120-200 beats per minute.")
exang_options = {
    0: "No",
    1: "Yes"
}
exang = st.radio("Experience of Exercise Induced Angina", options=list(exang_options.keys()), 
                 format_func=lambda x: exang_options[x],
                 help="Exercise-induced angina is chest pain while exercising or doing any strenuous work. Select 'Yes' if you experience this, 'No' if you do not.")
#exang = st.selectbox("Exercise Induced Angina", [0, 1]) ## (1 = yes; 0 = no)
oldpeak = st.slider("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0,value=0.0,
                          help="ST segment depression (in ECG) induced by exercise, relative to rest. The ST segment / T wave is affected during a heart attack")
slope_options = {
    0: "Upwards (Upsloping)",
    1: "Flat Straight",
    2: "Downwards (Downsloping)"
}
slope = st.selectbox("Peak Exercise ST Segment slope direction:", options=list(slope_options.keys()), 
                     format_func=lambda x: slope_options[x],
                     help="Indicates the pattern of heart's electrical activity during your maximum level of exercise. Select 'Upwards' if the pattern was sloping up, 'Flat Straight' if the pattern was flat, 'Downwards' if the pattern was sloping down")
#slope = st.selectbox("Slope of the Peak Exercise ST Segment", [0, 1, 2])
ca = st.slider("Number of Major Vessels Colored by fluoroscopy in test", min_value=0, max_value=4,value=2,
                     help="Enter the number of your heart’s major blood vessels that were colored by dye in testing. This test helps to visualize the inner structure of your heart's blood vessels. Numbers could be from 0 to 4.")
thal_options = {
    0: "Normal",
    1: "Fixed Defect",
    2: "Reversible Defect",
    3: "Unknown"
}
thal = st.selectbox("Status of Thalassemia", options=list(thal_options.keys()), 
                    format_func=lambda x: thal_options[x],
                    help="Thalassemia is a blood disorder. Please select the option as diagnosed by the doctor: 'Normal' if you have no conditions, 'Fixed Defect' if permanent defect was detected, 'Reversible Defect' for conditional disease, and 'Uncertain' if the diagnosis results are inconclusive.")
#thal = st.selectbox("Thalassemia", [0, 1, 2, 3])

# Add the toggle button/checkbox
enable_analytics = st.checkbox("Enable Analytics", value=True, help="This will collect basic data to improve application performance and ML model accuracy verification")

if st.button("Predict"):
    # Logging essential information
    logger.info(f"Data Submitted: {now}")
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

    make_prediction(data,model_type)
