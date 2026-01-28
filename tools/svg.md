---
id: svg
name: SVG Interactivo
category: Frontend
level: solid
---

# SVG Interactivo

Gráficos vectoriales escalables con interactividad JavaScript.

## Uso Principal

Overlays de análisis, visualizaciones interactivas, herramientas de dibujo.

## Técnicas Dominadas

### Bindeo de puntos arrastrables
```javascript
function getSVGPoint(e) {
  const pt = svg.createSVGPoint();
  pt.x = e.clientX; pt.y = e.clientY;
  return pt.matrixTransform(svg.getScreenCTM().inverse());
}

h.addEventListener('pointerdown', onDown);
window.addEventListener('pointermove', onMove);
window.addEventListener('pointerup', onUp);
```

### Capas con toggle
```javascript
html += `<g class="layer" id="layer-${name}" style="display:none">...</g>`;
document.getElementById('layer-' + name).style.display = cb.checked ? '' : 'none';
```

### Bezier curves con control points
```javascript
const cpx = (p1.x + p2.x)/2 + (p2.y - p1.y)*0.3;
const cpy = (p1.y + p2.y)/2 - (p2.x - p1.x)*0.3;
html += `<path d="M ${p1.x},${p1.y} Q ${cpx},${cpy} ${p2.x},${p2.y}" .../>`;
```

### Markers (flechas)
```javascript
html += `<defs>
  <marker id="arrowhead" markerWidth="15" markerHeight="10"
          refX="13.5" refY="5" orient="auto" fill="#color">
    <polygon points="0 0, 15 5, 0 10"/>
  </marker>
</defs>`;
html += `<path ... marker-end="url(#arrowhead)"/>`;
```

### Coordenadas porcentuales (responsive)
```javascript
// Puntos en % del viewBox
pts[id].x = p.x / VB_W * 100;
pts[id].y = p.y / VB_H * 100;

// Render en px del viewBox
const px = pts[id].x / 100 * VB_W;
```

## Proyectos Relacionados

- Estudio de Encaje Venus (60+ puntos, 15 capas, medición, comparación)
- EigenLab simulaciones (overlays de análisis)

## Tips

- `preserveAspectRatio="xMidYMid meet"` para mantener proporciones
- `pointer-events: none` en capas de visualización para no bloquear clicks
- Usar `transform` en el wrapper para zoom/pan, no en el SVG
- `getScreenCTM().inverse()` para convertir coords de pantalla a SVG
