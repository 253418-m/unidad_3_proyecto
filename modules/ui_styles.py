import streamlit as st

def apply_custom_css():
    st.markdown("""
        <style>
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        h1 {
            color: #1E3A8A;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-weight: 700;
        }
        h2, h3 {
            color: #2563EB;
        }
        div.stInfo {
            background-color: #EFF6FF;
            border-left: 5px solid #3B82F6;
        }
        div.stSuccess {
            background-color: #F0FDF4;
            border-left: 5px solid #22C55E;
        }
        </style>
    """, unsafe_allow_html=True)