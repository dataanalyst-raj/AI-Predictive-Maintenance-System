import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_prediction_history
from styles import load_css

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

load_css()

st.markdown(
    '<div class="hero-title">📈 AI Predictive Maintenance Analytics</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">'
    'Deep-dive statistics, correlations and machine performance analytics.'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# ==========================================================
# LOAD DATABASE
# ==========================================================

df = get_prediction_history()

# ==========================================================
# DATABASE CHECK
# ==========================================================

if df.empty:

    st.warning("""
### ⚠ Database Connection Unavailable

The Analytics dashboard requires prediction history stored
inside Microsoft SQL Server.

This is expected when using the public demo.

The following modules are still fully functional:

✅ Machine Failure Prediction

✅ Explainable AI (SHAP)

✅ PDF Report Generation
""")

    st.info("""
To enable Analytics:

• Start SQL Server

• Connect PredictiveMaintenanceDB

• Refresh this page
""")

    st.stop()

# ==========================================================
# SENSOR COLUMNS
# ==========================================================

SENSOR_COLS = [
    "AirTemperature",
    "ProcessTemperature",
    "RotationalSpeed",
    "Torque",
    "ToolWear",
    "Confidence"
]

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">📋</div>
        <div style="font-size:1.4rem;font-weight:700;">
        {len(df)}
        </div>
        <div style="font-size:0.9rem;">
        Total Records
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">⚙</div>
        <div style="font-size:1.4rem;font-weight:700;">
        {df["Torque"].mean():.2f}
        </div>
        <div style="font-size:0.9rem;">
        Avg Torque
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🔧</div>
        <div style="font-size:1.4rem;font-weight:700;">
        {df["ToolWear"].mean():.2f}
        </div>
        <div style="font-size:0.9rem;">
        Avg Tool Wear
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🎯</div>
        <div style="font-size:1.4rem;font-weight:700;">
        {df["Confidence"].mean():.2f}%
        </div>
        <div style="font-size:0.9rem;">
        Avg Confidence
        </div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

st.subheader("📊 Sensor Statistics")

stats = df[SENSOR_COLS].describe()

st.dataframe(
    stats,
    use_container_width=True
)

st.divider()

# ==========================================================
# CORRELATION MATRIX
# ==========================================================

st.subheader("🔗 Correlation Matrix")

corr = df[SENSOR_COLS].corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="RdBu_r"
)

fig.update_layout(
    margin=dict(
        l=10,
        r=10,
        t=10,
        b=10
    )
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# DISTRIBUTIONS
# ==========================================================

st.subheader("📉 Sensor Distributions")

left, right = st.columns(2)

with left:

    fig = px.histogram(
        df,
        x="Torque",
        nbins=20,
        title="Torque Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    fig = px.histogram(
        df,
        x="ToolWear",
        nbins=20,
        title="Tool Wear Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

fig = px.box(
    df,
    y="Confidence",
    points="all",
    title="Prediction Confidence"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.divider()

# ==========================================================
# MACHINE TYPE ANALYSIS
# ==========================================================

st.subheader("🏭 Machine Type Analysis")

machine_stats = df.groupby("MachineType").agg(

    Average_Torque=("Torque", "mean"),

    Average_ToolWear=("ToolWear", "mean"),

    Average_RPM=("RotationalSpeed", "mean"),

    Average_Confidence=("Confidence", "mean"),

    Total_Predictions=("MachineType", "count")

)

st.dataframe(
    machine_stats,
    use_container_width=True
)

st.divider()

# ==========================================================
# DOWNLOAD ANALYTICS
# ==========================================================

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Analytics Data (CSV)",
    data=csv,
    file_name="analytics_data.csv",
    mime="text/csv"
)
