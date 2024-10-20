import pandas as pd
from datapreproc import preprocess_data
from model_training import train_model
from modelevelution import evaluate_model


data = pd.read_csv('Churn_Modelling.csv')

X_train, X_test, y_train, y_test = preprocess_data(data)

model = train_model(X_train, y_train)

evaluate_model(model, X_test, y_test)