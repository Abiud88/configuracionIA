"""
Secret Scanner - Escáner de seguridad ultrarrápido
Detecta credenciales, API keys (OpenAI, Anthropic, AWS, GitHub, Google),
tokens JWT y claves privadas antes de compartirlas con un LLM o comitearlas a Git.
"""

import re
import sys
import os
import json

PATTERNS = {
    "OpenAI API Key": r"sk-[a-zA-Z0-9_-]{32,64}",
    "Anthropic API Key": r"sk-ant-[a-zA-Z0-9_-]{32,64}",
    "Google Gemini/Cloud Key": r"AIza[0-9A-Za-z-_]{35}",
    "AWS Access Key ID": r"AKIA[0-9A-Z]{16}",
    "GitHub Token": r"(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{36,255}",
    "Generic Private Key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
    "Generic Bearer Token": r"(?:Bearer\s+)[a-zA-Z0-9\._-]{20,}",
    "Slack Webhook / Token": r"https://hooks\.slack\.com/services/T[0-9A-Z]+/B[0-9A-Z]+/[0-9A-Za-z]+",
    "Database Connection String": r"(?:postgres|mysql|mongodb(?:\+srv)?):\/\/[^\s:]+:[^\s@]+@[^\s\/]+"
}

def scan_text(text: str, source_name: str = "input") -> list:
    findings = []
    lines = text.splitlines()
    for line_idx, line in enumerate(lines, 1):
        for secret_type, regex in PATTERNS.items():
            matches = re.finditer(regex, line)
            for m in matches:
                matched_val = m.group(0)
                # Ocultar la mayor parte del secreto
                masked = matched_val[:4] + "*" * (len(matched_val) - 8) + matched_val[-4:] if len(matched_val) > 8 else "***"
                findings.append({
                    "source": source_name,
                    "line": line_idx,
                    "type": secret_type,
                    "preview": masked,
                    "severity": "CRITICAL"
                })
    return findings

def scan_file_or_directory(path: str) -> list:
    results = []
    if os.path.isfile(path):
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                results.extend(scan_text(f.read(), path))
        except Exception as e:
            pass
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".venv", "__pycache__"}]
            for file in files:
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        results.extend(scan_text(f.read(), full_path))
                except Exception:
                    continue
    return results

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    findings = scan_file_or_directory(target)
    print(json.dumps({"total_findings": len(findings), "issues": findings}, indent=2))
