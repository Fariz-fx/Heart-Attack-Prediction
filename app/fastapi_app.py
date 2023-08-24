import datetime
from fastapi import FastAPI, HTTPException
import logging
from openai_integration import generate_response
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from sklearn.ensemble import RandomForestClassifier
#import pickle
import joblib
import pandas as pd
import numpy as np

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

app = FastAPI()

# Load the trained model 
# model = pickle.load(open('model/model.pkl', 'rb'))
# scaler = pickle.load(open('model/scaler.pkl', 'rb')) 
model = joblib.load('model/model.joblib')
scaler = joblib.load('model/scaler.joblib') 

class HeartAttackPredictionRequest(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int
    ever_experienced_chest_pain: str  # yes or no
    ever_diagnosed_high_bp: str  # yes or no
    ever_had_cholesterol_test: str  # yes or no
    ever_diagnosed_diabetes: str  # yes or no
    smoking_status: str  # never, former, current
    physical_activity_frequency: str  # sedentary, sometimes, regularly
    family_history_heart_disease: str  # yes or no
    
def preprocess(data: HeartAttackPredictionRequest):
    df = pd.DataFrame(data.dict(), index=[0])  # fixed code error
    #df = pd.DataFrame(data)
    return scaler.transform(df)

@app.post("/predict_chatgpt")
def predict_heart_attack(data: HeartAttackPredictionRequest):
    try:
        # Logging essential information
        logger.info(f"Data Submitted: {now}")
        # logger.info(f"Age: {data.age}")
        # logger.info(f"Sex: {data.sex}")
        # logger.info(f"CP: {data.cp}")
        # logger.info(f"Trestbps: {data.trestbps}")
        # logger.info(f"Chol: {data.chol}")
        # logger.info(f"FBS: {data.fbs}")
        # logger.info(f"Restecg: {data.restecg}")
        # logger.info(f"Thalach: {data.thalach}")
        # logger.info(f"Exang: {data.exang}")
        # logger.info(f"Oldpeak: {data.oldpeak}")
        # logger.info(f"Slope: {data.slope}")
        # logger.info(f"CA: {data.ca}")
        # logger.info(f"Thal: {data.thal}")
        prompt = f"Predict the probability of a heart attack with the following input:\n\nAge: {data.age}\nSex: {data.sex}\nChest Pain Type: {data.cp}\nTrestbps: {data.trestbps}\nChol: {data.chol}\nFBS: {data.fbs}\nRestecg: {data.restecg}\nThalach: {data.thalach}\nExang: {data.exang}\nOldpeak: {data.oldpeak}\nSlope: {data.slope}\nCA: {data.ca}\nThal: {data.thal}\n\nRisk factors for heart attack are: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history."
        
        prediction = generate_response(prompt)
        #prompt = f"Predict the probability of a heart attack with the following input:\n\nAge: {data.age}\nSex: {data.sex}\nChest Pain Type: {data.cp}\nTrestbps: {data.trestbps}\nChol: {data.chol}\nFBS: {data.fbs}\nRestecg: {data.restecg}\nThalach: {data.thalach}\nExang: {data.exang}\nOldpeak: {data.oldpeak}\nSlope: {data.slope}\nCA: {data.ca}\nThal: {data.thal}\n\nRisk factors for heart attack are: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history."
        prediction = generate_response(prompt)
        logger.info(f"Prompting: {prediction}")
        return {"prediction": prediction}
            #return {"prediction": prediction.item()}  # Return prediction as a single value

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Failed to process the request."}

@app.post("/predict_custom_model")
def predict_heart_attack_custom_model(data: HeartAttackPredictionRequest):
    try:
        # Logging essential information
        logger.info(f"Data Submitted: {now}")

        # preprocessing
        data_preprocessed = preprocess(data)

        # Make prediction
        prediction = model.predict(data_preprocessed)

        logger.info(f"Prompting: {prediction}")
        # Return formatted prediction result
        return {"prediction": int(prediction[0])}  # Return prediction as a single value

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Failed to process the request."}

@app.post("/normal_user_predict_chatgpt")
def predict_heart_attack(data: HeartAttackPredictionRequest):
    try:
        # Logging essential information
        logger.info(f"Data Submitted: {now}")
        prompt = f"Predict the percentage of a heart attack with the following general health information:\n\n\
        Age: {data.age}\n\
        Gender: {data.sex}\n\
        Ever Experienced Chest Pain: {data.ever_experienced_chest_pain}\n\
        Ever Diagnosed with High BP: {data.ever_diagnosed_high_bp}\n\
        Ever Had a Cholesterol Test: {data.ever_had_cholesterol_test}\n\
        Ever Diagnosed with Diabetes: {data.ever_diagnosed_diabetes}\n\
        Smoking Status: {data.smoking_status}\n\
        Physical Activity Frequency: {data.physical_activity_frequency}\n\
        Family History of Heart Disease: {data.family_history_heart_disease}\n\n\
        Risk factors for a heart attack include: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history of the disease."
        prediction = generate_response(prompt)
        #prompt = f"Predict the probability of a heart attack with the following input:\n\nAge: {data.age}\nSex: {data.sex}\nChest Pain Type: {data.cp}\nTrestbps: {data.trestbps}\nChol: {data.chol}\nFBS: {data.fbs}\nRestecg: {data.restecg}\nThalach: {data.thalach}\nExang: {data.exang}\nOldpeak: {data.oldpeak}\nSlope: {data.slope}\nCA: {data.ca}\nThal: {data.thal}\n\nRisk factors for heart attack are: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history."
        prediction = generate_response(prompt)
        logger.info(f"Prompting: {prediction}")
        return {"prediction": prediction}
            #return {"prediction": prediction.item()}  # Return prediction as a single value

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Failed to process the request."}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
