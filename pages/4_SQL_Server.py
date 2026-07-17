import streamlit as st
import pandas as pd
from database import get_prediction_history
from styles import load_css

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(page_title="Database Monitor", page_icon="💾", layout="wide")

load_css()

st.markdown('<div class="hero-title">💾 Database Monitor</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Microsoft SQL Server Integration — live status and prediction history.</div>', unsafe_allow_html=True)

# ----------------------------------------------------
# Load Data
# ----------------------------------------------------

try:
    df = get_prediction_history()
    connected = True
except Exception as e:
    connected = False
    st.markdown('<span class="status-pill-failed">🔴 Connection Failed</span>', unsafe_allow_html=True)
    st.error(f"Database Connection Failed\n\n{e}")

# ----------------------------------------------------
# Database Status
# ----------------------------------------------------

if connected:

    st.markdown('<span class="status-pill-connected">🟢 SQL Server Connected</span>', unsafe_allow_html=True)

    st.write("")
    st.divider()

    total_predictions = len(df)
    healthy = len(df[df["Prediction"] == "Healthy"])
    failures = len(df[df["Prediction"] == "Failure"])
    latest_prediction = df.iloc[0]["PredictionTime"]

    # ----------------------------------------------------
    # KPI Cards
    # ----------------------------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <div style="font-size:1.6rem;">🔌</div>
            <div style="font-size:1.3rem; font-weight:700;">Connected</div>
            <div style="font-size:0.85rem; opacity:0.9;">Database</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <div style="font-size:1.6rem;">📋</div>
            <div style="font-size:1.4rem; font-weight:700;">{total_predictions}</div>
            <div style="font-size:0.85rem; opacity:0.9;">Total Records</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="metric-box-green">
            <div style="font-size:1.6rem;">🟢</div>
            <div style="font-size:1.4rem; font-weight:700;">{healthy}</div>
            <div style="font-size:0.85rem; opacity:0.9;">Healthy</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class="metric-box-red">
            <div style="font-size:1.6rem;">🔴</div>
            <div style="font-size:1.4rem; font-weight:700;">{failures}</div>
            <div style="font-size:0.85rem; opacity:0.9;">Failures</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # ----------------------------------------------------
    # Database Information
    # ----------------------------------------------------

    st.subheader("🗄️ Database Information")

    info1, info2 = st.columns(2)

    with info1:
        st.markdown("""
        <div class="info-card">
            <div class="info-card-label">Server</div>
            <div class="info-card-value">DESKTOP-JS0I57G\\SQLEXPRESS</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <div class="info-card-label">Database</div>
            <div class="info-card-value">PredictiveMaintenanceDB</div>
        </div>
        """, unsafe_allow_html=True)

    with info2:
        st.markdown("""
        <div class="info-card">
            <div class="info-card-label">Table</div>
            <div class="info-card-value">PredictionHistory</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="info-card">
            <div class="info-card-label">Latest Prediction</div>
            <div class="info-card-value">{latest_prediction}</div>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # ----------------------------------------------------
    # Latest Records
    # ----------------------------------------------------

    st.subheader("📄 Latest Prediction Records")

    st.dataframe(
        df.head(20).style.map(
            lambda v: "color: #56ab2f; font-weight: 600" if v == "Healthy"
            else ("color: #cb2d3e; font-weight: 600" if v == "Failure" else ""),
            subset=["Prediction"]
        ),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------
    # Actions
    # ----------------------------------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    action1, action2 = st.columns(2)

    with action1:
        st.download_button(
            label="📥 Download Database (CSV)",
            data=csv,
            file_name="PredictionHistory.csv",
            mime="text/csv",
            use_container_width=True
        )

    with action2:
        if st.button("🔄 Refresh Database", use_container_width=True):
            st.rerun()
