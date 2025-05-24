import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
df = pd.read_csv("symptom_disease_data.csv")  # Should be preprocessed

# Feature matrix and label
X = df[symptoms]  # Ensure these columns exist
y = df['prognosis']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "disease_prediction_model.pkl")
