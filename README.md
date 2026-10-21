# Módulo 3 — Machine Learning Aplicado

Material de clase del Diplomado en Big Data e Inteligencia Artificial, preparado para CEC EPN / Banco Central del Ecuador.

## Propósito y organización

El documento institucional declara **25 horas: 20 sincrónicas y 5 autónomas**, en cinco unidades. La ruta docente acordada comprende **siete jornadas de 3 horas de clase (21 horas)**; por tanto difiere en una hora sincrónica de la declaración institucional. Esta diferencia se registra, sin cambiar aquí la duración aprobada. El plan de ajustes y comprobación está en [`PLAN_AJUSTES_MODULO3.md`](PLAN_AJUSTES_MODULO3.md). El notebook del Día 1 permanece intacto. Los días 2–7 pueden leerse desde conocimientos casi iniciales y siguen el patrón: problema → intuición → ejemplo pequeño → datos → código comentado → lectura de resultados → límites → ejercicio.

Los notebooks señalan una ruta presencial de tres horas; el resto de explicaciones y experimentos siguen disponibles para el autoestudio. No es necesario ejecutar todas las variantes en vivo para poder comprenderlas y practicarlas después.

Las actividades autónomas institucionales suman cinco horas; su distribución formal debe confirmarse con el instrumento vigente. Las celdas de profundización no sustituyen el recorrido de tres horas de cada jornada.

## Ruta por jornada y contenidos oficiales

| Día | Notebook | Temas del Módulo 3 |
|---|---|---|
| 1 | `notebooks/01_Dia1_Datos_y_Regresion.ipynb` | Regresión lineal y múltiple, exploración, métricas y datos económicos. Referencia pedagógica. |
| 2 | `notebooks/02_Dia2_Evaluacion_Arboles_Regresion.ipynb` | Regresión y evaluación Holdout/K-Fold con indicadores del Banco Mundial; under/overfitting, árbol y Random Forest **de regresión**. |
| 3 | `notebooks/03_Dia3_Clasificacion_Arboles_RF_KNN_SVM.ipynb` | Clasificación desde cero: desbalance, baseline, árbol/Gini, matriz de confusión, Random Forest, KNN, SVM y comparación común de cuatro enfoques. |
| 4 | `notebooks/04_Dia4_Clustering_Segmentacion_Economica.ipynb` | Clustering: segmentación de 8 950 clientes de tarjeta de crédito con K-Means y clustering jerárquico (`datos/CC_GENERAL.csv`). |
| 5 | `notebooks/05_Dia5_PCA_Seleccion_Features.ipynb` | PCA, selección de variables e ingeniería de características. |
| 6 | `notebooks/06_Dia6_Visualizacion_Optimizacion_y_Reto.ipynb` | Visualización multidimensional, búsqueda de hiperparámetros y diseño del proyecto. |
| 7 | `notebooks/07_Dia7_Pipelines_Forecasting_Presentacion.ipynb` | Pipeline y forecasting móvil de un paso sobre serie sintética; práctica final con notebook y síntesis escrita, **sin exposición oral**. |

El notebook `01_1_Dia1_Regularizacion_Ridge_Lasso_ElasticNet.ipynb` es material complementario.

## Datos locales y reproducibilidad

Los notebooks de los días 3–7 leen datasets desde `datos/`. **No descargan datos en ejecución desde APIs, UCI, Kaggle ni OpenML.** Las fuentes originales se atribuyen en `datos/README.md`; las copias se conservan para que todas las personas de clase trabajen con la misma versión.

- `bank_marketing_uci.csv`: dataset público UCI Bank Marketing (41 188 contactos), usado en Día 3 para los cuatro clasificadores sobre la misma muestra estratificada. Datos de campañas bancarias portuguesas; no representan clientes ecuatorianos ni al BCE.
- `world_bank_latam_ml.csv`: panel anual de indicadores macroeconómicos de países latinoamericanos, usado en Día 2 para regresión y Holdout/K-Fold y en Días 4–6 para segmentación, PCA y optimización. Datos observacionales, sujetos a faltantes, definiciones y revisiones.
- `macro_mensual_demo.csv`: **sintético didáctico**, usado en Día 7 para explicar lags, baselines y división temporal con un ejemplo mensual manejable. No son estadísticas oficiales y no debe citarse como evidencia económica.
- `actividad_economica_demo.csv` y `actividad_economica_reto.csv`: ejercicios **sintéticos didácticos** existentes, incluido el reto del Día 1.
- `telco_churn_fallback.csv`: **sintético didáctico** con 4 500 clientes simulados; opción de clasificación del proyecto para practicar categorías, abandono `Yes/No` y matriz de confusión. No son registros de una operadora real.

