import streamlit as st
# from pages import home, ask_me, dashboard, privacy, prediction, precautions

# PAGES = {
#     "Home": home,
#     "Ask Me": ask_me,
#     "Dashboard": dashboard,
#     "Privacy": privacy,
#     "Prediction": prediction,
#     "Precautions": precautions
# }

def main():
    # st.sidebar.title('Navigation')
    # selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    # page = PAGES[selection]

    # with st.spinner(f"Loading {selection} ..."):
    #     page.show()
    st.header("About Heart Attack")
    st.write("Heart attacks are a critical health issue that occur when blood flow to the heart is blocked...")

if __name__ == "__main__":
    main()