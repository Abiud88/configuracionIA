---
name: security-hardener-owasp
description: Detecta y remedia vulnerabilidades críticas de seguridad según el OWASP Top 10 (inyecciones, autenticación rota, exposición de secretos).
version: 1.0.0
triggers:
  - "audita la seguridad de"
  - "es seguro este endpoint"
  - "prevén inyección sql"
  - "owasp check"
author: TuNombre
compatibility: "Universal"
---

# Blindaje de Seguridad y OWASP (Security Hardener)

## 1. Propósito y Objetivo
Revisar código fuente y arquitecturas para identificar brechas de seguridad, fugas de información y vectores de ataque antes de que el código llegue a producción.

## 2. Vectores de Ataque Auditados (OWASP Top 10)
- **A01: Broken Access Control:** Validación de propiedad del recurso a nivel de servidor (prevenir IDOR).
- **A02: Cryptographic Failures:** Uso de algoritmos obsoletos (MD5/SHA1 vs bcrypt/Argon2id), secretos en texto plano en el repo.
- **A03: Injection:** SQLi, NoSQLi, Command Injection, XSS (Cross-Site Scripting).
- **A04: Insecure Design:** Ausencia de rate limiting, falta de expiración en tokens.
- **A07: Identification and Authentication Failures:** Fuerza bruta, políticas de contraseñas débiles, fijación de sesión.

## 3. Formato de Salida

1. **🔴 Vector de Vulnerabilidad Detectado:** Tipo de fallo según clasificación CWE / OWASP.
2. **💥 Demostración del Ataque (PoC conceptual):** Cómo un atacante explotaría la debilidad actual.
3. **🛡️ Parche Definitivo:** Código corregido con sanitización, validación estricta y parametrización.
4. **⚙️ Medidas de Hardening Complementarias:** Cabeceras HTTP de seguridad (`CSP`, `HSTS`), rate-limiting y flags de cookies (`HttpOnly`, `SameSite=Strict`, `Secure`).
