import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.svm import SVC 
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import xgboost as xgb
import lightgbm as lgb
import joblib

# Load data
df = pd.read_csv("data.csv") 

# Data exploration and feature engineering
print("Data shape:", df.shape)
print("Missing values check:", df.isnull().sum())

# Feature selection
X = df[['column1', 'column2', 'column3']] # select important features

# Target column
y = df['output']

# Normalize features
scaler = MinMaxScaler()  
X = scaler.fit_transform(X)

# Stratify split to maintain class ratio 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Evaluate algorithms using CV
models = [RandomForestClassifier(), 
          SVC(),
          xgb.XGBClassifier(),
          lgb.LGBMClassifier(), 
          LogisticRegression()]

scores = []
for model in models:
  cv = StratifiedKFold(n_splits=5)
  scores.append(cross_val_score(model, X_train, y_train, cv=cv).mean())

print("CV accuracies:", scores) 

# Select best model based on CV score 
model = models[scores.index(max(scores))]

# Tune hyperparameters 
params = {"n_estimators":[100,200,300], "max_depth": [5,8,15]}  
gsearch = GridSearchCV(estimator = model, param_grid = params, scoring="accuracy", cv = 5)
gsearch.fit(X_train, y_train)
best_params = gsearch.best_params_

# Re-fit best model on whole dataset
model.set_params(**best_params)
model.fit(X, y)

# Save model
joblib.dump(model, 'finalized_model.joblib')
joblib.dump(scaler, 'scaler.joblib')

# Evaluate on test set
y_pred = model.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, y_pred))