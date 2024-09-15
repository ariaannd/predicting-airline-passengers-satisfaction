import pickle
import pandas as pd
import streamlit

# Load the SVC model
with open('model.pkl', 'rb') as file:
    model_svc_loaded = pickle.load(file)

def predict_default(features):

    # Predict using the model
    prediction = model_svc_loaded.predict(features)
    return prediction[0]