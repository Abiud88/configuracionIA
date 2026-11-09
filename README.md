# 🧠 Configuración IA (Universal Skills & Tools)

Repositorio centralizado, agnóstico y estandarizado para almacenar **Habilidades (Skills)** y **Herramientas (Tools / MCP)** compatibles con cualquier modelo de lenguaje grande (Claude, ChatGPT, Gemini, Antigravity, Cursor, Ollama, DeepSeek, Mistral, etc.).

---

## 📂 Arquitectura del Repositorio

```text
configuracionIA/
├── .github/workflows/      # Validaciones automáticas (CI/CD)
├── skills/                 # Catálogo universal de habilidades operativas
│   ├── templates/          # Plantilla oficial estándar (SKILL_TEMPLATE.md)
│   ├── core/               # Razonamiento metacognitivo, control y anti-alucinaciones
│   ├── optimization/       # Ahorro de tokens, caché, poda de contexto y enrutamiento
│   ├── coding/             # Desarrollo de software, arquitectura, refactor y testing
│   ├── devops/             # Git, terminal seguro, Docker y pipelines CI/CD
│   ├── documentation/      # Documentación técnica, técnica Feynman y changelogs
│   ├── ai-data/            # Expresiones regulares, análisis EDA y ciencia de datos
│   └── general/            # Optimizador avanzado de prompts
├── tools/                  # Herramientas ejecutables
│   ├── mcp-servers/        # Servidores compatibles con Model Context Protocol (FastMCP)
│   └── scripts/            # Scripts utilitarios ejecutables (Python, Bash, etc.)
├── schemas/                # Schemas universales JSON para Function Calling directo
└── configs/                # Conectores listos para Claude Desktop, Antigravity, etc.
```

---

## 📚 Catálogo Completo de Skills

### ⚡ 1. Optimización de Recursos y Tokens (Optimization)
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **Token Compressor** | Reduce el consumo de tokens de entrada entre un 40% y 70% mediante compresión semántica densa. | [`SKILL.md`](skills/optimization/token-compressor/SKILL.md) |
| **Context Window Pruner** | Poda historiales largos de chat y contextos RAG para evitar la saturación y el efecto *Lost in the Middle*. | [`SKILL.md`](skills/optimization/context-window-pruner/SKILL.md) |
| **Prompt Caching Strategist** | Estructura prompts en bloques estáticos y dinámicos para maximizar aciertos de caché (ahorro de hasta 90%). | [`SKILL.md`](skills/optimization/llm-cache-strategist/SKILL.md) |
| **Structured Output Optimizer** | Minimiza los tokens de salida (que son 3x a 5x más caros) diseñando formatos compactos y directos. | [`SKILL.md`](skills/optimization/structured-output-optimizer/SKILL.md) |
| **Model Router & Cascade** | Enrutamiento inteligente entre modelos pequeños (Flash/Haiku) y pesados (Opus/o1) con fallbacks. | [`SKILL.md`](skills/optimization/model-router-cascade/SKILL.md) |

### 🧠 2. Razonamiento y Control (Core)
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **First-Principles Reasoning** | Descompone problemas complejos en axiomas fundamentales antes de diseñar soluciones. | [`SKILL.md`](skills/core/first-principles-reasoning/SKILL.md) |
| **Fact-Checker Skeptic** | Audita afirmaciones, versiones y referencias con escala de certeza epistémica para erradicar alucinaciones. | [`SKILL.md`](skills/core/fact-checker-skeptic/SKILL.md) |
| **Decision Matrix Analyzer** | Evaluación numérica de tradeoffs, alternativas técnicas y matrices de decisión ponderadas. | [`SKILL.md`](skills/core/decision-matrix-analyzer/SKILL.md) |

