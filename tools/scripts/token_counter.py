"""
Token Counter & Cost Calculator - Herramienta CLI y Módulo Universal
Calcula el número estimado de tokens y el coste económico en dólares
para los principales modelos de IA (OpenAI, Anthropic, Google Gemini, DeepSeek).
"""

import sys
import json
import math

# Precios por millón de tokens (Input / Output en USD)
MODEL_PRICING = {
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
    "claude-3-5-haiku": {"input": 0.80, "output": 4.00},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "deepseek-v3": {"input": 0.14, "output": 0.28}
}

def estimate_tokens(text: str) -> int:
    """Estimación heurística de alta fidelidad para BPE / Byte-Pair Encoding."""
    if not text:
        return 0
    words = len(text.split())
    chars = len(text)
    # Heurística empírica (~4 caracteres por token en inglés/código, ~3 en español)
    tokens_by_words = words * 1.3
    tokens_by_chars = chars / 3.6
    return max(1, int(math.ceil((tokens_by_words + tokens_by_chars) / 2)))

def calculate_costs(token_count: int, output_ratio: float = 0.3) -> dict:
    input_tokens = int(token_count * (1 - output_ratio))
    output_tokens = int(token_count * output_ratio)
    
    breakdown = {}
    for model, rates in MODEL_PRICING.items():
        cost_in = (input_tokens / 1_000_000) * rates["input"]
        cost_out = (output_tokens / 1_000_000) * rates["output"]
        total_cost = cost_in + cost_out
        breakdown[model] = {
            "total_usd": round(total_cost, 6),
            "input_cost": round(cost_in, 6),
            "output_cost": round(cost_out, 6)
        }
    return {
        "tokens": token_count,
        "input_tokens_est": input_tokens,
        "output_tokens_est": output_tokens,
        "costs_by_model": breakdown
    }

if __name__ == "__main__":
    sample_text = sys.stdin.read() if not sys.stdin.isatty() else "Ejemplo de texto para prueba de tokens y costes."
    tokens = estimate_tokens(sample_text)
    report = calculate_costs(tokens)
    print(json.dumps(report, indent=2))
