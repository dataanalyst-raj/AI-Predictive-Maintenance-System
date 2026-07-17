import streamlit as st
def load_css():
    st.markdown("""
    <style>

        /* ---------------------------------
           Hero / Header Text
        --------------------------------- */
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

        /* ---------------------------------
           Generic Card
        --------------------------------- */
        .card {
            background-color: #f8f9fb;
            border: 1px solid #e6e6e6;
            border-radius: 12px;
            padding: 1.2rem 1.4rem;
            height: 100%;
        }

        /* ---------------------------------
           Metric Boxes (gradient)
        --------------------------------- */
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
        .metric-box-amber {
            background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);
            border-radius: 12px;
            padding: 1rem;
            color: #1a1a2e;
            text-align: center;
        }

        /* ---------------------------------
           Status Pills
        --------------------------------- */
        .status-pill-connected {
            display: inline-block;
            background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.95rem;
        }
        .status-pill-failed {
            display: inline-block;
            background: linear-gradient(135deg, #cb2d3e 0%, #ef473a 100%);
            color: white;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.95rem;
        }
        .status-pill-warning {
            display: inline-block;
            background: linear-gradient(135deg, #f7971e 0%, #ffd200 100%);
            color: #1a1a2e;
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.95rem;
        }

        /* ---------------------------------
           Result Cards (Prediction outcomes)
        --------------------------------- */
        .result-card-healthy {
            background: linear-gradient(135deg, #56ab2f 0%, #a8e063 100%);
            border-radius: 14px;
            padding: 1.5rem;
            color: white;
            text-align: center;
        }
        .result-card-failure {
            background: linear-gradient(135deg, #cb2d3e 0%, #ef473a 100%);
            border-radius: 14px;
            padding: 1.5rem;
            color: white;
            text-align: center;
        }

        /* ---------------------------------
           Info Cards (labeled key/value)
        --------------------------------- */
        .info-card {
            background-color: #f8f9fb;
            border-left: 4px solid #667eea;
            border-radius: 8px;
            padding: 0.9rem 1.1rem;
            margin-bottom: 0.8rem;
        }
        .info-card-label {
            font-size: 0.8rem;
            color: #888;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .info-card-value {
            font-size: 1.05rem;
            color: #1a1a2e;
            font-weight: 600;
            margin-top: 0.2rem;
        }

    </style>
    """, unsafe_allow_html=True)
