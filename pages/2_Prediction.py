import streamlit as st
import pandas as pd
import joblib

# -------------------------
# Load Model
# -------------------------
model = joblib.load("xgboost_predictive_maintenance.pkl")

st.title("🤖 Machine Failure Prediction")
st.markdown("---")

# Two-column layout
col1, col2 = st.columns(2)

with col1:

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

with col2:

    rot_speed = st.number_input(
        "Rotational Speed (RPM)",
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

st.markdown("---")

if st.button("🔍 Predict"):

    temp_difference = process_temp - air_temp

    type_l = 1 if machine_type == "L" else 0
    type_m = 1 if machine_type == "M" else 0

    input_df = pd.DataFrame([{
        "Air_temperature_K": air_temp,
        "Process_temperature_K": process_temp,
        "Rotational_speed_rpm": rot_speed,
        "Torque_Nm": torque,
        "Tool_wear_min": tool_wear,
        "Temperature_Difference": temp_difference,
        "Type_L": type_l,
        "Type_M": type_m
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]
    failure = "Failure" if prediction == 1 else "Healthy"

cursor.execute("""
INSERT INTO PredictionHistory
(
MachineType,
AirTemperature,
ProcessTemperature,
RotationalSpeed,
Torque,
ToolWear,
FailurePrediction,
FailureProbability
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""",
machine_type,
air_temp,
process_temp,
rot_speed,
torque,
tool_wear,
failure,
float(probability)
)

conn.commit()

    st.markdown("## Prediction Result")

    if prediction == 1:
        st.error("⚠️ Machine Failure Predicted")
    else:
        st.success("✅ Machine is Healthy")

    st.progress(float(probability))

    st.metric(
        "Failure Probability",
        f"{probability*100:.2f}%"
    )

    st.subheader("Input Summary")

    st.dataframe(input_df, use_container_width=True)
