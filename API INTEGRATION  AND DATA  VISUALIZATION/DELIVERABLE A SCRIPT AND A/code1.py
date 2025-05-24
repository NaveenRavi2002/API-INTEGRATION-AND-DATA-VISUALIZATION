# disease_prediction_app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# -------------------- Load the trained model --------------------
model = joblib.load("disease_prediction_model.pkl")

# -------------------- List of symptoms --------------------
symptoms = [
    'fever', 'cough', 'fatigue', 'headache', 'nausea',
    'vomiting', 'diarrhea', 'shortness of breath', 'chest pain',
    'sore throat', 'loss of smell', 'loss of taste', 'runny nose',
    'muscle pain', 'joint pain', 'rash', 'abdominal pain'
]

# -------------------- Streamlit UI --------------------
st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction from Symptoms")
st.markdown("Select the symptoms you are experiencing:")

# Multi-select for symptoms
selected_symptoms = st.multiselect("Symptoms", symptoms)

# Predict Button
if st.button("Predict Disease"):
    input_data = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
    prediction = model.predict([input_data])[0]
    st.success(f"✅ Predicted Disease: **{prediction}**")

# -------------------- Data Visualization --------------------
st.markdown("## 📊 Symptom Frequency (Example Data)")

# Example symptom frequency data
symptom_data = {
    "Symptom": symptoms,
    "Frequency": np.random.randint(10, 100, size=len(symptoms))  # Placeholder data
}

df_symptoms = pd.DataFrame(symptom_data)

# Visualization
st.bar_chart(df_symptoms.set_index("Symptom"))
