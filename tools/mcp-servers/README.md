# Servidores MCP (Model Context Protocol)

Esta carpeta está pensada para alojar servidores compatibles con el estándar **Model Context Protocol (MCP)**.

## ¿Qué es MCP?
MCP es el estándar abierto promovido por Anthropic y soportado por Google Antigravity, Cursor, Claude Desktop y herramientas de código abierto como LibreChat y Open WebUI. Permite exponer herramientas y recursos a cualquier modelo de IA mediante un protocolo unificado.

## Cómo añadir un nuevo servidor MCP

### En Python (Recomendado: FastMCP)
```python
# Ejemplo: server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MiServidor")

@mcp.tool()
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

### Cómo ejecutarlo
```bash
uv run python server.py
# o bien
python server.py
```
