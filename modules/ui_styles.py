import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #F8FAFC;
        }

        .block-container {
            padding-top: 2rem;
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #00A3A0 0%, #0185D3 100%);
        }

        [data-testid="stSidebar"], [data-testid="stSidebar"] p, [data-testid="stSidebar"] span, [data-testid="stSidebar"] div, [data-testid="stSidebar"] label {
            color: #FFFFFF !important;
        }

        .sidebar-title {
            font-size: 2.2rem !important;
            font-weight: 800 !important;
            color: #FFFFFF !important;
            margin-bottom: 0rem;
            line-height: 1.2;
        }

        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.05);
            border: 1px solid #E2E8F0;
            margin-bottom: 1rem;
        }

        h1, h2, h3 {
            color: #1E293B !important;
            font-weight: 700 !important;
        }

        p, span, label {
            color: #334155;
        }

        div.stInfo {
            background-color: rgba(0, 163, 160, 0.1) !important;
            color: #00A3A0 !important;
            border-left: 4px solid #00A3A0 !important;
            border-radius: 8px;
        }

        [data-testid="stSidebar"] .stButton>button {
            background-color: rgba(255, 255, 255, 0.15);
            color: #FFFFFF !important;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        [data-testid="stSidebar"] .stButton>button:hover {
            background-color: rgba(255, 255, 255, 0.3);
            border-color: #FFFFFF;
        }

        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        </style>
    """, unsafe_allow_html=True)