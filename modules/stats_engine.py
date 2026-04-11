import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def render_hypothesis_testing(df, variable):
    st.markdown("---")
    st.header("3. Prueba de Hipotesis (Prueba Z)")
    
    if variable is None:
        st.warning("Variables categoricas no admitidas para esta prueba.")
        return None
        
    datos = df[variable].dropna()
    n = len(datos)
    
    if n < 30:
        st.error(f"Tamaño de muestra insuficiente (n={n}). Se requiere n >= 30.")
        return None
        
    media_muestral = datos.mean()
    desviacion_pob = datos.std()
    
    st.write(f"**Estadisticos base:** n = {n} | Media = {media_muestral:.2f} | Desviacion = {desviacion_pob:.2f}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        h0_valor = st.number_input("Hipotesis Nula (H0):", value=float(media_muestral))
    with col2:
        tipo_prueba = st.selectbox("Tipo de prueba:", ["Bilateral", "Cola izquierda", "Cola derecha"])
    with col3:
        alpha = st.selectbox("Nivel de significancia (alpha):", [0.01, 0.05, 0.10], index=1)
        
    error_estandar = desviacion_pob / np.sqrt(n)
    z_stat = (media_muestral - h0_valor) / error_estandar
    
    if tipo_prueba == "Bilateral":
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
        z_crit = stats.norm.ppf(1 - alpha / 2)
        rechazar = abs(z_stat) > z_crit
    elif tipo_prueba == "Cola derecha":
        p_value = 1 - stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(1 - alpha)
        rechazar = z_stat > z_crit
    else:
        p_value = stats.norm.cdf(z_stat)
        z_crit = stats.norm.ppf(alpha)
        rechazar = z_stat < z_crit
        
    st.subheader("Resultados Analiticos")
    res1, res2, res3 = st.columns(3)
    res1.metric("Estadistico Z", f"{z_stat:.4f}")
    res2.metric("Valor p (p-value)", f"{p_value:.4f}")
    
    decision_texto = "Rechazar H0" if rechazar else "No rechazar H0"
    res3.metric("Decision Automatica", decision_texto)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    x = np.linspace(-4, 4, 1000)
    y = stats.norm.pdf(x, 0, 1)
    
    ax.plot(x, y, color="#1E293B")
    
    if tipo_prueba == "Bilateral":
        ax.fill_between(x, y, where=(x > z_crit), color="#EF4444", alpha=0.3)
        ax.fill_between(x, y, where=(x < -z_crit), color="#EF4444", alpha=0.3)
    elif tipo_prueba == "Cola derecha":
        ax.fill_between(x, y, where=(x > z_crit), color="#EF4444", alpha=0.3)
    else:
        ax.fill_between(x, y, where=(x < z_crit), color="#EF4444", alpha=0.3)
        
    ax.axvline(z_stat, color="#26B293", linestyle="--", linewidth=2.5, label=f"Z Calc ({z_stat:.2f})")
    ax.set_title("Distribucion Normal Estandar y Region Critica")
    ax.legend()
    st.pyplot(fig)
    
    return {
        "n": n, "media": media_muestral, "h0": h0_valor, "std": desviacion_pob,
        "alpha": alpha, "tipo": tipo_prueba, "z": z_stat, "p": p_value, "rechazar": rechazar
    }