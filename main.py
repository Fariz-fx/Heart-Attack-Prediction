from fastapi import FastAPI
import openai
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Initialize FastAPI app
app = FastAPI()

# Define a POST route to predict heart attack
@app.post("/predict_heart_attack")
async def predict_heart_attack(data: dict):
    # Extract necessary information from the request data
    age = data['age']
    sex = data['sex']
    cp = data['chest_pain_type']
    trestbps = data['resting_blood_pressure']
    chol = data['cholesterol']
    fbs = data['fasting_blood_sugar']
    restecg = data['resting_ecg']
    thalach = data['max_heart_rate']
    exang = data['exercise_induced_angina']
    oldpeak = data['st_depression']
    slope = data['st_slope']
    ca = data['num_major_vessels']
    thal = data['thalassemia']

    # Generate a prompt for GPT-3
    prompt = f"Predict the probability of heart attack based on the following inputs:\n\nAge: {age}\nSex: {sex}\nChest Pain Type: {cp}\nResting Blood Pressure: {trestbps}\nCholesterol: {chol}\nFasting Blood Sugar: {fbs}\nResting ECG: {restecg}\nMax Heart Rate: {thalach}\nExercise Induced Angina: {exang}\nST Depression: {oldpeak}\nST Slope: {slope}\nNum Major Vessels: {ca}\nThalassemia: {thal}\n\n"

    # Use GPT-3 to generate the prediction
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1,
        n=1,
        stop=None,
        temperature=0.2,##0.5,
        top_p=0.9,##1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if prediction := response.choices[0].text.strip():
        # Convert prediction to percentage
        prediction_percentage = float(prediction) * 100
        # Return the prediction as a JSON response
        return {"prediction": prediction, "percentage": prediction_percentage, "prediction_percentage": f"{prediction_percentage:.2f}%"}
    else:
        return {"message": "Unable to make a prediction"}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)