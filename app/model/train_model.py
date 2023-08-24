import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
#import pickle

# Load your data
df = pd.read_csv("data.csv")

# 'target' should be replaced with your actual target column
X = df.drop('output', axis=1)
y = df['output']

# Normalize the feature data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)#42)

# Initialize classifier
#model = RandomForestClassifier(n_estimators=100)
#model = LogisticRegression()

#model = SVC()

models = [('LR', LogisticRegression())]
models.append(('RF', RandomForestClassifier()))
models.append(('SVC', SVC(probability=True)))
models.append(('KNN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
models.append(('Bernoulli', BernoulliNB()))
models.append(('GBoost', GradientBoostingClassifier()))


results = []
# names = []
# print("Summary: ")
    
for name, model in models:
    # Train model
    model.fit(X_train, y_train)

    # Accuracy
    acc = model.score(X_test, y_test)

    # Cross validation
    cv_score = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5).mean()

    results.append([name, acc, cv_score])

# Convert the results to dataframe and print
df_result = pd.DataFrame(results, columns=['Model', 'Accuracy', 'CrossValidationScore'])
print(df_result)

    # Save the trained model and scaler
    # pickle.dump(model, open('model.pkl', 'wb'))
    # pickle.dump(scaler, open('scaler.pkl', 'wb'))

    # Make Prediction
#     y_pred = model.predict(X_test)
#     # Get accuracy of the Model
#     acc = accuracy_score(y_test, y_pred)

        
#     # Get prediction in percentage
#     y_proba = model.predict_proba(X_test)
        
#     # Cross validation
#     scores = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5).mean()
#     results.append(acc,scores)
#     names.append(name)
        
#     # print(f'Model: {name}')
#     # print(f'Accuracy: {acc * 100.0:.2f}%')
#     # print(f'Cross Validation Score: {scores.mean() * 100.0:.2f}%\n')

#     return pd.DataFrame(list(zip(names, results)), columns=['Model', 'Accuracy'])

# # Run models
# model_summary = run_models(models, X_train, y_train, X_test, y_test)
# print(model_summary)

#         # print('Accuracy of %s: %f' % (name, acc))
#         # print(pd.DataFrame(list(zip(names, results)), columns=['Model', 'Accuracy']))
#         # # Cross validation
#         # scores = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5)
#         # print(f"{name} Cross Validation Score: {scores.mean()}\n")
        
# #print("Model Accuracy: ", accuracy_score(y_test, y_pred))
