# Z-Lab: Análisis Estadístico con IA

Z-Lab es una aplicación interactiva creada con Streamlit para apoyar el aprendizaje y la práctica del análisis estadístico, en especial pruebas de hipótesis Z. Combina carga de datos, visualización exploratoria, cálculo estadístico y una evaluación asistida por IA usando Google Gemini.

---

## Características principales

- **Carga de datos**
  - Genera una muestra sintética normal de prueba.
  - Permite cargar un archivo CSV local.
- **Exploración visual**
  - Histograma con KDE y diagrama de caja para variables numéricas.
  - Gráfica de conteo para variables categóricas.
  - Cuestionario de observación visual para normalidad, sesgo y outliers.
- **Prueba de hipótesis Z**
  - Calcula estadísticos de muestra, estadístico Z, valor p y región crítica.
  - Soporta pruebas bilaterales, de cola izquierda y de cola derecha.
- **Asistencia de IA**
  - Usa Google Gemini para evaluar la consistencia del análisis del estudiante.
  - Requiere la clave de API `GEMINI_API_KEY` en un archivo `.env`.

---

## Estructura del proyecto

- `app.py` - Punto de entrada principal de Streamlit.
- `modules/ui_styles.py` - Aplica estilos personalizados a la interfaz.
- `modules/data_loader.py` - Gestiona la carga y generación de datos.
- `modules/visualizer.py` - Renderiza gráficos y preguntas de inspección visual.
- `modules/stats_engine.py` - Ejecuta la prueba de hipótesis Z y muestra resultados.
- `modules/ai_assistant.py` - Conecta con Google Gemini para análisis guiado.

---

## Requisitos

- Python 3.10 o superior
- Dependencias listadas en `requirements.txt`

### Dependencias principales

- `streamlit`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scipy`
- `google-generativeai`
- `python-dotenv`

---

## Instalación

1. Crea y activa un entorno virtual (recomendado):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Instala las dependencias:
   ```powershell
   pip install -r requirements.txt
   ```
3. Crea un archivo `.env` en la raíz del proyecto con la clave de Gemini:
   ```text
   GEMINI_API_KEY=tu_api_key_aqui
   ```

---

## Uso

1. Ejecuta la aplicación:
   ```powershell
   streamlit run app.py
   ```
2. Abre el navegador en la URL que Streamlit indique.
3. En la barra lateral selecciona:
   - `Carga de Datos` para subir un CSV o generar datos sintéticos.
   - `Analisis Visual` para seleccionar una variable y ver sus gráficos.
   - `Prueba de Hipotesis` para calcular Z, p-value y tomar decisión.
4. En la sección de IA, selecciona una conclusión y presiona `Consultar a Gemini`.

---

## Flujo recomendado

1. Usa `Carga de Datos` para generar o subir una tabla.
2. Revisa la `Vista Previa` y asegúrate de contar con variables numéricas.
3. Ve a `Analisis Visual` y observa la forma de la distribución.
4. Contesta las preguntas de normalidad, sesgo y outliers.
5. Avanza a `Prueba de Hipotesis` y completa los parámetros.
6. Compara tu conclusión con la evaluación automática y consulta a Gemini.

---

## Notas importantes

- La prueba de hipótesis solo funciona con variables numéricas.
- El cálculo Z requiere al menos `n >= 30` para ser válido según la implementación actual.
- Si no tienes `GEMINI_API_KEY`, la sección de IA no podrá funcionar.

---

## Licencia

Este proyecto es una demostración educativa. Ajusta y reutiliza el código según tus necesidades.
