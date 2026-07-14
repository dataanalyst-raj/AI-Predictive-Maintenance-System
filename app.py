import streamlit as st

st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Predictive Maintenance System")

st.write("Welcome to the Predictive Maintenance Application!")

st.success("Application Started Successfully!")
import streamlit as st
import joblib

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Load Trained Model
# ---------------------------
model = joblib.load("xgboost_predictive_maintenance.pkl")

# ---------------------------
# Title
# ---------------------------
st.title("🤖 AI Predictive Maintenance System")

st.markdown("---")

st.write("Enter the machine parameters below to predict whether machine failure is likely.")

# ---------------------------
# User Inputs
# ---------------------------

type_machine = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)

rot_speed = st.number_input(
    "Rotational Speed (rpm)",
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    value=10
)import streamlit as st
import joblib

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="AI Predictive Maintenance",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# Load Trained Model
# ---------------------------
model = joblib.load("xgboost_predictive_maintenance.pkl")

# ---------------------------
# Title
# ---------------------------
st.title("🤖 AI Predictive Maintenance System")

st.markdown("---")

st.write("Enter the machine parameters below to predict whether machine failure is likely.")

# ---------------------------
# User Inputs
# ---------------------------

type_machine = st.selectbox(
    "Machine Type",
    ["L", "M", "H"]
)

air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)

process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)

rot_speed = st.number_input(
    "Rotational Speed (rpm)",
    value=1500
)

torque = st.number_input(
    "Torque (Nm)",
    value=40.0
)

tool_wear = st.number_input(
    "Tool Wear (min)",
    value=10
)
exit()
