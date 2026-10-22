# Datos del Módulo 3

Todos los notebooks leen estos archivos desde disco; no se descarga nada durante la ejecución.

| Archivo | Procedencia | Uso | Filas | Advertencias |
|---|---|---|---|---|
| `actividad_economica_demo.csv` | **Sintético didáctico** | Día 1: exploración y regresión | 289 | Periodos, regiones y sectores simulados; no es información oficial del BCE. |
| `actividad_economica_reto.csv` | **Sintético didáctico** | Día 1: reto de regresión | 193 | Faltantes en `indice_confianza`; `region` y `sector` son categorías. |
| `world_bank_latam_ml.csv` | Banco Mundial, [World Development Indicators](https://databank.worldbank.org/source/world-development-indicators) | Día 2: regresión, Holdout y K-Fold | 140 | Panel anual 2005–2024 de 7 países; 13 inflaciones faltantes. Las filas de un mismo país no son independientes. |
| `BankChurners.csv` | Kaggle, *Credit Card customers* (LEAPS Analyttica) | Días 2, 3, 5 y 6: abandono de la tarjeta | 10 127 | 16 % de abandonos. **Quitar** `CLIENTNUM` y las dos columnas `Naive_Bayes_Classifier_…` (contienen la respuesta). |
| `paysim_muestra.csv` | Kaggle, PaySim (Lopez-Rojas, Elmir y Axelsson, 2016): **simulación** de dinero móvil | Día 3: fraude | 100 198 | Todos los 8 213 fraudes del archivo original y 91 985 transacciones normales al azar. **No usar** las columnas de saldo: delatan la respuesta. |
| `credit_risk_dataset.csv` | Kaggle, *Credit Risk Dataset* | Días 3, 5, 6 y 7: impago | 32 581 | 22 % de impagos. 5 edades > 100, 2 antigüedades > 60 años y 165 duplicados; faltantes en tasa de interés y antigüedad. |
| `CC_GENERAL.csv` | Kaggle, *Credit Card Dataset for Clustering* (Arjun Bhasin) | Días 4 a 7: segmentación, PCA y visualización | 8 950 | 17 variables de comportamiento en 6 meses; 313 faltantes en `MINIMUM_PAYMENTS` y 1 en `CREDIT_LIMIT`. Sin etiquetas. |
| `macro_mensual_demo.csv` | **Sintético didáctico** | Día 7: forecasting | 144 | Meses 2014–2025 de 4 indicadores simulados. No inferir nada sobre la economía real del Ecuador. |

Revisa la licencia de cada fuente antes de reutilizar los datos fuera del curso. Ninguno representa clientes ni estadísticas del Ecuador o del BCE.
