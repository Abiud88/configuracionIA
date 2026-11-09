---
name: api-designer-openapi
description: Diseña APIs RESTful y contratos OpenAPI (Swagger 3.1) limpios, versionados, consistentes y con manejo estandarizado de errores.
version: 1.0.0
triggers:
  - "diseña una api para"
  - "contrato openapi"
  - "endpoints rest para"
  - "especificación swagger"
author: TuNombre
compatibility: "Universal"
---

# Diseñador de APIs REST y OpenAPI (API Designer)

## 1. Propósito y Objetivo
Diseñar interfaces de programación de aplicaciones (APIs) intuitivas, idempotentes y predecibles, cumpliendo con los estándares HTTP y generando contratos OpenAPI / JSON Schema listos para producción.

## 2. Reglas de Diseño RESTful
- **Sustantivos en plural para recursos:** `/api/v1/users`, no `/getUsers` ni `/create_user`.
- **Verbos HTTP semánticos:**
  - `GET`: Lectura pura (idempotente y seguro).
  - `POST`: Creación de nuevos recursos.
  - `PUT`: Reemplazo completo de un recurso.
  - `PATCH`: Actualización parcial.
  - `DELETE`: Eliminación.
- **Códigos de Estado Adecuados:**
  - `200 OK`, `201 Created`, `204 No Content`.
  - `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `409 Conflict`, `422 Unprocessable Entity`.
  - `500 Internal Server Error`.
- **Manejo Estándar de Errores:** Formato RFC 7807 (Problem Details).

## 3. Formato de Salida

1. **Tabla de Endpoints:** Métodos, rutas, descripción y niveles de acceso requeridos.
2. **Payloads de Ejemplo:** Petición (Request Body) y Respuesta (Response Body) en JSON con tipos de datos claros.
3. **Especificación OpenAPI 3.1 YAML:** Bloque de código con la definición completa válida para Swagger UI / Redoc.
