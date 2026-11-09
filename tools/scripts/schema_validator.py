"""
JSON Schema Validator (Zero-Dependency)
Valida documentos JSON contra esquemas básicos de estructura de campos,
tipos obligatorios y restricciones sin necesidad de dependencias externas.
"""

import sys
import json
import os

def validate_primitive(val, expected_type: str) -> bool:
    if expected_type == "string":
        return isinstance(val, str)
    elif expected_type == "integer":
        return isinstance(val, int) and not isinstance(val, bool)
    elif expected_type == "number":
        return isinstance(val, (int, float)) and not isinstance(val, bool)
    elif expected_type == "boolean":
        return isinstance(val, bool)
    elif expected_type == "array":
        return isinstance(val, list)
    elif expected_type == "object":
        return isinstance(val, dict)
    return True

def validate_json_schema(data, schema: dict, path: str = "root") -> list:
    errors = []
    
    # 1. Validar tipo raíz
    expected_type = schema.get("type")
    if expected_type and not validate_primitive(data, expected_type):
        errors.append(f"En '{path}': Se esperaba tipo '{expected_type}', pero se recibió '{type(data).__name__}'")
        return errors

    # 2. Si es objeto, validar campos requeridos y propiedades
    if isinstance(data, dict):
        required_fields = schema.get("required", [])
        for req in required_fields:
            if req not in data:
                errors.append(f"En '{path}': Campo obligatorio ausente: '{req}'")

        properties = schema.get("properties", {})
        for prop_name, prop_schema in properties.items():
            if prop_name in data:
                sub_path = f"{path}.{prop_name}"
                errors.extend(validate_json_schema(data[prop_name], prop_schema, sub_path))

    # 3. Si es array, validar items
    elif isinstance(data, list):
        items_schema = schema.get("items")
        if items_schema:
            for idx, item in enumerate(data):
                sub_path = f"{path}[{idx}]"
                errors.extend(validate_json_schema(item, items_schema, sub_path))

    return errors

if __name__ == "__main__":
    sample_schema = {
        "type": "object",
        "required": ["id", "username", "is_active"],
        "properties": {
            "id": {"type": "integer"},
            "username": {"type": "string"},
            "is_active": {"type": "boolean"}
        }
    }
    sample_data = {"id": 42, "username": "admin", "is_active": True}

    if len(sys.argv) > 2:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f_data:
                sample_data = json.load(f_data)
            with open(sys.argv[2], "r", encoding="utf-8") as f_schema:
                sample_schema = json.load(f_schema)
        except Exception as e:
            print(f"Error al leer archivos: {e}")
            sys.exit(1)

    issues = validate_json_schema(sample_data, sample_schema)
    output = {
        "is_valid": len(issues) == 0,
        "errors_count": len(issues),
        "errors": issues
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))
