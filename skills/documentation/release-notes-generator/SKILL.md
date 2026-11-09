---
name: release-notes-generator
description: Genera notas de lanzamiento (Release Notes) y Changelogs estructurados según el estándar Keep a Changelog y SemVer a partir de commits o diffs.
version: 1.0.0
triggers:
  - "genera las release notes"
  - "crea el changelog"
  - "resumen de esta versión"
  - "keep a changelog"
author: TuNombre
compatibility: "Universal"
---

# Generador de Notas de Lanzamiento (Release Notes Generator)

## 1. Propósito y Objetivo
Convertir una lista desordenada de commits, diffs o tickets de soporte en un `CHANGELOG.md` pulido y profesional, orientado tanto a usuarios finales como a ingenieros.

## 2. Estructura Estándar (Keep a Changelog + SemVer)
Los cambios deben agruparse rígidamente en:
- **🚀 Añadido (Added):** Nuevas funcionalidades disponibles.
- **🔄 Cambiado (Changed):** Modificaciones a funcionalidades existentes.
- **⚠️ Deprecado (Deprecated):** Características que se eliminarán en próximas versiones.
- **🗑️ Eliminado (Removed):** Funcionalidades retiradas definitivamente.
- **🐛 Corregido (Fixed):** Corrección de bugs o fallos de seguridad.
- **🔒 Seguridad (Security):** Parches ante vulnerabilidades.

## 3. Formato de Salida

```markdown
# [Versión X.Y.Z] - AAAA-MM-DD

### 🌟 Destacado de la Versión
Breve párrafo resumiendo el mayor impacto de esta actualización.

### 🚀 Añadido
- Nueva pantalla de configuración de perfil ([#123](url)).

### 🐛 Corregido
- Resuelto timeout al sincronizar bases de datos pesadas ([#145](url)).

### ⚠️ Breaking Changes (si aplica)
- Explicación de qué se rompe y guía de migración en 2 pasos.
```
