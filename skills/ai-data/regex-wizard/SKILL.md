---
name: regex-wizard
description: Construye, explica y optimiza expresiones regulares (Regex) de alta precisión previniendo vulnerabilidades ReDoS y fallos en casos límite.
version: 1.0.0
triggers:
  - "crea una regex para"
  - "explica esta expresión regular"
  - "valida este formato con regex"
  - "optimiza esta regex"
author: TuNombre
compatibility: "Universal"
---

# Mago de Expresiones Regulares (Regex Wizard)

## 1. Propósito y Objetivo
Diseñar expresiones regulares legibles, precisas y a prueba de bombas, eliminando el riesgo de ataques de denegación de servicio por expresiones regulares (*ReDoS - Catastrophic Backtracking*).

## 2. Pautas de Diseño
- **Prevención de ReDoS:** Evitar cuantificadores anidados sobre grupos ambiguos (ej: `(a+)+` o `([a-zA-Z]+)*`).
- **Anclajes Claros:** Usar `^` y `$` cuando se valide una cadena completa para evitar coincidencias parciales no deseadas.
- **Grupos con Nombre:** Utilizar `(?P<nombre>...)` para mejorar la legibilidad del código consumidor.
- **Flags Explícitas:** Especificar siempre las banderas requeridas (ej: `g` global, `i` case-insensitive, `m` multilínea).

## 3. Formato de Salida

1. **🎯 Patrón Regex:** Expresión regular completa en bloque de código.
2. **📖 Desglose Anatómico:** Explicación token por token de qué hace cada símbolo.
3. **🧪 Casos de Prueba Verificados:**
   - ✅ Coincidencias válidas (deben hacer match).
   - ❌ Coincidencias inválidas (deben fallar o ser rechazadas).
4. **🐍 Ejemplo de Implementación:** Código funcional en Python (`re`), JavaScript (`RegExp`) o el lenguaje solicitado.
