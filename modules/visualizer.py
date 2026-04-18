import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def render_visualization_section(df):
    st.markdown("---")
    st.header("2. Exploracion Visual de los Datos")
    
    columnas = df.columns.tolist()
    
    try:
        default_idx = columnas.index(st.session_state.selected_var)
    except:
        default_idx = 0
        
    variable = st.selectbox(
        "Selecciona la variable que deseas analizar:", 
        columnas,
        index=default_idx
    )
    
    st.session_state.selected_var = variable
    
    st.markdown(f"### Analisis de la distribucion: `{variable}`")
    es_numerica = pd.api.types.is_numeric_dtype(df[variable])
    
    sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#FFFFFF", "figure.facecolor": "#FFFFFF"})
    paleta_colores = ["#00A3A0", "#FE9416", "#0185D3", "#DE242D", "#FDC405", "#8EC93D"]
    
    if es_numerica:
        datos_limpios = df[variable].dropna()
        col1, col2 = st.columns(2)
        
        with col1:
            fig_hist, ax_hist = plt.subplots(figsize=(6, 4))
            sns.histplot(datos_limpios, kde=True, color=paleta_colores[0], ax=ax_hist)
            st.pyplot(fig_hist)
            
        with col2:
            fig_box, ax_box = plt.subplots(figsize=(6, 4))
            sns.boxplot(x=datos_limpios, color=paleta_colores[1], ax=ax_box)
            st.pyplot(fig_box)
            
        st.markdown("### Analisis del Estudiante")
        c1, c2, c3 = st.columns(3)
        
        with c1:
            st.selectbox("¿Parece normal?", ["Pendiente", "Si", "No", "Incierto"], key="ans_normal")
        with c2:
            st.selectbox("¿Hay sesgo?", ["Pendiente", "Sin sesgo", "Derecha", "Izquierda"], key="ans_sesgo")
        with c3:
            st.selectbox("¿Hay outliers?", ["Pendiente", "Si", "No"], key="ans_outliers")
            
        return variable
        
    else:
        st.warning("Aviso Estadistico: Esta es una variable categorica. No pasara al motor de hipotesis.")
        fig_cat, ax_cat = plt.subplots(figsize=(8, 4))
        datos_cat = df[variable].dropna()
        num_cat = len(datos_cat.unique())
        paleta_actual = paleta_colores * (num_cat // len(paleta_colores) + 1)
        sns.countplot(y=datos_cat, hue=datos_cat, palette=paleta_actual[:num_cat], ax=ax_cat, legend=False)
        ax_cat.set_xlabel("Frecuencia")
        ax_cat.set_ylabel("Categorias")
        st.pyplot(fig_cat)
        
        return None