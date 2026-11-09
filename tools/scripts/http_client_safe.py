"""
Safe Sandboxed HTTP Client (SSRF Protected)
Realiza peticiones HTTP(S) seguras desde el agente o modelo,
bloqueando automáticamente direcciones IP locales/privadas (127.0.0.1, 10.x, 192.168.x),
servicios de metadatos de nube (169.254.169.254) y puertos restringidos para prevenir ataques SSRF.
"""

import urllib.request
import urllib.parse
import socket
import ipaddress
import sys
import json

BLOCKED_IP_RANGES = [
    ipaddress.ip_network("127.0.0.0/8"),      # Loopback
    ipaddress.ip_network("10.0.0.0/8"),       # Privada Clase A
    ipaddress.ip_network("172.16.0.0/12"),    # Privada Clase B
    ipaddress.ip_network("192.168.0.0/16"),   # Privada Clase C
    ipaddress.ip_network("169.254.0.0/16"),   # Link-Local / Metadata de AWS, GCP, Azure
    ipaddress.ip_network("::1/128"),          # IPv6 Loopback
    ipaddress.ip_network("fc00::/7")          # IPv6 Unique Local
]

ALLOWED_SCHEMES = {"http", "https"}
ALLOWED_PORTS = {80, 443, 8080, 8443}

def is_ip_blocked(ip_str: str) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str)
        return any(ip in net for net in BLOCKED_IP_RANGES)
    except ValueError:
        return True

def safe_request(url: str, method: str = "GET", payload: str = None, timeout: int = 8) -> dict:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme.lower() not in ALLOWED_SCHEMES:
        return {"error": f"Esquema de URL no permitido: {parsed.scheme}. Solo http y https son válidos."}

    hostname = parsed.hostname
    if not hostname:
        return {"error": "URL inválida: falta el host."}

    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    if port not in ALLOWED_PORTS:
        return {"error": f"Puerto no permitido: {port}. Solo se permiten {ALLOWED_PORTS}."}

    # Resolución DNS y validación anti-SSRF
    try:
        resolved_ips = socket.gethostbyname_ex(hostname)[2]
    except Exception as e:
        return {"error": f"Fallo en resolución DNS para {hostname}: {str(e)}"}

    for ip in resolved_ips:
        if is_ip_blocked(ip):
            return {
                "error": f"Acceso Bloqueado por Seguridad (SSRF Protection). La IP {ip} pertenece a una red privada o restringida."
            }

    data = payload.encode("utf-8") if payload else None
    headers = {"User-Agent": "UniversalSafeHTTPClient/1.0", "Accept": "*/*"}
    req = urllib.request.Request(url, data=data, headers=headers, method=method.upper())

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            content_type = resp.headers.get_content_type()
            body_bytes = resp.read(25000)  # Límite de 25KB
            body_str = body_bytes.decode("utf-8", errors="ignore")
            return {
                "status_code": resp.status,
                "content_type": content_type,
                "resolved_ip": resolved_ips[0],
                "body": body_str
            }
    except Exception as e:
        return {"error": f"Fallo al ejecutar petición HTTP: {str(e)}"}

if __name__ == "__main__":
    target_url = sys.argv[1] if len(sys.argv) > 1 else "https://api.github.com"
    result = safe_request(target_url)
    print(json.dumps(result, indent=2))
