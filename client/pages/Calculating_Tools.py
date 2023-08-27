import streamlit as st

def calculate_resting_blood_pressure(age, heart_rate):
    return 120 + (0.5 * age) - (0.1 * heart_rate)

def main():
    st.title("Resting Blood Pressure Calculator")
    st.write("Enter your age and heart rate to calculate your Resting Blood Pressure [mm Hg].")

    # Input fields
    age = st.slider("Age", min_value=18, max_value=100, value=30)
    heart_rate = st.slider("Heart Rate", min_value=1, value=300,help="To get best accuracy, ensure to follow mentioned steps")

    # Calculate button
    if st.button("Calculate Resting Blood Pressure"):
        resting_blood_pressure = calculate_resting_blood_pressure(age, heart_rate)
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