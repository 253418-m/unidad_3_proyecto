import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def configure_api():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("API Key no encontrada. Verifica el archivo .env")
        return False
    genai.configure(api_key=api_key)
    return True

def render_ai_section(stats_data):
    st.markdown("---")
    st.header("4. Analisis Asistido por IA")
    
    if st.button("Consultar a Gemini", type="primary"):
        if not configure_api():
            return
            
        with st.spinner("Generando interpretacion..."):
            decision = "Rechazar H0" if stats_data['rechazar'] else "No rechazar H0"
            
            prompt = f"""
            Se realizo una prueba Z con los siguientes parametros:
            media muestral = {stats_data['media']:.2f}, media hipotetica = {stats_data['h0']}, 
            n = {stats_data['n']}, sigma = {stats_data['std']:.2f}, alpha = {stats_data['alpha']}, 
            tipo de prueba = {stats_data['tipo']}.

            El estadistico Z fue = {stats_data['z']:.4f} y el p-value = {stats_data['p']:.4f}.
            Decision matematica: {decision}.

            ¿Se rechaza H0? Explica la decision y si los supuestos de la prueba son razonables.
            """
            
            try:
                modelo_disponible = None
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        modelo_disponible = m.name.replace('models/', '')
                        if 'vision' not in modelo_disponible.lower():
                            break
                
                if not modelo_disponible:
                    st.error("No se encontraron modelos de texto compatibles para esta API Key.")
                    return

                model = genai.GenerativeModel(modelo_disponible)
                response = model.generate_content(prompt)
                
                st.caption(f"Modelo utilizado: {modelo_disponible}")
                st.info(response.text)
                
            except Exception as e:
                st.error(f"Error de conexion con la API: {e}")