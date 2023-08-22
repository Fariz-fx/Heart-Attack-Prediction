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
import pickle

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
models.append(('SVC', SVC()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('NB', GaussianNB()))
models.append(('Bernoulli', BernoulliNB()))
models.append(('GBoost', GradientBoostingClassifier()))

results = []
names = []

for name, model in models:
# Train model
    model.fit(X_train, y_train)

    # Save the trained model and scaler
    # pickle.dump(model, open('model.pkl', 'wb'))
    # pickle.dump(scaler, open('scaler.pkl', 'wb'))

    # Get and print accuracy of the model
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    results.append(acc)
    names.append(name)
    print('Accuracy of %s: %f' % (name, acc))

    print("Summary: ")
    print(pd.DataFrame(list(zip(names, results)), columns=['Model', 'Accuracy']))
    # Cross validation
    scores = cross_val_score(estimator=model, X=X_train, y=y_train, cv=5)
    print(f"{name} Cross Validation Score: {scores.mean()}\n")
#print("Model Accuracy: ", accuracy_score(y_test, y_pred))
