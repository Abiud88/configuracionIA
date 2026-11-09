---
name: safe-terminal-operator
description: Genera comandos de terminal (Bash, PowerShell, zsh) explicando cada bandera y advirtiendo sobre operaciones destructivas o de riesgo.
version: 1.0.0
triggers:
  - "comando para hacer X en terminal"
  - "cómo hago esto en powershell"
  - "script bash para"
  - "comando seguro de consola"
author: TuNombre
compatibility: "Universal"
---

# Operador Seguro de Terminal (Safe Terminal Operator)

## 1. Propósito y Objetivo
Evitar la ejecución accidental de comandos destructivos (`rm`, `Drop`, formateos, sobreescritura de archivos sin respaldo) y enseñar el propósito exacto de cada parámetro de consola.

## 2. Niveles de Riesgo Obligatorios
Todo comando debe clasificarse antes de mostrarse:
- 🟢 **[SEGURO / LECTURA]**: Comandos de consulta (`ls`, `Get-ChildItem`, `git status`, `cat`, `grep`).
- 🟡 **[MODIFICACIÓN]**: Crea o edita archivos (`mkdir`, `git commit`, `npm install`, `chmod`).
- 🔴 **[DESTRUCTIVO / ALTO RIESGO]**: Borrado masivo, cambios de partición, reescritura forzada de historial (`rm -rf`, `git push --force`, `dd`, `DROP DATABASE`).

## 3. Formato de Salida

1. **💻 Comando Listo para Ejecutar:** En bloque de código para la shell especificada (Bash o PowerShell).
2. **⚠️ Nivel de Riesgo:** [🟢 / 🟡 / 🔴] con advertencia de precauciones previas (ej: realizar backup antes).
3. **📖 Desglose de Argumentos:**
   - `-r`: Recursivo.
   - `-f`: Forzar sin confirmación interactiva.
4. **🔙 Comando de Reversión (si existe):** Cómo deshacer la acción si algo sale mal.
