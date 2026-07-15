import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_prediction_history

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📈 AI Predictive Maintenance Analytics")

# -----------------------
# Load Data
# -----------------------
df = get_prediction_history()

if df.empty:
    st.warning("No prediction data available.")
    st.stop()

# -----------------------
# Sensor Statistics
# -----------------------

st.header("📊 Sensor Statistics")

stats = df[[
    "AirTemperature",
    "ProcessTemperature",
    "RotationalSpeed",
    "Torque",
    "ToolWear",
    "Confidence"
]].describe()

st.dataframe(stats, use_container_width=True)

# -----------------------
# Correlation Matrix
# -----------------------

st.header("🔗 Correlation Matrix")

corr = df[[
    "AirTemperature",
    "ProcessTemperature",
    "RotationalSpeed",
    "Torque",
    "ToolWear",
    "Confidence"
]].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Torque Distribution
# -----------------------

st.header("⚙️ Torque Distribution")

fig = px.histogram(
    df,
    x="Torque",
    nbins=20
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Tool Wear Distribution
# -----------------------

st.header("🔧 Tool Wear Distribution")

fig = px.histogram(
    df,
    x="ToolWear",
    nbins=20
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Confidence Distribution
# -----------------------

st.header("🎯 Prediction Confidence")

fig = px.box(
    df,
    y="Confidence",
    points="all"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------
# Machine Type Analysis
# -----------------------

st.header("🏭 Machine Type Analysis")

machine_stats = df.groupby("MachineType").agg(
    Average_Torque=("Torque","mean"),
    Average_ToolWear=("ToolWear","mean"),
    Average_RPM=("RotationalSpeed","mean"),
    Average_Confidence=("Confidence","mean"),
    Total_Predictions=("MachineType","count")
)

st.dataframe(machine_stats, use_container_width=True)
