---
name: llm-cache-strategist
description: Estructura prompts y contextos para maximizar el uso de Prompt Caching (Anthropic, Gemini, OpenAI), reduciendo costes hasta un 90%.
version: 1.0.0
triggers:
  - "cómo uso prompt caching"
  - "optimiza mi prompt para caché"
  - "reduce el coste de api con caché"
  - "cache hit para llm"
author: TuNombre
compatibility: "Universal"
---

# Estratega de Caché de Prompts (Prompt Caching Strategist)

## 1. Propósito y Objetivo
Organizar la estructura sintáctica de prompts y peticiones de API para garantizar *Cache Hits* consistentes en proveedores que soportan Context/Prompt Caching (como Google Gemini, Anthropic Claude y OpenAI), logrando ahorros económicos de hasta el 75%-90% y reduciendo la latencia de primer token (TTFT).

## 2. Reglas de Oro para Cache Hits Ininterrumpidos

1. **Orden Canónico Estricto (Estático -> Dinámico):**
   - **Inicio (100% Estático / Cacheable):** Instrucciones del sistema, rol, reglas fijas, documentación base y ejemplos few-shot idénticos.
   - **Final (100% Dinámico / No Cacheable):** Entrada del usuario, marcas de tiempo cambiantes, variables de sesión o preguntas puntuales.
2. **Umbrales Mínimos de Tokens:**
   - La mayoría de motores de caché requieren un bloque estático mínimo (ej: 1024 tokens en Anthropic Claude). Si el contexto estático es menor, la caché no se activa.
3. **Evitar Variabilidad Accidental en el Prefijo:**
   - Nunca incluir fechas u horas del sistema en el System Prompt inicial si cambian por segundo o minuto, ya que invalidan el hash de caché de todo el prefijo.

## 3. Formato de Salida

1. **🧱 Estructura Reorganizada del Prompt:**
   - `[BLOQUE CACHEABLE (Fijo)]` -> Instrucciones, manuales, ejemplos.
   - `[BLOQUE DINÁMICO (Variable)]` -> Pregunta o datos de la petición actual.
2. **⚠️ Errores de Invalidación Detectados:** Elementos en el prompt original que rompían la reutilización de caché.
3. **💰 Estimación de Ahorro Económico:** Reducción esperada en factura mensual si se envían múltiples llamadas consecutivas.
