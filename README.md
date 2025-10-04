# Fraud Detection App

This is an End-to-end Machine Learning application to detect fraud in financial institutions. This is based on transaction type, balance of sender, balance of receiver, etc.
The process demonstrate a full Machine Learning Lifecycle from data collection, to preprocessing and using ADASYN for oversampling minority and modelling to deployment with an interactive User Interface.


<img width="1424" height="788" alt="Fraud" src="https://github.com/user-attachments/assets/9a36a0d6-2221-4fdb-8bb6-a01a08ccc0c5" />


---
## Project Overview

Fraud detection is a critical challenge in finance. Using transaction data, this project trains a machine learning model to classify transactions as fraudulent (1) or non-fraudulent (0).

## Key highlights:

* Data Preprocessing: Cleaning, encoding, scaling, and oversampling minority using ADASYN.
* Model Training: Saved best model as fraud_detection.pkl.
* Backend: FastAPI API for serving predictions.
* Frontend: Streamlit app for user-friendly input.
* Deployment: Fully hosted on Render and hugging face.

## Features
* Interactive fraud prediction using transaction inputs.
* REST API with JSON support for integration into other apps.
* Real-time predictions with probability scores.
* Cloud-deployed and publicly accessible.

## Project Structure
```bash fraud-detection/
│
├── data/                # Dataset(s) (excluded, too large for GitHub)
├── models/              # Trained model artifact (fraud_detection.pkl)
├── notebooks/           # Jupyter/Colab notebooks
├── src/                 # FastAPI backend code
│   ├── main.py          # FastAPI app
├── streamlit_app.py     # Streamlit frontend
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── .gitignore           # Ignore datasets, venv, etc.
```
---
## How to Run Locally
1. Clone the repo
```bash git clone https://github.com/Legacywave1/fraud-detection.git```
```bash cd fraud-detection```
2. Create & activate virtual environment
```bash python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
3. Install dependencies
```bash pip install -r requirements.txt```

4. Start FastAPI backend
```bash uvicorn src.main:app --reload```
   
```bash Open http://127.0.0.1:8000/docs to test the API.```

5. Start Streamlit frontend
```bash streamlit run streamlit_app.py```
---

# Example API Usage

POST /predict

```bash
{
  "type": "TRANSFER",
  "amount": 1200.50,
  "oldbalanceOrg": 5000.00,
  "newbalanceOrig": 3800.00,
  "oldbalanceDest": 1000.00,
  "newbalanceDest": 2200.50
}

```
Response:

```bash
{
  "fraud_prediction": 0
}
```
---

## Live Demo
* FastAPI(Render): https://fraud-detection-bg5u.onrender.com/docs
* Streamlit(Hugging Face Spaces): https://huggingface.co/spaces/Cyprian121/fraud-detection

---

## Deployment
* Backend (FastAPI) → Render
* Frontend (Streamlit) → Hugging Face

## Tech Stack
* Python 3.12+
* Pandas, Seaborn, Scikit-learn, Imbalance, Joblib
* FastAPI (backend)
* Streamlit (frontend)
* Render (deployment)









