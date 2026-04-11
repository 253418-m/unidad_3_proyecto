import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def render_visualization_section(df):
    """Renderiza la selección de variables y los gráficos estadísticos."""
    
    st.markdown("---")
    st.header("2. Exploración Visual de los Datos")

    columnas = df.columns.tolist()
        
    with st.container():
        st.markdown("#### Selección de Parámetros")
        variable = st.selectbox(
            "Selecciona la variable que deseas analizar:", 
            columnas,
            help="Elige la columna sobre la cual realizaremos la exploración."
        )
    
    st.markdown(f"### Análisis de la distribución: `{variable}`")

    es_numerica = pd.api.types.is_numeric_dtype(df[variable])
    
    sns.set_theme(style="whitegrid", rc={"axes.facecolor": "#FFFFFF", "figure.facecolor": "#FFFFFF"})
    color_grafico = "#26B293"
    
    if es_numerica:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Histograma y KDE")
            fig_hist, ax_hist = plt.subplots(figsize=(6, 4))
            sns.histplot(df[variable], kde=True, color=color_grafico, ax=ax_hist, edgecolor="white")
            ax_hist.set_ylabel("Frecuencia")
            ax_hist.set_xlabel("Valores")
            st.pyplot(fig_hist)
            
        with col2:
            st.subheader("Diagrama de Caja (Boxplot)")
            fig_box, ax_box = plt.subplots(figsize=(6, 4))
            sns.boxplot(x=df[variable], color=color_grafico, ax=ax_box)
            ax_box.set_xlabel("Valores")
            st.pyplot(fig_box)

        st.markdown("### Análisis del Estudiante")
        st.info("Observa las gráficas superiores y responde a las siguientes preguntas requeridas:")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            st.selectbox("¿La distribución parece normal?", ["Sí", "No", "Incierto"], index=None, placeholder="Selecciona...")
        with c2:
            st.selectbox("¿Hay presencia de sesgo?", ["Sin sesgo (Simétrica)", "Sesgo a la derecha", "Sesgo a la izquierda"], index=None, placeholder="Selecciona...")
        with c3:
            st.selectbox("¿Se observan outliers (atípicos)?", ["Sí", "No"], index=None, placeholder="Selecciona...")
            
        return variable 
    else:
        st.warning("**Aviso Estadístico:** Esta es una variable categórica. La Prueba Z requiere variables numéricas continuas para calcular promedios. A continuación se muestra su frecuencia, pero no pasará al motor de hipótesis.")
        
        fig_cat, ax_cat = plt.subplots(figsize=(8, 4))
        sns.countplot(y=df[variable], color=color_grafico, ax=ax_cat, order=df[variable].value_counts().index)
        ax_cat.set_xlabel("Frecuencia")
        ax_cat.set_ylabel("Categorías")
        st.pyplot(fig_cat)
        
        return None 