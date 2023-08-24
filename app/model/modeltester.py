import itertools
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.preprocessing import StandardScaler
import openpyxl

# Load data
df = pd.read_csv("data.csv")
X = df.drop('output', axis=1)
y = df['output']

# Normalize the feature data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# List of models
models = [('LR', LogisticRegression()), 
          ('RF', RandomForestClassifier()), 
          ('SVC', SVC(probability=True)),  
          ('KNN', KNeighborsClassifier()), 
          ('NB', GaussianNB()), 
          ('Bernoulli', BernoulliNB()), 
          ('GBoost', GradientBoostingClassifier())]

# Define all possible values
test_sizes = [0.2, 0.3, 0.4]
random_states = [0, 42, 52, 62]
cvs = [3, 5, 7]

all_results = []

for test_size, random_state, cv in itertools.product(test_sizes, random_states, cvs):
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    for name, model in models:
        # Fit the model
        model.fit(X_train, y_train)

        # Accuracy
        acc = model.score(X_test, y_test)

        # Cross validation
        cv_score = cross_val_score(estimator=model, X=X_train, y=y_train, cv=cv).mean()

        all_results.append([name, test_size, random_state, cv, acc, cv_score])

# Convert the results to dataframe and print
df_all_results = pd.DataFrame(all_results, columns=['Model', 'TestSize', 'RandomState', 'CV', 'Accuracy', 'CrossValidationScore'])
print(df_all_results)
# Export to Excel
df_all_results.to_excel("model_performance.xlsx", index=False)