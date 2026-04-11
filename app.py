import streamlit as st
from modules.ui_styles import apply_custom_css
from modules.data_loader import render_data_upload_section

st.set_page_config(
    page_title="Prueba de Hipótesis App", 
    page_icon="📈", 
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

st.title("Análisis Estadístico y Prueba de Hipótesis")
st.markdown("*Plataforma interactiva para evaluación de distribuciones y decisiones estadísticas asistidas por IA.*")
st.markdown("---")

df = render_data_upload_section()

if df is not None:
    with st.expander("🔍 Ver vista previa del conjunto de datos", expanded=True):
        st.dataframe(df.head(10), use_container_width=True)
        st.caption(f"Total de registros cargados: {df.shape[0]} filas y {df.shape[1]} columnas.")