import sys
import os
import pandas as pd
from src.model_evaluation import evaluate_model
from src.data_preprocessing import preprocess_data
from src.model_training import train_model

# Add the parent directory of 'src' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Specify the path to the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), '..', 'Churn_Modelling.csv')

# Load the data
try:
    data = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print(f"The file {csv_file_path} was not found.")
    exit()

# Preprocess the data
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train the model
model = train_model(X_train, y_train)

# Evaluate the model
evaluate_model(model, X_test, y_test)
