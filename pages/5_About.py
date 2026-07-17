import streamlit as st
from styles import load_css

load_css()

st.markdown('<div class="hero-title">ℹ️ About</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">AI Predictive Maintenance Platform — industrial failure prediction powered by Machine Learning and Explainable AI.</div>', unsafe_allow_html=True)

st.divider()

# ----------------------------------------------------
# Overview
# ----------------------------------------------------

st.markdown("""
<div class="card">
The AI Predictive Maintenance Platform is an industrial machine failure prediction
system developed using Machine Learning and Explainable AI.
<br><br>
The application predicts machine failures based on operating conditions,
stores prediction history inside Microsoft SQL Server, and generates
professional PDF reports for maintenance engineers.
</div>
""", unsafe_allow_html=True)

st.write("")
st.divider()

# ----------------------------------------------------
# Developer & Technologies
# ----------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("👨‍💻 Developer")
    st.markdown("""
    <div class="info-card">
        <div class="info-card-label">Name</div>
        <div class="info-card-value">Raj Patil</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Background</div>
        <div class="info-card-value">MSc Advanced Chemical &amp; Process Engineering, University of Strathclyde</div>
    </div>
    <div class="info-card">
        <div class="info-card-label">Focus</div>
        <div class="info-card-value">Machine Learning Enthusiast &amp; Python Developer</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("⚙️ Technologies")
    tech_stack = [
        "Python", "Streamlit", "XGBoost", "SHAP Explainable AI",
        "SQL Server", "Pandas", "Scikit-Learn", "Plotly", "ReportLab"
    ]
    st.markdown('<div class="card">', unsafe_allow_html=True)
    tcol1, tcol2 = st.columns(2)
    for i, tech in enumerate(tech_stack):
        target = tcol1 if i % 2 == 0 else tcol2
        target.markdown(f"✅ {tech}")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.divider()

# ----------------------------------------------------
# Key Features
# ----------------------------------------------------

st.subheader("🚀 Key Features")

features = [
    "Machine Failure Prediction",
    "Explainable AI (SHAP)",
    "SQL Server Integration",
    "Prediction History",
    "Analytics Dashboard",
    "PDF Report Generation",
    "Interactive Dashboard",
    "Industrial User Interface",
]

fcol1, fcol2 = st.columns(2)
for i, feature in enumerate(features):
    target = fcol1 if i % 2 == 0 else fcol2
    target.markdown(f"""
    <div class="info-card">
        <div class="info-card-value">✔ {feature}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# ----------------------------------------------------
# Machine Learning Model
# ----------------------------------------------------

st.subheader("🧠 Machine Learning Model")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🧠</div>
        <div style="font-size:1.3rem; font-weight:700;">XGBoost</div>
        <div style="font-size:0.85rem; opacity:0.9;">Algorithm</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🗄️</div>
        <div style="font-size:1.3rem; font-weight:700;">SQL Server</div>
        <div style="font-size:0.85rem; opacity:0.9;">Database</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🚀</div>
        <div style="font-size:1.3rem; font-weight:700;">Streamlit</div>
        <div style="font-size:0.85rem; opacity:0.9;">Application</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

st.caption("Version 2.0 | AI Predictive Maintenance Platform")
