from fastapi import FastAPI
import joblib
import pandas as pd
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_PATH, 'models', 'fraud_detection.pkl')

model = joblib.load(model_path)
app = FastAPI()

@app.post('/predict')

def predict(features: dict):
    df = pd.DataFrame([features])
    df['balanceDiffOrig'] = df['oldbalanceOrg'] - df['newbalanceOrig']
    df['balanceDiffDest'] = df['newbalanceDest'] - df['oldbalanceDest']

    pred = model.predict(df)

    return {
        'Fraud Prediction': int(pred[0])
    }