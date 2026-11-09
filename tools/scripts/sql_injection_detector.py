"""
SQL Injection & Unsafe Query Detector
Detecta consultas SQL dinámicas vulnerables a inyección SQL (SQLi)
provocadas por interpolación de cadenas, format(), f-strings o concatenación directa (+).
"""

import re
import sys
import os
import json

SQLI_PATTERNS = [
    (r'(?:SELECT|INSERT|UPDATE|DELETE|DROP)\s+.*?\s*[\+\%]\s*[a-zA-Z0-9_]+', "Concatenación directa con operador + o %"),
    (r'f["\'].*?(?:SELECT|INSERT|UPDATE|DELETE|DROP)\b.*?\{[a-zA-Z0-9_\.]+\}', "F-string de Python con sentencia SQL interpolada"),
    (r'`.*?(?:SELECT|INSERT|UPDATE|DELETE|DROP)\b.*?\$\{[a-zA-Z0-9_\.]+\}`', "Template literal de JavaScript/TypeScript con interpolación SQL"),
    (r'(?:\.format\(|\%s|\%d).*?(?:SELECT|INSERT|UPDATE|DELETE|DROP)', "Formateo de cadena dinámico en consulta SQL")
]

def scan_code_for_sqli(code: str, source_name: str = "snippet") -> list:
    findings = []
    lines = code.splitlines()
    for idx, line in enumerate(lines, 1):
        for pattern, reason in SQLI_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append({
                    "source": source_name,
                    "line": idx,
                    "code_snippet": line.strip(),
                    "vulnerability": "POTENTIAL_SQL_INJECTION",
                    "reason": reason,
                    "recommendation": "Utilizar consultas parametrizadas con placeholders (?, $1, :param) o un ORM seguro."
                })
    return findings

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            with open(arg, "r", encoding="utf-8", errors="ignore") as f:
                code_to_scan = f.read()
        else:
            code_to_scan = arg
    else:
        code_to_scan = 'query = f"SELECT * FROM users WHERE username = \'{user_input}\'"'
    
    results = scan_code_for_sqli(code_to_scan)
    print(json.dumps({"issues_found": len(results), "findings": results}, indent=2, ensure_ascii=False))
