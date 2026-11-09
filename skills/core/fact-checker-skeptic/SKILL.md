---
name: fact-checker-skeptic
description: Audita rigurosamente afirmaciones, datos técnicos, versiones de librerías y estadísticas para erradicar alucinaciones.
version: 1.0.0
triggers:
  - "verifica estos datos"
  - "audita este texto para evitar alucinaciones"
  - "comprueba si esto es cierto"
  - "fact check"
author: TuNombre
compatibility: "Universal"
---

# Verificador Escéptico y Anti-Alucinaciones (Fact-Checker Skeptic)

## 1. Propósito y Objetivo
Eliminar afirmaciones dudosas, referencias inexistentes, métodos deprecados o inventados en librerías y datos numéricos inexactos antes de que lleguen al usuario final.

## 2. Escala de Certeza Epistémica
Cada afirmación auditada debe recibir una etiqueta inequívoca:
- 🟢 **[HECHO VERIFICADO]**: Comprobado empíricamente o respaldado por documentación oficial estable.
- 🟡 **[PROBABLE / CONDICIONAL]**: Válido bajo ciertas versiones, contextos o supuestos que deben especificarse.
- 🔴 **[NO VERIFICABLE / POTENCIAL ALUCINACIÓN]**: No existe evidencia en la documentación oficial, nombre inventado de función o dato no contrastado.

## 3. Instrucciones de Auditoría
1. Extraer todas las afirmaciones factuales, nombres de paquetes, endpoints o métodos invocados.
2. Comprobar firmas de funciones y compatibilidad con versiones específicas.
3. Si un dato no puede ser corroborado con total certeza, el modelo **debe admitir el límite de su conocimiento** en vez de aproximar.

## 4. Formato de Salida

### 📋 Reporte de Verificación
| Afirmación / Elemento | Nivel de Certeza | Observaciones / Fuente oficial |
| :--- | :--- | :--- |
| `ejemplo_metodo()` | 🟢 Hecho Verificado | Presente en v3.10+ |
| `libreria_fantasma` | 🔴 Alucinación | No existe en PyPI/npm. Usar alternativa `X` |

### 🛠️ Versión Corregida
Texto o código con todas las correcciones integradas, eliminando ambigüedades.
