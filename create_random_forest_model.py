# create_random_forest_model.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1️⃣ Load a sample dataset (Iris dataset)
data = load_iris()
X = data.data
y = data.target

# 2️⃣ Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4️⃣ Save the trained model to a file named 'random_forest_model.pkl'
joblib.dump(model, "random_forest_model.pkl")

print("Random Forest model has been saved as 'random_forest_model.pkl'")
