# Dashboard de Seguimiento Personal

> Dashboard interactivo para tracking de aprendizaje y proyectos - Filosofía minerOS

## Descripción
Dashboard semanal para seguimiento personal de objetivos, stack técnico,
y tareas con sistema Kanban. Persistencia en LocalStorage, historial de
semanas, y filosofía KISS.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/dashboard-seguimiento
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un dashboard de seguimiento personal semanal con las siguientes
especificaciones:

## Stack
- HTML5 single-file
- CSS3 con variables, Grid, Flexbox
- JavaScript ES6+ vanilla
- LocalStorage para persistencia
- Sin dependencias externas (KISS)

## Estructura
```
dashboard-seguimiento/
├── index.html    # Dashboard principal (~800 líneas)
└── README.md
```

## Layout (7 Secciones)

### 0. Periodo y Contexto
- Selector de semana/mes
- Campo de "Foco principal"
- Fecha de inicio

### 1. Resumen Ejecutivo
- Textarea para objetivo principal
- Campo "Definición de éxito"

### 2. Panel RAG (Red/Amber/Green)
- 3-4 áreas a evaluar (ej: Código, Aprendizaje, Salud, Proyectos)
- Cada área con 3 chips clickables: 🔴 🟡 🟢
- Click para seleccionar estado

### 3. Objetivos
- Lista de 2-3 entregables concretos
- Cada uno con:
  - Descripción
  - Fecha límite
  - Checkbox de completado

### 4. Kit de Herramientas
- Inventario de stack técnico por categorías
- Categorías: Web, Python, IA/ML, Tools
- Cada herramienta con nivel clickable:
  - Explorando → Básico → Funcional → Dominado
- Sección "Por explorar" (wishlist)

### 5. Sprint Kanban
- 3 columnas: To Do | Doing | Done
- Añadir tarea: input + Enter
- Eliminar: botón ×
- Drag & drop entre columnas (opcional)

### 6. Cierre
- Textarea para retrospectiva
- Lista de prioridades para siguiente semana

## Funcionalidades

### Nueva Semana
```javascript
function newWeek() {
    // Guardar semana actual en historial
    saveToHistory(currentData);

    // Resetear campos editables
    currentData = {
        period: getNextWeek(),
        focus: '',
        summary: '',
        rag: { codigo: null, aprendizaje: null, salud: null },
        objectives: [],
        kanban: { todo: [], doing: [], done: [] },
        retrospective: ''
    };

    render();
}
```

### Auto-guardado
```javascript
// Debounced save on any change
let saveTimeout;
function scheduleAutoSave() {
    clearTimeout(saveTimeout);
    saveTimeout = setTimeout(() => {
        localStorage.setItem('dashboard-seguimiento-v1', JSON.stringify(data));
        showSaveIndicator();
    }, 1000);
}

// Attach to all inputs
document.querySelectorAll('input, textarea').forEach(el => {
    el.addEventListener('input', scheduleAutoSave);
});
```

### Historial de Semanas
```javascript
const history = JSON.parse(localStorage.getItem('dashboard-historial') || '[]');
// Guardar últimas 10 semanas
if (history.length > 10) history.shift();
history.push({...currentData, savedAt: Date.now()});
```

### Importar Tareas
Soportar formato markdown:
```javascript
function importTasks(text) {
    const lines = text.split('\n');
    lines.forEach(line => {
        const match = line.match(/^- \[ \] (.+)$/);
        if (match) {
            kanban.todo.push(match[1]);
        }
    });
}
```

### Exportar JSON
```javascript
function exportData() {
    const dataStr = JSON.stringify(data, null, 2);
    const blob = new Blob([dataStr], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `dashboard-${data.period}.json`;
    a.click();
}
```

## Kit de Herramientas

### Estructura
```javascript
const toolkit = {
    web: [
        { name: 'HTML5', level: 3 },       // 0-3
        { name: 'CSS Grid', level: 2 },
        { name: 'JS vanilla', level: 3 },
    ],
    python: [
        { name: 'Flask', level: 2 },
        { name: 'SQLite', level: 2 },
    ],
    ia: [
        { name: 'Claude API', level: 1 },
        { name: 'Embeddings', level: 0 },
    ],
    tools: [
        { name: 'Git', level: 2 },
        { name: 'Claude Code', level: 3 },
    ],
    toExplore: ['Docker', 'FastAPI', 'LangChain']
};
```

### Niveles (click para rotar)
- 0: Explorando (gris)
- 1: Básico (amarillo)
- 2: Funcional (azul)
- 3: Dominado (verde)

## Tema Visual
```css
:root {
    --bg: #0f172a;
    --bg-card: #1e293b;
    --border: #334155;
    --text: #f1f5f9;
    --text-muted: #94a3b8;
    --accent: #fbbf24;
    --red: #ef4444;
    --amber: #f59e0b;
    --green: #22c55e;
}
```

## Filosofía minerOS

1. **Modularidad** - Cada sección independiente
2. **Sin magia negra** - Todo debuggeable en consola
3. **Datos primero** - LocalStorage explorable
4. **Incremental** - Cada mejora aporta valor
5. **Local primero** - Sin cloud, sin login
6. **KISS** - Vanilla JS, sin frameworks

## Indicador de Guardado
- Esquina inferior derecha
- "Guardado ✓" que aparece y desaparece
- Transición suave

## Responsive
- Grid adaptativo
- Kanban en columnas en desktop, stack en móvil
- Chips RAG táctiles
```

---

## Tags
`dashboard` `tracking` `kanban` `productividad` `mineros` `localStorage`

## Complejidad
Baja-Media (~800 LOC) - Dashboard con persistencia

## Fecha
Diciembre 2024
