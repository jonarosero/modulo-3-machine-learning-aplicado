# Catálogo de datos para el Módulo 3

Todos los archivos se leen desde disco; las jornadas 3–7 no consultan APIs, Kaggle, UCI ni OpenML durante la ejecución. Conserva este catálogo junto a los CSV para atribución, contexto y límites de uso.

| Archivo | Procedencia / tipo | Uso didáctico | Unidad y advertencias |
|---|---|---|---|
| `bank_marketing_uci.csv` | UCI Machine Learning Repository, Bank Marketing, variante `bank-additional-full`; datos públicos. Fuente: <https://archive.ics.uci.edu/dataset/222/bank+marketing>. | Clasificación, métricas, KNN y SVM (Día 3). | 41 188 contactos de campañas de un banco portugués, 20 variables predictoras y target `y`. La duración `duration` se excluye para demostrar predicción previa a la llamada (evitar leakage). No representa clientes del Ecuador ni del BCE. Respetar atribución y términos indicados por UCI.
| `world_bank_latam_ml.csv` | Indicadores de World Development Indicators del Banco Mundial, descargados previamente y guardados en CSV. Fuente: <https://databank.worldbank.org/source/world-development-indicators>. | Segmentación país-año (Día 4); PCA/selección (Día 5); visualización y optimización (Día 6). | Panel anual 2005–2024 para Argentina, Brasil, Chile, Colombia, Ecuador, México y Perú. Puede contener faltantes, cambios metodológicos y revisiones. Las observaciones país-año de un mismo país no son independientes. La tabla local, no una consulta en vivo, determina la muestra de cada ejecución.
| `macro_mensual_demo.csv` | Serie **sintética didáctica** incluida en el proyecto; no es descarga ni estadística oficial. | Lags, baselines temporales, split cronológico y pipeline (Día 7). | 144 observaciones mensuales simuladas. No inferir niveles, tendencias ni relaciones reales sobre Ecuador; sirve solo para practicar el procedimiento.
| `actividad_economica_demo.csv` | **Sintético didáctico** incluido en el proyecto. | Ejercicios exploratorios y de regresión del Día 1. | Filas simuladas de periodos, sectores y regiones; no representa actividad observada por el BCE.
| `actividad_economica_reto.csv` | **Sintético didáctico** incluido en el proyecto. | Reto de regresión del Día 1 y alternativas para proyecto de práctica. | No es información oficial ni registro administrativo.
| `latam_indicadores_fallback.csv`, `*_fallback.csv`, `*_demo.csv` | Archivos auxiliares, principalmente sintéticos didácticos; verificar `tipo_dato` y descripción antes de usar. | Respaldo de notebooks previos y ejercicios de clase. | No presentar como estadística oficial.

## Uso responsable

- Mantén los CSV junto con el repositorio y no los reemplaces silenciosamente: fecha de corte y fuente afectan resultados.
- Para un análisis aplicado, valida licencia, definiciones, revisiones, periodos comparables y autorización de uso.
- No incorporar datos confidenciales/institucionales en repositorios o servicios externos.
- Una agrupación es exploratoria, una importancia es predictiva y una correlación no establece causalidad.
