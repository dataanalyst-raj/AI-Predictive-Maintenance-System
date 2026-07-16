import streamlit as st

def load_css():
    st.markdown("""
    <style>

    .main {
        background-color: #f5f7fa;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .status-card{
        background:white;
        padding:20px;
        border-radius:15px;
        box-shadow:0px 4px 12px rgba(0,0,0,.08);
        border-left:8px solid #2E86DE;
        margin-bottom:15px;
    }

    .healthy{
        border-left:8px solid #2ECC71;
    }

    .failure{
        border-left:8px solid #E74C3C;
    }

    .section-title{
        font-size:28px;
        font-weight:bold;
        color:#1B2631;
        margin-bottom:10px;
    }

    .sub-title{
        color:#5D6D7E;
        font-size:16px;
        margin-bottom:20px;
    }

    .footer{
        text-align:center;
        color:gray;
        margin-top:50px;
        font-size:14px;
    }

    div[data-testid="stMetric"]{
        background:white;
        border-radius:12px;
        padding:15px;
        box-shadow:0 2px 8px rgba(0,0,0,.08);
    }

    </style>
    """, unsafe_allow_html=True)
