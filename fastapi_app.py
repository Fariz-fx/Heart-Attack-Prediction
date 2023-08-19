from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from openai_integration import generate_response
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()

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

@app.post("/predict")
def predict_heart_attack(data: HeartAttackPredictionRequest):
    try:
        # Log the values
        logger.info(f"CP: {data.cp}")
        logger.info(f"Trestbps: {data.trestbps}")
        logger.info(f"Chol: {data.chol}")
        logger.info(f"FBS: {data.fbs}")
        prompt = f"Predict the probability of a heart attack with the following input:\n\nAge: {data.age}\nSex: {data.sex}\nChest Pain Type: {data.cp}\nTrestbps: {data.trestbps}\nChol: {data.chol}\nFBS: {data.fbs}\nRestecg: {data.restecg}\nThalach: {data.thalach}\nExang: {data.exang}\nOldpeak: {data.oldpeak}\nSlope: {data.slope}\nCA: {data.ca}\nThal: {data.thal}\n\nRisk factors for heart attack are: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history."

        prediction = generate_response(prompt)
        
        return {"prediction": prediction}
        #return {"prediction": prediction.item()}  # Return prediction as a single value
    
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Failed to process the request."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)