# ============================================================
# SAMPLE TEST CASES — Disease Prediction App
# ============================================================
# Use these values in the app to demonstrate predictions.
# Enter them manually into the input fields during your demo.
# ============================================================


# ── PARKINSON'S DISEASE ──────────────────────────────────────────────────────

# Case 1: HEALTHY patient
# Low jitter, low shimmer, high HNR, low NHR, very negative spread1, low PPE
# Expected result: Healthy

PARKINSONS_HEALTHY = {
    "MDVP:Fo(Hz)"      : 197.08,
    "MDVP:Fhi(Hz)"     : 206.90,
    "MDVP:Flo(Hz)"     : 192.06,
    "MDVP:Jitter(%)"   : 0.00289,
    "MDVP:Jitter(Abs)" : 0.00001,
    "MDVP:RAP"         : 0.00166,
    "MDVP:PPQ"         : 0.00168,
    "Jitter:DDP"       : 0.00498,
    "MDVP:Shimmer"     : 0.01098,
    "MDVP:Shimmer(dB)" : 0.09700,
    "Shimmer:APQ3"     : 0.00563,
    "Shimmer:APQ5"     : 0.00680,
    "MDVP:APQ"         : 0.00802,
    "Shimmer:DDA"      : 0.01689,
    "NHR"              : 0.00339,
    "HNR"              : 26.775,
    "RPDE"             : 0.42210,
    "DFA"              : 0.74148,
    "spread1"          : -7.3121,
    "spread2"          : 0.17186,
    "D2"               : 1.74377,
    "PPE"              : 0.08566,
}

# Case 2: PARKINSON'S DETECTED
# High jitter, high shimmer, lower HNR, higher NHR, less negative spread1, high PPE
# Expected result: Parkinson's Disease Detected

PARKINSONS_DETECTED = {
    "MDVP:Fo(Hz)"      : 116.68,
    "MDVP:Fhi(Hz)"     : 137.87,
    "MDVP:Flo(Hz)"     : 111.37,
    "MDVP:Jitter(%)"   : 0.01050,
    "MDVP:Jitter(Abs)" : 0.00007,
    "MDVP:RAP"         : 0.00530,
    "MDVP:PPQ"         : 0.00610,
    "Jitter:DDP"       : 0.01590,
    "MDVP:Shimmer"     : 0.05749,
    "MDVP:Shimmer(dB)" : 0.47700,
    "Shimmer:APQ3"     : 0.02650,
    "Shimmer:APQ5"     : 0.03530,
    "MDVP:APQ"         : 0.05320,
    "Shimmer:DDA"      : 0.07960,
    "NHR"              : 0.02609,
    "HNR"              : 19.085,
    "RPDE"             : 0.55820,
    "DFA"              : 0.68540,
    "spread1"          : -4.8270,
    "spread2"          : 0.31400,
    "D2"               : 2.65150,
    "PPE"              : 0.28490,
}


# ── CHRONIC KIDNEY DISEASE ───────────────────────────────────────────────────

# Case 3: HEALTHY patient
# Normal creatinine, normal hemoglobin, no albumin/sugar in urine,
# no hypertension, no diabetes, good appetite
# Expected result: Healthy

CKD_HEALTHY = {
    # Numeric features
    "age"  : 48,
    "bp"   : 70,
    "sg"   : 1.025,
    "al"   : 0,
    "su"   : 0,
    "bgr"  : 117,
    "bu"   : 25,
    "sc"   : 0.9,
    "sod"  : 142,
    "pot"  : 4.5,
    "hemo" : 15.4,
    "pcv"  : 44,
    "wc"   : 7600,
    "rc"   : 5.2,
    # Categorical features
    "rbc"  : "normal",
    "pc"   : "normal",
    "pcc"  : "notpresent",
    "ba"   : "notpresent",
    "htn"  : "no",
    "dm"   : "no",
    "cad"  : "no",
    "appet": "good",
    "pe"   : "no",
    "ane"  : "no",
}

# Case 4: CKD DETECTED
# Very high creatinine (5.2), low hemoglobin (9.2), high albumin (3),
# sugar in urine (2), hypertension, diabetes, poor appetite, anemia, edema
# Expected result: Chronic Kidney Disease Detected

CKD_DETECTED = {
    # Numeric features
    "age"  : 62,
    "bp"   : 90,
    "sg"   : 1.010,
    "al"   : 3,
    "su"   : 2,
    "bgr"  : 195,
    "bu"   : 72,
    "sc"   : 5.2,
    "sod"  : 128,
    "pot"  : 6.1,
    "hemo" : 9.2,
    "pcv"  : 28,
    "wc"   : 11400,
    "rc"   : 3.1,
    # Categorical features
    "rbc"  : "abnormal",
    "pc"   : "abnormal",
    "pcc"  : "present",
    "ba"   : "present",
    "htn"  : "yes",
    "dm"   : "yes",
    "cad"  : "no",
    "appet": "poor",
    "pe"   : "yes",
    "ane"  : "yes",
}


# ── PRINT ALL CASES ──────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 60)
    print("CASE 1: Parkinson's — Healthy")
    print("=" * 60)
    for k, v in PARKINSONS_HEALTHY.items():
        print(f"  {k:<25} {v}")

    print()
    print("=" * 60)
    print("CASE 2: Parkinson's — Detected")
    print("=" * 60)
    for k, v in PARKINSONS_DETECTED.items():
        print(f"  {k:<25} {v}")

    print()
    print("=" * 60)
    print("CASE 3: CKD — Healthy")
    print("=" * 60)
    for k, v in CKD_HEALTHY.items():
        print(f"  {k:<25} {v}")

    print()
    print("=" * 60)
    print("CASE 4: CKD — Detected")
    print("=" * 60)
    for k, v in CKD_DETECTED.items():
        print(f"  {k:<25} {v}")
