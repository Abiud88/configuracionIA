---
name: git-workflow-master
description: Escribe commits semánticos profesionales (Conventional Commits), redacta Pull Requests estructuradas y resuelve conflictos de Git.
version: 1.0.0
triggers:
  - "mensaje de commit para"
  - "redacta esta pull request"
  - "cómo resuelvo este conflicto de git"
  - "conventional commit"
author: TuNombre
compatibility: "Universal"
---

# Maestro de Flujo Git (Git Workflow Master)

## 1. Propósito y Objetivo
Mantener un historial de Git limpio, legible, trazable y listo para herramientas automáticas de generación de versiones (SemVer) y changelogs.

## 2. Convención Semántica Obligatoria (Conventional Commits 1.0)
Formato: `<tipo>(<alcance_opcional>): <descripción imperativa breve>`

Tipos permitidos:
- `feat`: Nueva característica para el usuario.
- `fix`: Corrección de un bug.
- `refactor`: Cambio de código que no arregla un bug ni añade una función.
- `perf`: Mejora de rendimiento.
- `test`: Añadir o corregir pruebas unitarias.
- `docs`: Cambios exclusivamente en documentación.
- `chore`: Tareas de mantenimiento, dependencias o tooling.
- `ci`: Modificaciones en pipelines de CI/CD.

## 3. Formato de Salida para Pull Requests (PR)

```markdown
## 📌 Resumen de Cambios
- Descripción concisa en viñetas de qué cambia este PR.

## 🔍 Tipo de Cambio
- [ ] 🐛 Bug fix (corrección sin romper compatibilidad)
- [ ] ✨ Nueva funcionalidad (añade capacidad)
- [ ] ⚠️ Breaking change (rompe compatibilidad con versiones previas)

## 🧪 Pruebas Realizadas
- Detalle de pruebas manuales y unitarias ejecutadas.

## 📸 Capturas o Logs (si aplica)
- Evidencia visual o consola.
```
