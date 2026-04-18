import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def render_hypothesis_testing(df, _unused_var):
    variable = st.session_state.get('selected_var')
    
    st.markdown("---")
    st.header(f"3. Prueba de Hipotesis: {variable}")
    
    if variable is None:
        st.warning("Regresa a la seccion de Visualizacion y selecciona una variable primero.")
        return None
        
    datos = df[variable].dropna()
    n = len(datos)
    
    if n < 30:
        st.error(f"Tamaño de muestra insuficiente (n={n}). Se requiere n >= 30.")
        return None
        
    media_muestral = datos.mean()
    desviacion_pob = np.std(datos, ddof=1)
    
    st.write(f"**Estadisticos base:** n = {n} | Media (x̄) = {media_muestral:.4f} | Desviacion (s) = {desviacion_pob:.4f}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        h0_valor = st.number_input("Hipotesis Nula (H0): μ =", value=float(media_muestral))
    with col2:
        tipo_prueba = st.selectbox("Hipotesis Alternativa (H1):", ["Bilateral (≠)", "Cola izquierda (<)", "Cola derecha (>)"])
    with col3:
        alpha = st.selectbox("Nivel de significancia (α):", [0.01, 0.05, 0.10], index=1)
        
    error_estandar = desviacion_pob / np.sqrt(n)
    
    if error_estandar == 0:
        st.error("Error: La desviacion estandar es 0. No se puede calcular Z.")
        return None
        
    z_stat = (media_muestral - h0_valor) / error_estandar
    
    if tipo_prueba == "Bilateral (≠)":
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        z_crit = stats.norm.ppf(1 - alpha / 2)
        rechazar = abs(z_stat) > z_crit
        region_texto = f"Z < {-z_crit:.4f} o Z > {z_crit:.4f}"
    elif tipo_prueba == "Cola derecha (>)":
        p_value = 1 - stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(1 - alpha)
        rechazar = z_stat > z_crit
        region_texto = f"Z > {z_crit:.4f}"
    else:
        p_value = stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(alpha)
        rechazar = z_stat < z_crit
        region_texto = f"Z < {z_crit:.4f}"
        
    st.subheader("Salida (Resultados Analíticos)")
    
    color_decision = "#EF4444" if rechazar else "#26B293" 
    decision_texto = "Rechazar H0" if rechazar else "No rechazar H0"
    
    tarjetas_html = f"""
    <div style="display: flex; flex-wrap: wrap; gap: 15px; margin-bottom: 25px;">
        <div style="flex: 1; min-width: 150px; background-color: #FFFFFF; border-left: 6px solid #0185D3; padding: 15px 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 1px solid #F1F5F9; border-right: 1px solid #F1F5F9; border-bottom: 1px solid #F1F5F9;">
            <p style="margin:0; font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Valor Z Calculado</p>
            <p style="margin:0; font-size: 28px; font-weight: 900; color: #1E293B;">{z_stat:.4f}</p>
        </div>
        <div style="flex: 1; min-width: 150px; background-color: #FFFFFF; border-left: 6px solid #FE9416; padding: 15px 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 1px solid #F1F5F9; border-right: 1px solid #F1F5F9; border-bottom: 1px solid #F1F5F9;">
            <p style="margin:0; font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Región Crítica</p>
            <p style="margin:0; font-size: 22px; font-weight: 900; color: #1E293B;">{region_texto}</p>
        </div>
        <div style="flex: 1; min-width: 150px; background-color: #FFFFFF; border-left: 6px solid #00A3A0; padding: 15px 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 1px solid #F1F5F9; border-right: 1px solid #F1F5F9; border-bottom: 1px solid #F1F5F9;">
            <p style="margin:0; font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">p-value</p>
            <p style="margin:0; font-size: 28px; font-weight: 900; color: #1E293B;">{p_value:.4f}</p>
        </div>
        <div style="flex: 1; min-width: 150px; background-color: #FFFFFF; border-left: 6px solid {color_decision}; padding: 15px 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); border-top: 1px solid #F1F5F9; border-right: 1px solid #F1F5F9; border-bottom: 1px solid #F1F5F9;">
            <p style="margin:0; font-size: 12px; color: #64748B; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Decisión Automática</p>
            <p style="margin:0; font-size: 22px; font-weight: 900; color: {color_decision};">{decision_texto}</p>
        </div>
    </div>
    """
    st.markdown(tarjetas_html, unsafe_allow_html=True)
  
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    ax.plot(x, y, color="#1E293B", linewidth=1.5)
    
    if tipo_prueba == "Bilateral (≠)":
        ax.fill_between(x, y, where=(x > z_crit), color="#EF4444", alpha=0.5, label="Zona Rechazo (H0)")
        ax.fill_between(x, y, where=(x < -z_crit), color="#EF4444", alpha=0.5)
        ax.fill_between(x, y, where=((x >= -z_crit) & (x <= z_crit)), color="#26B293", alpha=0.2, label="Zona No Rechazo")
    elif tipo_prueba == "Cola derecha (>)":
        ax.fill_between(x, y, where=(x > z_crit), color="#EF4444", alpha=0.5, label="Zona Rechazo (H0)")
        ax.fill_between(x, y, where=(x <= z_crit), color="#26B293", alpha=0.2, label="Zona No Rechazo")
    else:
        ax.fill_between(x, y, where=(x < z_crit), color="#EF4444", alpha=0.5, label="Zona Rechazo (H0)")
        ax.fill_between(x, y, where=(x >= z_crit), color="#26B293", alpha=0.2, label="Zona No Rechazo")
        
    ax.axvline(z_stat, color="#1E293B", linestyle="--", linewidth=2.5, label=f"Z Calc ({z_stat:.2f})")
    
    ax.set_title("Curva Normal con Zonas de Rechazo y No Rechazo")
    ax.legend(loc="upper right")
    st.pyplot(fig)
    
    return {
        "n": n, "media": media_muestral, "h0": h0_valor, "std": desviacion_pob,
        "alpha": alpha, "tipo": tipo_prueba, "z": z_stat, "p": p_value, "rechazar": rechazar
    }