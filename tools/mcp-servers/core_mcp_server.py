"""
Core MCP Toolkit Server
Servidor Model Context Protocol (MCP) que expone herramientas esenciales
de auditoría, estimación de tokens y optimización de contexto a cualquier cliente MCP.
"""

import sys
import os

# Permitir importar scripts locales
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "scripts"))

try:
    from mcp.server.fastmcp import FastMCP
    mcp = FastMCP("UniversalAIToolkit")
except ImportError:
    # Si fastmcp no está instalado en el entorno, permitir ejecución como script
    mcp = None

from token_counter import estimate_tokens, calculate_costs
from secret_scanner import scan_text
from json_to_markdown import json_to_markdown_table

if mcp:
    @mcp.tool()
    def count_tokens_and_cost(text: str) -> dict:
        """Calcula el número de tokens y el coste estimado en USD para diferentes modelos (GPT-4o, Claude, Gemini, DeepSeek)."""
        tokens = estimate_tokens(text)
        return calculate_costs(tokens)

    @mcp.tool()
    def audit_secrets_in_code(code_snippet: str) -> list:
        """Escanea código en busca de API Keys expuestas, credenciales AWS, GitHub tokens o claves privadas."""
        return scan_text(code_snippet, "snippet")

    @mcp.tool()
    def compact_json_to_markdown(json_payload: str) -> str:
        """Transforma arrays JSON en tablas Markdown compactas para ahorrar hasta un 60% de tokens al alimentar un LLM."""
        return json_to_markdown_table(json_payload)

if __name__ == "__main__":
    if mcp:
        mcp.run()
    else:
        print("MCP SDK no instalado en este entorno Python. Para usar como servidor MCP: pip install mcp")
