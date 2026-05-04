# Customer Churn Analysis & Prediction

## Overview
This project analyzes customer churn in a banking dataset and builds a machine learning model to predict whether a customer will leave.

---

## Tools & Technologies
- SQL (MySQL)
- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Machine Learning (Scikit-learn)
- Streamlit (Dashboard)

---

## Key Insights
- Customers in Germany have the highest churn rate (~32%)
- Female customers churn more than male customers
- Inactive members are more likely to leave
- High-balance customers are also at risk of churn

---

## Model Performance
- Model: Logistic Regression
- Accuracy: ~70%
- Improved recall for churn prediction

---

## Features Used
- Credit Score
- Age
- Balance
- Number of Products
- Geography
- Activity Status

---

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
