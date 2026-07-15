import streamlit as st
import pandas as pd
import joblib
from database import save_prediction

# -----------------------
# Load Model
# -----------------------

model = joblib.load("xgboost_predictive_maintenance.pkl")

# -----------------------
# Page Title
# -----------------------

st.title("🤖 Machine Failure Prediction")

st.write("Enter the machine parameters below.")

# -----------------------
# User Inputs
# -----------------------

machine_type = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)

rot_speed = st.number_input(
    "Rotational Speed (rpm)",
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    value=10
)

# -----------------------
# Feature Engineering
# -----------------------

temp_difference = process_temp - air_temp

st.info(f"Temperature Difference = {temp_difference:.2f} K")

# -----------------------
# One-Hot Encoding
# -----------------------

Type_L = 1 if machine_type == "L" else 0
Type_M = 1 if machine_type == "M" else 0

# -----------------------
# Prediction Button
# -----------------------

if st.button("Predict Machine Failure"):

    input_data = pd.DataFrame([[
        air_temp,
        process_temp,
        rot_speed,
        torque,
        tool_wear,
        temp_difference,
        Type_L,
        Type_M
    ]], columns=[
        "Air_temperature_K",
        "Process_temperature_K",
        "Rotational_speed_rpm",
        "Torque_Nm",
        "Tool_wear_min",
        "Temperature_Difference",
        "Type_L",
        "Type_M"
    ])

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = float(max(probability) * 100)

    st.markdown("---")

    # -----------------------
    # Prediction Result
    # -----------------------

    if prediction == 0:

        prediction_text = "Healthy"

        st.success("✅ Machine is Healthy")

    else:

        prediction_text = "Failure"

        st.error("⚠️ Machine Failure Predicted")

    st.metric(
        "Prediction Confidence",
        f"{confidence:.2f}%"
    )

    # -----------------------
    # Explainable AI
    # -----------------------

    reasons = []

    # Tool Wear
    if tool_wear > 150:
        reasons.append("🔴 Tool Wear is extremely high")

    elif tool_wear > 100:
        reasons.append("🟠 Tool Wear is high")

    else:
        reasons.append("🟢 Tool Wear is normal")

    # Torque
    if torque > 60:
        reasons.append("🔴 Torque is very high")

    elif torque > 45:
        reasons.append("🟠 Torque is above normal")

    else:
        reasons.append("🟢 Torque is normal")

    # Temperature Difference
    if temp_difference > 15:
        reasons.append("🔴 Temperature Difference is very high")

    elif temp_difference > 10:
        reasons.append("🟠 Temperature Difference is elevated")

    else:
        reasons.append("🟢 Temperature Difference is normal")

    # Rotational Speed
    if rot_speed < 1200:
        reasons.append("🟠 Rotational Speed is low")

    elif rot_speed > 1800:
        reasons.append("🟠 Rotational Speed is high")

    else:
        reasons.append("🟢 Rotational Speed is normal")

    # -----------------------
    # AI Explanation
    # -----------------------

    st.markdown("---")

    st.subheader("🧠 AI Decision Explanation")

    for reason in reasons:
        st.write(reason)

    # -----------------------
    # Risk Level
    # -----------------------

    st.markdown("---")

    if prediction == 0:

        st.success("🟢 Overall Risk Level : LOW")

    else:

        st.error("🔴 Overall Risk Level : HIGH")

    # -----------------------
    # Save to SQL Server
    # -----------------------

    save_prediction(
        machine_type,
        air_temp,
        process_temp,
        rot_speed,
        torque,
        tool_wear,
        temp_difference,
        prediction_text,
        confidence
    )

    st.success("✅ Prediction saved to SQL Server successfully!")
