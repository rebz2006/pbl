import streamlit as st
import pandas as pd
import joblib

model = joblib.load("rf_model_ckd.pkl")

st.set_page_config(page_title="CKD Prediction", page_icon="🩺")
st.title("🩺 Chronic Kidney Disease Prediction")
st.markdown("Fill in the patient details below and click **Predict**.")

st.subheader("Patient Information")
col1, col2 = st.columns(2)

with col1:
    age  = st.number_input("Age",              min_value=0,   max_value=120, value=45)
    bp   = st.number_input("Blood Pressure",   min_value=0,   max_value=200, value=80)
    sg   = st.number_input("Specific Gravity", min_value=1.0, max_value=1.03,value=1.02, format="%.3f")
    al   = st.number_input("Albumin",          min_value=0,   max_value=5,   value=0)
    su   = st.number_input("Sugar",            min_value=0,   max_value=5,   value=0)
    bgr  = st.number_input("Blood Glucose Random", min_value=0.0, value=100.0)
    bu   = st.number_input("Blood Urea",       min_value=0.0, value=30.0)
    sc   = st.number_input("Serum Creatinine", min_value=0.0, value=1.0, format="%.1f")
    sod  = st.number_input("Sodium",           min_value=0.0, value=135.0)
    pot  = st.number_input("Potassium",        min_value=0.0, value=4.0, format="%.1f")
    hemo = st.number_input("Hemoglobin",       min_value=0.0, value=12.0, format="%.1f")
    pcv  = st.number_input("Packed Cell Volume", min_value=0.0, value=40.0)

with col2:
    wc   = st.number_input("White Blood Cell Count", min_value=0.0, value=8000.0)
    rc   = st.number_input("Red Blood Cell Count",   min_value=0.0, value=4.5, format="%.1f")

    rbc   = st.selectbox("Red Blood Cells",       ["normal", "abnormal"])
    pc    = st.selectbox("Pus Cell",              ["normal", "abnormal"])
    pcc   = st.selectbox("Pus Cell Clumps",       ["notpresent", "present"])
    ba    = st.selectbox("Bacteria",              ["notpresent", "present"])
    htn   = st.selectbox("Hypertension",          ["yes", "no"])
    dm    = st.selectbox("Diabetes Mellitus",     ["yes", "no"])
    cad   = st.selectbox("Coronary Artery Disease",["yes", "no"])
    appet = st.selectbox("Appetite",              ["good", "poor"])
    pe    = st.selectbox("Pedal Edema",           ["yes", "no"])
    ane   = st.selectbox("Anemia",                ["yes", "no"])

# ── Build input dataframe in same column order as training ──────────────────
input_dict = {
    "age": age, "bp": bp, "sg": sg, "al": al, "su": su,
    "rbc": rbc, "pc": pc, "pcc": pcc, "ba": ba,
    "bgr": bgr, "bu": bu, "sc": sc, "sod": sod, "pot": pot,
    "hemo": hemo, "pcv": pcv, "wc": wc, "rc": rc,
    "htn": htn, "dm": dm, "cad": cad, "appet": appet,
    "pe": pe, "ane": ane,
}

# Encode categorical values exactly as LabelEncoder would (alphabetical order)
cat_map = {
    "rbc"  : {"abnormal": 0, "normal": 1},
    "pc"   : {"abnormal": 0, "normal": 1},
    "pcc"  : {"notpresent": 0, "present": 1},
    "ba"   : {"notpresent": 0, "present": 1},
    "htn"  : {"no": 0, "yes": 1},
    "dm"   : {"no": 0, "yes": 1},
    "cad"  : {"no": 0, "yes": 1},
    "appet": {"good": 0, "poor": 1},
    "pe"   : {"no": 0, "yes": 1},
    "ane"  : {"no": 0, "yes": 1},
}

encoded = input_dict.copy()
for col, mapping in cat_map.items():
    encoded[col] = mapping[input_dict[col]]

input_df = pd.DataFrame([encoded])

# ── Predict ─────────────────────────────────────────────────────────────────
if st.button("Predict"):
    prediction = model.predict(input_df)

    # LabelEncoder encodes ckd=0, notckd=1
    if prediction[0] == 0:
        st.error("⚠️ Chronic Kidney Disease Detected")
        st.markdown("Please consult a nephrologist for further evaluation.")
    else:
        st.success("✅ No Chronic Kidney Disease Detected")
        st.markdown("Patient appears healthy based on the provided values.")

st.markdown("---")
st.caption("Model: Random Forest | Accuracy: 98.75% | Dataset: UCI CKD")
