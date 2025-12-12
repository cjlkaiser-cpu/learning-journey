# Dashboard Mobile minerOS

> PWA móvil para consulta de proyectos y capturas de ideas - Hub de conocimiento

## Descripción
Dashboard móvil instalable como PWA para consultar proyectos, capturar ideas,
y sincronizar con DirectOS. Mobile-first, funciona offline, single-file HTML.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/dashboard-mobile-mineros
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un dashboard móvil PWA para gestión de conocimiento con las siguientes
especificaciones:

## Stack
- HTML5 single-file (~3500 líneas)
- CSS3 con variables (tema oscuro)
- JavaScript ES6+ vanilla
- LocalStorage para persistencia
- Service Worker para offline
- Web Manifest para instalación

## Estructura del Proyecto
```
dashboard-mobile-mineros/
├── index.html          # App completa
├── manifest.json       # Config PWA
├── sw.js              # Service Worker
└── icons/
    └── icon.svg       # Icono base
```

## Diseño Mobile-First
- Viewport: iPhone SE (375px) como base
- Bottom navigation (4 tabs)
- Cards con esquinas redondeadas
- Swipe gestures para acciones

## Secciones (4 tabs)

### 1. Proyectos
- Lista de proyectos filtrable por estado
- Estados: Activo, Pausado, Completado, Idea
- Card por proyecto:
  - Nombre y descripción
  - Estado (chip de color)
  - Links detectados (GitHub, URL)
  - Fecha de actualización
- FAB para añadir proyecto
- Swipe izquierda para eliminar

### 2. Capturas
- Lista de ideas rápidas, dudas, bugs
- Prioridades: Alta (rojo), Media (amarillo), Baja (verde)
- Soporte para markdown básico
- Timestamp automático
- Swipe para eliminar

### 3. Stack (Hub de Conocimiento)
- Tabs secundarios: Tools, Patterns, Flows
- Cards con modal de detalle
- Importar desde DirectOS API

### 4. Ajustes
- Conexión DirectOS (IP + puerto)
- Backup: Export/Import JSON
- Limpiar datos
- Acerca de

## PWA Features

### manifest.json
```json
{
    "name": "minerOS Dashboard",
    "short_name": "minerOS",
    "start_url": "/index.html",
    "display": "standalone",
    "background_color": "#0f172a",
    "theme_color": "#fbbf24",
    "icons": [...]
}
```

### Service Worker (sw.js)
```javascript
const CACHE_NAME = 'mineros-v1.2';
const urlsToCache = ['/', '/index.html', '/manifest.json'];

self.addEventListener('install', e => {
    e.waitUntil(caches.open(CACHE_NAME).then(cache =>
        cache.addAll(urlsToCache)
    ));
});

self.addEventListener('fetch', e => {
    e.respondWith(caches.match(e.request).then(r =>
        r || fetch(e.request)
    ));
});
```

## Sync con DirectOS

### Detección automática de IP
```javascript
async function detectDirectOS() {
    const ips = [
        'localhost:8000',
        `${location.hostname}:8000`,  // Misma IP que el dashboard
    ];
    for (const ip of ips) {
        try {
            const r = await fetch(`http://${ip}/api/health`, {timeout: 2000});
            if (r.ok) return ip;
        } catch {}
    }
    return null;
}
```

### Endpoints consumidos
- `GET /api/health` - Verificar conexión
- `GET /api/tools` - Lista de herramientas
- `GET /api/patterns` - Lista de patrones
- `GET /api/flows` - Lista de flujos

## Smart Features

### Smart Links
Detectar URLs y mostrar iconos:
```javascript
function detectLinkType(url) {
    if (url.includes('github.com')) return { icon: '🐙', label: 'GitHub' };
    if (url.includes('youtube.com')) return { icon: '▶️', label: 'YouTube' };
    if (url.includes('notion.')) return { icon: '📝', label: 'Notion' };
    return { icon: '🔗', label: 'Link' };
}
```

### Swipe to Delete
```javascript
let startX, currentX;
card.addEventListener('touchstart', e => startX = e.touches[0].clientX);
card.addEventListener('touchmove', e => {
    currentX = e.touches[0].clientX;
    const diff = startX - currentX;
    if (diff > 50) card.style.transform = `translateX(-${diff}px)`;
});
card.addEventListener('touchend', () => {
    if (startX - currentX > 100) deleteItem();
    else card.style.transform = '';
});
```

## Persistencia

### Estructura de Datos
```javascript
const data = {
    projects: [
        { id, name, description, status, links: [], created, updated }
    ],
    captures: [
        { id, content, priority, created }
    ],
    settings: {
        directosIP: 'localhost:8000',
        theme: 'dark'
    }
};
localStorage.setItem('mineros-mobile', JSON.stringify(data));
```

### Backup
```javascript
function exportData() {
    const data = localStorage.getItem('mineros-mobile');
    const blob = new Blob([data], {type: 'application/json'});
    const url = URL.createObjectURL(blob);
    // Trigger download
}

function importData(file) {
    const reader = new FileReader();
    reader.onload = e => {
        localStorage.setItem('mineros-mobile', e.target.result);
        location.reload();
    };
    reader.readAsText(file);
}
```

## Tema Visual
```css
:root {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-card: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #94a3b8;
    --accent: #fbbf24;
    --danger: #ef4444;
    --success: #22c55e;
    --warning: #f59e0b;
}
```

## Convenciones minerOS
- Single-file HTML (KISS)
- Vanilla JS, sin frameworks
- LocalStorage explorable
- Tema oscuro
- Acento dorado (#fbbf24)
- Offline-first
```

---

## Tags
`pwa` `mobile` `offline` `mineros` `dashboard` `sync`

## Complejidad
Media (~3.5k LOC) - PWA completa con sync

## Fecha
Diciembre 2024
