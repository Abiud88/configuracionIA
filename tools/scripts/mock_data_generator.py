"""
Mock Data Generator
Genera conjuntos de datos JSON de prueba realistas (usuarios, transacciones, eventos)
a partir de especificaciones de campos, sin requerir APIs externas ni exponer datos reales.
"""

import sys
import random
import uuid
import datetime
import json

FIRST_NAMES = ["Carlos", "Elena", "Lucas", "Sofia", "David", "Lucia", "Mateo", "Valentina", "Adrian", "Martina"]
LAST_NAMES = ["Garcia", "Rodriguez", "Lopez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez"]
DOMAINS = ["gmail.com", "outlook.com", "empresa.es", "techcorp.io", "startup.dev"]
CITIES = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Malaga", "Zaragoza"]
STATUSES = ["ACTIVO", "PENDIENTE", "SUSPENDIDO", "CANCELADO"]

def generate_record(schema_types: dict, idx: int) -> dict:
    record = {}
    for field, f_type in schema_types.items():
        if f_type == "id":
            record[field] = idx + 1
        elif f_type == "uuid":
            record[field] = str(uuid.uuid4())
        elif f_type == "name":
            record[field] = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        elif f_type == "email":
            name_part = f"{random.choice(FIRST_NAMES).lower()}.{random.choice(LAST_NAMES).lower()}{random.randint(10,99)}"
            record[field] = f"{name_part}@{random.choice(DOMAINS)}"
        elif f_type == "city":
            record[field] = random.choice(CITIES)
        elif f_type == "status":
            record[field] = random.choice(STATUSES)
        elif f_type == "amount":
            record[field] = round(random.uniform(9.99, 1499.50), 2)
        elif f_type == "timestamp":
            past_days = random.randint(0, 90)
            date = datetime.datetime.now() - datetime.timedelta(days=past_days, hours=random.randint(0,23))
            record[field] = date.isoformat()
        elif f_type == "boolean":
            record[field] = random.choice([True, False])
        else:
            record[field] = f"Sample_{field}_{idx}"
    return record

def generate_dataset(schema_spec: dict, count: int = 5) -> list:
    return [generate_record(schema_spec, i) for i in range(count)]

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 5
    default_spec = {
        "id": "id",
        "nombre_completo": "name",
        "correo": "email",
        "ciudad": "city",
        "balance_usd": "amount",
        "estado": "status",
        "fecha_creacion": "timestamp"
    }
    dataset = generate_dataset(default_spec, count)
    print(json.dumps(dataset, indent=2, ensure_ascii=False))
