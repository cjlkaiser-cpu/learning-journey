# Learning Journey

> Sistema de documentación personal con dashboard interactivo y Knowledge Graph.

## Contenido

| Archivo | Descripción |
|---------|-------------|
| `knowledge-base.md` | Base de conocimiento 2026 (~100 líneas, limpio) |
| `dashboard.html` | Launchpad interactivo con 42 proyectos |
| `graph.html` | Knowledge Graph D3.js con 50+ nodos |
| `archive/` | Histórico por año |
| `projects/` | Detalles de proyectos individuales |
| `tools/` | Detalles de tecnologías |
| `patterns/` | Patrones arquitectónicos |

## URLs

- **Dashboard**: [cjlkaiser-cpu.github.io/learning-journey/dashboard.html](https://cjlkaiser-cpu.github.io/learning-journey/dashboard.html)
- **Graph**: [cjlkaiser-cpu.github.io/learning-journey/graph.html](https://cjlkaiser-cpu.github.io/learning-journey/graph.html)

## Stack

- HTML5 + Tailwind CSS (CDN)
- JavaScript vanilla
- D3.js v7 (force-directed graph)
- GitHub Pages

## Filosofía

> "Piano piano se arriva lontano"
> Aprender a aprender. Los proyectos son vehículos, no destinos.

---

<details>
<summary><strong>Prompt de Reproducción</strong></summary>

## Learning Journey - Prompt de Reproducción

Crea un sistema de documentación personal ("Personal Knowledge Vault") con dashboard interactivo y visualización de grafo de conocimiento.

### Stack
- HTML5 (archivos autocontenidos)
- CSS con Tailwind via CDN
- JavaScript vanilla
- D3.js v7 para grafo
- Font Awesome para iconos
- Google Fonts: Inter
- GitHub Pages para hosting

### Estructura
```
learning-journey/
├── README.md              # Introducción y filosofía
├── knowledge-base.md      # Base 2026 (~100 líneas)
├── dashboard.html         # Launchpad interactivo
├── graph.html             # Knowledge Graph D3.js
├── archive/               # Histórico
│   └── 2025-year-in-review.md
├── projects/              # Proyectos individuales
├── tools/                 # Tecnologías
└── patterns/              # Patrones
```

### Módulos

#### 1. knowledge-base.md
Base de conocimiento en Markdown con secciones:
- Estadísticas de progreso
- minerOS (metodología propia)
- Proyectos completados (tabla)
- Proyectos en desarrollo
- Áreas de conocimiento (Web, Python, IA/ML, BD)
- Agentes de IA y HITL
- Arquitectura Híbrida
- Memoria Evolutiva
- Sistema de decisión universal
- Roadmap Git/GitHub
- Changelog cronológico

#### 2. dashboard.html
Launchpad estilo Vercel/Linear con:
- Header sticky con logo y quick actions
- Hero stats (proyectos, GitHub, local, tecnologías)
- Sección "En Progreso" con 3 cards de proyectos activos
- Filtros interactivos (GitHub/Local, Producción, Web, Python, IA)
- Tabla de proyectos con:
  - Nombre y stack
  - Estado (badge coloreado)
  - Ubicación (GitHub link o path local copiable)
- Panel lateral: Memoria Evolutiva + minerOS
- Grid de skills/tecnologías (badges)
- Footer con cita motivacional
- Modales: "Subir a GitHub" y "Nuevo Proyecto"

#### 3. graph.html
Knowledge Graph interactivo con D3.js:
- Force-directed layout con física
- 4 tipos de nodos:
  - Proyectos (azul/verde según estado)
  - Tecnologías (verde)
  - Metodologías (púrpura)
  - Conceptos (ámbar)
- Conexiones que muestran relaciones
- Sidebar con filtros y stats
- Búsqueda con highlight
- Zoom/pan/drag
- Tooltips con descripción y conexiones
- Link bidireccional con dashboard

### Modelo de Datos

#### Nodo (graph.html)
```javascript
{
  id: "directos",
  label: "DirectOS",
  type: "project|tech|methodology|concept",
  status: "produccion|activo|completado",  // solo proyectos
  desc: "Descripción breve",
  category: "backend|frontend|ia|database"  // solo tech
}
```

#### Conexión
```javascript
{ source: "proyecto-id", target: "tech-id" }
```

### Convenciones
- Idioma: Español
- Tema: Dark mode (#0f172a base)
- Colores por tipo:
  - Producción: emerald (#10b981)
  - Activo: blue (#3b82f6)
  - Completado: indigo (#6366f1)
- Estadísticas actualizadas manualmente
- Changelog con formato: `**DD mmm YYYY**: EMOJI TÍTULO`

### Features Clave
1. **Click-to-copy** paths locales
2. **Filtros combinables** por categoría
3. **Responsive** (mobile-friendly)
4. **Offline-first** (sin backend)
5. **GitHub Pages** ready
6. **Interconexión** dashboard ↔ graph
7. **Force simulation** con colisiones
8. **Highlight** de conexiones en hover

</details>

---

*Iniciado: Noviembre 2024 | Reestructurado: Diciembre 2025 | En constante evolución*
