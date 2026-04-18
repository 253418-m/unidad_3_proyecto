import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def configure_api():
    """Configura la conexion con el modelo de Google Gemini."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("API Key no encontrada. Asegurate de tenerla en el archivo .env")
        return False
    genai.configure(api_key=api_key)
    return True

def render_ai_section(stats_data):
    """
    Renderiza la seccion de IA, evaluando la coherencia entre el analisis 
    visual del estudiante, los datos calculados y su conclusion final.
    """
    st.markdown("---")
    st.header("4. Analisis Asistido por IA")
    
    user_obs_normal = st.session_state.get("ans_normal", "No respondido")
    user_obs_sesgo = st.session_state.get("ans_sesgo", "No respondido")
    user_obs_outliers = st.session_state.get("ans_outliers", "No respondido")

    with st.container():
        st.subheader("Evaluacion del Analista")
        st.write("Antes de consultar a la IA, debes fijar tu postura segun los resultados obtenidos.")

        decision_estudiante = st.selectbox(
            "En base a tu analisis, ¿cual es tu conclusion para H0?",
            ["Selecciona tu conclusion...", "Rechazar H0", "No rechazar H0"]
        )
    
    if st.button("Consultar a Gemini", type="primary"):
        if decision_estudiante == "Selecciona tu conclusion...":
            st.warning("Por favor, selecciona una decision antes de consultar a la IA.")
            return
            
        if not configure_api():
            return
            
        with st.spinner("Gemini esta analizando la coherencia de tu reporte..."):
            decision_correcta = "Rechazar H0" if stats_data['rechazar'] else "No rechazar H0"
            
            prompt = f"""
            Actua como un tutor experto en Probabilidad y Estadistica. 
            Tu objetivo es evaluar el analisis de un estudiante sobre una Prueba Z.

            RESUMEN DE DATOS TECNICOS:
            - Tamaño de muestra (n): {stats_data['n']}
            - Media de la muestra (x̄): {stats_data['media']:.4f}
            - Desviacion estandar (s): {stats_data['std']:.4f}
            - Hipotesis Nula (H0): μ = {stats_data['h0']}
            - Nivel de significancia (α): {stats_data['alpha']}
            - Tipo de prueba: {stats_data['tipo']}
            - Estadistico Z calculado: {stats_data['z']:.4f}
            - Valor p (p-value): {stats_data['p']:.4f}
            - Decision Matematica Real: {decision_correcta}

            ANALISIS PREVIO DEL ESTUDIANTE (Observacion Visual):
            - ¿Dijo que los datos eran normales?: {user_obs_normal}
            - ¿Detecto sesgo?: {user_obs_sesgo}
            - ¿Detecto outliers?: {user_obs_outliers}
            
            CONCLUSION FINAL DEL ESTUDIANTE:
            - El estudiante decidio: "{decision_estudiante}"

            TAREA:
            1. Evalua la observacion visual: Indica si sus respuestas sobre normalidad, sesgo y outliers son coherentes con los estadisticos (n, media, s).
            2. Califica la conclusion: Indica claramente si el estudiante ACERTO o SE EQUIVOCO al comparar su decision con la decision matematica real.
            3. Explicacion: Justifica la decision usando la relacion entre el p-value y alpha, y el valor de Z frente a la region critica.
            4. Da un consejo breve para mejorar su analisis estadistico.
            """
            
            try:
                modelo_disponible = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        nombre_modelo = m.name.replace('models/', '')
                        if 'vision' not in nombre_modelo.lower():
                            modelo_disponible = nombre_modelo
                            if 'flash' in nombre_modelo.lower():
                                break
                
                if not modelo_disponible:
                    st.error("No se encontraron modelos de texto compatibles para esta API Key.")
                    return

                model = genai.GenerativeModel(modelo_disponible)
                response = model.generate_content(prompt)
 
                st.markdown("#### Interpretacion de la IA")
                st.info(response.text)
                st.caption(f"Analisis generado por: {modelo_disponible}")
                
            except Exception as e:
                st.error(f"Error al conectar con la IA: {e}")