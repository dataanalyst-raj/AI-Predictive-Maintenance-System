import streamlit as st
from pdf_report import generate_pdf
import pandas as pd
import joblib
import shap
import os

from database import save_prediction

# ---------------------------------
# Load Model
# ---------------------------------

model = joblib.load("xgboost_predictive_maintenance.pkl")
explainer = shap.TreeExplainer(model)

# ---------------------------------
# Page Title
# ---------------------------------

st.title("🤖 Machine Failure Prediction")
st.write("Enter the machine parameters below.")

# ---------------------------------
# User Inputs
# ---------------------------------

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

# ---------------------------------
# Feature Engineering
# ---------------------------------

temp_difference = process_temp - air_temp

st.info(f"Temperature Difference = {temp_difference:.2f} K")

# ---------------------------------
# One Hot Encoding
# ---------------------------------

Type_L = 1 if machine_type == "L" else 0
Type_M = 1 if machine_type == "M" else 0

# ---------------------------------
# Prediction
# ---------------------------------

if st.button("Predict Machine Failure"):

    input_data = pd.DataFrame(
        [[
            air_temp,
            process_temp,
            rot_speed,
            torque,
            tool_wear,
            temp_difference,
            Type_L,
            Type_M
        ]],
        columns=[
            "Air_temperature_K",
            "Process_temperature_K",
            "Rotational_speed_rpm",
            "Torque_Nm",
            "Tool_wear_min",
            "Temperature_Difference",
            "Type_L",
            "Type_M"
        ]
    )

    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    confidence = float(max(probability) * 100)

    # ---------------------------------
    # SHAP Explainability
    # ---------------------------------

    shap_values = explainer.shap_values(input_data)

    importance = pd.DataFrame({
        "Feature": input_data.columns,
        "Contribution": shap_values[0]
    })

    importance["Impact"] = importance["Contribution"].abs()

    importance = importance.sort_values(
        by="Impact",
        ascending=False
    )
    # Top 5 SHAP Features

    top_features = importance["Feature"].head(5).tolist()

    # ---------------------------------
    # Prediction Result
    # ---------------------------------

    st.markdown("---")

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

    # ---------------------------------
    # SHAP Explanation
    # ---------------------------------

    st.markdown("---")

    st.subheader("🧠 AI Model Explanation (SHAP)")

    st.dataframe(
        importance[["Feature", "Contribution"]],
        use_container_width=True
    )

    # ---------------------------------
    # Engineering Explanation
    # ---------------------------------

    reasons = []

    if tool_wear > 150:
        reasons.append("🔴 Tool Wear is extremely high")
    elif tool_wear > 100:
        reasons.append("🟠 Tool Wear is high")
    else:
        reasons.append("🟢 Tool Wear is normal")

    if torque > 60:
        reasons.append("🔴 Torque is very high")
    elif torque > 45:
        reasons.append("🟠 Torque is above normal")
    else:
        reasons.append("🟢 Torque is normal")

    if temp_difference > 15:
        reasons.append("🔴 Temperature Difference is very high")
    elif temp_difference > 10:
        reasons.append("🟠 Temperature Difference is elevated")
    else:
        reasons.append("🟢 Temperature Difference is normal")

    if rot_speed < 1200:
        reasons.append("🟠 Rotational Speed is low")
    elif rot_speed > 1800:
        reasons.append("🟠 Rotational Speed is high")
    else:
        reasons.append("🟢 Rotational Speed is normal")

    st.markdown("---")

    st.subheader("🛠 Engineering Interpretation")

    for reason in reasons:
        st.write(reason)

    # ---------------------------------
    # Risk Level
    # ---------------------------------

    st.markdown("---")

    if prediction == 0:
        st.success("🟢 Overall Risk Level : LOW")
    else:
        st.error("🔴 Overall Risk Level : HIGH")

    # ---------------------------------
    # Save Prediction
    # ---------------------------------

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
    # ---------------------------------
    # ---------------------------------
    # Generate PDF
    # ---------------------------------

    pdf_file = generate_pdf(
        machine_type,
        air_temp,
        process_temp,
        rot_speed,
        torque,
        tool_wear,
        temp_difference,
        prediction_text,
        confidence,
        top_features
    )

    # ---------------------------------
    # Download PDF Button
    # ---------------------------------

    if os.path.exists(pdf_file):

        with open(pdf_file, "rb") as pdf:

            st.download_button(
                label="📄 Download Prediction Report",
                data=pdf,
                file_name="Prediction_Report.pdf",
                mime="application/pdf"
            )
