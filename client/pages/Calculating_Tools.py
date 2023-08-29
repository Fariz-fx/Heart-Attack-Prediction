import streamlit as st
import math

def calculate_resting_blood_pressure(age, heart_rate):
    return 120 + (0.5 * age) - (0.1 * heart_rate)

def calculate_cholesterol(age, gender, total_cholesterol):
    return (
        total_cholesterol - (0.2 * age)
        if gender == "Male"
        else total_cholesterol + (0.1 * age)
    )

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def calculate_bmr(weight, height, age, gender):
    if gender == "Male":
        return 66.5 + (13.75 * weight) + (5.003 * height * 100) - (6.75 * age)
    else:
        return 655 + (9.563 * weight) + (1.850 * height * 100) - (4.676 * age)

def main():
    st.title("Health Calculator")
    st.write("Use the following calculators to assess your health parameters.")

    # Explanation
    st.write("BMI Calculator helps you assess your Body Mass Index.")
    st.write("BMR Calculator estimates your Basal Metabolic Rate.")
    st.write("Resting Blood Pressure Calculator calculates your resting blood pressure.")
    st.write("Total Cholesterol Calculator estimates your cholesterol level.")

    st.write("Enter your age and heart rate to calculate your Resting Blood Pressure [mm Hg].")

    rbp_column, spacer, cholesterol_column = st.columns([1, 0.1, 1])

    with rbp_column:
        rbp_section_data()

    # Spacer for visual separation
    with spacer:
        st.write("")

    with cholesterol_column:
        st.header("Total Cholesterol Calculator")
        # Input fields
        age_cholesterol = st.slider("Age", min_value=18, max_value=100, value=30,key="cholesterol")
        gender = st.selectbox("Gender", ["Male", "Female"])
        total_cholesterol = st.number_input("Total Cholesterol", min_value=1, value=200)


        # Calculate button
        if st.button("Calculate Cholesterol Level"):
            cholesterol_level = calculate_cholesterol(age_cholesterol, gender, total_cholesterol)
            st.success(f"Your calculated Cholesterol level: {cholesterol_level:.2f} mg/dL")

    # Column Layout
    columns = st.columns(2)

    # BMI Column
    with columns[0]:
        st.header("BMI Calculator")
        weight_bmi = st.number_input("Weight (kg)", min_value=1)
        height_bmi = st.number_input("Height (m)", min_value=0.01)

        if st.button("Calculate BMI"):
            bmi = calculate_bmi(weight_bmi, height_bmi)
            st.success(f"Your calculated BMI: {bmi:.2f}")

    # BMR Column
    with columns[1]:
       bmr_calculator()
    # Spacer for visual separation
    st.write("")
    st.write("---")


def bmr_calculator():
    st.header("BMR Calculator")
    weight_bmr = st.number_input("Weight (kg)", min_value=1,key="bmr_weight")
    height_bmr = st.number_input("Height (m)", min_value=0.01,key="bmr_height")
    age_bmr = st.slider("Age", min_value=1, max_value=100, value=30)
    gender_bmr = st.selectbox("Gender", ["Male", "Female"],key="bmr_gender")

    if st.button("Calculate BMR"):
        bmr = calculate_bmr(weight_bmr, height_bmr, age_bmr, gender_bmr)
        st.success(f"Your calculated BMR: {bmr:.2f} calories/day")

def rbp_section_data():
    st.header("Resting Blood Pressure Calculator")
    age_rbp = st.slider("Age", min_value=18, max_value=100, value=30)
    heart_rate = st.slider("Heart Rate", min_value=1, value=300,help="To get best accuracy, ensure to follow mentioned steps")

    if st.button("Calculate Resting Blood Pressure"):
        resting_blood_pressure = calculate_resting_blood_pressure(age_rbp, heart_rate)
        st.success(f"Your calculated Resting Blood Pressure: {resting_blood_pressure:.2f} mm Hg")

    RBP_Best_Practices=st.expander("Best Practices to follow")
    with RBP_Best_Practices:

        rest_Blood_pressure_best_practices()
    
    

def rest_Blood_pressure_best_practices():
    # Additional information
    st.write("To measure your resting blood pressure accurately, follow these best practices recommended by health organizations:")
    st.write("You can make use of Fitness Trackers, Smartwatches, Dedicated Heart Rate Monitors, Mobile Apps, Medical Devices and Smartphone Sensors")
    st.write("1. Don’t eat or drink anything 30 minutes before taking your blood pressure.")
    st.write("2. Empty your bladder before the reading.")
    st.write("3. Sit in a comfortable chair with back support for at least 5 minutes before the reading.")
    st.write("4. Put both feet flat on the ground and keep your legs uncrossed.")
    st.write("5. Rest your arm with the cuff on a table at chest height.")
    st.write("6. Make sure the blood pressure cuff is snug but not too tight, against bare skin.")
    st.write("7. Don’t talk while your blood pressure is being measured.")
    st.write("For accurate at-home readings, also consider these tips:")
    st.write("- Use a properly sized blood pressure cuff.")
    st.write("- Have your blood pressure measured twice, with a brief break in between. If the readings are different by 5 points or more, have it done a third time.")
    st.write("For more information, you can refer to the following references:")

    # References
    st.write("1. [CDC - How to Measure Blood Pressure](https://www.cdc.gov/bloodpressure/measure.htm)")
    st.write("2. [Harvard Health - Tips to Measure Your Blood Pressure Correctly](https://www.health.harvard.edu/heart-health/tips-to-measure-your-blood-pressure-correctly)")

if __name__ == "__main__":
    main()