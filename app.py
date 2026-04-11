import streamlit as st
from modules.ui_styles import apply_custom_css
from modules.data_loader import render_data_upload_section
from modules.visualizer import render_visualization_section

st.set_page_config(
    page_title="Dashboard Estadístico",  
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

with st.sidebar:
    st.markdown("## StatHub Pro")
    st.caption("Panel de Análisis y Pruebas")
    st.markdown("---")
    
    st.button("Carga de Datos", use_container_width=True, type="primary")
    st.button("Visualización", use_container_width=True)
    st.button("Prueba de Hipótesis", use_container_width=True)
    st.button("Asistente IA (Gemini)", use_container_width=True)
    
    st.markdown("---")
    st.info("**Tip:** Comienza cargando un dataset para habilitar el análisis.")

st.title("Módulo de Reclutamiento / Análisis de Datos")
st.markdown("*Plataforma interactiva para evaluación estadística asistida por IA.*")
st.markdown("---")

with st.container():
    df = render_data_upload_section()

if df is not None:
    with st.container():
        st.subheader("Vista Previa de Registros")
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Total de registros activos: {df.shape[0]}")
        variable_analizar = render_visualization_section(df) 