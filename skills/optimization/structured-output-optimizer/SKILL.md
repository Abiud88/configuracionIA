---
name: structured-output-optimizer
description: Diseña formatos de respuesta estructurados ultra-eficientes (CSV, TSV, JSON compacto) para reducir los costosos tokens de salida.
version: 1.0.0
triggers:
  - "ahorra tokens de salida"
  - "reduce el coste de respuesta"
  - "formato estructurado compacto"
  - "optimiza el json de respuesta"
author: TuNombre
compatibility: "Universal"
---

# Optimizador de Tokens de Salida (Structured Output Optimizer)

## 1. Propósito y Objetivo
Los tokens de salida (*Output Tokens*) suelen costar entre **3 y 5 veces más** que los tokens de entrada y ralentizan el tiempo total de respuesta. Esta habilidad diseña esquemas de respuesta mínimos y libres de verbosidad que devuelven exactamente la información requerida con el menor número de tokens posible.

## 2. Técnicas de Reducción de Tokens de Salida

1. **Claves Cortas vs Claves Descriptivas en JSON:**
   - En lugar de `{"user_identification_number": 1234}`, usar `{"id": 1234}`. En listas de 50 elementos, esto ahorra cientos de tokens.
2. **Formato Tabular / Delimitado vs Objetos Anidados:**
   - Si la salida es una lista homogénea de datos, un formato TSV (delimitado por tabulaciones) o CSV consume entre un 50% y 60% menos tokens que un array de objetos JSON repetitivos.
3. **Prohibición de Preámbulo y Conclusión:**
   - Instrucción estricta: *"Responde ÚNICAMENTE con el bloque de datos crudo. Cero explicaciones previas o posteriores."*
4. **Booleanos y Enums Compactos:**
   - Usar `1`/`0` o flags de una sola letra en lugar de cadenas de texto largas.

## 3. Formato de Salida

1. **📉 Comparativa de Formatos:** Tokens estimados con JSON tradicional vs Formato Optimizado.
2. **📋 Esquema de Salida Recomendado:** Definición exacta que el modelo debe seguir.
3. **🔒 Cláusula de Control de Salida:** Directiva para copiar en el prompt que garantiza que el modelo no genere texto sobrante.
