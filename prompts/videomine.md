# VideoMine

> Extrae pepitas de conocimiento de videos de YouTube usando IA - Metodología minerOS

## Descripción
Sistema CLI + Web para extraer, estructurar y conectar conocimiento de videos de YouTube.
Pipeline de procesamiento con múltiples motores LLM (Ollama, Claude Code, Claude API).
Incluye Knowledge Graph y Laboratorio de Embeddings.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/videomine
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un sistema de extracción de conocimiento de videos de YouTube con las
siguientes especificaciones:

## Stack
- Python 3.9+
- Flask + Flask-CORS (servidor web)
- Jinja2 (templates HTML)
- yt-dlp (descarga videos/subtítulos)
- openai-whisper (transcripción de audio)
- anthropic (Claude API)
- Ollama (LLM local)
- D3.js (visualización grafo)

## Metodología minerOS (Vocabulario)
Usar terminología de minería consistente en todo el proyecto:
```
🔦 Tunnel      → Scanner (yt-dlp descubre el video)
⛏️ Pickaxe     → Extractor (subtítulos o Whisper)
💎 Gemcutter   → Clasificador (LLM resume y estructura)
🏛️ Vault       → Base de datos (nuggets.json + HTML)
🧭 Compass     → Interfaz web (Flask)
🗺️ Cartographer → Grafo de conocimiento (conexiones semánticas)
🔬 Prospector  → Laboratorio de embeddings (búsqueda semántica)
```

## Estructura del Proyecto
```
videomine/
├── videomine.py          # CLI principal (orquesta pipeline)
├── compass.py            # Configuración global
├── compass_server.py     # Servidor Flask (API REST)
├── pickaxe.py            # Utilidades de extracción
├── tunnel/
│   └── __init__.py       # scan_video(), extract_subtitles(), transcribe_audio()
├── gemcutter/
│   └── __init__.py       # cut_with_ollama(), cut_with_claude(), parse_nugget()
├── cartographer/
│   ├── __init__.py       # API pública del grafo
│   ├── extractor.py      # Extrae conceptos con Claude Code
│   ├── graph.py          # KnowledgeGraph class
│   └── embeddings_lab.py # Lab de embeddings con nomic-embed-text
├── vault/
│   ├── __init__.py       # load_nuggets(), save_nugget(), forge_html()
│   ├── nuggets.json      # Base de datos JSON
│   └── *.html            # Nuggets renderizados
├── compass/templates/
│   ├── index.html        # Índice del vault
│   ├── nugget.html       # Template de nugget individual
│   ├── graph.html        # Visualización D3.js del grafo
│   └── lab.html          # Laboratorio de embeddings
├── mine                  # Wrapper script bash
└── VideoMine.command     # Launcher macOS (doble-click)
```

## Pipeline de Minería (dig function)
1. **Tunnel**: yt-dlp extrae metadatos (título, canal, duración, thumbnail)
2. **Pickaxe**: Busca subtítulos automáticos, si no usa Whisper
3. **Gemcutter**: LLM genera JSON estructurado del contenido
4. **Vault**: Jinja2 renderiza HTML, guarda en DB
5. **Compass**: Actualiza índice web

## Estructura de un Nugget (JSON)
```json
{
  "idea_principal": "Una o dos oraciones con la idea central",
  "puntos_clave": ["punto 1", "punto 2", "punto 3"],
  "codigo_comandos": ["comando o código mencionado"],
  "recursos_mencionados": ["recurso o herramienta"],
  "preguntas_profundizar": ["pregunta para seguir aprendiendo"],
  "glosario": {"término": "definición breve"}
}
```

## CLI (videomine.py)
```bash
python videomine.py URL                  # Minar con Ollama (local)
python videomine.py URL --claude-code    # Usar Claude Code CLI
python videomine.py URL --claude         # Usar Claude API
python videomine.py URL --manual         # Guardar transcripción para después
python videomine.py --server             # Iniciar Compass (web)
python videomine.py --delete VIDEO_ID    # Eliminar nugget
python videomine.py --finish VIDEO_ID    # Completar nugget pendiente
python videomine.py --map VIDEO_ID       # Extraer conceptos al grafo
python videomine.py --rebuild-graph      # Reconstruir grafo completo
python videomine.py --graph              # Abrir grafo en navegador
```

## API REST (compass_server.py)
| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/api/videos` | GET | Listar nuggets |
| `/api/add` | POST | Minar video `{url, motor}` |
| `/api/progress/<id>` | GET | Progreso de minería |
| `/api/delete/<id>` | DELETE | Eliminar nugget |
| `/api/search?q=` | GET | Buscar en vault |
| `/api/export/<id>` | GET | Exportar Markdown |
| `/api/export-html/<id>` | GET | HTML imprimible |
| `/api/export-anki/<id>` | GET | Flashcards TSV |
| `/api/expand` | POST | Expandir punto con IA |
| `/api/concept-map/<id>` | GET | Mapa conceptual SVG |
| `/api/cartographer/graph` | GET | Grafo D3.js |
| `/api/cartographer/rebuild` | POST | Reconstruir grafo |
| `/api/cartographer/related/<id>` | GET | Videos relacionados |
| `/vault/graph` | GET | Vista interactiva grafo |
| `/lab` | GET | Laboratorio embeddings |
| `/api/lab/search` | POST | Búsqueda semántica |
| `/api/lab/similarity` | POST | Similitud entre conceptos |
| `/api/lab/quiz` | GET | Pregunta quiz |

## Knowledge Graph (Cartographer)
- Cada concepto es un nodo, videos son fuentes
- Extracción automática con Claude Code
- Unificación de sinónimos ("Python 3" = "python")
- Visualización D3.js force-directed
- Panel lateral con videos fuente

## Laboratorio Embeddings (Prospector)
- Modelo: nomic-embed-text (Ollama)
- Búsqueda semántica por significado
- Quiz de similitud
- Comparador de conceptos (0-1)
- Mapa 2D por clusters

## Variables de Entorno
| Variable | Default | Descripción |
|----------|---------|-------------|
| `VIDEOMINE_MODEL` | `llama3.2` | Modelo Ollama |
| `VIDEOMINE_MAX_CHARS` | `12000` | Max caracteres transcripción |
| `VIDEOMINE_TIMEOUT` | `300` | Timeout LLM (seg) |
| `VIDEOMINE_HOST` | `127.0.0.1` | Host servidor |
| `VIDEOMINE_PORT` | `5555` | Puerto servidor |

## Convenciones
- Idioma código: Inglés
- Idioma UI/docs: Español
- Nombres archivos: snake_case
- Color principal: dorado (#ffa500)
- "Videos" son "nuggets" (pepitas de conocimiento)
- Local primero: Ollama por defecto, Claude como alternativa

## Dependencias Sistema
- ffmpeg (requerido por Whisper)
- ollama con modelo llama3.2 y nomic-embed-text

## Funciones Interactivas UI
- "Explícame más": Expande punto clave con Ollama
- Mapa conceptual SVG: Nodos por tipo, tamaño por importancia
- Exportar: Markdown, HTML imprimible, Anki flashcards
```

---

## Ecosistema minerOS
Parte de una familia de herramientas:
- **VideoMine** - Videos de YouTube
- PhotoMine - Fotografías
- DocMine - Documentos
- DocMine-Fiscal - Fiscalidad

## Complejidad
Media-Alta (~2k LOC) - Pipeline modular, múltiples integraciones LLM,
Knowledge Graph con D3.js, Lab de embeddings.

## Fecha de Análisis
Diciembre 2024
