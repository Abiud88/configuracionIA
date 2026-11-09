"""
Core MCP Toolkit Server (Full Suite)
Servidor Model Context Protocol (MCP) que expone herramientas esenciales
de auditoría, estimación de tokens, seguridad, mockups y empaquetado de repositorios a cualquier cliente MCP.
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("UniversalAIToolkit")
except ImportError:
    mcp = None

from token_counter import estimate_tokens, calculate_costs
from secret_scanner import scan_text
from json_to_markdown import json_to_markdown_table
from code_anonymizer import anonymize_text
from codebase_packer import pack_directory
from diff_summarizer import summarize_diff
from sql_injection_detector import scan_code_for_sqli
from mock_data_generator import generate_dataset
from http_client_safe import safe_request

if mcp:
    @mcp.tool()
    def count_tokens_and_cost(text: str) -> dict:
        """Calcula el número de tokens y desglose de coste en USD para GPT-4o, Claude 3.5, Gemini 1.5 y DeepSeek."""
        tokens = estimate_tokens(text)
        return calculate_costs(tokens)

    @mcp.tool()
    def audit_secrets_in_code(code_snippet: str) -> list:
        """Escanea código en busca de API Keys expuestas, credenciales AWS, GitHub tokens o claves privadas."""
        return scan_text(code_snippet, "snippet")

    @mcp.tool()
    def compact_json_to_markdown(json_payload: str) -> str:
        """Transforma arrays JSON en tablas Markdown compactas para ahorrar hasta un 60% de tokens."""
        return json_to_markdown_table(json_payload)

    @mcp.tool()
    def anonymize_code_and_logs(text: str) -> dict:
        """Anonimiza información personal identificable (IPs, emails, DNIs, tarjetas) en logs o código."""
        return anonymize_text(text)

    @mcp.tool()
    def pack_codebase_directory(directory_path: str, max_file_size_kb: int = 200) -> str:
        """Empaqueta un repositorio o carpeta en un documento XML estructurado para la ventana de contexto del LLM."""
        return pack_directory(directory_path, max_file_size_kb)

    @mcp.tool()
    def summarize_git_diff(diff_text: str) -> dict:
        """Resume un parche o git diff estructurando archivos modificados, adiciones, eliminaciones y símbolos."""
        return summarize_diff(diff_text)

    @mcp.tool()
    def detect_sql_injection(code_snippet: str) -> list:
        """Detecta consultas SQL dinámicas inseguras provocadas por concatenación o interpolación directa."""
        return scan_code_for_sqli(code_snippet)

    @mcp.tool()
    def generate_mock_data(count: int = 5) -> list:
        """Genera conjuntos de prueba realistas en JSON (usuarios, emails, balances, ciudades) para testing."""
        default_spec = {
            "id": "id",
            "nombre": "name",
            "email": "email",
            "ciudad": "city",
            "balance": "amount",
            "estado": "status"
        }
        return generate_dataset(default_spec, count)

    @mcp.tool()
    def safe_http_get(url: str) -> dict:
        """Realiza una petición HTTP GET segura con protección anti-SSRF (bloquea IPs privadas y metadatos de nube)."""
        return safe_request(url, method="GET")

if __name__ == "__main__":
    if mcp:
        mcp.run()
    else:
        print("MCP SDK no disponible en este entorno. Para usar como servidor MCP: pip install mcp")
