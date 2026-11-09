"""
JSON to Markdown / Compact Table Converter
Convierte objetos y arrays JSON extensos en tablas Markdown o formato delimitado,
reduciendo drásticamente el consumo de tokens al alimentar un LLM con datos.
"""

import sys
import os
import json

def json_to_markdown_table(data) -> str:
    if isinstance(data, str):
        try:
            data = json.loads(data)
        except Exception:
            return "Error: JSON inválido"

    if isinstance(data, dict):
        lines = ["| Clave | Valor |", "| :--- | :--- |"]
        for k, v in data.items():
            val_str = json.dumps(v, ensure_ascii=False) if isinstance(v, (dict, list)) else str(v)
            lines.append(f"| `{k}` | {val_str} |")
        return "\n".join(lines)

    elif isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = []
        for item in data:
            for k in item.keys():
                if k not in headers:
                    headers.append(k)

        header_row = "| " + " | ".join(headers) + " |"
        sep_row = "| " + " | ".join([":---" for _ in headers]) + " |"
        rows = [header_row, sep_row]

        for item in data:
            row_vals = []
            for h in headers:
                val = item.get(h, "")
                if isinstance(val, (dict, list)):
                    val = json.dumps(val, ensure_ascii=False)
                row_vals.append(str(val).replace("|", "\\|").replace("\n", " "))
            rows.append("| " + " | ".join(row_vals) + " |")

        return "\n".join(rows)

    return str(data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            with open(arg, "r", encoding="utf-8") as f:
                raw_input = f.read()
        else:
            raw_input = arg
    else:
        raw_input = '[{"id": 101, "servicio": "Auth Service", "estado": "Activo", "latencia_ms": 42}, {"id": 102, "servicio": "Payment Gateway", "estado": "Degradado", "latencia_ms": 320}]'
    
    print(json_to_markdown_table(raw_input))
