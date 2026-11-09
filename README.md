# 🧠 Configuración IA (Universal Skills & Tools)

Repositorio centralizado y agnóstico para almacenar **Habilidades (Skills)** y **Herramientas (Tools / MCP)** compatibles con cualquier modelo de lenguaje e IA (Claude, ChatGPT / GPT-4o, Google Gemini, Antigravity, Cursor, Ollama, DeepSeek, etc.).

---

## 📂 Estructura del Repositorio

```text
configuracionIA/
├── .github/workflows/      # Validaciones automáticas de sintaxis
├── skills/                 # Conocimiento procedimental y prompts estructurados
│   ├── templates/          # Plantilla oficial para crear nuevas skills
│   ├── coding/             # Skills orientadas a desarrollo y programación
│   └── general/            # Skills de propósito general y productividad
├── tools/                  # Herramientas ejecutables
│   ├── mcp-servers/        # Servidores compatibles con Model Context Protocol
│   └── scripts/            # Scripts utilitarios ejecutables (Python, Bash, etc.)
├── schemas/                # Schemas universales JSON para Function Calling
└── configs/                # Plantillas de configuración para diferentes clientes
```

---

## 🎯 ¿Cómo usar este repositorio?

### 1. En Interfaces Web (ChatGPT, Claude.ai, Gemini, etc.)
- Ve a la carpeta `skills/` y abre la habilidad que te interese (por ejemplo: [`skills/coding/code-reviewer/SKILL.md`](skills/coding/code-reviewer/SKILL.md)).
- Copia el contenido del archivo y pégalo al inicio de tu conversación o guárdalo como **Instrucción Personalizada / Custom GPT**.

### 2. En Agentes de Código (Google Antigravity, Cursor, Windsurf, Claude Code)
- Clona este repositorio o copia la carpeta `skills/` dentro de tu proyecto.
- Los agentes con soporte para archivos de contexto pueden leer directamente los archivos `SKILL.md` bajo demanda cuando se mencione una tarea relacionada.

### 3. En Herramientas con Model Context Protocol (MCP)
- Consulta la carpeta [`configs/`](configs/) para ver cómo registrar servidores y herramientas en aplicaciones como Claude Desktop o Antigravity.

---

## 📚 Catálogo de Skills

| Skill | Categoría | Descripción | Archivo |
| :--- | :--- | :--- | :--- |
| **Code Reviewer** | Coding | Revisión exhaustiva de código, detección de vulnerabilidades y optimizaciones. | [`SKILL.md`](skills/coding/code-reviewer/SKILL.md) |
| **Prompt Enhancer** | General | Mejora y refina prompts de usuario usando técnicas avanzadas (Few-Shot, Chain-of-Thought). | [`SKILL.md`](skills/general/prompt-enhancer/SKILL.md) |

---

## 🛠️ Herramientas y Schemas

| Herramienta | Tipo | Descripción |
| :--- | :--- | :--- |
| **System Info** | Script Python | Script CLI para obtener diagnósticos rápidos del entorno. |
| **Weather Tool** | Schema JSON | Ejemplo estándar de Function Calling compatible con OpenAI, Gemini y Ollama. |

---

## ✍️ Cómo añadir una nueva Skill

1. Copia el archivo [`skills/templates/SKILL_TEMPLATE.md`](skills/templates/SKILL_TEMPLATE.md).
2. Crea una carpeta dentro de `skills/<categoria>/<nombre-de-tu-skill>/`.
3. Pega la plantilla y renómbrala como `SKILL.md`.
4. Rellena los metadatos YAML superiores y las instrucciones en Markdown.
5. Haz commit y push a GitHub.
