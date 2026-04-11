import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .stApp {
            background-color: #F4F7F8;
        }
        
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 16px rgba(0, 0, 0, 0.04);
            border: 1px solid #E2E8F0;
            margin-bottom: 1rem;
        }

        h1, h2, h3 {
            color: #1E293B;
            font-weight: 700 !important;
        }
        
        div.stInfo {
            background-color: #E8F6F3;
            color: #1E293B;
            border-left: 4px solid #26B293;
            border-radius: 8px;
        }
        div.stSuccess {
            background-color: #ECFDF5;
            color: #1E293B;
            border-left: 4px solid #10B981;
            border-radius: 8px;
        }

        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(38, 178, 147, 0.2);
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)