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

# prompt = "What are the risk factors for heart attack?"
# response = generate_response(prompt)

# print(response)