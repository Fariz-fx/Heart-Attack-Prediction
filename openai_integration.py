import openai
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
    )
    
    return response.choices[0].text.strip()

def advanced_generate_response(data):
    message_log = [
        {"role": "system", "content": "You are a The Health Data Scientist and Healthcare Entrepreneur. You will make use of your database and get [Age, Sex, Chest Pain Type as (0: Typical Angina, 1: Atypical Angina, 2: Non-anginal Pain, 3: Asymptomatic), Resting Blood Pressure [mm Hg], Cholesterol [mg/dl], Fasting Blood Sugar as (0:No,1: Yes(>120mg/dl)), Resting Electrocardiographic Results(0: Normal, 1: ST-T Wave Normality, 2: Left Ventricular Hypertrophy), Maximum Heart Rate Achieved, Exercise Induced Angina(0:No, 1:Yes), ST Depression Induced by Exercise, Slope of the Peak Exercise ST Segment(0: Upsloping,1: Flat,2: Downsloping), Number of Major Vessels Colored by Fluoroscopy, Thalassemia(0: Normal,1: Fixed Defect,2: Reversible Defect,3: Unknown)] these data from users and provide prediction % with message"},
        {"role": "user", "content":
            f"Predict the probability of a heart attack with the following input:"
            f"\n\nAge: {data.age}"
            f"\nSex: {data.sex}"
            f"\nChest Pain Type: {data.cp}"
            f"\nTrestbps: {data.trestbps}"
            f"\nChol: {data.chol}"
            f"\nFBS: {data.fbs}"
            f"\nRestecg: {data.restecg}"
            f"\nThalach: {data.thalach}"
            f"\nExang: {data.exang}"
            f"\nOldpeak: {data.oldpeak}"
            f"\nSlope: {data.slope}"
            f"\nCA: {data.ca}"
            f"\nThal: {data.thal}"
            f"\n\nRisk factors for heart attack are: smoking, high blood pressure, high cholesterol, obesity, diabetes, sedentary lifestyle, and family history."
        },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
    )
    return next(
        (
            choice["message"]["content"]
            for choice in response.choices
            if "message" in choice and "content" in choice["message"]
        ),
        "Error: No valid chatbot response found.",
    )