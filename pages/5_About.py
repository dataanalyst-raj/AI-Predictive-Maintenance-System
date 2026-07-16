import streamlit as st
from styles import load_css

load_css()

st.title("ℹ️ About")

st.markdown("---")

st.header("AI Predictive Maintenance Platform")

st.write("""
The AI Predictive Maintenance Platform is an industrial machine failure prediction
system developed using Machine Learning and Explainable AI.

The application predicts machine failures based on operating conditions,
stores prediction history inside Microsoft SQL Server and generates
professional PDF reports for maintenance engineers.
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    st.subheader("👨‍💻 Developer")

    st.write("""
**Raj Patil**

Petrochemical Engineer

Machine Learning Enthusiast

Python Developer
""")

with col2:

    st.subheader("⚙ Technologies")

    st.write("""
✅ Python

✅ Streamlit

✅ XGBoost

✅ SHAP Explainable AI

✅ SQL Server

✅ Pandas

✅ Scikit-Learn

✅ Plotly

✅ ReportLab
""")

st.markdown("---")

st.subheader("🚀 Key Features")

st.write("""

✔ Machine Failure Prediction

✔ Explainable AI (SHAP)

✔ SQL Server Integration

✔ Prediction History

✔ Analytics Dashboard

✔ PDF Report Generation

✔ Interactive Dashboard

✔ Industrial User Interface

""")

st.markdown("---")

st.subheader("🧠 Machine Learning Model")

col1, col2, col3 = st.columns(3)

col1.metric("Algorithm", "XGBoost")

col2.metric("Database", "SQL Server")

col3.metric("Application", "Streamlit")

st.markdown("---")

st.caption("Version 2.0 | AI Predictive Maintenance Platform")
