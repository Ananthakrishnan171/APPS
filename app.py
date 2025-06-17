import streamlit as st
import pickle
import numpy as np

# Load the model
with open('bank_customer.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("Bank Customer Churn Prediction")
st.write("Enter customer details to predict whether they will churn.")

# Input fields
tenure = st.slider("Tenure (in years)", 0, 10, 3)
balance = st.number_input("Account Balance", min_value=0, step=1000)
num_products = st.selectbox("Number of Products", [1, 2, 3, 4])
estimated_salary = st.number_input("Estimated Salary", min_value=0, step=1000)

# Predict button
if st.button("Predict Churn"):
    input_data = np.array([[tenure, balance, num_products, estimated_salary]])
    prediction = model.predict(input_data)
    
    # Output result
    if prediction[0] == 1:
        st.error("🔴 The customer is likely to churn.")
    else:
        st.success("🟢 The customer is likely to stay.")
