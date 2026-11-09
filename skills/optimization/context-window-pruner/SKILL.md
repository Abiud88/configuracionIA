---
name: context-window-pruner
description: Poda y jerarquiza historiales extensos de chat y documentos en sistemas RAG para no saturar la ventana de contexto ni perder atención.
version: 1.0.0
triggers:
  - "el chat se está haciendo muy largo"
  - "resume este historial para la IA"
  - "poda este contexto para que entre en la ventana"
  - "optimiza el contexto del agente"
author: TuNombre
compatibility: "Universal"
---

# Podador de Ventana de Contexto (Context Window Pruner)

## 1. Propósito y Objetivo
Evitar la degradación del rendimiento por saturación de contexto (*Lost in the Middle effect*), condensando historiales conversacionales y grandes bloques de texto recuperados (RAG) en resúmenes operacionales de alta fidelidad.

## 2. Estrategia de Poda y Jerarquización

1. **Estado Actual Inmutable (State of Truth):**
   - Extraer todas las decisiones definitivas tomadas hasta el momento (ej: *Librería elegida: FastAPI*, *Puerto: 8080*).
2. **Tareas Pendientes Activas (Backlog Operativo):**
   - Listar únicamente los elementos por resolver, descartando discusiones intermedias ya resueltas.
3. **Purgado de Intentos Fallidos:**
   - Si se probaron 3 soluciones y fallaron antes de dar con la buena, conservar únicamente la causa por la que fallaron (para evitar reintentarlas) y descartar el código erróneo extenso.
4. **Colocación Estratégica (Recency & Primacy):**
   - Situar las instrucciones permanentes al principio y el objetivo inmediato al final del prompt condensado.

## 3. Formato de Salida

```markdown
### 🧠 Memoria de Contexto Condensada

#### 1. Decisiones Técnicas Confirmadas (Inmutables)
- [Decisión 1]
- [Decisión 2]

#### 2. Variables y Parámetros del Entorno
- Clave: Valor

#### 3. Lo que NO funcionó (Anti-Patrones descartados)
- Evitar X porque produjo error Y.

#### 4. Siguiente Tarea Inmediata
- [Acción exacta a ejecutar por el modelo en el siguiente turno]
```
