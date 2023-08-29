import streamlit as st

def main():
    st.set_page_config(
        page_title="HU-Heart: Your Heart Health Companion",
        page_icon="💓",
        #layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("HU-Heart: Your Heart Health Companion")
    st.header("Welcome to the HU-Heart App!")
    st.caption("Empowering you to assess your heart health and risk of heart attack using machine learning.")
    
    # Add a section for Importance of Heart
    st.header("The Importance of Heart Health")
    st.write("Your heart is the engine of your body, pumping life-giving blood to every corner. Nurturing your heart health is essential for a vibrant and active life.")
    
    # Add a section for Heart Attack Information
    st.header("Understanding Heart Attacks")
    st.write("A heart attack, or myocardial infarction, occurs when a part of the heart muscle is deprived of blood flow. This can lead to severe damage and life-threatening complications.")
    
    # Add a section for Motive and Aim of the App
    st.header("Our Motive and Aim")
    st.write("HU-Heart is designed to provide you with a simple tool to gauge your heart attack risk. By leveraging advanced machine learning, we aspire to raise awareness about heart health and promote proactive care.")
    
if __name__ == "__main__":
    main()
