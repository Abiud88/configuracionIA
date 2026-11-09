---
name: model-router-cascade
description: Diseña estrategias de enrutamiento y cascada de modelos (LLM Routing) asignando la tarea al modelo más económico y rápido según su dificultad.
version: 1.0.0
triggers:
  - "qué modelo debo usar para esto"
  - "enruta esta tarea entre modelos"
  - "cascada de modelos"
  - "ahorra costes eligiendo modelo"
author: TuNombre
compatibility: "Universal"
---

# Enrutador y Cascada de Modelos (Model Router & Cascade)

## 1. Propósito y Objetivo
Evitar utilizar modelos frontera masivos y costosos (como Claude 3.5 Sonnet, GPT-4o o Gemini 1.5 Pro) para tareas rutinarias o triviales. Esta habilidad define un árbol de decisión para enviar cada consulta al modelo óptimo en coste/latencia/calidad.

## 2. Niveles de Enrutamiento (Tiers)

- **Tier 1: Modelos Ultraligeros / Locales (Coste mínimo o cero):**
  - *Ejemplos:* Gemini 1.5 Flash / Flash-8B, GPT-4o-mini, Claude 3.5 Haiku, Llama 3.2 (local en Ollama).
  - *Tareas:* Clasificación de texto, extracción simple de entidades, formateo de datos, resúmenes breves, filtrado de spam.
- **Tier 2: Modelos de Capacidad Media / Balanceados:**
  - *Ejemplos:* Gemini 1.5 Flash / Pro, Qwen 2.5 Coder 32B, DeepSeek-V3.
  - *Tareas:* Programación estándar, redacción de tests, explicación de código, traducción de documentos medianos.
- **Tier 3: Modelos Frontera / Razonamiento Profundo:**
  - *Ejemplos:* Claude 3.7 Sonnet / Opus, OpenAI o1 / o3-mini, Gemini Pro con Deep Thought.
  - *Tareas:* Arquitectura de sistemas complejos, depuración de bugs con trazas confusas, demostraciones matemáticas, auditorías críticas de seguridad.

## 3. Patrón de Cascada con Fallback
1. Enviar la consulta al **Tier 1**.
2. Evaluar mediante un validador rápido (heurística, regex o schema JSON) si la respuesta es válida y completa.
3. Si la respuesta falla o la confianza es baja, escalar automáticamente al **Tier 2** o **Tier 3**.

## 4. Formato de Salida

1. **🎯 Modelo Recomendado:** Asignación directa con justificación económica.
2. **💰 Comparativa de Costes Estimada:** Diferencia de precio por millón de tokens.
3. **🔄 Regla de Fallback:** En qué caso específico debería transferirse la tarea a un modelo superior.
