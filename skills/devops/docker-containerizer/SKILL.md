---
name: docker-containerizer
description: Genera Dockerfiles optimizados multicapa (multi-stage), configuraciones de docker-compose y prácticas de seguridad en contenedores.
version: 1.0.0
triggers:
  - "dockeriza este proyecto"
  - "crea un dockerfile para"
  - "optimiza mi imagen docker"
  - "docker compose para"
author: TuNombre
compatibility: "Universal"
---

# Contenedorizador Docker Profesional (Docker Containerizer)

## 1. Propósito y Objetivo
Crear imágenes de Docker ligeras, seguras y de arranque rápido, minimizando capas, aprovechando la caché del build y evitando la ejecución como usuario root.

## 2. Reglas de Contenedorización Obligatorias
- **Multi-Stage Builds:** Separar la etapa de compilación/instalación de dependencias pesadas de la imagen final de producción.
- **Principio de Mínimo Privilegio:** Crear y usar un usuario no root (`USER appuser`).
- **Aprovechamiento de Capas de Caché:** Copiar archivos de dependencias (`package.json`, `requirements.txt`, `go.mod`) antes que el código fuente para no invalidar la caché innecesariamente.
- **Imágenes Base Minimalistas:** Preferir `alpine`, `slim` o `distroless`.
- **Inclusión de `.dockerignore`:** Excluir siempre `node_modules`, `.git`, `.env` y temporales.

## 3. Formato de Salida

1. **📄 Dockerfile Optimizado:** Con comentarios claros en cada directiva.
2. **🛡️ `.dockerignore` Sugerido:** Lista de exclusiones críticas.
3. **🐙 `docker-compose.yml` (si aplica):** Con redes aisladas y volúmenes persistentes.
4. **🚀 Comandos de Construcción y Ejecución:** Comandos precisos para compilar (`docker build -t app .`) y correr (`docker run -p 8080:8080 app`).
