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

# ---------------- SIDEBAR ----------------
st.sidebar.title("📊 RetailPulse")

page = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "EDA",
        "Forecasting",
        "Segmentation",
        "Recommendations",
        "Churn"
    ]
)

# ---------------- OVERVIEW ----------------
if page == "Overview":

    st.title("📊 RetailPulse Dashboard")
    st.subheader("AI Powered Retail Analytics & Demand Forecasting")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Transactions", len(df))

    with col2:
        st.metric("Total Products", df["Description"].nunique())

    with col3:
        st.metric("Total Customers", df["CustomerID"].nunique())

    st.divider()

    st.header("📂 Dataset Preview")
    st.dataframe(df.head())

    st.divider()

    st.header("🚀 Completed Modules")

    st.success("✔ Sales Analysis")
    st.success("✔ Demand Forecasting")
    st.success("✔ Customer Segmentation")
    st.success("✔ Product Recommendation System")
    st.success("✔ Customer Churn Prediction")

# ---------------- EDA ----------------
elif page == "EDA":

    st.title("📈 Exploratory Data Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph1.png", caption="Sales Trend Analysis", use_container_width=True)

    with col2:
        st.image("screenshots/graph 2.png", caption="Country-wise Quantity Sold", use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 3.png", caption="Top Products", use_container_width=True)

    with col2:
        st.image("screenshots/graph 4.png", caption="Revenue Distribution", use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 5.png", caption="Sales Distribution", use_container_width=True)

    with col2:
        st.image("screenshots/graph 6.png", caption="Monthly Revenue", use_container_width=True)

    st.image("screenshots/graph 7.png", caption="Monthly Orders", use_container_width=True)

# ---------------- FORECASTING ----------------
elif page == "Forecasting":

    st.title("🔮 Demand Forecasting")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 8.png", caption="Actual vs Predicted Revenue", use_container_width=True)

    with col2:
        st.image("screenshots/graph 9.png", caption="Future Revenue Forecast", use_container_width=True)

    st.image("screenshots/graph 10.png", caption="Forecast Analysis", use_container_width=True)

# ---------------- SEGMENTATION ----------------
elif page == "Segmentation":

    st.title("👥 Customer Segmentation")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 11.png", caption="Customer Segments", use_container_width=True)

    with col2:
        st.image("screenshots/graph 12.png", caption="Cluster Distribution", use_container_width=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 13.png", caption="RFM Analysis", use_container_width=True)

    with col2:
        st.image("screenshots/graph 14.png", caption="Customer Categories", use_container_width=True)

# ---------------- RECOMMENDATIONS ----------------
elif page == "Recommendations":

    st.title("🛒 Product Recommendation System")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 15.png", caption="Product Similarity", use_container_width=True)

    with col2:
        st.image("screenshots/graph 16.png", caption="Recommended Products", use_container_width=True)

# ---------------- CHURN ----------------
elif page == "Churn":

    st.title("⚠ Customer Churn Prediction")

    col1, col2 = st.columns(2)

    with col1:
        st.image("screenshots/graph 17.png", caption="Customer Churn Overview", use_container_width=True)

    with col2:
        st.image("screenshots/graph 18.png", caption="Churn Analysis", use_container_width=True)

    st.image("screenshots/graph 19.png", caption="High Risk Customers", use_container_width=True)

# ---------------- FOOTER ----------------
st.divider()

st.markdown(
    """
    ### RetailPulse

    AI Powered Retail Analytics & Demand Forecasting Platform

    Features:
    - Sales Analysis
    - Demand Forecasting
    - Customer Segmentation
    - Product Recommendation System
    - Customer Churn Prediction
    """
)