Los datasets públicos son para práctica metodológica. No se incluyen microdatos institucionales ni información confidencial. No confundas correlación, importancia predictiva o agrupaciones exploratorias con causalidad, segmentos oficiales o recomendaciones de política.

## Preparación y ejecución

Usa Python 3.10 o posterior y Jupyter. Instala previamente, si hacen falta, `numpy`, `pandas`, `matplotlib`, `scikit-learn` y `scipy`. No hay instalaciones ni conexiones de datos automáticas dentro de las celdas. Abre el repositorio como carpeta en Jupyter y ejecuta las celdas de cada notebook en orden; las rutas buscan `datos/` desde la raíz o desde `notebooks/`.

Los Días 2–7 usan copias CSV locales, sin consultas a servicios externos durante la ejecución. El Día 1 conserva celdas opcionales de actualización en vivo del Banco Mundial.

## Evaluación alineada al plan de clase

El esquema es **60 puntos formativos + 40 finales** sobre el **mismo Proyecto Integrador**. La diagnóstica del Día 1 no puntúa; los laboratorios guiados de los Días 2–3 no añaden calificaciones. Las tres tareas guiadas formativas son: **Día 4, Tarea 1 (20):** pregunta, tipo y auditoría inicial del CSV; **Día 5, Tarea 2 (20):** limpieza, tres gráficos, partición y transformación sin fuga; **Día 6, Tarea 3 (20):** referencia, modelos, comparación en Validation y decisión fijada. El **Día 7** se entrega la **práctica final (40)**: comprobación en Test o estabilidad de clustering, notebook integrado y conclusión escrita, **sin exposición oral**. Las rúbricas con niveles y evidencias están en [`INSTRUMENTOS_EVALUACION_MODULO3.md`](INSTRUMENTOS_EVALUACION_MODULO3.md).

Cada actividad tiene su propio Word institucional en la raíz: `Instrumento_01_Diagnostica.docx` (20 preguntas A–D, 0,5 por acierto; bruto /10 que **no** se agrega a la nota), `Instrumento_02_Proyecto_Tarea1.docx`, `Instrumento_03_Proyecto_Tarea2.docx`, `Instrumento_04_Proyecto_Tarea3.docx` y `Instrumento_05_Proyecto_Practica_Final.docx`. Los cuatro primeros usan `Plantilla_Vertical.docx`; el último conserva la portada de `Plantilla_Manual.docx`. El cuestionario Word **no contiene respuestas**; su clave está exclusivamente en el [instrumento Markdown para el instructor](INSTRUMENTOS_EVALUACION_MODULO3.md), que no debe distribuirse al alumnado con la prueba.

En el proyecto, la **primera decisión** es justificar si la pregunta pide regresión (cantidad), clasificación (clase conocida) o clustering (grupos sin etiqueta). Después se documentan unidad de observación, fuente, tipos de columnas, nulos, limpieza y al menos tres visualizaciones; se separa Train/Validation/Test según tiempo, clases o grupos y se aprende cualquier transformación **solo en Train**. Si hay categorías predictoras, se identifican al explorar pero se convierten mediante One-Hot después de la partición, dentro de un Pipeline. Para clustering las particiones permiten estudiar estabilidad y perfiles, sin usar Accuracy de clasificación. El [catálogo de datos](datos/README.md) identifica la procedencia y límites de las cinco opciones.

## Fuentes y bibliografía

- UCI Machine Learning Repository, [Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing). Referencia y condiciones de uso descritas por UCI.
- World Bank, [World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) y [términos de uso](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets).
- James, G. et al. (2023). *An Introduction to Statistical Learning*. <https://www.statlearning.com>
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.
- Hastie, T., Tibshirani, R. & Friedman, J. (2021). *The Elements of Statistical Learning*. <https://hastie.su.domains/ElemStatLearn/>

## Seguridad y criterio institucional

No publicar ni enviar datos institucionales o confidenciales a GitHub, Kaggle, Colab, OpenML u otros servicios externos. Para adaptar los ejemplos a una pregunta del BCE, primero valida autorización, licenciamiento, clasificación de información, periodo, definiciones y disponibilidad temporal de cada variable.
