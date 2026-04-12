import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Disease Prediction App", page_icon="🏥", layout="wide")

# ── Sidebar selector ────────────────────────────────────────────────────────
st.sidebar.title("🏥 Disease Prediction")
st.sidebar.markdown("Select a disease to predict:")
choice = st.sidebar.radio("", ["Parkinson's Disease", "Chronic Kidney Disease"])
st.sidebar.markdown("---")
st.sidebar.caption("Models trained using Random Forest\nAlgorithm on UCI datasets.")

# =============================================================================
# PARKINSON'S APP
# =============================================================================
if choice == "Parkinson's Disease":
    st.title("🧠 Parkinson's Disease Prediction")
    st.markdown("Enter the vocal feature measurements below and click **Predict**.")
    st.markdown("---")

    model = joblib.load("model.pkl")

    features = [
        'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)',
        'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP',
        'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer',
        'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
        'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR',
        'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE'
    ]

    col1, col2, col3 = st.columns(3)
    inputs = []
    for i, f in enumerate(features):
        if i % 3 == 0:
            inputs.append(col1.number_input(f, value=0.0, key=f))
        elif i % 3 == 1:
            inputs.append(col2.number_input(f, value=0.0, key=f))
        else:
            inputs.append(col3.number_input(f, value=0.0, key=f))

    st.markdown("---")
    if st.button("Predict", key="pk_predict", use_container_width=True):
        input_df = pd.DataFrame([inputs], columns=features)
        prediction = model.predict(input_df)
        st.markdown("### Result")
        if prediction[0] == 1:
            st.error("⚠️ Parkinson's Disease Detected")
            st.markdown("Please consult a neurologist for further evaluation.")
        else:
            st.success("✅ No Parkinson's Disease Detected")
            st.markdown("Patient appears healthy based on the provided values.")

    st.markdown("---")
    st.caption("Model: Random Forest | Accuracy: 92.31% | Dataset: UCI Parkinson's")

# =============================================================================
# CKD APP
# =============================================================================
elif choice == "Chronic Kidney Disease":
    st.title("🩺 Chronic Kidney Disease Prediction")
    st.markdown("Fill in the patient details below and click **Predict**.")
    st.markdown("---")

    model = joblib.load("rf_model_ckd.pkl")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Numeric Features")
        age  = st.number_input("Age",                    min_value=0,   max_value=120, value=45)
        bp   = st.number_input("Blood Pressure",         min_value=0,   max_value=200, value=80)
        sg   = st.number_input("Specific Gravity",       min_value=1.0, max_value=1.03,value=1.02, format="%.3f")
        al   = st.number_input("Albumin",                min_value=0,   max_value=5,   value=0)
        su   = st.number_input("Sugar",                  min_value=0,   max_value=5,   value=0)
        bgr  = st.number_input("Blood Glucose Random",   min_value=0.0, value=100.0)
        bu   = st.number_input("Blood Urea",             min_value=0.0, value=30.0)
        sc   = st.number_input("Serum Creatinine",       min_value=0.0, value=1.0,  format="%.1f")
        sod  = st.number_input("Sodium",                 min_value=0.0, value=135.0)
        pot  = st.number_input("Potassium",              min_value=0.0, value=4.0,  format="%.1f")
        hemo = st.number_input("Hemoglobin",             min_value=0.0, value=12.0, format="%.1f")
        pcv  = st.number_input("Packed Cell Volume",     min_value=0.0, value=40.0)
        wc   = st.number_input("White Blood Cell Count", min_value=0.0, value=8000.0)
        rc   = st.number_input("Red Blood Cell Count",   min_value=0.0, value=4.5,  format="%.1f")

    with col2:
        st.subheader("Categorical Features")
        rbc   = st.selectbox("Red Blood Cells",          ["normal", "abnormal"])
        pc    = st.selectbox("Pus Cell",                 ["normal", "abnormal"])
        pcc   = st.selectbox("Pus Cell Clumps",          ["notpresent", "present"])
        ba    = st.selectbox("Bacteria",                 ["notpresent", "present"])
        htn   = st.selectbox("Hypertension",             ["yes", "no"])
        dm    = st.selectbox("Diabetes Mellitus",        ["yes", "no"])
        cad   = st.selectbox("Coronary Artery Disease",  ["yes", "no"])
        appet = st.selectbox("Appetite",                 ["good", "poor"])
        pe    = st.selectbox("Pedal Edema",              ["yes", "no"])
        ane   = st.selectbox("Anemia",                   ["yes", "no"])

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

    input_dict = {
        "age": age, "bp": bp, "sg": sg, "al": al, "su": su,
        "rbc": rbc, "pc": pc, "pcc": pcc, "ba": ba,
        "bgr": bgr, "bu": bu, "sc": sc, "sod": sod, "pot": pot,
        "hemo": hemo, "pcv": pcv, "wc": wc, "rc": rc,
        "htn": htn, "dm": dm, "cad": cad, "appet": appet,
        "pe": pe, "ane": ane,
    }

    encoded = input_dict.copy()
    for col, mapping in cat_map.items():
        encoded[col] = mapping[input_dict[col]]

    input_df = pd.DataFrame([encoded])

    st.markdown("---")
    if st.button("Predict", key="ckd_predict", use_container_width=True):
        prediction = model.predict(input_df)
        st.markdown("### Result")
        if prediction[0] == 0:
            st.error("⚠️ Chronic Kidney Disease Detected")
            st.markdown("Please consult a nephrologist for further evaluation.")
        else:
            st.success("✅ No Chronic Kidney Disease Detected")
            st.markdown("Patient appears healthy based on the provided values.")

    st.markdown("---")
    st.caption("Model: Random Forest | Accuracy: 98.75% | Dataset: UCI CKD")
