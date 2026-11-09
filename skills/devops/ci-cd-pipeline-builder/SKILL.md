---
name: ci-cd-pipeline-builder
description: Diseña e implementa pipelines de integración y entrega continua (CI/CD) para GitHub Actions o GitLab CI con validaciones y seguridad.
version: 1.0.0
triggers:
  - "crea un pipeline de github actions"
  - "configura ci cd para"
  - "workflow de pruebas y despliegue"
  - "automatiza el build"
author: TuNombre
compatibility: "Universal"
---

# Diseñador de Pipelines CI/CD (Pipeline Builder)

## 1. Propósito y Objetivo
Automatizar las fases de linting, ejecución de pruebas unitarias, escaneo de seguridad y despliegue continuo mediante flujos reproducibles y seguros en GitHub Actions o GitLab CI.

## 2. Buenas Prácticas de Pipeline
- **Acciones fijadas por versión:** Usar tags estables (`actions/checkout@v4`).
- **Caché de Dependencias:** Utilizar caché de paquetes (pip, npm, cargo) para reducir tiempos de ejecución de minutos a segundos.
- **Fail Fast:** Ejecutar primero las comprobaciones más rápidas (linters, formatos) antes de lanzar pruebas de integración pesadas.
- **Manejo Seguro de Secretos:** Nunca imprimir secretos en logs; utilizar variables de entorno protegidas (`${{ secrets.API_KEY }}`).

## 3. Formato de Salida

1. **📄 Archivo de Workflow YAML:** Ubicación sugerida (ej: `.github/workflows/ci.yml`).
2. **⚙️ Variables y Secretos Requeridos:** Lista de secretos que deben configurarse en los ajustes del repositorio.
3. **⏱️ Estimación de Rendimiento y Pasos:** Breve explicación del flujo y cómo opera el caché.
