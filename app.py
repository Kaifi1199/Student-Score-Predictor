import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, "poly_model.pkl")
transformer_path = os.path.join(base_path, "poly_transformer.pkl")

with open(model_path, "rb") as f:
    poly_model = pickle.load(f)

with open(transformer_path, "rb") as f:
    poly = pickle.load(f)
st.set_page_config(page_title="Student Score Predictor")
st.title("📚 Student Exam Score Predictor")
st.write("Enter the student's data to predict their expected exam score.")

# Input fields
hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, step=1)
attendance = st.slider("Attendance (%)", 0, 100, step=1)
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, step=1)
previous_scores = st.slider("Previous Scores", 0, 100, step=1)
tutoring_sessions = st.slider("Tutoring Sessions per week", 0, 7)

# Dropdowns for categorical inputs
pi_map = {'Low': 0, 'Medium': 1, 'High': 2}
ml_map = {'Low': 0, 'Medium': 1, 'High': 2}
pf_map = {'Negative': 0, 'Neutral': 1, 'Positive': 2}

parental_involvement_str = st.selectbox("Parental Involvement", options=list(pi_map.keys()))
motivation_level_str = st.selectbox("Motivation Level", options=list(ml_map.keys()))
peer_influence_str = st.selectbox("Peer Influence", options=list(pf_map.keys()))

# Map to numeric
parental_involvement = pi_map[parental_involvement_str]
motivation_level = ml_map[motivation_level_str]
peer_influence = pf_map[peer_influence_str]


# Submit button
if st.button("Predict Score"):
    # Create a dictionary for input
    input_dict = {
        'Hours_Studied': hours_studied,
        'Attendance': attendance,
        'Sleep_Hours': sleep_hours,
        'Previous_Scores': previous_scores,
        'Tutoring_Sessions': tutoring_sessions,
        'Parental_Involvement': parental_involvement,
        'Motivation_Level': motivation_level,
        'Peer_Influence': peer_influence
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([input_dict])

    # Polynomial transformation
    input_poly = poly.transform(input_df)

    # Predict
    predicted_score = poly_model.predict(input_poly)[0]
    st.success(f"🎯 Predicted Exam Score: **{predicted_score:.2f}**")