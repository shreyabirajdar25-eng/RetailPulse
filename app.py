import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="RetailPulse",
    page_icon="📊",
    layout="wide"
)

# ---------------- LOAD DATA ----------------
df = pd.read_excel("data/Online Retail.xlsx")

# ---------------- HEADER ----------------
st.title("📊 RetailPulse Dashboard")
st.subheader("AI Powered Retail Analytics & Demand Forecasting")

# ---------------- KPIs ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Transactions", len(df))

with col2:
    st.metric("Total Products", df["Description"].nunique())

with col3:
    st.metric("Total Customers", df["CustomerID"].nunique())

st.divider()

# ---------------- DATASET PREVIEW ----------------
st.header("📂 Dataset Preview")
st.dataframe(df.head())

st.divider()

# ---------------- PROJECT MODULES ----------------
st.header("🚀 Completed Project Modules")

st.success("✔ Sales Analysis")
st.success("✔ Demand Forecasting")
st.success("✔ Customer Segmentation")
st.success("✔ Product Recommendation System")
st.success("✔ Customer Churn Prediction")

st.divider()

# ---------------- EDA VISUALIZATIONS ----------------
st.header("📈 Exploratory Data Analysis")

try:
    st.image("graph1.png", caption="Sales Trend Analysis")
except:
    st.warning("graph1.png not found")

try:
    st.image("graph 2.png", caption="Country-wise Quantity Sold")
except:
    st.warning("graph 2.png not found")

try:
    st.image("graph 3.png", caption="Top Products")
except:
    st.warning("graph 3.png not found")

try:
    st.image("graph 4.png", caption="Revenue Distribution")
except:
    st.warning("graph 4.png not found")

try:
    st.image("graph 5.png", caption="Sales Distribution")
except:
    st.warning("graph 5.png not found")

try:
    st.image("graph 6.png", caption="Monthly Revenue")
except:
    st.warning("graph 6.png not found")

try:
    st.image("graph 7.png", caption="Monthly Orders")
except:
    st.warning("graph 7.png not found")

st.divider()

# ---------------- DEMAND FORECASTING ----------------
st.header("🔮 Demand Forecasting")

try:
    st.image("graph 8.png", caption="Actual vs Predicted Revenue")
except:
    st.warning("graph 8.png not found")

try:
    st.image("graph 9.png", caption="Future Revenue Forecast")
except:
    st.warning("graph 9.png not found")

try:
    st.image("graph 10.png", caption="Forecast Analysis")
except:
    st.warning("graph 10.png not found")

st.divider()

# ---------------- CUSTOMER SEGMENTATION ----------------
st.header("👥 Customer Segmentation")

try:
    st.image("graph 11.png", caption="Customer Segments")
except:
    st.warning("graph 11.png not found")

try:
    st.image("graph 12.png", caption="Cluster Distribution")
except:
    st.warning("graph 12.png not found")

try:
    st.image("graph 13.png", caption="RFM Analysis")
except:
    st.warning("graph 13.png not found")

try:
    st.image("graph 14.png", caption="Customer Categories")
except:
    st.warning("graph 14.png not found")

st.divider()

# ---------------- PRODUCT RECOMMENDATION ----------------
st.header("🛒 Product Recommendation System")

try:
    st.image("graph 15.png", caption="Product Similarity")
except:
    st.warning("graph 15.png not found")

try:
    st.image("graph 16.png", caption="Recommended Products")
except:
    st.warning("graph 16.png not found")

st.divider()

# ---------------- CUSTOMER CHURN ----------------
st.header("⚠ Customer Churn Prediction")

try:
    st.image("graph 17.png", caption="Customer Churn Overview")
except:
    st.warning("graph 17.png not found")

try:
    st.image("graph 18.png", caption="Churn Analysis")
except:
    st.warning("graph 18.png not found")

try:
    st.image("graph 19.png", caption="High Risk Customers")
except:
    st.warning("graph 19.png not found")

st.divider()

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    """
    ### RetailPulse
    AI-Powered Retail Analytics & Demand Forecasting Platform
    
    Features:
    - Sales Analysis
    - Demand Forecasting
    - Customer Segmentation
    - Product Recommendation System
    - Customer Churn Prediction
    """
)