# Educación Auditiva

> Aplicación web para entrenamiento auditivo musical - Curso de Armonía

## Descripción
App de entrenamiento auditivo basada en el curso de armonía de bustena.com.
20 unidades con teoría, diagramas y ejercicios de reconocimiento de
progresiones armónicas.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/educacion-auditiva
- **Autor:** Carlos (cjlkaiser-cpu)
- **Contenido:** Basado en bustena.com
- **Licencia:** MIT

---

## Prompt

```
Crea una aplicación de entrenamiento auditivo musical para un curso de armonía
con las siguientes especificaciones:

## Stack
- HTML5 single-file
- Tailwind CSS (via CDN)
- Font Awesome (iconos)
- JavaScript vanilla ES6+
- Google Fonts (Inter)
- Audio: archivos MP3 pregrabados

## Estructura
```
educacion-auditiva/
├── index.html           # Aplicación completa (~1500 líneas)
└── imagenes/            # Diagramas de teoría
    ├── unidad01_*.png   # ~5 imágenes por unidad
    ├── unidad02_*.png
    └── ...              # ~70 imágenes total
```

## Contenido: 20 Unidades

| # | Tema |
|---|------|
| 1 | Morfología de triadas (Mayor, menor, dim, aug) |
| 2 | Funciones tonales (T, S, D) |
| 3 | Disposición y enlace de acordes |
| 4 | Conducción de voces |
| 5 | Cifrado barroco |
| 6 | Acordes de cuarta (cadenciales) |
| 7 | Primera inversión (acordes de sexta) |
| 8 | Series de sextas |
| 9 | Secuencias armónicas |
| 10 | Cadencias |
| 11 | Dominantes secundarias (triadas) |
| 12 | Inversiones de séptima |
| 13 | Acordes de séptima diatónicos |
| 14 | Notas de paso y acordes de paso |
| 15 | Retardos y series de séptimas |
| 16 | Acordes de novena |
| 17 | VII grado con séptima |
| 18 | VII7 disminuido y sensible |
| 19 | Sexta aumentada (alemana, francesa, italiana) |
| 20 | Modulación |

## Modelo de Datos

### Estructura de Unidad
```javascript
const UNITS = [
    {
        id: 1,
        title: "Morfología de los acordes de triada",
        shortTitle: "Triadas",
        description: "Especies: Mayor, menor, disminuido, aumentado",
        images: ["unidad01_01_*.png", "unidad01_02_*.png", ...],
        theory: `<h3>Título</h3><p>Contenido HTML...</p>`,
        exercises: [
            {
                id: "u1_ex1",
                audio: "audio/u1_ex1.mp3",
                answer: "I - IV - V - I",
                hint: "Progresión básica en modo mayor"
            },
            // ... más ejercicios
        ]
    },
    // ... 19 unidades más
];
```

## Interfaz de Usuario

### Layout (3 columnas en desktop)
```
┌─────────────────────────────────────────────────────┐
│ [≡]  Educación Auditiva - Armonía                   │
├──────────┬──────────────────────────────────────────┤
│ SIDEBAR  │  CONTENIDO PRINCIPAL                     │
│          │                                          │
│ Progreso │  [▼ Teoría - acordeón colapsable]       │
│ ████░ 45%│                                          │
│          │  Ejercicios Auditivos                    │
│ Unidades │  ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│ ○ U1     │  │ ▶ Ex.1  │ │ ▶ Ex.2  │ │ ▶ Ex.3  │   │
│ ● U2     │  │ ░░░░░░░ │ │ ░░░░░░░ │ │ ░░░░░░░ │   │
│ ○ U3     │  │ Revelar │ │ Revelar │ │ Revelar │   │
│ ...      │  └─────────┘ └─────────┘ └─────────┘   │
│          │                                          │
│ [Aleatorio]                                         │
└──────────┴──────────────────────────────────────────┘
```

### Sidebar
- Logo y título
- Barra de progreso general (% completado)
- Lista de unidades (navegación)
- Indicador visual de unidades completadas
- Botón modo aleatorio

### Sección Teoría (acordeón)
- Colapsable por defecto
- Contenido HTML con:
  - Títulos h3 estilizados
  - Párrafos explicativos
  - Listas con bullets
  - Notas destacadas (recuadro azul)
  - Imágenes/diagramas de la carpeta imagenes/

### Ejercicios Auditivos
- Grid responsive (3 cols desktop, 1 móvil)
- Card por ejercicio:
  - Botón play/pause
  - Barra de progreso del audio
  - Botón "Revelar respuesta"
  - Respuesta oculta (se expande al revelar)
  - Indicador de completado

## Funcionalidades

### Reproductor de Audio
```javascript
const audioElement = new Audio(src);
audioElement.play();
// Actualizar barra de progreso
audioElement.ontimeupdate = () => {
    const progress = (audio.currentTime / audio.duration) * 100;
    progressBar.style.width = progress + '%';
};
```

### Sistema de Progreso
- Guardar en localStorage
- Tracking por ejercicio (completado/no completado)
- Cálculo de porcentaje por unidad y global
- Persistencia entre sesiones

### Modo Aleatorio
- Selecciona ejercicio random de cualquier unidad
- Útil para repaso general

### Responsive
- Mobile-first con Tailwind
- Sidebar como drawer en móvil (toggle con hamburguesa)
- Grid de ejercicios: 3 cols → 2 cols → 1 col

## Estilos

### Tema Oscuro
```css
--bg-primary: #0f172a (slate-950)
--bg-secondary: #1e293b (slate-900)
--border: #334155 (slate-700)
--text-primary: #f1f5f9 (slate-100)
--text-secondary: #94a3b8 (slate-400)
--accent: #3b82f6 (blue-500)
--success: #22c55e (green-500)
```

### Animaciones
- Acordeón de teoría con transición suave
- Respuesta con expand animation
- Indicador de reproducción (pulse)
- Hover en cards

## Convenciones
- Idioma: Español (sin acentos en código)
- Terminología musical en español
- Cifrado: números romanos (I, IV, V, etc.)
- Imágenes nombradas: unidadXX_YY_descripcion.png
```

---

## Tags
`música` `armonía` `educación` `audio` `tailwind` `ear-training`

## Complejidad
Media (~1.5k LOC) - App educativa con audio y progreso

## Fecha
Diciembre 2024