### 💻 3. Desarrollo de Software y Arquitectura (Coding)
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **Code Reviewer** | Auditoría integral de código: fallos de lógica, seguridad, buenas prácticas y refactorización limpia. | [`SKILL.md`](skills/coding/code-reviewer/SKILL.md) |
| **Systematic Debugger** | Depuración metódica basada en hipótesis, aislamiento de fallos y análisis de causa raíz. | [`SKILL.md`](skills/coding/systematic-debugger/SKILL.md) |
| **Test-Driven Development** | Creación de suites de pruebas unitarias (Arrange-Act-Assert) cubriendo happy paths y edge cases. | [`SKILL.md`](skills/coding/test-driven-development/SKILL.md) |
| **Software Architect** | Diseño estructural, patrones GoF, principios SOLID y arquitectura limpia (Hexagonal/Clean). | [`SKILL.md`](skills/coding/software-architect/SKILL.md) |
| **API Designer OpenAPI** | Contratos de API RESTful con verbos semánticos, errores RFC 7807 y especificación OpenAPI 3.1. | [`SKILL.md`](skills/coding/api-designer-openapi/SKILL.md) |
| **SQL Performance Optimizer** | Optimización de consultas SQL, análisis de planes de ejecución y recomendaciones de índices compuestos. | [`SKILL.md`](skills/coding/sql-performance-optimizer/SKILL.md) |
| **Security Hardener (OWASP)** | Detección de brechas críticas (Inyecciones, IDOR, fugas de secretos) y sanitización defensiva. | [`SKILL.md`](skills/coding/security-hardener-owasp/SKILL.md) |

### 🐙 4. DevOps, Git y Terminal
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **Git Workflow Master** | Commits semánticos (Conventional Commits), plantillas de Pull Request y resolución de conflictos. | [`SKILL.md`](skills/devops/git-workflow-master/SKILL.md) |
| **Safe Terminal Operator** | Comandos de consola con clasificación de riesgo (🟢/🟡/🔴), desglose de flags y prevención de desastres. | [`SKILL.md`](skills/devops/safe-terminal-operator/SKILL.md) |
| **Docker Containerizer** | Multi-stage builds, imágenes ligeras (alpine/distroless), usuarios no-root y docker-compose. | [`SKILL.md`](skills/devops/docker-containerizer/SKILL.md) |
| **CI/CD Pipeline Builder** | Flujos de automatización para GitHub Actions / GitLab CI con caché, linting y pruebas automáticas. | [`SKILL.md`](skills/devops/ci-cd-pipeline-builder/SKILL.md) |

### 📝 5. Documentación y Pedagogía
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **Tech Docs Writer** | Creación de READMEs de nivel profesional con diagramas Mermaid interactivos y guías de uso. | [`SKILL.md`](skills/documentation/tech-docs-writer/SKILL.md) |
| **Feynman Explainer** | Explica conceptos altamente complejos mediante analogías cotidianas y eliminación de jerga técnica. | [`SKILL.md`](skills/documentation/feynman-explainer/SKILL.md) |
| **Release Notes Generator** | Transforma commits o diffs en notas de lanzamiento bajo el estándar Keep a Changelog y SemVer. | [`SKILL.md`](skills/documentation/release-notes-generator/SKILL.md) |

### 📊 6. Datos e Inteligencia Artificial
| Skill | Descripción | Archivo |
| :--- | :--- | :--- |
| **Data Analysis & EDA** | Análisis exploratorio con Pandas/Polars: detección de outliers, correlaciones y visualizaciones. | [`SKILL.md`](skills/ai-data/data-analysis-eda/SKILL.md) |
| **Regex Wizard** | Expresiones regulares de alta precisión con desglose anatómico, tests y prevención de ReDoS. | [`SKILL.md`](skills/ai-data/regex-wizard/SKILL.md) |
| **Prompt Enhancer** | Refactorización de instrucciones mediante ingeniería de prompts (Few-Shot, CoT y Delimitadores). | [`SKILL.md`](skills/general/prompt-enhancer/SKILL.md) |

---

## 🎯 ¿Cómo utilizar estas skills en tu día a día?

1. **En ChatGPT / Claude.ai / Gemini Web:** Abre el archivo de la skill que necesites, copia su contenido y pégalo como primer mensaje (o agrégalo en tus *Custom Instructions / Instrucciones Personalizadas*).
2. **En Agentes (Antigravity, Cursor, Claude Code):** Mantén este repositorio abierto o copia la carpeta `skills/` en tus proyectos de trabajo.
3. **Para crear tus propias skills:** Copia [`skills/templates/SKILL_TEMPLATE.md`](skills/templates/SKILL_TEMPLATE.md), completa los campos YAML y añade tu procedimiento paso a paso.
