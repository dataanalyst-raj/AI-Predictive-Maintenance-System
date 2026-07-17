import streamlit as st

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

# ==========================================
# Header
# ==========================================

st.title("🤖 AI Predictive Maintenance System")
st.caption("Industrial Equipment Health Monitoring using Artificial Intelligence")

st.divider()

# ==========================================
# Introduction
# ==========================================

st.markdown("""
### Welcome

This application predicts **machine failures** using an **XGBoost Machine Learning model** and provides engineering insights through **Explainable AI (SHAP)**.

The system is designed to help engineers monitor machine health, reduce downtime, and support predictive maintenance decisions.
""")

st.divider()

# ==========================================
# Technology Stack
# ==========================================

st.subheader("🛠 Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("🐍 Python")
    st.success("🤖 XGBoost")
    st.success("🧠 SHAP Explainable AI")

with col2:
    st.info("📊 Streamlit")
    st.info("🗄 SQL Server")
    st.info("📈 Plotly Analytics")

with col3:
    st.warning("📄 PDF Reports")
    st.warning("💾 Prediction History")
    st.warning("📉 Machine Analytics")

st.divider()

# ==========================================
# System Overview
# ==========================================

st.subheader("📌 System Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Machine Learning", "XGBoost")

with col2:
    st.metric("Database", "SQL Server")

with col3:
    st.metric("Explainability", "SHAP")

with col4:
    st.metric("System Status", "🟢 Online")

st.divider()

# ==========================================
# Features
# ==========================================

st.subheader("🚀 Features")

st.markdown("""
✅ Machine Failure Prediction

✅ Explainable AI (SHAP)

✅ SQL Server Integration

✅ Prediction History

✅ Analytics Dashboard

✅ PDF Report Generation

✅ Engineering Interpretation
""")

st.divider()

# ==========================================
# Navigation Guide
# ==========================================

st.subheader("📂 Application Modules")

module1, module2 = st.columns(2)

with module1:
    st.success("🏠 Home")
    st.success("🔮 Prediction")
    st.success("📊 Dashboard")

with module2:
    st.info("📈 Analytics")
    st.info("🗄 SQL History")
    st.info("ℹ About")

st.divider()

# ==========================================
# Footer
# ==========================================

st.markdown(
    """
    <div style="text-align:center;color:gray;">
        <hr>
        <h4>AI Predictive Maintenance System</h4>
        <p>Powered by Python • Streamlit • XGBoost • SQL Server • SHAP</p>
        <p>Version 1.0</p>
    </div>
    """,
    unsafe_allow_html=True
