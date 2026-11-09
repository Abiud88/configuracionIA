---
name: token-compressor
description: Comprime textos, prompts extensos y bases de conocimiento reduciendo el conteo de tokens entre un 40% y 70% sin perder significado semántico.
version: 1.0.0
triggers:
  - "comprime este prompt para gastar menos tokens"
  - "reduce los tokens de este texto"
  - "haz este contexto más corto sin perder información"
  - "optimiza el uso de tokens"
author: TuNombre
compatibility: "Universal"
---

# Compresor Semántico de Tokens (Token Compressor)

## 1. Propósito y Objetivo
Minimizar el consumo de tokens de entrada (Input Tokens) en peticiones a modelos de lenguaje, reduciendo costes de API y latencia de inferencia, sin degradar la precisión ni el contexto instructivo.

## 2. Técnicas de Compresión Obligatorias

1. **Eliminación de Relleno Conversacional (Politeness & Fluff Removal):**
   - Suprimir saludos, despedidas, frases de cortesía (*"Por favor", "Si no es molestia"*) y meta-comentarios (*"A continuación te presento..."*).
2. **Sintaxis Telegráfica e Información Densa:**
   - Convertir párrafos descriptivos en listas de atributos con notación `clave: valor`.
   - Utilizar símbolos lógicos (`->`, `&`, `|`, `!=`) en lugar de conectores verbales extensos.
3. **Compactación de Código y Datos:**
   - Eliminar comentarios obvios en fragmentos de código.
   - En datos estructurados, convertir objetos JSON repetitivos en tablas Markdown o listas delimitadas por comas.
4. **Preservación de Restricciones Negativas Críticas:**
   - Las reglas de seguridad o restricciones clave deben mantenerse intactas para no alterar el comportamiento del modelo.

## 3. Formato de Salida

1. **📊 Métrica de Ahorro Estimado:** Reducción porcentual aproximada de palabras/tokens.
2. **🚀 Prompt / Contexto Comprimido:** Bloque de texto optimizado listo para enviar al LLM.
3. **🔑 Claves Preservadas:** Breve lista de 2 o 3 directivas críticas que se mantuvieron para asegurar la calidad de la respuesta.

## 4. Ejemplo (Few-Shot)

### Entrada original (Innecesariamente extensa):
> "Hola, espero que estés teniendo un buen día. Me gustaría pedirte si serías tan amable de revisar este código en Python. Necesito que mires si tiene errores de seguridad y que además me digas si la función de login está bien estructurada, porque me da la impresión de que podría fallar si un usuario mete una contraseña vacía."

### Salida comprimida (Ahorro ~60%):
> "Rol: Auditor Python. Audita: seguridad & función login. Valida especialmente: gestión de contraseñas vacías. Salida: vulnerabilidades + fix."
