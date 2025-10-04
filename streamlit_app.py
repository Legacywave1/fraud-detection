import streamlit as st
import pandas as pd
import joblib
import os


BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_PATH, 'models', 'models/fraud_detection.pkl')

model = joblib.load(model_path)

st.title('Fraud Detection Prediction App')

st.markdown("Please enter the transaction details and use the predict button below")

st.divider()

transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT','DEPOSIT'])
amount = st.number_input('Amount', min_value=0.0, value = 1000.0)
oldbalanceOrg = st.number_input('Old Balance (Sender)', min_value= 0.0, value = 10000.0)
newbalanceOrig = st.number_input('New Balance (sender)', min_value = 0.0, value = 9000.0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value= 0.0, value = 0.0 )
newbalanceDest = st.number_input('New Balace (Receiver)', min_value = 0.0, value = 0.0 )
balanceDiffOrig = oldbalanceOrg - newbalanceOrig
balanceDiffDest = oldbalanceDest - newbalanceDest


if st.button('Predict'):
    input_data = pd.DataFrame([{
        'type': transaction_type,
        'amount' : amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'balanceDiffOrig': balanceDiffOrig,
        'balanceDiffDest': balanceDiffDest
    }])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] if hasattr(model, 'predict_proba') else None
    st.subheader(f"Predition: '{int(prediction)}'")

    if prediction == 1:
        st.error('This transaction can be Fraud⚠')
    else:
        st.success('This transaction does not seem fraudulent.')