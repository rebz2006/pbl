import streamlit as st
import joblib
import numpy as np

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Disease Prediction App",
    page_icon="🩺",
    layout="wide",
)

# ── Load models (cached so they don't reload every interaction) ─────────────
@st.cache_resource
def load_models():
    park_model = joblib.load("model.pkl")
    ckd_model  = joblib.load("rf_model_ckd.pkl")
    return park_model, ckd_model

park_model, ckd_model = load_models()

# ── Sidebar navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.title("🩺 Disease Predictor")
    st.markdown("---")
    page = st.selectbox(
        "Select Disease Module",
        ["🏠 Home", "🧠 Parkinson's Disease", "🫘 Chronic Kidney Disease"]
    )
    st.markdown("---")
    st.caption("Models: Random Forest Classifier\nAccuracy: Parkinson's 92.3% | CKD 98.75%")

# ══════════════════════════════════════════════════════════════════════════════
# HOME PAGE
# ══════════════════════════════════════════════════════════════════════════════
if page == "🏠 Home":
    st.title("🩺 Disease Prediction System")
    st.markdown("""
    Welcome! This app uses **Machine Learning (Random Forest)** to predict the
    likelihood of two diseases based on clinical measurements.

    ---

    ### 📋 Available Modules

    | Module | Disease | Input Type | Model Accuracy |
    |--------|---------|------------|----------------|
    | 🧠 Parkinson's Disease | Neurological disorder | 22 vocal measurements | 92.31% |
    | 🫘 Chronic Kidney Disease | Kidney function disorder | 24 lab test values | 98.75% |

    ---

    ### 🚀 How to Use
    1. Select a disease module from the **sidebar on the left**
    2. Enter the required measurement values
    3. Click **Run Prediction**
    4. The app will tell you whether the disease is **detected or not**

    > ⚠️ This tool is for educational/research purposes only.
    > It is not a substitute for professional medical diagnosis.
    """)

# ══════════════════════════════════════════════════════════════════════════════
# PARKINSON'S PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🧠 Parkinson's Disease":
    st.title("🧠 Parkinson's Disease Prediction")
    st.markdown("Enter the **22 vocal measurement features** from the patient's voice recording.")
    st.markdown("---")

    # Default/example values from the dataset mean
    defaults = {
        "MDVP:Fo(Hz)": 154.23, "MDVP:Fhi(Hz)": 197.10, "MDVP:Flo(Hz)": 116.32,
        "MDVP:Jitter(%)": 0.00622, "MDVP:Jitter(Abs)": 0.00004, "MDVP:RAP": 0.00317,
        "MDVP:PPQ": 0.00349, "Jitter:DDP": 0.00951, "MDVP:Shimmer": 0.02971,
        "MDVP:Shimmer(dB)": 0.28200, "Shimmer:APQ3": 0.01540, "Shimmer:APQ5": 0.01780,
        "MDVP:APQ": 0.02497, "Shimmer:DDA": 0.04619, "NHR": 0.02488,
        "HNR": 21.886, "RPDE": 0.49888, "DFA": 0.71817,
        "spread1": -5.6840, "spread2": 0.22692, "D2": 2.38176, "PPE": 0.20654,
    }

    col1, col2, col3 = st.columns(3)
    features = list(defaults.keys())
    values = []

    for i, feat in enumerate(features):
        col = [col1, col2, col3][i % 3]
        with col:
            val = st.number_input(feat, value=defaults[feat], format="%.5f", key=f"p_{feat}")
            values.append(val)

    st.markdown("---")

    col_btn, col_info = st.columns([1, 3])
    with col_btn:
        predict_btn = st.button("🔍 Run Prediction", type="primary", use_container_width=True)
    with col_info:
        st.caption("💡 Tip: The default values above are dataset averages. Change them to patient-specific values.")

    if predict_btn:
        input_array = np.array(values).reshape(1, -1)
        prediction = park_model.predict(input_array)[0]
        proba = park_model.predict_proba(input_array)[0]

        st.markdown("---")
        if prediction == 1:
            st.error(f"### ⚠️ Result: Parkinson's Disease **Detected**")
            st.metric("Confidence", f"{proba[1]*100:.1f}%")
        else:
            st.success(f"### ✅ Result: **Healthy** — No Parkinson's Detected")
            st.metric("Confidence", f"{proba[0]*100:.1f}%")

        with st.expander("See raw model output"):
            st.write(f"Predicted class: {prediction}")
            st.write(f"Probabilities — Healthy: {proba[0]:.4f} | Parkinson's: {proba[1]:.4f}")

