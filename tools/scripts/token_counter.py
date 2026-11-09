"""
Token Counter & Cost Calculator - Herramienta CLI y Módulo Universal
Calcula el número estimado de tokens y el coste económico en dólares
para los principales modelos de IA (OpenAI, Anthropic, Google Gemini, DeepSeek).
"""

import sys
import os
import json
import math

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
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.isfile(arg):
            with open(arg, "r", encoding="utf-8", errors="ignore") as f:
                sample_text = f.read()
        else:
            sample_text = " ".join(sys.argv[1:])
    else:
        sample_text = "Texto base de demostración para cálculo de tokens y costes en modelos de inteligencia artificial."
    
    tokens = estimate_tokens(sample_text)
    report = calculate_costs(tokens)
    print(json.dumps(report, indent=2))
