# app.py
from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load your trained RandomForest model (replace with your actual model file)
model = joblib.load("random_forest_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()       # get data from Streamlit
        df = pd.DataFrame(data)         # convert to DataFrame
        predicted_cluster = model.predict(df)
        return jsonify({"PredictedCluster": int(predicted_clusters[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

