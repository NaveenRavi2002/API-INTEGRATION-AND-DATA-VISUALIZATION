# disease_prediction_app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
st.markdown("## 📊 Symptom Frequency Analysis")

# Example data - Replace with actual dataset
symptom_freq = {
    "Symptom": symptoms,
    "Frequency": np.random.randint(10, 100, size=len(symptoms))
}
df_symptom_freq = pd.DataFrame(symptom_freq)

# ---- Matplotlib Bar Plot ----
st.markdown("### 🔵 Bar Plot (Matplotlib)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_symptom_freq["Symptom"], df_symptom_freq["Frequency"], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Frequency")
plt.title("Symptom Frequency (Example Data)")
st.pyplot(fig)

# ---- Seaborn Heatmap ----
st.markdown("### 🔥 Heatmap (Seaborn)")
# Generate fake correlation data for demo
corr_data = np.random.rand(len(symptoms), len(symptoms))
df_corr = pd.DataFrame(corr_data, index=symptoms, columns=symptoms)

fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.heatmap(df_corr, cmap="YlGnBu", ax=ax2)
plt.title("Symptom Correlation Heatmap (Demo)")
st.pyplot(fig2)
