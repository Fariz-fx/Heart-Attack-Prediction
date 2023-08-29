import datetime
from dotenv import load_dotenv
import logging
import os
import requests 
import streamlit as st

load_dotenv()

# Load environment variables
github_token = os.getenv('GITHUB_PAT_TOKEN') 
github_repo = os.getenv('REPO_NAME')

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

# Streamlit setup
st.title("HeartGuard: Feedback")
st.write("We value your feedback! Please share your thoughts, suggestions, and comments with us.")

# Feedback form
feedback_title = st.text_area("Your Feedback Title", "", help="Explain your feedback in 3 words", max_chars=100)
feedback_text = st.text_area("Your Valuable Feedback:", "", help="Type your anonymous valuable feedback here.")

def submit_feedback():
    if feedback_text:
        st.success("Thank you for your feedback! We appreciate your input.")
        submit_to_github(feedback_title, feedback_text)
    else:
        st.warning("Please enter your feedback before submitting.")

def submit_to_github(title, body):
    github_issue_title = f"[App Generated]: {title}"
    github_issue_body = f"New Feedback:\n\n{body}"

    github_api_url = f"https://api.github.com/repos/{github_repo}/issues"
    github_headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    github_payload = {
        "title": github_issue_title,
        "body": github_issue_body
    }

    try:
        response = requests.post(github_api_url, json=github_payload, headers=github_headers, timeout=10)
        if response.status_code == 201:
            st.info("Feedback submitted as [GitHub issue!](https://github.com/Fariz-fx/Heart-Attack-Prediction/issues)")
            logger.info("Feedback submitted as [GitHub issue!](https://github.com/Fariz-fx/Heart-Attack-Prediction/issues)")
        else:
            logger.warning("Failed to submit feedback as GitHub issue.")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error submitting feedback: {e}")
        st.error("An error occurred while submitting feedback. Please try again later.")

# Submit button
if st.button("Submit Feedback"):
    submit_feedback()
