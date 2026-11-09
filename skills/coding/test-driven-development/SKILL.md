---
name: test-driven-development
description: Genera suites de pruebas unitarias, de integración y mocks exhaustivos cubriendo happy paths, errores esperados y casos límite.
version: 1.0.0
triggers:
  - "escribe tests para"
  - "crea pruebas unitarias"
  - "tdd para esta función"
  - "suite de pruebas"
author: TuNombre
compatibility: "Universal"
---

# Desarrollo Guiado por Pruebas (Test-Driven Development - TDD)

## 1. Propósito y Objetivo
Crear baterías de pruebas automatizadas limpias, independientes y con alta cobertura, garantizando que el software sea verificable antes o después de la implementación.

## 2. Estándar de Prueba: Triple A (Arrange - Act - Assert)
Cada test unitario debe seguir rígidamente:
1. **Arrange (Preparar):** Inicializar variables, mocks, stubs y datos de entrada.
2. **Act (Actuar):** Ejecutar la función o método bajo prueba.
3. **Assert (Verificar):** Validar el resultado esperado, estado final o excepciones lanzadas.

## 3. Cobertura Requerida por Defecto
Toda suite generada debe contener al menos 3 categorías de tests:
- ✅ **Happy Path:** Entradas normales y esperadas.
- ⚠️ **Edge Cases (Casos Límite):** Arrays vacíos, cadenas con caracteres especiales, enteros extremos (`0`, `-1`, `MAX_INT`), valores nulos/undefined.
- 🛑 **Error Handling:** Asegurar que se lancen las excepciones correctas ante entradas ilícitas.

## 4. Formato de Salida

1. **Framework y Dependencias:** Explicar qué librería se utiliza (ej: Pytest, Jest, Vitest, JUnit 5).
2. **Bloque de Pruebas Completo:** Código fuente listo para ejecutar sin imports faltantes.
3. **Instrucción de Ejecución:** Comando exacto de terminal para correr las pruebas (ej: `pytest tests/test_auth.py -v`).
