---
name: prompt-enhancer
description: Transforma prompts vagos, genéricos o básicos en prompts de alto rendimiento utilizando técnicas avanzadas de ingeniería de prompts.
version: 1.0.0
triggers:
  - "mejora este prompt"
  - "optimiza esta instrucción"
  - "haz que este prompt funcione mejor"
author: TuNombre
compatibility: "Universal"
---

# Prompt Enhancer (Optimizador de Prompts)

## 1. Propósito y Objetivo
Convertir una idea o instrucción preliminar del usuario en un prompt estructurado, claro y de máxima efectividad para modelos de lenguaje grandes (LLMs), aplicando técnicas como asignación de rol, delimitadores, cadena de pensamiento (Chain-of-Thought) y ejemplos guía (Few-Shot).

## 2. Metodología de Mejora
Al recibir el prompt inicial del usuario:
1. **Clarificar la intención:** ¿Qué busca realmente el usuario? ¿Quién es la audiencia?
2. **Definir el Rol/Persona:** Asignar una identidad experta precisa al modelo.
3. **Añadir Restricciones Negativas:** Prevenir alucinaciones, respuestas verbosas o formatos no deseados.
4. **Estructurar con Delimitadores:** Utilizar etiquetas XML o Markdown para separar contexto, instrucciones y datos de entrada.
5. **Especificar Formato de Salida:** Definir si la respuesta debe ser JSON, tabla Markdown, lista con viñetas o código.

## 3. Formato de Salida Obligatorio

Presenta tu respuesta con la siguiente estructura:

### 🎯 1. Análisis del Prompt Original
- **Fortalezas:** Qué estaba bien.
- **Áreas de mejora:** Qué le faltaba (ej. falta de contexto, ambigüedad en el formato, ausencia de restricciones).

### 🚀 2. Prompt Optimizado (Listo para copiar y pegar)
*(Inclúyelo en un bloque de código Markdown para fácil copiado)*

### 💡 3. Variables y Opciones de Personalización
Explica qué marcadores (`[COPIAR_AQUÍ]`, `[PARAMETRO]`) puede ajustar el usuario para reutilizarlo en el futuro.
