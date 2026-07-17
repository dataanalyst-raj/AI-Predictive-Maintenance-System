import streamlit as st
from pdf_report import generate_pdf
import pandas as pd
import joblib
import shap
import os

from database import save_prediction

st.set_page_config(page_title="Prediction", page_icon="🔮", layout="wide")

# ---------------------------------
# Shared Custom CSS (same as Home)
# ---------------------------------
st.markdown("""
<style>
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
        color: #555;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #f8f9fb;
        border: 1px solid #e6e6e6;
        border-radius: 12px;
        padding: 1.2rem 1.4rem;
        height: 100%;
    }
    .result-card-healthy {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        border-radius: 14px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    .result-card-failure {
        background: linear-gradient(135deg, #cb2d3e 0%, #ef473a 100%);
        border-radius: 14px;
        padding: 1.5rem;
        color: white;
        text-align: center;
    }
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------
# Load Model
# ---------------------------------

model = joblib.load("xgboost_predictive_maintenance.pkl")
explainer = shap.TreeExplainer(model)

# ---------------------------------
# Page Header
# ---------------------------------

st.markdown('<div class="hero-title">🔮 Machine Failure Prediction</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Enter live machine parameters to get an instant AI-powered health prediction.</div>', unsafe_allow_html=True)

# ---------------------------------
# User Inputs (in a card, laid out in columns)
# ---------------------------------

st.markdown("### ⚙️ Machine Parameters")

with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        machine_type = st.selectbox("Machine Type", ["L", "M", "H"])
        air_temp = st.number_input("Air Temperature (K)", value=300.0)
        process_temp = st.number_input("Process Temperature (K)", value=310.0)

    with col2:
        rot_speed = st.number_input("Rotational Speed (rpm)", value=1500)
        torque = st.number_input("Torque (Nm)", value=40.0)
        tool_wear = st.number_input("Tool Wear (min)", value=10)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------
# Feature Engineering
# ---------------------------------

temp_difference = process_temp - air_temp

st.info(f"🌡️ Temperature Difference = {temp_difference:.2f} K")

# ---------------------------------
# One Hot Encoding
# ---------------------------------

Type_L = 1 if machine_type == "L" else 0
Type_M = 1 if machine_type == "M" else 0

# ---------------------------------
# Prediction
# ---------------------------------

st.write("")
predict_clicked = st.button("🚀 Predict Machine Failure", use_container_width=True)

if predict_clicked:

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
    importance = importance.sort_values(by="Impact", ascending=False)

    top_features = importance["Feature"].head(5).tolist()

    # ---------------------------------
    # Prediction Result (big styled card)
    # ---------------------------------

    st.markdown("---")

    if prediction == 0:
        prediction_text = "Healthy"
        result_col1, result_col2 = st.columns([2, 1])
        with result_col1:
            st.markdown(f"""
            <div class="result-card-healthy">
                <div style="font-size:2rem;">✅</div>
                <div style="font-size:1.4rem; font-weight:700;">Machine is Healthy</div>
                <div style="opacity:0.9;">No immediate action required</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        prediction_text = "Failure"
        result_col1, result_col2 = st.columns([2, 1])
        with result_col1:
            st.markdown(f"""
            <div class="result-card-failure">
                <div style="font-size:2rem;">⚠️</div>
                <div style="font-size:1.4rem; font-weight:700;">Machine Failure Predicted</div>
                <div style="opacity:0.9;">Immediate inspection recommended</div>
            </div>
            """, unsafe_allow_html=True)

    with result_col2:
        st.markdown(f"""
        <div class="metric-box">
            <div style="font-size:1.6rem;">🎯</div>
            <div style="font-size:1.4rem; font-weight:700;">{confidence:.2f}%</div>
            <div style="font-size:0.85rem; opacity:0.9;">Prediction Confidence</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------------------------
    # SHAP Explanation
    # ---------------------------------

    st.markdown("---")
    st.subheader("🧠 AI Model Explanation (SHAP)")

    st.dataframe(
        importance[["Feature", "Contribution"]],
        use_container_width=True
    )

    st.bar_chart(
        importance.set_index("Feature")["Contribution"]
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

    r1, r2 = st.columns(2)
    for i, reason in enumerate(reasons):
        target = r1 if i % 2 == 0 else r2
        target.markdown(f"- {reason}")

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

   saved = save_prediction(
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

if saved:
    st.success("✅ Prediction saved to SQL Server successfully!")

else:
    st.info(
        "ℹ Database is unavailable. Prediction was generated successfully, "
        "but it was not stored."
    )
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
