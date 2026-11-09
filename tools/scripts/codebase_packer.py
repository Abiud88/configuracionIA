"""
Codebase Packer (RepoPacker)
Empaqueta un repositorio o directorio en un único documento estructurado en XML
ideal para inyectar en la ventana de contexto de cualquier LLM (Claude, Gemini, GPT).
Ignora automáticamente binarios, carpetas de dependencias y temporales.
"""

import os
import sys
import fnmatch

IGNORE_DIRS = {
    ".git", ".svn", ".hg", "node_modules", ".venv", "venv", "env",
    "__pycache__", "dist", "build", ".next", ".nuxt", "target",
    "vendor", ".idea", ".vscode", "coverage"
}

IGNORE_EXTS = {
    ".pyc", ".pyd", ".pyo", ".exe", ".dll", ".so", ".dylib",
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".webp",
    ".zip", ".tar", ".gz", ".7z", ".rar", ".pdf", ".lock"
}

def is_text_file(filepath: str) -> bool:
    ext = os.path.splitext(filepath)[1].lower()
    return ext not in IGNORE_EXTS

def pack_directory(root_dir: str, max_file_size_kb: int = 200) -> str:
    output = []
    output.append(f'<codebase root="{os.path.abspath(root_dir)}">')
    
    # 1. Árbol de archivos
    output.append("  <directory_structure>")
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        rel_path = os.path.relpath(root, root_dir)
        indent = "    " + "  " * (rel_path.count(os.sep) if rel_path != "." else 0)
        output.append(f"{indent}📁 {os.path.basename(root)}/")
        for f in sorted(files):
            if is_text_file(f):
                output.append(f"{indent}  📄 {f}")
    output.append("  </directory_structure>\n")

    # 2. Contenido de los archivos
    output.append("  <files>")
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS and not d.startswith(".")]
        for f in sorted(files):
            full_path = os.path.join(root, f)
            rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
            if not is_text_file(full_path):
                continue
            
            # Limitar tamaño de archivo para no reventar contexto
            size_kb = os.path.getsize(full_path) / 1024
            if size_kb > max_file_size_kb:
                output.append(f'    <file path="{rel_path}" skipped="true" reason="Tamaño excede {max_file_size_kb}KB" />')
                continue

            try:
                with open(full_path, "r", encoding="utf-8", errors="ignore") as file_in:
                    content = file_in.read()
                output.append(f'    <file path="{rel_path}">\n<![CDATA[\n{content}\n]]>\n    </file>')
            except Exception as e:
                output.append(f'    <file path="{rel_path}" error="{str(e)}" />')

    output.append("  </files>")
    output.append("</codebase>")
    return "\n".join(output)

if __name__ == "__main__":
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    packed = pack_directory(target_dir)
    print(packed)
