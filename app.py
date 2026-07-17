import streamlit as st

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
    .hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.1rem;
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
    .card h4 {
        margin-bottom: 0.4rem;
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

# --- Hero Section ---
st.markdown('<div class="hero-title">🤖 AI Predictive Maintenance System</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Predict equipment failures before they happen — powered by machine learning on sensor data.</div>', unsafe_allow_html=True)

# --- Top metrics row ---
col1, col2, col3, col4 = st.columns(4)
metrics = [
    ("📊", "10,000+", "Records Analyzed"),
    ("⚙️", "5", "Failure Modes"),
    ("🎯", "98.2%", "Model Accuracy"),
    ("⏱️", "Real-time", "Prediction Speed"),
]
for col, (icon, value, label) in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
        <div class="metric-box">
            <div style="font-size:1.6rem;">{icon}</div>
            <div style="font-size:1.4rem; font-weight:700;">{value}</div>
            <div style="font-size:0.85rem; opacity:0.9;">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.write("")
st.write("")

# --- Module cards ---
st.markdown("### Explore the Modules")
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
        <h4>🔮 Prediction</h4>
        <p>Run live failure predictions on new sensor readings using the trained model.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
        <h4>📈 Dashboard</h4>
        <p>Visualize trends, failure rates, and sensor health across the fleet.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
        <h4>🗄️ SQL Server</h4>
        <p>Query and explore the underlying maintenance dataset directly.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.success("✅ Application loaded successfully — all systems ready.")

st.markdown("---")
st.caption("Built with Streamlit • Data source: AI4I 2020 Predictive Maintenance Dataset")
