import streamlit as st

st.set_page_config(page_title="AI Predictive Maintenance", page_icon="🤖")

st.title("🤖 AI Predictive Maintenance System")

st.markdown("---")

st.header("Welcome")

st.write("""
This application predicts machine failures using Artificial Intelligence.

It is built using:

- 🐍 Python
- 🤖 XGBoost Machine Learning
- 📊 Streamlit
- 🗄 SQL Server
- 📈 Data Analytics
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model", "XGBoost")

with col2:
    st.metric("Accuracy", "99%")

with col3:
    st.metric("Status", "Active")

st.markdown("---")

st.subheader("Project Modules")

st.success("🏠 Home")
st.info("🤖 Prediction")
st.info("📊 Dashboard")
st.info("🗄 SQL Server")
st.info("📈 Prediction History")
st.info("ℹ About")
