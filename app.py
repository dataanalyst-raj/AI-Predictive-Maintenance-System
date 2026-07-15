import streamlit as st

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Predictive Maintenance System")

st.markdown("""
Welcome to the **AI Predictive Maintenance System**.

This application uses **Machine Learning (XGBoost)** to predict machine failures
based on sensor values.

---

## 📋 Application Modules

### 🏠 Home
Overview of the Predictive Maintenance System.

### 🤖 Prediction
Enter machine sensor values and predict whether the machine is Healthy or likely to Fail.

### 📊 Dashboard
View prediction history, charts and KPIs from SQL Server.

### 🗄 SQL Server
Monitor database connectivity and stored prediction records.

### 📈 Analytics
Explore statistical analysis, correlation matrix and machine analytics.

### ℹ About
Project details, technologies and developer information.

---

### 🚀 Technologies Used

- Python
- Streamlit
- XGBoost
- SQL Server
- Pandas
- Plotly
- PyODBC

---

Use the **navigation menu on the left** to explore the application.
""")
