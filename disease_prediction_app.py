import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="assets/favicon.ico" if False else None,
    layout="wide",
)

# =============================================================================
# Custom CSS for a cleaner, more professional look
# =============================================================================
st.markdown("""
    <style>
        .main-title {
            font-size: 2rem;
            font-weight: 700;
            color: #1a1a2e;
            margin-bottom: 0.2rem;
        }
        .sub-title {
            font-size: 1rem;
            color: #555555;
            margin-bottom: 1.5rem;
        }
        .result-box {
            padding: 1rem;
            border-radius: 6px;
            font-size: 1rem;
        }
        .section-header {
            font-size: 1rem;
            font-weight: 600;
            color: #2c3e50;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05rem;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# =============================================================================
# Sidebar
# =============================================================================
st.sidebar.markdown("## Disease Prediction System")
st.sidebar.markdown("Select a disease module to proceed.")
st.sidebar.markdown("---")
choice = st.sidebar.radio(
    "Select Module",
    ["Parkinson's Disease", "Chronic Kidney Disease"],
    label_visibility="collapsed",
)
st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small>Algorithm: Random Forest<br>"
    "Data: UCI ML Repository<br>"
    "For research purposes only.</small>",
    unsafe_allow_html=True,
)

# =============================================================================
# PARKINSON'S MODULE
# =============================================================================
if choice == "Parkinson's Disease":

    st.markdown('<div class="main-title">Parkinson\'s Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Enter vocal feature measurements to generate a prediction.</div>', unsafe_allow_html=True)
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
            inputs.append(col1.number_input(f, value=0.0, key=f"pk_{f}"))
        elif i % 3 == 1:
            inputs.append(col2.number_input(f, value=0.0, key=f"pk_{f}"))
        else:
            inputs.append(col3.number_input(f, value=0.0, key=f"pk_{f}"))

    st.markdown("---")
    if st.button("Run Prediction", key="pk_predict", use_container_width=True):
        input_df   = pd.DataFrame([inputs], columns=features)
        prediction = model.predict(input_df)
        st.markdown("#### Prediction Result")
        if prediction[0] == 1:
            st.error("Parkinson's Disease Detected — Please consult a neurologist for further clinical evaluation.")
        else:
            st.success("No Parkinson's Disease Detected — Patient appears healthy based on the provided measurements.")

    st.markdown("---")
    st.caption("Random Forest Classifier  |  Test Accuracy: 92.31%  |  Dataset: UCI Parkinson's (195 samples, 22 features)")

# =============================================================================
# CKD MODULE
# =============================================================================
elif choice == "Chronic Kidney Disease":

    st.markdown('<div class="main-title">Chronic Kidney Disease Prediction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Enter patient clinical measurements to generate a prediction.</div>', unsafe_allow_html=True)
    st.markdown("---")

    model = joblib.load("rf_model_ckd.pkl")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">Numeric Features</div>', unsafe_allow_html=True)
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
        st.markdown('<div class="section-header">Categorical Features</div>', unsafe_allow_html=True)
        rbc   = st.selectbox("Red Blood Cells",           ["normal", "abnormal"])
        pc    = st.selectbox("Pus Cell",                  ["normal", "abnormal"])
        pcc   = st.selectbox("Pus Cell Clumps",           ["notpresent", "present"])
        ba    = st.selectbox("Bacteria",                  ["notpresent", "present"])
        htn   = st.selectbox("Hypertension",              ["yes", "no"])
        dm    = st.selectbox("Diabetes Mellitus",         ["yes", "no"])
        cad   = st.selectbox("Coronary Artery Disease",   ["yes", "no"])
        appet = st.selectbox("Appetite",                  ["good", "poor"])
        pe    = st.selectbox("Pedal Edema",               ["yes", "no"])
        ane   = st.selectbox("Anemia",                    ["yes", "no"])

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
    if st.button("Run Prediction", key="ckd_predict", use_container_width=True):
        prediction = model.predict(input_df)
        st.markdown("#### Prediction Result")
        if prediction[0] == 0:
            st.error("Chronic Kidney Disease Detected — Please consult a nephrologist for further clinical evaluation.")
        else:
            st.success("No Chronic Kidney Disease Detected — Patient appears healthy based on the provided measurements.")

    st.markdown("---")
    st.caption("Random Forest Classifier  |  Test Accuracy: 98.75%  |  Dataset: UCI CKD (400 samples, 24 features)")
