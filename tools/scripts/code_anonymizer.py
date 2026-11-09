"""
Code & Log Anonymizer (PII Redactor)
Anonimiza información personal identificable (PII) como direcciones IP,
correos electrónicos, tarjetas de crédito, teléfonos y dominios internos
en código fuente, trazas de error y logs antes de compartirlos con cualquier LLM.
"""

import re
import sys
import os
import json

PATTERNS = {
    "EMAIL": (r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", "[EMAIL_REDACTED]"),
    "IPV4": (r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b", "[IP_REDACTED]"),
    "CREDIT_CARD": (r"\b(?:\d{4}[-\s]?){3}\d{4}\b", "[CREDIT_CARD_REDACTED]"),
    "PHONE_ES_INTL": (r"(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}\b", "[PHONE_REDACTED]"),
    "DNI_NIE_ES": (r"\b\d{8}[A-HJ-NP-TV-Z]\b|\b[XYZ]\d{7}[A-Z]\b", "[ID_DOCUMENT_REDACTED]")
}

def anonymize_text(text: str) -> dict:
    redacted = text
    stats = {}
    for pii_type, (regex, replacement) in PATTERNS.items():
        matches = len(re.findall(regex, redacted))
        if matches > 0:
            stats[pii_type] = matches
            redacted = re.sub(regex, replacement, redacted)
    return {
        "anonymized_text": redacted,
        "replacements_count": sum(stats.values()),
        "breakdown": stats
    }

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            with open(arg, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
        else:
            content = " ".join(sys.argv[1:])
    else:
        content = "Error en servidor con IP 192.168.1.45 de juan.perez@empresa-secreta.com con DNI 12345678Z."
    
    result = anonymize_text(content)
    print(json.dumps(result, indent=2, ensure_ascii=False))
