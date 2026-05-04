import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Customer Churn Analysis Dashboard")

# Load data
df = pd.read_csv("Churn_Modelling.csv")

# KPIs
st.subheader("Key Metrics")
col1, col2 = st.columns(2)

col1.metric("Total Customers", df.shape[0])
col2.metric("Churn Rate", f"{df['Exited'].mean():.2%}")

# -----------------------------
# Filter
st.sidebar.header("Filter Data")
gender_filter = st.sidebar.selectbox("Select Gender", ["All", "Male", "Female"])

if gender_filter != "All":
    df = df[df["Gender"] == gender_filter]

# -----------------------------
# Churn by Gender
st.subheader("Churn by Gender")
fig1, ax1 = plt.subplots()
sns.barplot(x='Gender', y='Exited', data=df, ax=ax1)
st.pyplot(fig1)

# -----------------------------
# Churn by Geography
st.subheader("Churn by Geography")
fig2, ax2 = plt.subplots()
sns.barplot(x='Geography', y='Exited', data=df, ax=ax2)
st.pyplot(fig2)

# -----------------------------
# Age Distribution
st.subheader("Age vs Churn")
fig3, ax3 = plt.subplots()
sns.histplot(data=df, x='Age', hue='Exited', bins=30, ax=ax3)
st.pyplot(fig3)

# -----------------------------
st.subheader("Churn Prediction")

# User inputs
credit_score = st.number_input("Credit Score", 300, 900, 600)
age = st.slider("Age", 18, 80, 30)
balance = st.number_input("Balance", 0.0, 200000.0, 50000.0)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
is_active = st.selectbox("Active Member", [0, 1])

# Simple rule-based prediction (for demo)
if st.button("Predict"):
    if is_active == 0 and age > 40 and num_products <= 2:
        st.error("High Risk of Churn")
    else:
        st.success("Low Risk of Churn")