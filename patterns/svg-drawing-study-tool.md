---
id: svg-drawing-study-tool
name: SVG Drawing Study Tool
problem: Crear herramientas de estudio visual con análisis superpuesto interactivo
flow: [html, css, javascript, svg]
---

# SVG Drawing Study Tool

Pattern para construir herramientas de estudio de dibujo/arte con overlays de análisis.

## Problema

Estudiar proporciones, anatomía y composición de una referencia visual requiere superponer líneas de análisis, medir proporciones, y comparar con el propio trabajo.

## Solución

Single HTML file con:
1. **Imagen de referencia** como base
2. **SVG overlay** con capas de análisis arrastrables
3. **Panel de controles** con toggles por capa
4. **Herramientas auxiliares** (medición, comparación, undo/redo)

## Estructura

```
.container
├── .panel (sidebar)
│   ├── tab-bar
│   ├── tab-pages (controles, contenido)
│   └── sliders/toggles
├── .canvas-area
│   ├── .wrap
│   │   ├── img (referencia)
│   │   ├── img#userDrawing (dibujo propio, opcional)
│   │   └── svg.overlay (capas de análisis)
│   └── .canvas-toolbar (zoom, mirror, compare, measure)
└── .lightbox (zoom imágenes)
```

## Componentes Clave

### 1. Puntos arrastrables con coordenadas %
```javascript
const DEFAULT_POINTS = {
  punto_id: { x: 50, y: 30, label: 'Nombre' },
  // x,y en porcentaje del viewBox
};

function px(id) {
  return {
    x: pts[id].x / 100 * VB_W,
    y: pts[id].y / 100 * VB_H
  };
}
```

### 2. Capas con toggle
```javascript
html += `<g class="layer" id="layer-${nombre}" style="display:none">
  <line x1="${p1.x}" y1="${p1.y}" x2="${p2.x}" y2="${p2.y}" .../>
</g>`;

// Toggle
cb.addEventListener('change', () => {
  document.getElementById('layer-' + cb.dataset.layer)
    .style.display = cb.checked ? '' : 'none';
});
```

### 3. Undo/Redo stack
```javascript
const undoStack = [], redoStack = [], MAX_UNDO = 50;

function pushUndo() {
  undoStack.push(JSON.parse(JSON.stringify(pts)));
  if (undoStack.length > MAX_UNDO) undoStack.shift();
  redoStack.length = 0;
}
```

### 4. Herramienta de medición
```javascript
// Click en 2 puntos → mostrar distancia, ángulo, proporción
const distPx = Math.sqrt(dx*dx + dy*dy);
const headH = /* altura coronilla-barbilla */;
const headRatio = distPx / headH;  // "X cabezas"
```

### 5. Vista comparativa
```javascript
// Crear segundo wrap con copia del SVG
// Sincronizar puntos: mover en uno → re-render ambos
```

### 6. Persistencia localStorage
```javascript
localStorage.setItem(SLOT_PREFIX + slot, JSON.stringify(pts));
localStorage.setItem('venus_user_drawing', dataURL);
```

## Capas de Análisis Típicas

| Capa | Propósito |
|------|-----------|
| Envolvente | Bounding box de la figura |
| Ejes (hombros, caderas) | Inclinación, contrapposto |
| Plomadas verticales | Alineación puntos clave |
| Triángulos (torso, piernas) | Proporciones geométricas |
| Espacios negativos | Shapes entre formas |
| Módulo de cabeza | Proporciones en cabezas |
| Quintos | División vertical en 5 |
| Grid | Cuadrícula ajustable |
| Mapa de valores | Zonas luz/medio/sombra |
| Terminador | Línea transición luz-sombra |
| Volúmenes simplificados | Formas geométricas básicas |

## CSS Clave

```css
.wrap { position: relative; }
.wrap img { height: 100%; pointer-events: none; }
svg.overlay { position: absolute; inset: 0; }
.handle { cursor: grab; }
.handle circle.hit { fill: transparent; }  /* área clickeable amplia */
```

## Exportación

```javascript
function exportPNG() {
  const canvas = document.createElement('canvas');
  ctx.drawImage(img, 0, 0);
  ctx.drawImage(svgAsImage, 0, 0);  // via XMLSerializer + Blob
  link.href = canvas.toDataURL('image/png');
}
```

## Proyectos que usan este pattern

- Estudio de Encaje Venus

## Variaciones

- **Anatomía**: Capas de músculos, landmarks óseos
- **Perspectiva**: Líneas de fuga, horizonte
- **Color**: Análisis de paleta, armonías
- **Composición**: Proporción áurea, rule of thirds
