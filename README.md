# Módulo 3 — Machine Learning Aplicado

Material preparado para CEC EPN / Banco Central del Ecuador.

## Filosofía de esta versión

Los notebooks son **material de estudio**, no scripts de demostración. Cada jornada sigue: problema → entender datos → teoría → código comentado → interpretación del resultado → diagnóstico → preguntas.

No existe instalación automática de librerías. Cada notebook inicia con un único bloque de imports y, cuando hay paquetes opcionales, se indica manualmente qué `%pip install ...` ejecutar si fuera necesario.

## Orden

1. `01_Dia1_Datos_y_Regresion.ipynb`: NumPy/Pandas/Matplotlib, EDA, regresión simple y múltiple, métricas, Train/Val/Test, categorías, causalidad.
2. `02_Dia2_Evaluacion_Overfitting_Arboles.ipynb`: Ridge, Lasso, Elastic Net, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting, XGBoost, LightGBM, CatBoost.
3. `03_Dia3_SVM_KNN_Metricas_KMeans.ipynb`: clasificación, Logistic baseline, métricas, KNN, SVM, ROC/PR, transición a K-Means.
4. `04_Dia4_Clustering_Segmentacion_Economica.ipynb`: K-Means, Elbow, Silhouette, perfiles, clustering jerárquico y estabilidad.
5. `05_Dia5_PCA_Seleccion_Features.ipynb`: PCA, varianza explicada, loadings, selección, p-values, VIF, feature engineering.
6. `06_Dia6_Visualizacion_Optimizacion_y_Reto.ipynb`: hiperparámetros, Grid/Randomized Search, Kaggle/OpenML y diseño del proyecto.
7. `07_Dia7_Pipelines_Forecasting_Presentacion.ipynb`: pipelines, forecasting, lags, split temporal, baselines, Test y comunicación.

## Datos

Los datasets `*_fallback.csv` y `*_demo.csv` son **SINTÉTICOS DIDÁCTICOS** salvo que se indique una fuente pública real. Nunca deben confundirse con estadísticas oficiales.

`actividad_economica_reto.csv` es un segundo dataset incluido para el reto del Día 1.

## Seguridad

No subir datos institucionales/confidenciales a Kaggle, Colab, OpenML u otros servicios externos.
