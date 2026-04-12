import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Parkinson's Disease Prediction")

features = [
    'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)',
    'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP',
    'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer',
    'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
    'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
    'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
]

inputs = []
for f in features:
    inputs.append(st.number_input(f, value=0.0))

if st.button("Predict"):
    input_df = pd.DataFrame([inputs], columns=features)
    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("Parkinson's Detected")
    else:
        st.success("Healthy")