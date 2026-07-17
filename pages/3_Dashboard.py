import streamlit as st
import plotly.express as px
from database import get_prediction_history

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Predictive Maintenance Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------
# Shared Custom CSS (same as Home / Prediction)
# ----------------------------
st.markdown("""
<style>
    .hero-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1a1a2e;
        margin-bottom: 0.2rem;
    }
    .hero-subtitle {
        font-size: 1.05rem;
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
    .metric-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }
    .metric-box-green {
        background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }
    .metric-box-red {
        background: linear-gradient(135deg, #cb2d3e 0%, #ef473a 100%);
        border-radius: 12px;
        padding: 1rem;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Consistent color mapping used across every chart on this page
STATUS_COLORS = {"Healthy": "#56ab2f", "Failure": "#cb2d3e"}

# ----------------------------
# Header
# ----------------------------
st.markdown('<div class="hero-title">📊 AI Predictive Maintenance Dashboard</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Live overview of machine health predictions, trends, and confidence across your fleet.</div>', unsafe_allow_html=True)

# ----------------------------
# Load Data
# ----------------------------
df = get_prediction_history()
# ----------------------------------------------------
# Database Availability Check
# ----------------------------------------------------

if df.empty:

    st.warning("""
⚠ Database is unavailable.

The public demo is running without SQL Server.

Prediction functionality is still available.
""")

    st.stop()

if df.empty:
    st.warning("No prediction data available.")
    st.stop()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔍 Filters")

machine_filter = st.sidebar.multiselect(
    "Machine Type",
    options=sorted(df["MachineType"].unique()),
    default=sorted(df["MachineType"].unique())
)

prediction_filter = st.sidebar.multiselect(
    "Prediction",
    options=sorted(df["Prediction"].unique()),
    default=sorted(df["Prediction"].unique())
)

filtered_df = df[
    (df["MachineType"].isin(machine_filter)) &
    (df["Prediction"].isin(prediction_filter))
]

if filtered_df.empty:
    st.info("No records match the selected filters.")
    st.stop()

# ----------------------------
# KPI Cards (styled)
# ----------------------------
total_predictions = len(filtered_df)
healthy = len(filtered_df[filtered_df["Prediction"] == "Healthy"])
failure = len(filtered_df[filtered_df["Prediction"] == "Failure"])
avg_confidence = filtered_df["Confidence"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">📋</div>
        <div style="font-size:1.4rem; font-weight:700;">{total_predictions}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Total Predictions</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box-green">
        <div style="font-size:1.6rem;">🟢</div>
        <div style="font-size:1.4rem; font-weight:700;">{healthy}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Healthy</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box-red">
        <div style="font-size:1.6rem;">🔴</div>
        <div style="font-size:1.4rem; font-weight:700;">{failure}</div>
        <div style="font-size:0.85rem; opacity:0.9;">Failure</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-box">
        <div style="font-size:1.6rem;">🎯</div>
        <div style="font-size:1.4rem; font-weight:700;">{avg_confidence:.2f}%</div>
        <div style="font-size:0.85rem; opacity:0.9;">Avg Confidence</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.divider()

# ----------------------------
# Charts
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    st.subheader("Prediction Distribution")

    prediction_counts = (
        filtered_df["Prediction"]
        .value_counts()
        .reset_index()
    )
    prediction_counts.columns = ["Prediction", "Count"]

    fig = px.pie(
        prediction_counts,
        names="Prediction",
        values="Count",
        hole=0.55,
        color="Prediction",
        color_discrete_map=STATUS_COLORS
    )
    fig.update_traces(textinfo="percent+label")
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        legend=dict(orientation="h", y=-0.15)
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Machine Type Distribution")

    machine_counts = (
        filtered_df["MachineType"]
        .value_counts()
        .reset_index()
    )
    machine_counts.columns = ["MachineType", "Count"]

    fig = px.bar(
        machine_counts,
        x="MachineType",
        y="Count",
        text="Count",
        color="MachineType",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    fig.update_traces(textposition="outside")
    fig.update_layout(
        margin=dict(t=10, b=10, l=10, r=10),
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

st.divider()

# ----------------------------
# Confidence Trend
# ----------------------------

st.subheader("📈 Prediction Confidence Trend")

fig = px.line(
    filtered_df.sort_values("PredictionTime"),
    x="PredictionTime",
    y="Confidence",
    color="Prediction",
    color_discrete_map=STATUS_COLORS,
    markers=True
)
fig.update_layout(
    margin=dict(t=10, b=10, l=10, r=10),
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ----------------------------
# Download CSV
# ----------------------------

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Prediction History (CSV)",
    data=csv,
    file_name="prediction_history.csv",
    mime="text/csv",
    use_container_width=True
)

st.divider()

# ----------------------------
# Prediction History
# ----------------------------

st.subheader("🗂️ Prediction History")

st.dataframe(
    filtered_df.style.map(
        lambda v: "color: #56ab2f; font-weight: 600" if v == "Healthy"
        else ("color: #cb2d3e; font-weight: 600" if v == "Failure" else ""),
        subset=["Prediction"]
    ),
    use_container_width=True
)
