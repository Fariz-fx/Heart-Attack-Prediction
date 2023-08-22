import pandas as pd
import numpy as np
import random

np.random.seed(0)
random.seed(0)

# Define the number of rows you want
n_rows = 330


# Define the choices for each variable
sex_choice = ['male', 'female']
yes_no_choice = ['yes', 'no']
smoking_status_choice = ['never', 'former', 'current']
physical_activity_frequency_choice = ['sedentary', 'sometimes', 'regularly']

# Create a DataFrame with random input for each category based on
# your description above in the original dataset.
df = pd.DataFrame({
    'age': np.random.randint(30,70,size=n_rows),
    'sex': np.random.randint(0,2,size=n_rows),
    # 'cp': np.random.randint(0,4,size=n_rows),
    # 'trestbps': np.random.randint(90,200,size=n_rows),
    # 'chol': np.random.randint(126,564,size=n_rows),
    # 'fbs': np.random.randint(0,2,size=n_rows),
    # 'restecg': np.random.randint(0,3,size=n_rows),
    # 'thalach': np.random.randint(70,200,size=n_rows),
    # 'exang': np.random.randint(0,2,size=n_rows),
    # 'oldpeak': np.round(np.random.uniform(0,6.2,size=n_rows), 1),
    # 'slope': np.random.randint(0,3,size=n_rows),
    # 'ca': np.random.randint(0,5,size=n_rows),
    # 'thal': np.random.randint(0,4,size=n_rows),
    'ever_experienced_chest_pain': np.random.choice(yes_no_choice, n_rows),
    'ever_diagnosed_high_bp': np.random.choice(yes_no_choice, n_rows),
    'ever_had_cholesterol_test': np.random.choice(yes_no_choice, n_rows),
    'ever_diagnosed_diabetes': np.random.choice(yes_no_choice, n_rows),
    'smoking_status': np.random.choice(smoking_status_choice, n_rows),
    'physical_activity_frequency': np.random.choice(physical_activity_frequency_choice, n_rows),
    'family_history_heart_disease': np.random.choice(yes_no_choice, n_rows),
    'result': np.random.uniform(0,100,n_rows)  # Assuming percentage between 0 and 100
})

# Save DataFrame to csv
df.to_csv("dummydata.csv", index = False)