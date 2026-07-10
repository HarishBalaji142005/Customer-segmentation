Customer Segmentation Dashboard

A machine learning project that segments customers into clusters based on their purchasing behavior, and serves predictions through a Flask API with an interactive Streamlit dashboard.

📌 Project Overview

This project analyzes customer data (income, spending score, loyalty score, purchase frequency, etc.) to group customers into meaningful segments using a Random Forest model.
🗂️ Project Structure

├── customer_segmentation_analysis.ipynb   # EDA and analysis notebook
├── create_random_forest_model.py          # Trains and saves the ML model
├── app.py                                 # Flask backend serving predictions
├── dashboard.py                           # Streamlit dashboard (frontend)
├── raw_data.csv                           # Original dataset
├── segmented_customers.csv                # Final segmented dataset
├── random_forest_model.pkl                # Trained model file
├── requirements.txt                       # Python dependencies
└── README.md

⚙️ Features


Exploratory data analysis on customer demographics and purchase behavior
Customer segmentation using a Random Forest model
Interactive dashboard with filters (Region, Product Category, Income, Spending Score)
Visualizations: cluster distribution (pie chart), income vs. spending score (scatter plot)
Real-time cluster prediction for new customer inputs via Flask API


🚀 Getting Started

Prerequisites


Python 3.9+
pip


Train the model

bashpython create_random_forest_model.py

This generates random_forest_model.pkl.
Run the Flask API

bashpython app.py

The API will be available at http://127.0.0.1:5000.

Run the Dashboard

In a separate terminal:

bashstreamlit run dashboard.py

This opens the dashboard at http://localhost:8501.

🛠️ Tech Stack


Python — pandas, scikit-learn, joblib
Backend — Flask
Frontend — Streamlit, Plotly
ML Model — Random Forest Classifier


📊 Dataset

The dataset includes customer attributes such as:


Demographics: Gender, Region
Behavior: Product Category, Purchase Frequency
Value metrics: Annual Income, Spending Score, Loyalty Score


📝 Notes


Update the dataset path in dashboard.py if running locally with a different file structure (avoid hardcoded absolute paths).
Make sure the Flask API (app.py) is running before submitting predictions from the dashboard.


📄 License

This project is open source and available under the MIT License.
