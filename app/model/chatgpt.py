import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib
import warnings
warnings.filterwarnings('ignore')

# Load your data
df = pd.read_csv("data.csv")

# 'target' should be replaced with your actual target column
X = df.drop('output', axis=1)
y = df['output']

# Normalize the feature data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)#42)

# Initialize classifiers
models = {
    'SVC': SVC(),
    'RandomForest': RandomForestClassifier(n_estimators=100),
    'LogisticRegression': LogisticRegression()
}

# Train models and print cross-validated accuracy
for model_name, model in models.items():
    model.fit(X_train, y_train)

    # Save the trained model and scaler
    joblib.dump(model, f'{model_name}.joblib')
    joblib.dump(scaler, f'{model_name}_scaler.joblib')

    # Get and print accuracy of the model
    y_pred = model.predict(X_test)
    print(f"{model_name} Accuracy: ", accuracy_score(y_test, y_pred))

    # Cross validation
    scores = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5)
    print(f"{model_name} Cross Validation Score: {scores.mean()}\n")