# Módulo 3 — Machine Learning Aplicado

Material de clase del **Diplomado en Big Data e Inteligencia Artificial** (CEC EPN · Banco Central del Ecuador).

Siete jornadas para aprender Machine Learning **desde cero y con datos económicos y financieros**: regresión, clasificación, clustering, reducción de dimensionalidad, optimización de modelos, automatización y forecasting. Cada tema se explica primero **a mano, con números pequeños**, y después en Python con scikit-learn, paso a paso y con el código comentado.

## Contenido

```
modulo3_ml/
├── notebooks/                 notebooks de cada jornada (ejecutados, con resultados)
├── material_apoyo/
│   ├── presentaciones/        diapositivas de los días 1 a 7 en PDF
│   └── *.png                  imágenes de apoyo de los notebooks
└── datos/                     los 8 datasets que usan los notebooks (ver datos/README.md)
```

## Ruta por jornada

| Día | Notebook | Presentación | Temas | Datos |
|---|---|---|---|---|
| 0 | `00_Dia0_Fundamentos_Python_NumPy_Pandas_Matplotlib` · `00_1_Dia0_Puente_a_Scikit_Learn` | — | Python, NumPy, Pandas y Matplotlib desde cero; el patrón `fit` / `predict` y `train_test_split` | Ejemplos en el propio notebook |
| 1 | `01_Dia1_Datos_y_Regresion` · `01_1_Dia1_Regularizacion_Ridge_Lasso_ElasticNet` | Día 1 | Exploración, limpieza y regresión lineal; regularización Ridge, Lasso y Elastic Net (complementario) | Actividad económica (sintético) |
| 2 | `02_Dia2_Evaluacion_Arboles_Regresion` | Día 2 | Train / Validation / Test, Holdout y K-Fold, sobreajuste, árbol y Random Forest de regresión | Banco Mundial (LATAM), BankChurners |
| 3 | `03_Dia3_Clasificacion_Arboles_RF_KNN_SVM` | Día 3 | Clasificación: Gini, matriz de confusión, Precision, Recall y F1, árbol, Random Forest, KNN, SVM, escalado y balanceo | PaySim, BankChurners, Credit Risk |
| 4 | `04_Dia4_Clustering_Segmentacion_Economica` | Día 4 | Supervisado y no supervisado; K-Means a mano, inercia, Silhouette, clustering jerárquico y dendrograma; asignar clientes nuevos | Clientes de tarjeta (CC GENERAL) |
| 5 | `05_Dia5_PCA_Seleccion_Features` | Día 5 | PCA a mano, varianza explicada y cargas; selección de variables (filtro, envoltura, embebido); ingeniería de características | CC GENERAL, BankChurners, Credit Risk |
| 6 | `06_Dia6_Visualizacion_Optimizacion_y_Reto` | Día 6 | Visualización multidimensional (coordenadas paralelas, PCA, t-SNE); validación cruzada, Grid Search y Random Search; elegir k en clustering | CC GENERAL, Credit Risk, BankChurners |
| 7 | `07_Dia7_Pipelines_Forecasting_Presentacion` | Día 7 | Automatizar con Pipeline y `joblib`; forecasting a un mes con rezagos, líneas base y `TimeSeriesSplit` | Credit Risk, CC GENERAL, serie macro mensual (sintética) |

### Cómo está organizado cada notebook (días 3 a 7)

Todos siguen los mismos pasos, para que el procedimiento se vuelva costumbre:

1. **Mirar los datos** (`head`, tipos y resumen) y **graficarlos**.
2. **Limpiar y preparar paso a paso**: faltantes, fugas, logaritmo, escalado, codificación y balanceo, con el antes y el después.
3. **Línea base**: la regla más simple que un modelo debe superar.
4. **El método a mano**, con números pequeños.
5. **Modelo simple con scikit-learn**, en pocas líneas comentadas.
6. **Métricas a mano y con scikit-learn**, siempre **Train frente a Validation**.
7. **Hiperparámetros explicados uno por uno** y combinaciones probadas con `for`.
8. **Resultado final**, con Test una sola vez.
9. **Comparación final**: todos los modelos en todos los datasets, para ver cómo se escoge el mejor en cada caso.

## Preparación y ejecución

1. Instala **Python 3.10 o posterior** con Jupyter (por ejemplo, con Anaconda).
2. Si hacen falta, instala: `numpy`, `pandas`, `matplotlib`, `scikit-learn`, `scipy` y `joblib`.
3. Abre la carpeta `modulo3_ml` en Jupyter y ejecuta cada notebook **en orden, de arriba hacia abajo**. Las rutas encuentran `datos/` tanto desde la raíz como desde `notebooks/`.

Los notebooks no descargan nada: todos los datos están en `datos/`. Tiempos aproximados de ejecución completa: Día 3 ≈ 5 min, Día 5 ≈ 4 min, Día 6 ≈ 5 min, los demás menos de 1 min. El Día 7 crea la carpeta `notebooks/resultados_dia7` con el modelo guardado y un informe de ejemplo.

## Datos

| Archivo | Fuente | Se usa en |
|---|---|---|
| `actividad_economica_demo.csv`, `actividad_economica_reto.csv` | Sintéticos didácticos | Día 1 |
| `world_bank_latam_ml.csv` | Banco Mundial, World Development Indicators | Día 2 |
| `BankChurners.csv` | Kaggle, *Credit Card customers* | Días 2, 3, 5 y 6 |
| `paysim_muestra.csv` | Kaggle, PaySim (sintético) | Día 3 |
| `credit_risk_dataset.csv` | Kaggle, *Credit Risk Dataset* | Días 3, 5, 6 y 7 |
| `CC_GENERAL.csv` | Kaggle, *Credit Card Dataset for Clustering* | Días 4, 5, 6 y 7 |
| `macro_mensual_demo.csv` | Sintético didáctico | Día 7 |

Procedencia, columnas y advertencias de cada archivo en [`datos/README.md`](datos/README.md). Ningún dataset describe clientes ni estadísticas del Ecuador o del BCE; los sintéticos sirven solo para practicar el procedimiento.

## Bibliografía

- James, G. et al. (2023). *An Introduction to Statistical Learning*. <https://www.statlearning.com>
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O'Reilly.
- Hastie, T., Tibshirani, R. y Friedman, J. (2021). *The Elements of Statistical Learning*. <https://hastie.su.domains/ElemStatLearn/>
- Hyndman, R. y Athanasopoulos, G. (2021). *Forecasting: Principles and Practice*. <https://otexts.com/fpp3/>

## Uso responsable

No subas datos institucionales ni confidenciales a GitHub, Kaggle, Colab u otros servicios externos. Una agrupación es exploratoria, una importancia es predictiva y una correlación no prueba causalidad.

---
Docente: Jonathan Rosero Soto
