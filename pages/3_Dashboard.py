import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 AI Predictive Maintenance Dashboard")

st.markdown("---")

# ==========================
# KPI Cards
# ==========================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Total Predictions",
        value="1250"
    )

with col2:
    st.metric(
        label="Healthy Machines",
        value="1180"
    )

with col3:
    st.metric(
        label="Failures",
        value="70"
    )

st.markdown("---")

# ==========================
# Sample Data
# ==========================

data = pd.DataFrame({
    "Machine Type": ["L", "M", "H"],
    "Failures": [20, 25, 25]
})

fig = px.bar(
    data,
    x="Machine Type",
    y="Failures",
    title="Machine Failures by Machine Type"
)

st.plotly_chart(fig, use_container_width=True)
