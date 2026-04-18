import streamlit as st
from modules.ui_styles import apply_custom_css
from modules.data_loader import render_data_upload_section
from modules.visualizer import render_visualization_section
from modules.stats_engine import render_hypothesis_testing
from modules.ai_assistant import render_ai_section

st.set_page_config(
    page_title="Z-Lab: Análisis Estadístico con IA", 
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_custom_css()

if 'page' not in st.session_state:
    st.session_state.page = 'Carga'

if 'selected_var' not in st.session_state:
    st.session_state.selected_var = None

def set_page(name):
    st.session_state.page = name

with st.sidebar:
    st.markdown('<p class="sidebar-title">Z-Lab: Análisis Estadistico con IA</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    if st.button("Carga de Datos", use_container_width=True, icon=":material/upload_file:"):
        set_page('Carga')
        
    if st.button("Analisis Visual", use_container_width=True, icon=":material/bar_chart:"):
        set_page('Visualizacion')
        
    if st.button("Prueba de Hipotesis", use_container_width=True, icon=":material/functions:"):
        set_page('Stats')
        
    st.markdown("---")

if st.session_state.page == 'Carga':
    st.title("Configuracion de Datos")
    with st.container():
        df = render_data_upload_section()
        if df is not None:
            st.subheader("Vista Previa")
            st.dataframe(df.head(10), use_container_width=True)

elif st.session_state.page == 'Visualizacion':
    st.title("Exploracion Visual")
    if 'df_cargado' in st.session_state:
        render_visualization_section(st.session_state.df_cargado)
    else:
        st.warning("Carga un archivo en la seccion de Carga de Datos primero.")

elif st.session_state.page == 'Stats':
    st.title("Calculo Estadistico e IA")
    if 'df_cargado' in st.session_state:
        df = st.session_state.df_cargado
        columnas = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
        if columnas:
            var = columnas[0] 
            res = render_hypothesis_testing(df, var)
            if res:
                render_ai_section(res)
        else:
            st.error("No hay variables numericas disponibles.")
    else:
        st.warning("Carga un archivo primero.")