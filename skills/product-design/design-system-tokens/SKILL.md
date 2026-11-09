---
name: design-system-tokens
description: Define sistemas de Design Tokens semánticos (color, espaciado, tipografía, elevación) compatibles con Figma, CSS Variables y Tailwind CSS.
version: 1.0.0
triggers:
  - "crea design tokens para"
  - "sistema de diseño con tokens"
  - "paleta de colores semántica"
  - "variables css de diseño"
author: TuNombre
compatibility: "Universal"
---

# Diseñador de Design Tokens (Design System Tokens)

## 1. Propósito y Objetivo
Establecer un lenguaje visual consistente y sincronizado entre diseño y código mediante la arquitectura de Design Tokens en 3 niveles (Globales, Semánticos y de Componente).

## 2. Los 3 Niveles de Tokens
1. **Tokens Globales / Primitivos:**
   - Valores puros sin contexto de uso: `blue-500: #3b82f6`, `space-4: 16px`.
2. **Tokens Semánticos (El corazón del sistema):**
   - Comunican propósito e intención, facilitando temas Claro/Oscuro de forma automática:
     - `bg-surface`: Fondo de tarjetas (`white` en claro, `#18181b` en oscuro).
     - `text-primary`: Texto principal con máximo contraste.
     - `text-muted`: Texto secundario de apoyo.
     - `action-primary-bg`: Fondo del botón de acción principal.
     - `border-subtle`: Bordes decorativos suaves.
3. **Tokens de Componente:**
   - Específicos para un elemento (`button-height`, `modal-backdrop`).

## 3. Formato de Salida

1. **📄 Variables CSS Semánticas (`:root` y `.dark`):** Listas para copiar en tu hoja de estilos principal.
2. **⚙️ Configuración Tailwind (`tailwind.config.js`):** Mapeo de los tokens semánticos a clases utilitarias.
3. **📐 Escala de Espaciado y Radios:** Estándar de múltiplos de 4px/8px para garantizar armonía geométrica.
