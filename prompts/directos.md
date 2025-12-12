# DirectOS

> Pipeline Builder Pro con IA integrada y Human-in-the-Loop - Ecosistema minerOS

## Descripción
Centro de operaciones visual para diseñar pipelines de automatización.
43 nodos, conexiones SVG, integración con Claude CLI, Knowledge Base RAG,
y sistema de memoria evolutiva.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/DirectOS
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un Pipeline Builder visual con IA integrada con las siguientes especificaciones:

## Stack
- **Frontend**: HTML5 single-file + Tailwind CSS + JavaScript vanilla + SVG
- **Backend**: FastAPI + sentence-transformers + ChromaDB
- **IA**: Claude Code CLI (sin coste API) + Ollama (local)
- **Dependencias**: Python 3.9+

## Estructura del Proyecto
```
DirectOS/
├── frontend/index.html     # UI completa (~3000 líneas, todo inline)
├── backend/
│   ├── main.py             # FastAPI server
│   ├── requirements.txt
│   └── modules/
│       ├── knowledge.py    # RAG: embeddings + ChromaDB
│       ├── scout.py        # Análisis con Claude API
│       ├── executor.py     # Ejecución de pipelines
│       └── scheduler.py    # Cron y triggers
├── data/
│   ├── content/
│   │   ├── flows/          # Recetas de flujos (.md)
│   │   ├── patterns/       # Patrones de prompts (.md)
│   │   └── presets/        # Configuraciones predefinidas
│   └── chromadb/           # Persistencia embeddings
└── start.sh                # Launcher (backend + frontend)
```

## Categorías de Nodos (43 total)

### Trigger (5)
- Manual, File Watch, Cron, Webhook, Telegram Trigger

### Proceso (6)
- Whisper (transcripción), Tesseract OCR, PDF Parser
- BeautifulSoup (scraping), REST API Call, Text Splitter

### IA (4)
- Claude (CLI), Claude Transform, Ollama, OpenAI

### Storage (6)
- ChromaDB (vectores), SQLite, Redis
- Notion, Airtable, Spreadsheet

### Flow (4)
- If (condicional), Loop, Delay, Inspector (HITL)

### Output (5)
- File, Notify, Email, Slack, Telegram Bot

## Canvas Visual (SVG)

### Renderizado de Nodos
```javascript
function renderNode(node) {
    // Crear elemento draggable
    // Mostrar: icono, nombre, puertos entrada/salida
    // Data attributes para configuración
    // Estados visuales: idle, executing, success, error
}
```

### Conexiones SVG
```javascript
function drawConnection(fromPort, toPort) {
    // Path SVG con curva bezier
    // Animación de flujo (dash-offset animado)
    // Click para eliminar
    // Tooltip: qué datos fluyen
}
```

### Interacciones
- Drag & drop nodos desde palette
- Conectar arrastrando entre puertos
- Insertar nodo en conexión existente
- Minimap con colores por categoría
- Zoom y pan
- Atajos: Ctrl+C/V (copiar/pegar), Supr (eliminar)

## Human-in-the-Loop (HITL)

### Nodo Inspector
Pausa ejecución y muestra modal con:
- Datos actuales del pipeline
- Opción de modificar antes de continuar
- Aprobar / Rechazar / Editar

### Dry Run
Ejecutar pipeline sin efectos secundarios:
- Simular outputs
- Validar conexiones
- Mostrar flujo de datos

## Integración Claude

### MINEROS BRAIN (Context System)
```javascript
const MINEROS_SYSTEM_PROMPT = `
Eres MINEROS, asistente de DirectOS...
[Identidad, capacidades, formato de respuesta]
`;

function buildClaudeContext(action, data) {
    // Construir contexto dinámico según acción
    // Incluir: pipeline actual, nodos seleccionados, historial
}

function askClaudeUnified(action, data) {
    // API unificada para todas las llamadas a Claude
    // Parsear respuesta JSON
}
```

### Funciones Claude
- **Claude Transform**: Nodo con prompt personalizable
- **Debug Inteligente**: Analiza errores y sugiere soluciones
- **Validación Semántica**: Revisa pipeline completo
- **Auto-documentación**: Genera README del pipeline
- **Sugerencias Proactivas**: Tips al añadir nodos
- **Chat Contextual**: FAB flotante para preguntas
- **Pipeline Assistant**: Crear pipeline desde lenguaje natural

## MINEROS MEMORY (Persistencia)

```javascript
const MinerosMemory = {
    // Tracking de uso
    nodesUsed: {},           // Contador por tipo de nodo
    pipelinesCreated: [],    // Historial de pipelines
    suggestionsGiven: [],    // Sugerencias mostradas

    // Chat
    chatHistory: [],         // Últimos 50 mensajes

    // Métodos
    save(),                  // Guardar en localStorage
    load(),                  // Cargar al inicio
    getSummaryForClaude()    // Resumen para contexto
};
```

## Knowledge Base (RAG)

### Embeddings
```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_document(text):
    return model.encode(text).tolist()
```

### ChromaDB
```python
import chromadb
client = chromadb.PersistentClient(path="./data/chromadb")
collection = client.get_or_create_collection("directos_kb")

# Indexar contenido de data/content/
# Buscar por similitud semántica
```

## API Endpoints (FastAPI)

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/api/health` | GET | Estado del sistema |
| `/api/tools` | GET | Lista de nodos disponibles |
| `/api/claude/ask` | POST | Ejecutar Claude CLI |
| `/api/agent/execute` | POST | Ejecutar pipeline |
| `/api/search` | POST | Búsqueda semántica en KB |
| `/docs` | GET | Swagger UI automático |

## Persistencia de Pipelines

```javascript
// Guardar pipeline
function savePipeline(name, nodes, connections) {
    const pipeline = { name, nodes, connections, created: Date.now() };
    const pipelines = JSON.parse(localStorage.getItem('pipelines') || '[]');
    pipelines.push(pipeline);
    localStorage.setItem('pipelines', JSON.stringify(pipelines));
}

// Cargar pipeline
function loadPipeline(name) {
    // Restaurar nodos y conexiones en canvas
}
```

## Sistema Educativo

### NODE_EDUCATION_DATA
Metadata por nodo:
- Qué hace (descripción detallada)
- Input esperado
- Output generado
- Cuándo usarlo
- Ejemplo de uso

### Learning Path Export
Genera guía Markdown con:
- Pipeline documentado
- Prompts para Claude Code
- Pasos de implementación

## Convenciones
- Frontend monolito HTML (fácil distribución)
- JS vanilla, sin frameworks
- Funciones globales en window
- Tailwind utility classes
- IDs descriptivos para DOM
- Color dorado (#fbbf24) para acento minerOS
```

---

## Tags
`pipeline` `automation` `claude` `rag` `fastapi` `visual-builder`

## Complejidad
Alta (~5k LOC) - Pipeline visual + RAG + integración Claude

## Fecha
Diciembre 2024
