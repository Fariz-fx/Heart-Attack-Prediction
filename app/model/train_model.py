import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import logging
import os

# Declaration
#file_name="../data/data.csv" # Provide File Name
file_name = os.path.abspath("../data/Heart_Attack_data.csv")  # Use absolute path
axis_value=1
result_column="output" # In CSV the result column name
scaler_joblib_name="SVC_Heart_Attack_scaler.joblib"
model_joblib_name="SVC_Heart_Attack_model.joblib"
test_size_declared=0.2 
random_state_declared=62 #0
cross_validation_value=7 #5

def load_data(path: str):
    try:
        return pd.read_csv(path)
    except FileNotFoundError as e:
        logging.error(f"The provided file path {path} does not exist.")
        raise
    except Exception as e:
        logging.error("Unable to load data.")
        raise

def normalize_data(raw_data):
    try:
        scaler = StandardScaler()
        normalized_data = scaler.fit_transform(raw_data)
        return normalized_data, scaler
    except Exception as e:
        logging.error("Unable to normalize data.")
        raise

def split_data(X, y, test_size=test_size_declared, random_state=random_state_declared):
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_test, y_train, y_test
    except Exception as e:
        logging.error("Unable to split data.")
        raise

def train_save_model(X_train, y_train, model_path):
    try:
        model = SVC(probability=True)
        model.fit(X_train, y_train)
        joblib.dump(model, model_path)
        return model
    except Exception as e:
        logging.error("Unable to train model.")
        raise

def test_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return accuracy_score(y_test, y_pred)

def perform_cross_validation(model, X_train, y_train, cv=cross_validation_value):
    scores = cross_val_score(estimator=model, X=X_train, y=y_train, cv=cv)
    return scores.mean()

def main():
    df = load_data(file_name)
    X = df.drop(result_column, axis=axis_value)
    y = df[result_column]
    X, scaler = normalize_data(X) 
    joblib.dump(scaler, scaler_joblib_name)
    X_train, X_test, y_train, y_test = split_data(X, y)
    model = train_save_model(X_train, y_train, model_joblib_name)
    print("Model Accuracy: ", test_model(model, X_test, y_test))
    print(f"Cross Validation Score: {perform_cross_validation(model, X_train, y_train)}\n")

if __name__ == '__main__':
    main()
