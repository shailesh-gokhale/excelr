print (' ~ ~ ~ ~ ~ ~ ~ ~ OM SHRI GANESHAAYA NAMAHA ~ ~ ~ ~ ~ ~ ~ ~ ')

import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Load the trained model
model = joblib.load('model.pkl')

# Create the UI elements
st.title('Bankruptcy Prevention')
st.sidebar.title("Data Entry Panel")
feature1 = st.sidebar.slider('industrial_risk: 0=low risk, 0.5=medium risk, 1=high risk.', 0.0, 1.0, step=0.5)
feature2 = st.sidebar.slider('management_risk: 0=low risk, 0.5=medium risk, 1=high risk', 0.0, 1.0, step=0.5)
feature3 = st.sidebar.slider('financial_flexibility: 0=low flexibility, 0.5=medium flexibility, 1=high flexibility', 0.0, 1.0, step=0.5)
feature4 = st.sidebar.slider('credibility: 0=low credibility, 0.5=medium credibility, 1=high credibility', 0.0, 1.0, step=0.5)
feature5 = st.sidebar.slider('competitiveness: 0=low competitiveness, 0.5=medium competitiveness, 1=high competitiveness', 0.0, 1.0, step=0.5)
feature6 = st.sidebar.slider('operating_risk: 0=low risk, 0.5=medium risk, 1=high risk', 0.0, 1.0, step=0.5)

# Make predictions
prediction = model.predict([[feature1, feature2, feature3, feature4, feature5, feature6]])

# Display the prediction
if prediction[0] == 1:
    st.write('BANKRUPT')
else:
    st.write('NON-BANKRUPT')