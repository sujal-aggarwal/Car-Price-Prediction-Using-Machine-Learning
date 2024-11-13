import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl') 

# Define the UI in Streamlit
st.title("Car Price Prediction App")
st.write("Enter the car details below to get a price prediction.")

# Input fields for user data
year = st.number_input("Car Year", min_value=1990, max_value=2023, step=1)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=100)
fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission Type", ["Manual", "Automatic"])
owner = st.number_input("Number of Previous Owners", min_value=0, step=1)

# Encoding categorical inputs
fuel_type_encoded = 0 if fuel_type == "Petrol" else 1 if fuel_type == "Diesel" else 2
seller_type_encoded = 0 if seller_type == "Dealer" else 1
transmission_encoded = 0 if transmission == "Manual" else 1

# Calculate the car's age
current_year = 2024
# age = current_year - year
age = year
# Make predictions
if st.button("Predict Price"):
    # Create input array for prediction
    features = np.array([[age, present_price, kms_driven, fuel_type_encoded, seller_type_encoded, transmission_encoded, owner]])
    # Predict using the model
    predicted_price = model.predict(features)
    st.write(f"Predicted Selling Price: ₹{predicted_price[0]:.2f} lakhs")


