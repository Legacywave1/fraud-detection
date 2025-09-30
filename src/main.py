from fastapi import FastAPI
import joblib
import pandas as pd


model = joblib.load('models/fraud_detection2.pkl')

app = FastAPI()

@app.post('/predict')

def predict(features: dict):
    df = pd.DataFrame([features])

    pred = model.predict(df)

    return {
        'Fraud Prediction': int(pred[0])
    }