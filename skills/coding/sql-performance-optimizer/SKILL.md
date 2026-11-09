---
name: sql-performance-optimizer
description: Analiza, reescribe y optimiza consultas SQL complejas para reducir tiempos de respuesta, uso de memoria y bloqueos de tablas.
version: 1.0.0
triggers:
  - "optimiza esta consulta sql"
  - "esta query es lenta"
  - "analiza este explain plan"
  - "mejora los indices de esta tabla"
author: TuNombre
compatibility: "Universal"
---

# Optimizador de Rendimiento SQL (SQL Performance Optimizer)

## 1. Propósito y Objetivo
Transformar consultas SQL ineficientes en queries de alto rendimiento, evitando escaneos secuenciales masivos (*Sequential/Table Scans*), bloqueos y consumo excesivo de CPU y RAM.

## 2. Puntos de Auditoría Obligatorios
- **Eliminación de `SELECT *`:** Seleccionar únicamente las columnas necesarias para aprovechar index-only scans.
- **Sargabilidad de filtros (`WHERE`):** Evitar funciones envolventes sobre columnas indexadas (ej: `WHERE YEAR(created_at) = 2024` -> `WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01'`).
- **Problema N+1 y Joins:** Reemplazar subconsultas correlacionadas por `JOIN` o Window Functions (`ROW_NUMBER()`, `DENSE_RANK()`).
- **Estrategia de Índices:** Recomendar índices compuestos `(col1, col2)` en el orden correcto de selectividad.

## 3. Formato de Salida

1. **⚠️ Diagnóstico del Cuello de Botella:** Qué hacía ineficiente a la consulta original.
2. **🚀 Consulta Optimizada:** SQL limpio, formateado con palabras clave en mayúsculas y comentarios puntuales.
3. **📌 Índices Recomendados:** Sentencias `CREATE INDEX ...` necesarias para máxima velocidad.
4. **📊 Comparativa Teórica de Coste:** Reducción esperada en lecturas de disco e I/O.
