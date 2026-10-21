# Datos para el trabajo en clase

Tres datasets, uno por tipo de problema. Cada problema tiene **un solo archivo CSV** (UTF-8, separado por comas, con encabezados). Todas las fuentes figuran en el catálogo Awesome Public Datasets (https://github.com/awesomedata/awesome-public-datasets), directamente o a través del repositorio UCI que el catálogo recopila. Descargados el 21 de octubre de 2026.

| Problema | Archivo | Filas × columnas | Variable objetivo |
|---|---|---|---|
| Regresión | `regresion_uk_supermarket_prices.csv` | 5 722 × 30 | `price` (precio en libras) |
| Clasificación | `clasificacion_banknote_authentication.csv` | 1 372 × 5 | `class` (0 = auténtico, 1 = falsificado) |
| Clustering | `clustering_undp_desarrollo_humano.csv` | 206 × 1 112 | Ninguna (no supervisado) |

---

## 1. Regresión: UK Supermarket Prices (Daily 212-Item Basket)

- **Fuente:** Kaggle, Russell Yapp (Yappman Data). https://www.kaggle.com/datasets/russellyapp/uk-supermarket-prices-daily-212-item-basket
- **Licencia:** CC BY 4.0. Citar como "Yappman Data, UK Supermarket Prices: Daily 212-Item Basket, Kaggle".
- **Qué es:** una canasta fija de 212 productos básicos, con su precio en línea cada día en Tesco, Sainsbury's, Asda y Aldi. Una fila = un producto en una cadena en un día.
- **Cómo se armó el archivo:** la copia de Kaggle es una foto del 24-sep al 8-oct-2026 (2 966 filas, 14 días). El autor publica el mismo dataset actualizado a diario, con las mismas 30 columnas, en Apify (https://api.apify.com/v2/datasets/ynAT9NPps2EdjMOJa/items?format=csv). Se unieron ambos y se quitaron duplicados por cadena + producto + fecha. Las 2 966 filas de Kaggle están todas incluidas. Resultado: **27 días, del 24-sep al 21-oct-2026**.
- **Notas:**
  - No hay registro del 25-sep.
  - El 29 y 30-sep tienen 211 filas, porque faltó un producto de Asda.
  - `price` no tiene faltantes (de 0,11 a 12,29 libras; mediana 1,85).
  - Faltantes: `loyaltyPrice` (precio con tarjeta de fidelidad, solo Tesco y Sainsbury's) y `wasPrice` (precio anterior a una promoción) están casi siempre vacíos. A `packSize` le faltan 668 valores y a `unitPrice/value`, 225.
  - Aldi no publica códigos EAN; sus productos se identifican por `matchKey`.
- **Columnas principales:** `retailer` (cadena), `name`, `brand`, `packSize`, `price`, `loyaltyPrice`, `wasPrice`, `promotionText`, `unitPrice/value` y `unitPrice/measure` (precio por unidad de medida), `inStock`, `categoryPath/0` a `/3` (categoría de la cadena), `ean/0` a `/4`, `rating/value`, `rating/count`, `scrapedAt` (fecha y hora de captura), `url`, `imageUrl`.

## 2. Clasificación: Banknote Authentication

- **Fuente:** UCI Machine Learning Repository, id 267. https://archive.ics.uci.edu/dataset/267/banknote+authentication
- **Licencia:** CC BY 4.0. Donado en 2013 por Volker Lohweg (Universidad de Ciencias Aplicadas de Ostwestfalen-Lippe).
- **Qué es:** cuatro medidas extraídas, con la transformada wavelet, de imágenes de 400×400 píxeles de billetes auténticos y falsificados.
- **Cómo se armó el archivo:** el original es un único `.txt` sin encabezados. Se agregaron los nombres de columna oficiales y se guardó como CSV.
- **Columnas:** `variance`, `skewness` (asimetría), `curtosis`, `entropy`, `class`.
- **Notas:**
  - Está completo: 1 372 filas sin faltantes.
  - Clases: 762 auténticos (0) y 610 falsificados (1).
  - Hay 24 filas duplicadas exactas; se dejaron como vienen en la fuente.

## 3. Clustering: UN Human Development Reports (UNDP)

- **Fuente:** PNUD, Informe sobre Desarrollo Humano 2025, archivo "Composite indices complete time series". https://hdr.undp.org/data-center/documentation-and-downloads
- **Cita recomendada:** UNDP (United Nations Development Programme). 2025. Human Development Report 2025.
- **Qué es:** indicadores de desarrollo humano por país, de 1990 a 2023, en formato ancho: una fila por país y una columna por indicador y año (por ejemplo, `hdi_2023`, `le_2023`).
- **Cómo se armó el archivo:** el original ya es un solo CSV. Se convirtió de Latin-1 a UTF-8 para que nombres como "Côte d'Ivoire" se lean bien en pandas.
- **Filas:** 195 países y territorios, más **11 filas de agregados** (cuatro grupos de desarrollo, seis regiones y World). Los agregados tienen un `iso3` que empieza con `ZZ` y hay que **quitarlos antes de agrupar**:

  ```python
  df[~df.iso3.str.startswith("ZZ")]
  ```

- **Faltantes en 2023:**
  - `hdi`, `mys`, `gnipc` y `co2_prod`: 2 países sin dato cada uno.
  - `gii`: 23 países sin dato.
  - `le`, `eys` y `pop_total`: completos.
  - En años antiguos faltan más valores.

**Diccionario** (prefijo de columna → significado; el sufijo `_AAAA` es el año):

| Prefijo | Indicador | Años |
|---|---|---|
| `iso3`, `country`, `hdicode`, `region` | Código, país, grupo de desarrollo (Very High/High/Medium/Low), región PNUD | — |
| `hdi_rank` | Posición en el IDH | 2023 |
| `hdi` | Índice de Desarrollo Humano | 1990-2023 |
| `le` | Esperanza de vida al nacer (años) | 1990-2023 |
| `eys` | Años esperados de escolaridad | 1990-2023 |
| `mys` | Años promedio de escolaridad | 1990-2023 |
| `gnipc` | Ingreso nacional bruto per cápita (PPA 2021, USD) | 1990-2023 |
| `gdi`, `gdi_group` | Índice de Desarrollo de Género y su grupo | 1990-2023 / 2023 |
| `hdi_f`, `le_f`, `eys_f`, `mys_f`, `gni_pc_f` | Lo mismo para mujeres | 1990-2023 |
| `hdi_m`, `le_m`, `eys_m`, `mys_m`, `gni_pc_m` | Lo mismo para hombres | 1990-2023 |
| `ihdi`, `coef_ineq`, `loss` | IDH ajustado por desigualdad, coeficiente de desigualdad, pérdida (%) | 2010-2023 |
| `ineq_le`, `ineq_edu`, `ineq_inc` | Desigualdad en esperanza de vida, educación e ingreso | 2010-2023 |
| `gii`, `gii_rank` | Índice de Desigualdad de Género y su posición | 1990-2023 / 2023 |
| `mmr` | Mortalidad materna (por 100 000 nacidos vivos) | 1990-2023 |
| `abr` | Natalidad adolescente (por 1 000 mujeres de 15-19 años) | 1990-2023 |
| `se_f`, `se_m` | Población con al menos algo de secundaria (% de 25 años o más), mujeres y hombres | 1990-2023 |
| `pr_f`, `pr_m` | Escaños en el parlamento (%), mujeres y hombres | 1990-2023 |
| `lfpr_f`, `lfpr_m` | Participación en la fuerza laboral (% de 15 años o más), mujeres y hombres | 1990-2023 |
| `phdi`, `diff_hdi_phdi`, `rankdiff_hdi_phdi` | IDH ajustado por presiones planetarias y su diferencia con el IDH | 1990-2023 |
| `co2_prod` | Emisiones de CO₂ per cápita (toneladas) | 1990-2023 |
| `mf` | Huella material per cápita (toneladas) | 1990-2023 |
| `pop_total` | Población total (millones) | 1990-2023 |

Sugerencia para clustering: usar un solo año, por ejemplo 2023, con columnas como `le_2023`, `eys_2023`, `mys_2023`, `gnipc_2023`, `gii_2023`, `co2_prod_2023`, `abr_2023` y `lfpr_f_2023`. Conviene aplicar logaritmo a `gnipc` y `co2_prod`, que son muy asimétricos, y luego escalar.
