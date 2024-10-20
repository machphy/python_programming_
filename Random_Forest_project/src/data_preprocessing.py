import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocess_data(data):
    
    data.fillna(method='ffill', inplace=True)


    data['Age_Tenure_Product'] = data['Age'] * data['Tenure'] * data['NumOfProducts']
    data['Balance'] = np.log1p(data['Balance']) 

    le = LabelEncoder()
    data['Geography'] = le.fit_transform(data['Geography'])
    data['Gender'] = le.fit_transform(data['Gender'])

    
    scaler = StandardScaler()
    data[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']] = scaler.fit_transform(data[['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']])

    
    X = data.drop('Exited', axis=1)
    y = data['Exited']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test