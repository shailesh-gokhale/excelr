print (' ~ ~ ~ ~ ~ ~ ~ ~ OM SHRI GANESHAAYA NAMAHA ~ ~ ~ ~ ~ ~ ~ ~ ')

# v2.0
# Updates: UI update, added class probabilities and threshold setting for LR

import streamlit as st
import joblib

# Load the trained model
model = joblib.load('model.pkl')


# Define a dictionary to map numerical values to category names
category_map = {'Low': 0, 'Medium': 0.5, 'High': 1}
threshold_map = {'15%': 15, '30%': 30, '45%': 45, '60%': 60, '75%': 75, '90%': 90}

# Create the UI elements
st.markdown(
    "<p style='font-size: 32px; color: blue'>Bankruptcy Prevention.</p>"
    "<p style='font-size: 24px; background-color: #eeeeee; display: inline; padding: 5px; border-radius: 5px;'>Selected Model: Logistic Regression</p>", 
    unsafe_allow_html=True
)
st.sidebar.title("Data Entry Panel")
feature1 = st.sidebar.selectbox("Industrial Risk: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])
feature2 = st.sidebar.selectbox("Management Risk: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])
feature3 = st.sidebar.selectbox("Financial Flexibility: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])
feature4 = st.sidebar.selectbox("Credibility: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])
feature5 = st.sidebar.selectbox("Competitiveness: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])
feature6 = st.sidebar.selectbox("Operating Risk: ", options=list(category_map.values()), format_func=lambda x: list(category_map.keys())[list(category_map.values()).index(x)])

threshold = st.sidebar.selectbox("Threshold: ", options=list(threshold_map.values()), format_func=lambda x: list(threshold_map.keys())[list(threshold_map.values()).index(x)], index=2)


# Make predictions
prediction = model.predict([[int(feature1), int(feature2), int(feature3), int(feature4), int(feature5), int(feature6)]])
probabilities = model.predict_proba([[int(feature1), int(feature2), int(feature3), int(feature4), int(feature5), int(feature6)]])
prob_0 = round(probabilities[0][0], 4)*100
prob_1 = round(probabilities[0][1], 4)*100

# Display the prediction
if prediction[0] == 1:
    st.markdown(
    "<p style='font-size: 20px; color: red'><b>Predicted Class (@threshold=50%): BANKRUPT [1]</b></p>", 
    unsafe_allow_html=True
)
else:
    st.markdown(
    "<p style='font-size: 20px; color: green'><b>Predicted Class (@threshold=50%): NON-BANKRUPT [0]</b></p>", 
    unsafe_allow_html=True
)

# Display the prediction for selected threshold
if prob_1 > threshold:
    st.markdown(
    "<p style='font-size: 20px; color: red'><b>Predicted Class (@threshold=" + str(threshold) + "%): BANKRUPT [1]</b></p>", 
    unsafe_allow_html=True
)
else:
    st.markdown(
    "<p style='font-size: 20px; color: green'><b>Predicted Class (@threshold=" + str(threshold) + "%): NON-BANKRUPT [0]</b></p>", 
    unsafe_allow_html=True
)

# Display the class probabilities
st.markdown("<p style='font-size: 20px; color: blue'><b>Class Probabilities: </p>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size: 18px; color: #666666'><b>Class Non-Bankrupt [0]: </b> <span style='background-color: #eeeeee; display: inline; padding: 3px; border-radius: 5px;'> " + 
    str(prob_0) +
    "%</span> | <b>Class Bankrupt [1]: </b><span style='background-color: #eeeeee; display: inline; padding: 3px; border-radius: 5px;'>" + str(prob_1) + "%</span></p>",
    unsafe_allow_html=True
)

# Display the selected parameters for all features
st.markdown("<p style='font-size: 20px; color: blue'><b>Predictors: </p>", unsafe_allow_html=True)
selected_features = {
    "Industrial Risk": list(category_map.keys())[list(category_map.values()).index(feature1)],
    "Management Risk": list(category_map.keys())[list(category_map.values()).index(feature2)],
    "Financial Flexibility": list(category_map.keys())[list(category_map.values()).index(feature3)],
    "Credibility": list(category_map.keys())[list(category_map.values()).index(feature4)],
    "Competitiveness": list(category_map.keys())[list(category_map.values()).index(feature5)],
    "Operating Risk": list(category_map.keys())[list(category_map.values()).index(feature6)]
}

selected_values = {key: category_map[value] for key, value in selected_features.items()}

st.write(selected_values)
print(selected_values)
#st.table(selected_values)