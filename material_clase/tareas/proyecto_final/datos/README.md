# Datasets del proyecto final

Escoja **uno** de estos ocho datasets. La variable objetivo y los puntos de cuidado están en el enunciado del proyecto final (PDF).

| Carpeta | Tipo | Archivo(s) | Variable objetivo |
|---|---|---|---|
| R1_california_housing | Regresión | housing.csv | median_house_value |
| R2_indicadores_desarrollo_mundial | Regresión | countries.csv, gdp_economy.csv, population_health.csv, education_technology.csv, environment_energy.csv (unir por country_id y year) | gdp_growth_pct |
| R3_world_happiness | Regresión | 2015.csv a 2019.csv (un archivo por año) | Happiness Score / Score |
| C1_bank_marketing | Clasificación | bank-additional-full.csv (separador `;`) | y |
| C2_credit_card_default | Clasificación | UCI_Credit_Card.csv | default.payment.next.month |
| K1_country_data | Clustering | Country-data.csv, data-dictionary.csv | (sin variable objetivo) |
| K2_wholesale_customers | Clustering | Wholesale customers data.csv | (sin variable objetivo) |
| K3_online_retail | Clustering | data.csv (codificación latin-1) | (sin variable objetivo) |

Ejemplos de carga con pandas:

```python
pd.read_csv("C1_bank_marketing/bank-additional-full.csv", sep=";")
pd.read_csv("K3_online_retail/data.csv", encoding="latin1")
```

Fuentes: Kaggle y UCI Machine Learning Repository. Los datos se usan con fines educativos; no describen al Ecuador.
