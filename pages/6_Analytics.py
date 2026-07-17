import streamlit as st
import pandas as pd
import plotly.express as px
from database import get_prediction_history
from styles import load_css

load_css()

st.markdown('<div class="hero-title">📈 AI Predictive Maintenance Analytics</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Deep-dive statistics, correlations, and distributions across all recorded predictions.</div>', unsafe_allow_html=True)

st.divider()

# -----------------------
# Load Data
# -----------------------
df = get_prediction_history()

if df.empty:
    st.warning("No prediction data available.")
    st.stop()

SENSOR_COLS = [
    "AirTemperature",
    "ProcessTemperature",
    "RotationalSpeed",
    "Torque",
    "ToolWear",
    "Confidence"
]

# -----------------------
# Top KPI Row
# -----------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">📋</div>
        <div style="font-size:1.4rem; font-weight:700;">{len(df)}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Total Records</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">⚙️</div>
        <div style="font-size:1.4rem; font-weight:700;">{df['Torque'].mean():.1f}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Avg Torque (Nm)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🔧</div>
        <div style="font-size:1.4rem; font-weight:700;">{df['ToolWear'].mean():.1f}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Avg Tool Wear (min)</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🎯</div>
        <div style="font-size:1.4rem; font-weight:700;">{df['Confidence'].mean():.1f}%</div>
        <div style="font-size:0.85rem; opacity:0.9;">Avg Confidence</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# -----------------------
# Sensor Statistics
# -----------------------

st.subheader("📊 Sensor Statistics")

stats = df[SENSOR_COLS].describe()

st.dataframe(stats, use_container_width=True)

st.divider()

# -----------------------
# Correlation Matrix
# -----------------------

st.subheader("🔗 Correlation Matrix")

corr = df[SENSOR_COLS].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)
fig.update_layout(margin=dict(t=10, b=10, l=10, r=10))

st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------
# Distributions
# -----------------------

st.subheader("📉 Distributions")

dcol1, dcol2 = st.columns(2)

with dcol1:
    st.markdown("**⚙️ Torque Distribution**")
    fig = px.histogram(df, x="Torque", nbins=20, color_discrete_sequence=["#667eea"])
    fig.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)

with dcol2:
    st.markdown("**🔧 Tool Wear Distribution**")
    fig = px.histogram(df, x="ToolWear", nbins=20, color_discrete_sequence=["#764ba2"])
    fig.update_layout(margin=dict(t=10, b=10, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)

st.write("")
st.markdown("**🎯 Prediction Confidence**")
fig = px.box(df, y="Confidence", points="all", color_discrete_sequence=["#56ab2f"])
fig.update_layout(margin=dict(t=10, b=10, l=10, r=10))
st.plotly_chart(fig, use_container_width=True)

st.divider()

# -----------------------
# Machine Type Analysis
# -----------------------

st.subheader("🏭 Machine Type Analysis")

machine_stats = df.groupby("MachineType").agg(
    Average_Torque=("Torque", "mean"),
    Average_ToolWear=("ToolWear", "mean"),
    Average_RPM=("RotationalSpeed", "mean"),
    Average_Confidence=("Confidence", "mean"),
    Total_Predictions=("MachineType", "count")
)

st.dataframe(machine_stats, use_container_width=True)
