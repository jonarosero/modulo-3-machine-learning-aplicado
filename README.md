# Módulo 3 — Machine Learning Aplicado

Material de clase del Diplomado en Big Data e Inteligencia Artificial, preparado para CEC EPN / Banco Central del Ecuador.

## Propósito y organización

El módulo oficial suma **25 horas: 20 sincrónicas y 5 autónomas**, en cinco unidades. Este repositorio acompaña la ruta de siete jornadas. Cada notebook de los días 3–7 se puede leer de forma autónoma y sigue el patrón didáctico del Día 1: problema → unidad y fuente de datos → exploración → concepto → código guiado → lectura de resultados → diagnóstico → actividad y preguntas.

Los notebooks estiman el tiempo para la sesión en sus portadas; el contenido central se prioriza para las horas disponibles y las actividades adicionales quedan como práctica autónoma. No es necesario ejecutar todos los experimentos durante la sesión para cubrir los resultados de aprendizaje.

Para los días actualizados, la distribución indicada sigue el plan oficial: Día 3 (3 h sincrónicas + 1 autónoma), Día 4 (3 + 1), Día 5 (3 sincrónicas), Día 6 (3 + 1) y Día 7 (2 + 1). Las celdas de ampliación se pueden dejar como lectura o trabajo autónomo.

## Ruta por jornada y contenidos oficiales

| Día | Notebook | Temas del Módulo 3 |
|---|---|---|
| 1 | `notebooks/01_Dia1_Datos_y_Regresion.ipynb` | Regresión lineal y múltiple, exploración, métricas y datos económicos. Referencia pedagógica. |
| 2 | `notebooks/02_Dia2_Overfitting_CV_Arboles_Clasificacion_WorldBank_v2.ipynb` | Evaluación predictiva, overfitting, validación cruzada, árboles y Random Forest. |
| 3 | `notebooks/03_Dia3_SVM_KNN_Metricas_KMeans.ipynb` | Clasificación, métricas, KNN y SVM. |
| 4 | `notebooks/04_Dia4_Clustering_Segmentacion_Economica.ipynb` | K-Means, clustering jerárquico, segmentación económica, patrones e interpretación. |
| 5 | `notebooks/05_Dia5_PCA_Seleccion_Features.ipynb` | PCA, selección de variables e ingeniería de características. |
| 6 | `notebooks/06_Dia6_Visualizacion_Optimizacion_y_Reto.ipynb` | Visualización multidimensional, búsqueda de hiperparámetros y diseño del proyecto. |
| 7 | `notebooks/07_Dia7_Pipelines_Forecasting_Presentacion.ipynb` | Construcción y comparación de modelos, Pipeline, forecasting y presentación final. |

El notebook `01_1_Dia1_Regularizacion_Ridge_Lasso_ElasticNet.ipynb` es material complementario.

## Datos locales y reproducibilidad

Los notebooks de los días 3–7 leen datasets desde `datos/`. **No descargan datos en ejecución desde APIs, UCI, Kaggle ni OpenML.** Las fuentes originales se atribuyen en `datos/README.md`; las copias se conservan para que todas las personas de clase trabajen con la misma versión.

- `bank_marketing_uci.csv`: dataset público UCI Bank Marketing (41 188 contactos), usado en Días 3 y como práctica de clasificación. Datos de campañas bancarias portuguesas; no representan clientes ecuatorianos ni al BCE.
- `world_bank_latam_ml.csv`: panel anual de indicadores macroeconómicos de países latinoamericanos, usado en Días 4–6 para segmentación, PCA y optimización. Datos observacionales, sujetos a faltantes, definiciones y revisiones.
- `macro_mensual_demo.csv`: **sintético didáctico**, usado en Día 7 para explicar lags, baselines y división temporal con un ejemplo mensual manejable. No son estadísticas oficiales y no debe citarse como evidencia económica.
- `actividad_economica_demo.csv` y `actividad_economica_reto.csv`: ejercicios **sintéticos didácticos** existentes, incluido el reto del Día 1.

Los datasets públicos son para práctica metodológica. No se incluyen microdatos institucionales ni información confidencial. No confundas correlación, importancia predictiva o agrupaciones exploratorias con causalidad, segmentos oficiales o recomendaciones de política.

## Preparación y ejecución

Usa Python 3.10 o posterior y Jupyter. Instala previamente, si hacen falta, `numpy`, `pandas`, `matplotlib`, `scikit-learn` y `scipy`. No hay instalaciones ni conexiones de datos automáticas dentro de las celdas. Abre el repositorio como carpeta en Jupyter y ejecuta las celdas de cada notebook en orden; las rutas buscan `datos/` desde la raíz o desde `notebooks/`.

Los notebooks originales de los Días 1–2 quedan fuera de esta actualización solicitada. Algunos bloques de esos notebooks ofrecen refrescar indicadores desde la API del Banco Mundial; para una sesión completamente sin conexión, usa los CSV locales existentes y no ejecutes las celdas de actualización en vivo. Los Días 3–7 reescritos trabajan con copias locales.

## Evaluación alineada al plan de clase

El plan de clase prevé **60 puntos formativos y 40 sumativos**. Actividades sugeridas para que la evidencia corresponda a los notebooks:

1. **Unidades 1–2 (20 puntos):** regresión del Día 1 y comparación de clasificadores de los días 2–3; justificar baseline y métricas.
2. **Unidad 3 (20 puntos):** perfiles, métodos y límites de la segmentación del Día 4.
3. **Unidad 4 (20 puntos):** PCA, selección/optimización e interpretación de los días 5–6.
4. **Unidad 5 (40 puntos):** notebook reproducible y presentación del Día 7, con rúbrica sugerida dentro del notebook.

Las puntuaciones y criterios finales deben seguir el instrumento institucional vigente.

## Fuentes y bibliografía

- UCI Machine Learning Repository, [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing). Referencia y condiciones de uso descritas por UCI.
- World Bank, [World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) y [términos de uso](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets).
- James, G. et al. (2023). *An Introduction to Statistical Learning*. <https://www.statlearning.com>
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.
- Hastie, T., Tibshirani, R. & Friedman, J. (2021). *The Elements of Statistical Learning*. <https://hastie.su.domains/ElemStatLearn/>

## Seguridad y criterio institucional

No publicar ni enviar datos institucionales o confidenciales a GitHub, Kaggle, Colab, OpenML u otros servicios externos. Para adaptar los ejemplos a una pregunta del BCE, primero valida autorización, licenciamiento, clasificación de información, periodo, definiciones y disponibilidad temporal de cada variable.
