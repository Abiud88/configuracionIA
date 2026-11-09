"""
Git Diff Summarizer
Analiza trazas de git diff o parches unificados y extrae un resumen
estructurado de cambios, archivos afectados, líneas agregadas/eliminadas
y funciones modificadas para alimentar revisiones de código de LLMs.
"""

import sys
import re
import json

def summarize_diff(diff_text: str) -> dict:
    file_chunks = re.split(r"(?=diff --git )", diff_text)
    files_summary = []
    total_added = 0
    total_deleted = 0

    for chunk in file_chunks:
        if not chunk.strip():
            continue
        
        file_match = re.search(r"diff --git a/(.*?) b/(.*)", chunk)
        file_name = file_match.group(2).split()[0] if file_match else "unknown_file"

        added_lines = [l[1:] for l in chunk.splitlines() if l.startswith("+") and not l.startswith("+++")]
        deleted_lines = [l[1:] for l in chunk.splitlines() if l.startswith("-") and not l.startswith("---")]
        
        added_count = len(added_lines)
        deleted_count = len(deleted_lines)
        total_added += added_count
        total_deleted += deleted_count

        # Detectar funciones o clases afectadas
        hunk_headers = re.findall(r"@@.*@@\s*(?:(?:def|class|function|async|public|private)\s+([a-zA-Z0-9_]+))?", chunk)
        symbols = [s for s in hunk_headers if s]

        files_summary.append({
            "file": file_name,
            "additions": added_count,
            "deletions": deleted_count,
            "symbols_affected": list(set(symbols))
        })

    return {
        "files_changed_count": len(files_summary),
        "total_additions": total_added,
        "total_deletions": total_deleted,
        "files": files_summary
    }

if __name__ == "__main__":
    raw_diff = sys.argv[1] if len(sys.argv) > 1 else """diff --git a/src/auth.py b/src/auth.py
--- a/src/auth.py
+++ b/src/auth.py
@@ -10,3 +10,5 @@ def login(user, password):
-    return check_password(password)
+    if not password:
+        raise ValueError("Password cannot be empty")
+    return verify_hash(password)
"""
    summary = summarize_diff(raw_diff)
    print(json.dumps(summary, indent=2))
