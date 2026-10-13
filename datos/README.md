# Catálogo de datos para el Módulo 3

Todos los archivos se leen desde disco; las jornadas 3–7 no consultan APIs, Kaggle, UCI ni OpenML durante la ejecución. Conserva este catálogo junto a los CSV para atribución, contexto y límites de uso.

| Archivo | Procedencia / tipo | Uso didáctico | Unidad y advertencias |
|---|---|---|---|
| `bank_marketing_uci.csv` | UCI Machine Learning Repository, Bank Marketing, variante `bank-additional-full`; datos públicos. Fuente: <https://archive.ics.uci.edu/dataset/222/bank+marketing>. | Clasificación, métricas, árbol, bosque, KNN y SVM (Día 3); opción B del proyecto. | 41 188 contactos de campañas de un banco portugués, 20 variables predictoras y target `y`. La duración `duration` se excluye para demostrar predicción previa a la llamada (evitar fuga de información). No representa clientes del Ecuador ni del BCE. Respetar atribución y términos indicados por UCI.
| `world_bank_latam_ml.csv` | Indicadores de World Development Indicators del Banco Mundial, descargados previamente y guardados en CSV. Fuente: <https://databank.worldbank.org/source/world-development-indicators>. | Regresión y comparación Holdout/K-Fold (Día 2); segmentación país-año (Día 4, opción D del proyecto); PCA/selección (Día 5); visualización y optimización (Día 6). | Panel anual 2005–2024 para Argentina, Brasil, Chile, Colombia, Ecuador, México y Perú. 140 filas, 13 inflaciones ausentes. Puede contener cambios metodológicos y revisiones. Las observaciones país-año de un mismo país no son independientes. La tabla local, no una consulta en vivo, determina la muestra de cada ejecución.
| `macro_mensual_demo.csv` | Serie **sintética didáctica** incluida en el proyecto; no es descarga ni estadística oficial. | Rezagos, baselines temporales, split cronológico y pipeline (Día 7; opción E del proyecto). | 144 observaciones mensuales simuladas. No inferir niveles, tendencias ni relaciones reales sobre Ecuador; sirve solo para practicar el procedimiento.
| `actividad_economica_demo.csv` | **Sintético didáctico** incluido en el proyecto. | Ejercicios exploratorios y de regresión del Día 1. | Filas simuladas de periodos, sectores y regiones; no representa actividad observada por el BCE.
| `actividad_economica_reto.csv` | **Sintético didáctico** incluido en el proyecto. | Reto de regresión del Día 1; opción A del proyecto integrador (193 registros fecha–región–sector). | Objetivo `crecimiento_actividad_pct`, faltantes en `indice_confianza`; `region` y `sector` son categorías. No es información oficial ni registro administrativo.
| `telco_churn_fallback.csv` | **Sintético didáctico** (`tipo_dato=SINTETICO_DIDACTICO`); respaldo local, no datos de una operadora real. | Opción C del proyecto: clasificación de abandono `Churn=Yes/No` sobre 4 500 clientes simulados. | `customerID` es un identificador; `Contract`, `InternetService` y `PaperlessBilling` son categorías a codificar después de dividir. `tipo_dato` documenta el carácter sintético, no es predictor.
| `latam_indicadores_fallback.csv`, `*_fallback.csv`, `*_demo.csv` | Archivos auxiliares, principalmente sintéticos didácticos; verificar `tipo_dato` y descripción antes de usar. | Respaldo de notebooks previos y ejercicios de clase. | No presentar como estadística oficial.

## Uso responsable

- Mantén los CSV junto con el repositorio y no los reemplaces silenciosamente: fecha de corte y fuente afectan resultados.
- Para un análisis aplicado, valida licencia, definiciones, revisiones, periodos comparables y autorización de uso.
- No incorporar datos confidenciales/institucionales en repositorios o servicios externos.
- Una agrupación es exploratoria, una importancia es predictiva y una correlación no establece causalidad.

## Cinco opciones locales para el proyecto

El enunciado completo y las etapas de limpieza, gráficos, particiones y codificación están en `notebooks/04_Dia4_Clustering_Segmentacion_Economica.ipynb`. Las opciones independientes son: A `actividad_economica_reto.csv` (regresión), B `bank_marketing_uci.csv` (clasificación), C `telco_churn_fallback.csv` (clasificación), D `world_bank_latam_ml.csv` (clustering país-año) y E `macro_mensual_demo.csv` (regresión temporal). Antes de elegir modelo, justificar el tipo de problema según la **respuesta buscada**; identificar categorías de entrada temprano, pero ajustar One-Hot/imputación/escalado **solo en Train** tras dividir. En clustering, las tres particiones sirven para estudiar estabilidad/perfiles sin fingir que hay etiquetas reales para Accuracy.
