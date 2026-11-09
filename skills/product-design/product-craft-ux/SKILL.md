---
name: product-craft-ux
description: Diseña experiencias de usuario (UX) fluidas con micro-copys humanos, estados vacíos elegantes (empty states) y prevención activa de fricción.
version: 1.0.0
triggers:
  - "diseña la experiencia de usuario de"
  - "mejora el ux de este flujo"
  - "diseño de producto digital"
  - "empty states y onboarding"
author: TuNombre
compatibility: "Universal"
---

# Artesanía de Producto y UX (Product Craft & UX)

## 1. Propósito y Objetivo
Elevar un producto de software de "funcional" a "excepcional". Esta habilidad aborda los estados que la mayoría de desarrolladores olvidan: estados de carga (*skeletons*), pantallas vacías motivadoras, feedback de error constructivo y reducción cognitiva en cada flujo.

## 2. Los 4 Estados Críticos de Toda Pantalla
Toda interfaz debe contemplar:
1. **Estado Ideal:** La pantalla con datos ricos y normales.
2. **Estado Vacío (Empty State):** El usuario acaba de registrarse y no tiene contenido aún.
   - *Regla de oro:* Nunca mostrar solo un icono triste y un texto vacío. Mostrar una ilustración o icono sutil, una frase motivadora y un botón de acción primaria claro para crear su primer elemento.
3. **Estado de Carga (Loading State):**
   - Reemplazar spinners genéricos por *Skeleton loaders* que anticipan la estructura real del contenido para reducir la sensación de espera percibida.
4. **Estado de Error / Recuperación:**
   - Explicar en lenguaje humano qué falló y ofrecer un botón directo de acción para resolverlo (*"Reintentar"*, *"Comprobar conexión"*), jamás un código crudo tipo `Error 500`.

## 3. Micro-Copywriting y Voz de Producto
- Títulos de botones orientados a la acción específica: *"Crear factura"* en lugar de *"Enviar"*; *"Eliminar cuenta"* en lugar de *"Aceptar"*.
- Feedback inmediato y tranquilizador: Notificaciones toast no intrusivas (*"Guardado automáticamente hace 2 seg"*).

## 4. Formato de Salida

1. **🗺️ Flujo de Pantalla Paso a Paso:** Pasos mínimos para completar la tarea clave.
2. **📝 Especificación de Estados (Ideal / Vacío / Carga / Error):** Con textos exactos de micro-copy.
3. **🛡️ Puntos de Fricción Identificados & Solución:** Dónde podría atascarse el usuario y cómo liberarlo.
