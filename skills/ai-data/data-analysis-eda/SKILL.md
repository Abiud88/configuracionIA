---
name: data-analysis-eda
description: Guía un Análisis Exploratorio de Datos (EDA) completo en Python (Pandas/Polars) con detección de anomalías, estadísticas y visualizaciones.
version: 1.0.0
triggers:
  - "analiza este dataset"
  - "haz un análisis exploratorio"
  - "eda con pandas"
  - "limpia estos datos"
author: TuNombre
compatibility: "Universal"
---

# Análisis Exploratorio de Datos (Data Analysis & EDA)

## 1. Propósito y Objetivo
Examinar conjuntos de datos tabulares, descubrir patrones subyacentes, detectar valores atípicos (outliers), datos nulos y formular hipótesis para modelos predictivos o toma de decisiones de negocio.

## 2. Flujo de Trabajo Metódico
1. **Inspección Inicial de Calidad:**
   - Dimensiones (`shape`), tipos de datos (`dtypes`) y memoria utilizada.
   - Conteo y porcentaje de valores ausentes (`nulls`/`NaN`).
   - Cardinalidad de variables categóricas.
2. **Estadística Descriptiva:**
   - Medidas de tendencia central y dispersión (media, mediana, desviación estándar, rango intercuartílico).
   - Asimetría (*skewness*) y curtosis de distribuciones continuas.
3. **Detección de Anomalías:**
   - Identificación de outliers mediante método IQR o Z-score.
4. **Análisis Bivariado y Correlaciones:**
   - Matriz de correlación de Pearson/Spearman y relaciones causa-efecto potenciales.

## 3. Formato de Salida

1. **📊 Diagnóstico de Salud del Dataset:** Resumen de problemas de calidad detectados (nulos, duplicados, inconsistencias).
2. **🐍 Script de Python Ejecutable:** Código limpio con `pandas` o `polars` y gráficos recomendados con `seaborn` o `matplotlib`.
3. **💡 Hallazgos Principales (Insights):** Las 3 conclusiones más relevantes extraídas de los datos.
4. **🚀 Recomendaciones de Limpieza e Ingeniería de Características:** Siguientes pasos para preparar los datos.
