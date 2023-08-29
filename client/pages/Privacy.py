import streamlit as st

# Define your content
header_text="🔒 Privacy Policy"
intro_text="Your privacy is important to us. We value your trust and are committed to protecting and safeguarding any personal information you give us. This document describes how we use and process your personal data and how we use cookies. It also tells you how you can contact us if you have questions about your personal information."
changes_privacy = "Note we will make changes in privacy abiding to law at any interval of time, since we are not collecting any of your personal or communication information requesting you to check this privacy page before proceeding further"
header_who_the_user = "## Who can make use of this website"
who_the_users = "Anyone above 18+ age are allowed to access this page. This website is making use of ML model with synthetic data to train and predict the result. Accuracy we maxed reached was 90%. However it makes some mistake and as always nothing can beat the doctor. So always consult doctor and rely on those records."
data_collection_text = "## Data Collection\n\nWe collect the following information from you when you use our service:"
data_collection_list = [
    "Age",
    "Sex",
    "Nature of Chest Pain",
    "Resting Blood Pressure",
    "Cholesterol Level",
    "Fasting Blood Sugar",
    "Resting Electrocardiographic Results",
    "Maximum Heart Rate Achieved",
    "Exercise Induced Angina",
    "ST Depression Induced by Exercise",
    "Peak Exercise ST Segment Slope",
    "Number of Major Vessels Colored by Fluoroscopy",
    "Status of Thalassemia"
]
data_collection = "\n".join([f"- {item}" for item in data_collection_list])
header_why_data_collection= "### Why these Data are collected"
why_data_collection_text = "For the prediction to work it needs these data"
data_retention= "The Data will be available in the system until you hit refresh button or close it. We are not storing any of your data so avoid refreshing and switching between pages"
analytics_text = "## Analytics\n\nWe use analytics to improve our application's performance. The following data is collected:"
analytics_list = [
    "Age",
    "Sex",
    "Nature of Chest Pain",
    "Resting Blood Pressure",
    "Cholesterol Level",
    "Fasting Blood Sugar",
    "Resting Electrocardiographic Results",
    "Maximum Heart Rate Achieved",
    "Exercise Induced Angina",
    "ST Depression Induced by Exercise",
    "Peak Exercise ST Segment Slope",
    "Number of Major Vessels Colored by Fluoroscopy",
    "Status of Thalassemia"
]
analytics_data = "\n".join([f"- {item}" for item in analytics_list])
header_why_analytics ="### Why Analytics is required to be enabled"
why_analytics_text ="By Default analytics is enabled which will help us in quick troubleshooting and know what data went and what data is received, this helps to validate is ML is working fine"
analytics_retention_text = "As of now, we are not storing analytics data, but planning to store in 3rd party public cloud provider for 30 days"
header_third_party_usage = "## 3rd Party Using your data"
third_party_usage_text = "In Prediction if you have selected ChatGPT then you are agreeing to [ChatGPT Privacy](https://openai.com/security)"
contact_text = "## Contact Us\n\nIf you have any questions or concerns about your personal information, you can contact us at [fareesdeveloper@outlook.com](mailto:fareesdeveloper@outlook.com). And this is open source project available in [GitHub](https://github.com/Fariz-fx/Heart-Attack-Prediction)"

# Build the UI
st.title(header_text)
st.write(intro_text)
st.info(changes_privacy)

st.markdown(header_who_the_user)
st.markdown(who_the_users)

st.markdown(data_collection_text)
st.markdown(data_collection)
st.markdown(header_why_data_collection)
st.markdown(why_data_collection_text)
st.info(data_retention)

st.markdown(analytics_text)
st.markdown(analytics_data)
st.markdown(header_why_analytics)
st.markdown(why_analytics_text)
st.info(analytics_retention_text)

st.markdown(header_third_party_usage)
st.markdown(third_party_usage_text)

st.markdown(contact_text)

# Add any additional UI elements for a more engaging experience
