---
name: decision-matrix-analyzer
description: Evalúa opciones técnicas o estratégicas usando matrices de decisión ponderadas, análisis de tradeoffs y evaluación de riesgos.
version: 1.0.0
triggers:
  - "ayúdame a decidir entre"
  - "compara estas opciones"
  - "matriz de decisión"
  - "evalúa pros y contras técnicos"
author: TuNombre
compatibility: "Universal"
---

# Analizador de Matriz de Decisión (Decision Matrix Analyzer)

## 1. Propósito y Objetivo
Resolver dilemas técnicos (ej: PostgreSQL vs MongoDB, Next.js vs Vite/React, AWS vs GCP) mediante criterios objetivos, ponderaciones numéricas y análisis de compromiso (tradeoffs).

## 2. Metodología Paso a Paso
1. **Definir Criterios Clave:** Identificar entre 4 y 6 dimensiones críticas (ej: Coste, Rendimiento, Curva de Aprendizaje, Mantenimiento, Escalabilidad).
2. **Ponderación:** Asignar un peso relativo del 1 al 5 a cada criterio según el contexto del usuario.
3. **Puntuación:** Calificar cada alternativa del 1 al 10 en cada criterio con justificación técnica explícita.
4. **Cálculo de Puntuación Ponderada:** Mostrar totales numéricos para eliminar sesgos.
5. **Recomendación Final Condicionada:** Explicar cuándo elegir la alternativa ganadora y bajo qué circunstancias excepcionales elegir la alternativa perdedora.

## 3. Formato de Salida

### 📊 1. Matriz Ponderada
| Criterio | Peso (1-5) | Opción A (Pts / Total) | Opción B (Pts / Total) |
| :--- | :--- | :--- | :--- |
| Rendimiento | 5 | 8 / 40 | 6 / 30 |
| Coste infra | 4 | 7 / 28 | 9 / 36 |
| **Total Ponderado** | | **XX** | **YY** |

### ⚖️ 2. Tradeoffs Fundamentales
- Lo que ganas con Opción A vs lo que sacrificas.
- Lo que ganas con Opción B vs lo que sacrificas.

### 🏆 3. Veredicto y Recomendación
Recomendación clara en una sola frase, acompañada de la regla de decisión (ej: *"Elige A si tu equipo ya domina X; elige B si el tiempo de salida al mercado es la prioridad número uno"*).
