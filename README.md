# Fraud Detection

This is an End-to-end Machine Learning application to detect fraud in financial institutions. This is based on transaction type, amount of send, amount of receiver, etc.
The process demonstrate a full Machine Learning Lifecycle from data collection, to preprocessing and modelling to deployment with an interactive User Interface.


<img width="1424" height="788" alt="Fraud" src="https://github.com/user-attachments/assets/9a36a0d6-2221-4fdb-8bb6-a01a08ccc0c5" />


---
## Project Overview

Fraud detection is a critical challenge in finance. Using transaction data, this project trains a machine learning model to classify transactions as fraudulent (1) or non-fraudulent (0).

## Key highlights:

* Data Preprocessing: Cleaning, encoding, scaling.
* Model Training: Saved best model as fraud_detection.pkl.
* Backend: FastAPI API for serving predictions.
* Frontend: Streamlit app for user-friendly input.
* Deployment: Fully hosted on Render (backend).

## Features
* Interactive fraud prediction using transaction inputs.
* REST API with JSON support for integration into other apps.
* Real-time predictions with probability scores.
* Cloud-deployed and publicly accessible.

## Project Structure
''' fraud-detection/
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
'''

## How to Run Locally
1. Clone the repo
'''git clone https://github.com/Legacywave1/fraud-detection.git
cd fraud-detection
'''
2. Create & activate virtual environment
'''python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
'''
3. Install dependencies
'''pip install -r requirements.txt'''

4. Start FastAPI backend
'''uvicorn src.main:app --reload

Open http://127.0.0.1:8000/docs to test the API.'''

5. Start Streamlit frontend
'''streamlit run streamlit_app.py'''

# Example API Usage

POST /predict

'''{
  "type": "TRANSFER",
  "amount": 1200.50,
  "oldbalanceOrg": 5000.00,
  "newbalanceOrig": 3800.00,
  "oldbalanceDest": 1000.00,
  "newbalanceDest": 2200.50
}

'''
Response:

'''{
  "fraud_prediction": 1,
  "fraud_probability": 0.87
}'''

🌐 Deployment
Backend (FastAPI) → [Render](https://fraud-detection-bg5u.onrender.com/docs)
Frontend (Streamlit) → [Hugging Face](https://huggingface.co/spaces/Cyprian121/fraud-detection)
🛠️ Tech Stack
Python 3.12+
Pandas, NumPy, Scikit-learn
Joblib
FastAPI (backend)
Streamlit (frontend)
Render (deployment)