# ══════════════════════════════════════════════════════════════════════════════
# CKD PAGE
# ══════════════════════════════════════════════════════════════════════════════
elif page == "🫘 Chronic Kidney Disease":
    st.title("🫘 Chronic Kidney Disease Prediction")
    st.markdown("Enter the patient's **lab test results** below.")
    st.markdown("---")

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

    numeric_features = {
        "age": 51.5, "bp": 76.5, "sg": 1.017, "al": 1.0, "su": 0.5,
        "bgr": 148.0, "bu": 57.4, "sc": 3.07, "sod": 137.5, "pot": 4.63,
        "hemo": 12.5, "pcv": 38.9, "wc": 8406.0, "rc": 4.71,
    }

    numeric_labels = {
        "age": "Age (years)", "bp": "Blood Pressure (mm/Hg)", "sg": "Specific Gravity",
        "al": "Albumin (0–5)", "su": "Sugar (0–5)", "bgr": "Blood Glucose Random (mg/dL)",
        "bu": "Blood Urea (mg/dL)", "sc": "Serum Creatinine (mg/dL)",
        "sod": "Sodium (mEq/L)", "pot": "Potassium (mEq/L)",
        "hemo": "Hemoglobin (g/dL)", "pcv": "Packed Cell Volume (%)",
        "wc": "White Blood Cell Count (cells/cumm)", "rc": "Red Blood Cell Count (millions/cmm)",
    }

    col1, col2 = st.columns(2)

    numeric_vals = {}
    num_keys = list(numeric_features.keys())
    for i, feat in enumerate(num_keys):
        col = col1 if i < 7 else col2
        with col:
            numeric_vals[feat] = st.number_input(
                numeric_labels[feat],
                value=numeric_features[feat],
                format="%.3f",
                key=f"c_{feat}"
            )

    st.markdown("##### Categorical Features")
    col3, col4 = st.columns(2)
    cat_vals = {}
    cat_keys = list(cat_map.keys())
    cat_labels = {
        "rbc": "Red Blood Cells", "pc": "Pus Cells",
        "pcc": "Pus Cell Clumps", "ba": "Bacteria",
        "htn": "Hypertension", "dm": "Diabetes Mellitus",
        "cad": "Coronary Artery Disease", "appet": "Appetite",
        "pe": "Pedal Edema", "ane": "Anemia",
    }
    for i, feat in enumerate(cat_keys):
        col = col3 if i < 5 else col4
        with col:
            options = list(cat_map[feat].keys())
            chosen = st.selectbox(cat_labels[feat], options, key=f"c_{feat}_cat")
            cat_vals[feat] = cat_map[feat][chosen]

    st.markdown("---")
    predict_btn = st.button("🔍 Run Prediction", type="primary")

    if predict_btn:
        # Build input in the correct feature order (must match training)
        feature_order = [
            "age","bp","sg","al","su","rbc","pc","pcc","ba",
            "bgr","bu","sc","sod","pot","hemo","pcv","wc","rc",
            "htn","dm","cad","appet","pe","ane"
        ]
        row = []
        for feat in feature_order:
            if feat in numeric_vals:
                row.append(numeric_vals[feat])
            else:
                row.append(cat_vals[feat])

        input_array = np.array(row).reshape(1, -1)
        prediction = ckd_model.predict(input_array)[0]
        proba = ckd_model.predict_proba(input_array)[0]

        st.markdown("---")
        # pred==0 → CKD detected, pred==1 → healthy
        if prediction == 0:
            st.error(f"### ⚠️ Result: Chronic Kidney Disease **Detected**")
            st.metric("Confidence", f"{proba[0]*100:.1f}%")
        else:
            st.success(f"### ✅ Result: **Healthy** — No CKD Detected")
            st.metric("Confidence", f"{proba[1]*100:.1f}%")

        with st.expander("See raw model output"):
            st.write(f"Predicted class: {prediction}")
            st.write(f"Probabilities — CKD: {proba[0]:.4f} | Healthy: {proba[1]:.4f}")
