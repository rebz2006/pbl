# Disease Prediction System

A machine learning web application that predicts two diseases — Parkinson's Disease and Chronic Kidney Disease — from clinical and vocal measurements. Both models use a Random Forest Classifier trained on publicly available UCI datasets.

**Live App:** https://ttaphjijvhtx4jzzgeutyy.streamlit.app/

---

## Overview

| Module | Disease | Input | Model Accuracy |
|--------|---------|-------|----------------|
| Parkinson's Disease | Neurological disorder detected via vocal measurements | 22 acoustic voice features | 92.31% |
| Chronic Kidney Disease | Kidney function disorder detected via lab results | 24 clinical features | 98.75% |

Both models are trained using a Random Forest Classifier with 200 decision trees. The app is built with Streamlit and deployed on Streamlit Cloud.

---

## Repository Structure

```
pbl/
├── app_final.py                  # Main Streamlit application
├── model.pkl                     # Trained Parkinson's Disease model
├── rf_model_ckd.pkl              # Trained Chronic Kidney Disease model
├── parkinsons.csv                # UCI Parkinson's dataset
├── sample_test_cases.py          # Sample healthy and detected cases for demo
├── requirements.txt              # Python dependencies
└── .streamlit/
    └── config.toml               # Light theme configuration
```

---

## How to Use the App

1. Open the live app at https://ttaphjijvhtx4jzzgeutyy.streamlit.app/
2. Select a disease module from the dropdown at the top of the page
3. Enter the required measurement values
4. Click **Run Prediction**
5. The app will display whether the disease is detected along with a confidence percentage

To test the app quickly without real patient data, refer to the values in `sample_test_cases.py`. It contains one healthy and one disease-detected case for each module.

---

## Models

### Parkinson's Disease
- **Dataset:** UCI Parkinson's Disease dataset (195 samples, 22 vocal features)
- **Algorithm:** Random Forest Classifier
- **Test Accuracy:** 92.31%
- **Features:** Acoustic measurements including jitter, shimmer, HNR, NHR, RPDE, DFA, PPE and others extracted from sustained vowel phonation recordings

### Chronic Kidney Disease
- **Dataset:** UCI CKD dataset (400 samples, 24 clinical features)
- **Algorithm:** Random Forest Classifier
- **Test Accuracy:** 98.75%
- **Features:** Blood and urine test results including serum creatinine, hemoglobin, albumin, blood urea, specific gravity, and categorical indicators such as hypertension and diabetes

### Random Forest Parameters (same for both models)
```python
RandomForestClassifier(
    n_estimators=200,
    max_depth=None,
    min_samples_split=5,
    min_samples_leaf=2,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1,
)
```

---

## Running Locally

### Prerequisites
- Python 3.8 or higher
- pip

### Steps

**1. Clone the repository**
```bash
git clone https://github.com/rebz2006/pbl.git
cd pbl
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app_final.py
```

The app will open in your browser at `http://localhost:8501`.

---

## Pushing Updates to GitHub

Use the following commands whenever you make changes and want to update the live app.

### First time setup in a new session (e.g. Google Colab)

```bash
git config --global user.email "your_email@example.com"
git config --global user.name "rebz2006"

cd /content/pbl
git remote set-url origin https://rebz2006:YOUR_GITHUB_TOKEN@github.com/rebz2006/pbl.git
```

Replace `YOUR_GITHUB_TOKEN` with your GitHub Personal Access Token. To generate one: GitHub Settings → Developer Settings → Personal Access Tokens → Generate new token (select `repo` scope).

### Pushing a single updated file

```bash
cd /content/pbl
git pull origin main
git add app_final.py
git commit -m "Your commit message here"
git push origin main
```

### Pushing all changed files at once

```bash
cd /content/pbl
git pull origin main
git add .
git commit -m "Your commit message here"
git push origin main
```

### Renaming a file

```bash
git mv old_filename.py new_filename.py
git commit -m "Rename old_filename to new_filename"
git push origin main
```

### Deleting a file

```bash
git rm filename.py
git commit -m "Remove filename"
git push origin main
```

Once changes are pushed to the `main` branch, Streamlit Cloud will automatically redeploy the live app within a minute or two.

---

## Redeploying on Streamlit Cloud

If you need to delete and redeploy the app from scratch:

1. Go to https://share.streamlit.io
2. Find the existing app, click the three-dot menu, and select Delete
3. Click New App
4. Set Repository to `rebz2006/pbl`, Branch to `main`, Main file path to `app_final.py`
5. Click Deploy

---

## Dependencies

```
streamlit
scikit-learn
pandas
numpy
joblib
```

---

## Disclaimer

This application is built for educational and research purposes only. It is not intended to be used as a substitute for professional medical diagnosis or clinical decision-making.

---

## Author

GitHub: [rebz2006](https://github.com/rebz2006)
