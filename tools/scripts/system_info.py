"""
System Info Tool - Script de diagnóstico universal
Útil para que cualquier modelo o agente de IA pueda recopilar
información técnica de la máquina en ejecución.
"""

import sys
import platform
import os
import json

def get_system_summary():
    return {
        "os": platform.system(),
        "os_release": platform.release(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "python_version": sys.version.split()[0],
        "cpu_count": os.cpu_count(),
        "current_directory": os.getcwd()
    }

if __name__ == "__main__":
    summary = get_system_summary()
    print(json.dumps(summary, indent=2))
