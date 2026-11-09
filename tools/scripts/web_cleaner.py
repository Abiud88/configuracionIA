"""
Web Cleaner & Semantic Markdown Extractor
Descarga una página web o procesa HTML crudo, eliminando scripts, estilos,
navegaciones, pies de página y anuncios, convirtiéndolo en Markdown limpio
optimizado para el consumo de LLMs con cero dependencias externas (Python puro).
"""

import urllib.request
import re
import sys
from html.parser import HTMLParser

class SemanticHTMLCleaner(HTMLParser):
    def __init__(self):
        super().__init__()
        self.result = []
        self.ignore_tag = False
        self.ignore_tags = {"script", "style", "noscript", "svg", "nav", "footer", "header", "aside"}
        self.in_heading = False
        self.in_list_item = False

    def handle_starttag(self, tag, attrs):
        if tag.lower() in self.ignore_tags:
            self.ignore_tag = True
        elif tag.lower() in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            level = int(tag[1])
            self.result.append("\n" + "#" * level + " ")
            self.in_heading = True
        elif tag.lower() == "li":
            self.result.append("\n- ")
            self.in_list_item = True
        elif tag.lower() in {"p", "div", "article", "section"}:
            self.result.append("\n\n")

    def handle_endtag(self, tag):
        if tag.lower() in self.ignore_tags:
            self.ignore_tag = False
        elif tag.lower() in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.result.append("\n")
            self.in_heading = False
        elif tag.lower() == "li":
            self.in_list_item = False

    def handle_data(self, data):
        if not self.ignore_tag:
            clean_text = data.strip()
            if clean_text:
                self.result.append(clean_text + " ")

def clean_html_to_markdown(html_content: str) -> str:
    parser = SemanticHTMLCleaner()
    parser.feed(html_content)
    raw_md = "".join(parser.result)
    # Colapsar saltos de línea repetidos
    cleaned = re.sub(r"\n{3,}", "\n\n", raw_md).strip()
    return cleaned

def fetch_url(url: str, max_chars: int = 25000) -> str:
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) UniversalAIBot/1.0"}
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as response:
        html = response.read().decode("utf-8", errors="ignore")
    cleaned_md = clean_html_to_markdown(html)
    return cleaned_md[:max_chars]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        target = sys.argv[1]
        if target.startswith("http://") or target.startswith("https://"):
            try:
                print(fetch_url(target))
            except Exception as e:
                print(f"Error al descargar URL: {e}")
        else:
            print(clean_html_to_markdown(target))
    else:
        sample_html = "<html><body><nav>Menu</nav><h1>Titulo Principal</h1><p>Parrafo con <b>contenido importante</b> para el modelo.</p><footer>Pie</footer></body></html>"
        print(clean_html_to_markdown(sample_html))
