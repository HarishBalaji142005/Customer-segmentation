# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# -----------------------------
# 1. Page setup
# -----------------------------
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")
st.title("📊 Customer Segmentation Dashboard")

# -----------------------------
# 2. Load data from CSV (or from Flask API)
# -----------------------------
# For testing, we can load CSV directly
# Replace this with API call if your Flask backend is ready
try:
    df = pd.read_csv(r"C:\Users\haris\Documents\consumer\filled_cleaned_data.csv")
except:
    st.error("⚠️ Could not load data. Make sure the CSV path is correct.")
    st.stop()

# -----------------------------
# 3. Filters
# -----------------------------
st.sidebar.header("Filters")

region_filter = st.sidebar.multiselect(
    "Select Region", options=df['Region'].unique(), default=df['Region'].unique()
)
product_filter = st.sidebar.multiselect(
    "Select Product Category", options=df['ProductCategory'].unique(), default=df['ProductCategory'].unique()
)
income_range = st.sidebar.slider(
    "Annual Income Range", int(df['AnnualIncome'].min()), int(df['AnnualIncome'].max()),
    (int(df['AnnualIncome'].min()), int(df['AnnualIncome'].max()))
)
score_range = st.sidebar.slider(
    "Spending Score Range", int(df['SpendingScore'].min()), int(df['SpendingScore'].max()),
    (int(df['SpendingScore'].min()), int(df['SpendingScore'].max()))
)

# Apply filters
filtered_df = df[
    (df['Region'].isin(region_filter)) &
    (df['ProductCategory'].isin(product_filter)) &
    (df['AnnualIncome'] >= income_range[0]) & (df['AnnualIncome'] <= income_range[1]) &
    (df['SpendingScore'] >= score_range[0]) & (df['SpendingScore'] <= score_range[1])
]

st.write(f"### Filtered Data ({len(filtered_df)} records)")
st.dataframe(filtered_df)

# -----------------------------
# 4. Visualizations
# -----------------------------
st.subheader("Cluster Distribution")
if 'Cluster' in filtered_df.columns:
    cluster_count = filtered_df['Cluster'].value_counts().reset_index()
    cluster_count.columns = ['Cluster', 'Count']
    fig = px.pie(cluster_count, names='Cluster', values='Count', title="Customer Clusters")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Income vs Spending Score by Cluster")
if 'Cluster' in filtered_df.columns:
    fig2 = px.scatter(
        filtered_df,
        x='AnnualIncome',
        y='SpendingScore',
        color='Cluster',
        hover_data=['Gender', 'Region', 'ProductCategory'],
        title="Income vs Spending Score"
    )
    st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# 5. Predict Customer Cluster (optional)
# -----------------------------
st.subheader("Predict Customer Cluster")
with st.form("predict_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    region = st.selectbox("Region", df['Region'].unique())
    product = st.selectbox("Product Category", df['ProductCategory'].unique())
    income = st.number_input("Annual Income", int(df['AnnualIncome'].min()), int(df['AnnualIncome'].max()))
    spending = st.number_input("Spending Score", int(df['SpendingScore'].min()), int(df['SpendingScore'].max()))
    loyalty = st.number_input("Loyalty Score", int(df['LoyaltyScore'].min()), int(df['LoyaltyScore'].max()))
    freq = st.number_input("Purchase Frequency", int(df['PurchaseFrequency'].min()), int(df['PurchaseFrequency'].max()))
    
    submitted = st.form_submit_button("Predict Cluster")
    
    if submitted:
        # Call Flask API if backend is ready
        # Example payload
        payload = {
            "Gender": [gender],
            "Region": [region],
            "ProductCategory": [product],
            "AnnualIncome": [income],
            "SpendingScore": [spending],
            "LoyaltyScore": [loyalty],
            "PurchaseFrequency": [freq]
        }
        try:
            response = requests.post("http://127.0.0.1:5000/predict", json=payload)
            data = response.json()  # convert Response object to dictionary
            st.success(f"Predicted Cluster: {data['PredictedCluster']}")
        except:
            st.warning("⚠️ Flask backend not running. Showing sample prediction instead.")
            st.info("Predicted Cluster: 1")  # placeholder
