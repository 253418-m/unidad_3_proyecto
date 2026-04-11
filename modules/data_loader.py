import streamlit as st
import pandas as pd
import numpy as np

def render_data_upload_section():
    """Renderiza la UI de carga de datos y retorna el DataFrame."""
    st.subheader("1. Importación de Datos")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        opcion_datos = st.radio(
            "Selecciona la fuente de datos:", 
            ("Generar distribución sintética", "Subir archivo CSV local")
        )
    
    df = None
    
    with col2:
        if opcion_datos == "Generar distribución sintética":
            st.info("Generando una muestra aleatoria (n=100) que sigue una distribución normal para pruebas.")
            if st.button("Generar Datos Ahora", type="primary"):
                np.random.seed(42)
                datos = np.random.normal(loc=120, scale=15, size=100)
                df = pd.DataFrame({'Variable_Analisis': datos})
                st.session_state['df_cargado'] = df 
                st.success("¡Datos generados y cargados en memoria!")
                
        elif opcion_datos == "Subir archivo CSV local":
            archivo_subido = st.file_uploader("Arrastra tu archivo CSV aquí", type=["csv"])
            if archivo_subido is not None:
                df = pd.read_csv(archivo_subido)
                
                columnas_a_ignorar = [col for col in df.columns if col.strip().lower() in ['marca temporal', 'timestamp']]
                if columnas_a_ignorar:
                    df = df.drop(columns=columnas_a_ignorar)
                   
                st.session_state['df_cargado'] = df
                st.success("¡Archivo CSV leído correctamente!")

    if 'df_cargado' in st.session_state:
        return st.session_state['df_cargado']
    return None