# EigenLab - Prompt de Reproducción

> Ecosistema de laboratorios virtuales donde las ecuaciones cobran vida

## Descripción
Colección de simulaciones interactivas de Física, Química, Bioquímica, Matemáticas y Astronomía. 8 laboratorios, 87+ simulaciones, archivos HTML autocontenidos.

## Fuente
- **Repo:** ~/Projects/EigenLab/
- **Autor:** Carlos Lorente Kaiser
- **Licencia:** MIT

---

## Prompt

```
# EigenLab - Simulaciones Interactivas

Crea un ecosistema de laboratorios virtuales educativos donde las ecuaciones cobran vida.
Colección de simulaciones interactivas de Física, Química, Bioquímica, Matemáticas y Astronomía.

## Stack

- **HTML5** - Archivos autocontenidos, sin bundler ni build step
- **CSS3** - Tema oscuro, variables CSS custom properties, responsive
- **JavaScript ES6+** - Vanilla, sin frameworks (React, Vue, etc.)
- **Canvas 2D** - Renderizado principal para simulaciones
- **Three.js** (CDN) - Visualizaciones 3D opcionales (química molecular, orbifolds)
- **Tailwind CSS** (CDN) - Opcional para índices de laboratorio
- **Web Audio API** - Síntesis de sonido para Sound Labs
- **Google Fonts: Inter** - Tipografía consistente

## Estructura

EigenLab/
├── _portal/
│   └── index.html              # Landing page con previews animados de cada lab
├── _templates/
│   ├── simulation-2d.html      # Plantilla base Canvas 2D
│   ├── simulation-3d.html      # Plantilla base Three.js
│   └── styles-base.css         # Variables CSS compartidas
├── Physics/
│   ├── Physics Visual Lab/     # 19 simulaciones (mecánica, ondas, relatividad)
│   └── Physics Sound Lab/      # 7+ generativos (metrónomos, música generativa)
├── Chemistry/
│   └── Chemistry Visual Lab/   # 17 simulaciones (atómica, termodinámica)
├── Biochemistry/
│   └── Biochem Visual Lab/     # 16 simulaciones (ADN, metabolismo)
├── Mathematics/
│   ├── Math Visual Lab/        # 22 simulaciones (fractales, caos, topología)
│   └── Math Generative Art Lab/# 7 simulaciones (Gray-Scott, L-Systems)
├── Astronomy/
│   ├── Astronomy Visual Lab/   # 6 simulaciones (Hubble, H-R, agujeros negros)
│   └── Astronomy Sound Lab/    # 3 simulaciones (púlsares, ondas gravitacionales)
├── README.md
└── ROADMAP.md

## Paleta de Colores por Disciplina

| Disciplina | Variable CSS | Hex |
|------------|--------------|-----|
| Physics Visual | --color-physics-visual | #22c55e (verde) |
| Physics Sound | --color-physics-sound | #a855f7 (púrpura) |
| Chemistry | --color-chemistry | #06b6d4 (cyan) |
| Biochemistry | --color-biochemistry | #ec4899 (rosa) |
| Mathematics | --color-mathematics | #f97316 (naranja) |
| Astronomy | --color-astronomy | #6366f1 (índigo) |

## Estructura de Simulación (Template)

Cada simulación es un archivo HTML autocontenido con:

1. **Header**: Título + breadcrumb de navegación
2. **Canvas container**: Área de renderizado (flex: 1)
3. **Panel de controles** (320px width):
   - Ecuación principal (Times New Roman, italic)
   - Sliders de parámetros con valor en tiempo real
   - Botones Play/Pause y Reset
   - Valores calculados (font monospace, color accent)

### Patrón de código JavaScript:

// 1. CONFIG object - parámetros y estado
const CONFIG = { param1: 50, running: false };

// 2. Canvas setup con devicePixelRatio
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let dpr = window.devicePixelRatio || 1;
function resizeCanvas() { /* ... */ }

// 3. Event listeners para controles
slider.addEventListener('input', (e) => { /* ... */ });

// 4. Estado de simulación
let state = { x: 0, y: 0, vx: 0, vy: 0 };
function init() { /* inicializar estado */ }

// 5. Física
function update(dt) { /* integración numérica */ }

// 6. Renderizado
function draw() { /* dibujar en canvas */ }

// 7. Loop principal con deltaTime
function loop(time) {
    const dt = Math.min((time - lastTime) / 1000, 0.1);
    update(dt);
    draw();
    requestAnimationFrame(loop);
}

## Métodos Numéricos

- **Runge-Kutta 4 (RK4)**: Integración de EDOs (péndulos, órbitas, atractores)
- **Newton-Raphson**: Ecuaciones trascendentes (anomalía de Kepler)
- **Diferencias finitas**: PDEs (difusión de calor, Gray-Scott)
- **Monte Carlo**: Distribuciones probabilísticas (orbitales atómicos)

## Características Clave

1. **Sin servidor** - Abrir index.html directamente en navegador
2. **Autocontenido** - Cada simulación = 1 archivo HTML (excepto CDNs)
3. **Responsive** - Funciona en desktop y móvil
4. **Tema oscuro** - --bg-primary: #030712, --bg-secondary: #0f172a
5. **Educativo** - Ecuaciones visibles, valores en tiempo real
6. **Interactivo** - Sliders, drag & drop, presets

## Convenciones

- **Idioma**: Español para UI, inglés para código
- **Naming**: camelCase para variables, kebab-case para archivos HTML
- **Comentarios**: Español para explicar física, inglés para código técnico
- **Archivos**: Un HTML por simulación, index.html por laboratorio
- **CSS**: Variables custom properties, inline en cada archivo
- **JS**: Vanilla ES6+, sin transpilación

## Portal Principal

El portal (_portal/index.html) incluye:
- Header con gradiente de todos los colores de disciplina
- Stats: laboratorios, simulaciones, disciplinas
- Grid de cards por disciplina con previews animados en canvas
- Cada preview es una mini-animación representativa del laboratorio

## Crear Nueva Simulación

1. Copiar _templates/simulation-2d.html
2. Cambiar --accent al color de la disciplina
3. Actualizar breadcrumbs
4. Escribir ecuación principal
5. Definir parámetros y sliders
6. Implementar update(dt) con física real
7. Implementar draw() con visualización
8. Añadir al index.html del laboratorio

## Sound Labs

Usan Web Audio API:
- AudioContext para crear contexto
- OscillatorNode para síntesis
- GainNode para volumen/ADSR
- AnalyserNode para FFT/visualización
- Sintetizar a partir de física (períodos orbitales → frecuencias)
```

---

## Variables
- `{disciplina}` - Physics, Chemistry, Biochemistry, Mathematics, Astronomy
- `{color-hex}` - Color de acento según disciplina
- `{ecuacion}` - Ecuación principal de la simulación

## Tags
`simulaciones` `fisica` `quimica` `matematicas` `astronomia` `canvas` `educativo` `interactivo` `web-audio`

## Complejidad
Alta

## Fecha
Diciembre 2025
