# Biblioteca de Prompts

Colección de prompts de reproducción y system prompts para proyectos y chatbots.

## Índice

### Ingeniería Inversa (Reproducción de Proyectos)
| Archivo | Descripción | Stack |
|---------|-------------|-------|
| [videomine.md](videomine.md) | Extractor de conocimiento YouTube | Python, Flask, Ollama |
| [directos.md](directos.md) | Pipeline Builder con IA | FastAPI, Claude, RAG |
| [factoria-demo.md](factoria-demo.md) | Sistema gestión escuela artes | Python, Flask, SQLite |
| [harmonices-mundi.md](harmonices-mundi.md) | Sistema Solar sonificado (Kepler) | Canvas, Web Audio |
| [educacion-auditiva.md](educacion-auditiva.md) | Entrenamiento auditivo musical | HTML, Tailwind, Audio |
| [physics-sound-lab.md](physics-sound-lab.md) | 7 metrónomos físicos | Canvas, Web Audio, RK4 |
| [math-kids.md](math-kids.md) | Juego matemáticas niños | HTML, CSS, gamificación |
| [dashboard-mobile-mineros.md](dashboard-mobile-mineros.md) | PWA móvil minerOS | PWA, Service Worker |
| [dashboard-seguimiento.md](dashboard-seguimiento.md) | Dashboard seguimiento personal | HTML, Kanban, localStorage |
| [obsidian-dataview.md](obsidian-dataview.md) | Plugin de queries para Obsidian | TypeScript, Preact |
| [dashboard-trebol-farmacias.md](dashboard-trebol-farmacias.md) | Dashboard de ventas farmacia | HTML, CSS, JS vanilla |

### Chatbots Farmacéuticos
| Archivo | Descripción | Contexto |
|---------|-------------|----------|
| [farmaceutico-conservador.md](farmaceutico-conservador.md) | Asistente clínico conservador | Genérico |
| [farmaia-web.md](farmaia-web.md) | Asistente web público | España, AEMPS |
| [farmazero-copiloto.md](farmazero-copiloto.md) | Copiloto de mostrador | Profesional, venta cruzada |

## Uso

Cada archivo `.md` contiene:
- **Descripción** del prompt/proyecto
- **Prompt completo** en bloque de código
- **Variables** a reemplazar (si aplica)
- **Tags** para búsqueda

## Crear nuevo prompt

```bash
# Copiar template
cp _template.md nuevo-prompt.md
```

## Comandos relacionados

```bash
# Generar prompt de reproducción desde proyecto local
/reproduce-prompt

# Analizar repo de GitHub
gh repo clone user/repo -- --depth 1
# + análisis con Claude Code
```

---

*Última actualización: Diciembre 2024*
