---
name: systematic-debugger
description: Guía un proceso metódico de depuración científica basado en formulación de hipótesis, aislamiento del fallo y análisis de causa raíz.
version: 1.0.0
triggers:
  - "depura este error"
  - "tengo este bug"
  - "por qué falla esto"
  - "analiza este stack trace"
author: TuNombre
compatibility: "Universal"
---

# Depurador Sistemático (Systematic Debugger)

## 1. Propósito y Objetivo
Eliminar el método de "prueba y error al azar". Esta habilidad aplica el método científico para encontrar la causa raíz (*root cause*) de bugs y excepciones de software, garantizando que la solución no introduzca efectos secundarios.

## 2. Protocolo de Depuración en 4 Etapas

### Fase 1: Comprensión del Síntoma
- Analizar el mensaje exacto de error y el stack trace.
- Diferenciar el **síntoma visible** (ej: `NullPointerException`) de la **causa raíz** (ej: variable de entorno no inyectada en tiempo de arranque).

### Fase 2: Formulación de Hipótesis
- Plantear 2 o 3 hipótesis técnicas ordenadas de mayor a menor probabilidad.

### Fase 3: Aislamiento y Reproducción
- Diseñar el caso de prueba o la verificación mínima reproducible que confirme o refute cada hipótesis.

### Fase 4: Solución Quirúrgica
- Aplicar la corrección mínima necesaria sin alterar código circundante innecesario.

## 3. Formato de Salida Obligatorio

1. **🚨 Diagnóstico del Síntoma:** Qué falló y en qué línea exacta.
2. **🔬 Causa Raíz Real:** Por qué ocurrió la falla en el flujo de ejecución.
3. **💡 Solución Quirúrgica:** Código corregido con comentarios explícitos sobre la línea modificada.
4. **🛡️ Medida Preventiva:** Cómo blindar el código para que este fallo sea imposible de repetir (ej: validación de tipos, aserciones, tests).
