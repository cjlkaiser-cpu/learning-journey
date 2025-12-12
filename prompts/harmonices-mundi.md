# Harmonices Mundi

> La Música de las Esferas - Sistema Solar sonificado según Kepler (1619)

## Descripción
Simulación interactiva que convierte las órbitas planetarias en música.
Cada planeta genera un tono basado en su velocidad orbital, siguiendo
los principios del tratado de Johannes Kepler.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/harmonices-mundi
- **Demo:** https://cjlkaiser-cpu.github.io/harmonices-mundi/
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT (código), CC BY 4.0 (contenido)

---

## Prompt

```
Crea una simulación interactiva del Sistema Solar con sonificación basada
en las teorías de Kepler (1619) con las siguientes especificaciones:

## Stack
- HTML5 single-file (todo inline)
- Canvas 2D para renderizado
- Web Audio API para síntesis de sonido
- CSS3 con Google Fonts (Inter)
- JavaScript vanilla ES6+

## Estructura
```
harmonices-mundi/
├── index.html      # Simulación principal (~800 líneas)
├── tutorial.html   # Tutorial interactivo
├── README.md
└── LICENSE
```

## Física Orbital

### Datos Planetarios (constantes)
Para cada planeta almacenar:
- nombre, color (hex)
- a: semieje mayor (UA)
- e: excentricidad
- T: período orbital (días terrestres)
- frecuenciaKepler: ratio armónico original de Kepler

### Ecuación de Kepler
```
M = E - e·sin(E)
```
Resolver con Newton-Raphson (5-10 iteraciones):
```javascript
function solveKepler(M, e, tolerance = 1e-6) {
    let E = M;
    for (let i = 0; i < 10; i++) {
        const dE = (E - e * Math.sin(E) - M) / (1 - e * Math.cos(E));
        E -= dE;
        if (Math.abs(dE) < tolerance) break;
    }
    return E;
}
```

### Posición desde Anomalía
```javascript
// Anomalía verdadera desde excéntrica
const trueAnomaly = 2 * Math.atan2(
    Math.sqrt(1 + e) * Math.sin(E / 2),
    Math.sqrt(1 - e) * Math.cos(E / 2)
);
// Distancia al Sol
const r = a * (1 - e * Math.cos(E));
// Coordenadas cartesianas
const x = r * Math.cos(trueAnomaly);
const y = r * Math.sin(trueAnomaly);
```

### Velocidad Orbital (vis-viva)
```javascript
const v = Math.sqrt(GM * (2/r - 1/a));
```

## Modos de Sonificación

### 1. Modo Kepler 1619 (default)
Frecuencias fijas basadas en los ratios armónicos originales:
| Planeta | Intervalo | Frecuencia base |
|---------|-----------|-----------------|
| Mercurio | Décima menor | 523 Hz |
| Venus | Diesis | 262 Hz |
| Tierra | Semitono | 294 Hz |
| Marte | Quinta | 220 Hz |
| Júpiter | Tercera menor | 131 Hz |
| Saturno | Tercera mayor | 98 Hz |

### 2. Modo Tiempo Real
Frecuencia proporcional a velocidad instantánea:
```javascript
const freq = mapRange(velocidad, vMin, vMax, freqMin, freqMax);
```

### 3. Modo Musical
Mapear velocidad a escala musical occidental (C major, pentatónica, etc.)

## Síntesis de Audio (Web Audio API)

### Arquitectura por planeta
```javascript
const audioCtx = new AudioContext();
// Por cada planeta:
const oscillator = audioCtx.createOscillator();
const gainNode = audioCtx.createGain();
oscillator.type = 'sine';  // o 'triangle' para suavizar
oscillator.connect(gainNode);
gainNode.connect(audioCtx.destination);
```

### Analizador FFT
```javascript
const analyser = audioCtx.createAnalyser();
analyser.fftSize = 2048;
// Conectar todos los gains al analyser antes del destination
```

## Interfaz de Usuario

### Panel de Control
- **Botones globales**: Play, Pause, Reset
- **Selector de modo**: Kepler 1619 / Tiempo Real / Musical
- **Escala tiempo**: Slider 1-365 días/segundo
- **Fecha simulada**: Display del tiempo transcurrido

### Mixer Planetario
Por cada planeta:
- Checkbox mute/unmute
- Slider de volumen (0-100)
- Indicador de frecuencia actual
- Color del planeta

### Presets Armónicos
Botones para configuraciones predefinidas:
- Coro Completo (todos)
- Rocosos (Mercurio-Marte)
- Gigantes (Júpiter, Saturno, Urano, Neptuno)
- Tríada Interior (Venus, Tierra, Marte)

### Visualización FFT
Canvas secundario mostrando espectro en tiempo real:
```javascript
analyser.getByteFrequencyData(dataArray);
// Dibujar barras de frecuencia
```

### Concert Hall Mode
Botón para pantalla completa inmersiva (solo canvas + audio)

## Renderizado Canvas

### Loop Principal
```javascript
function animate(timestamp) {
    // Actualizar tiempo simulado
    simTime += deltaTime * timeScale;

    // Limpiar canvas
    ctx.fillStyle = 'radial-gradient(#0a0a20, #000)';

    // Dibujar Sol (centro)
    // Dibujar órbitas (elipses)
    // Dibujar planetas (círculos con glow)
    // Actualizar frecuencias de audio

    requestAnimationFrame(animate);
}
```

### Escala Visual
- Factor de escala para que quepa el sistema
- Órbitas como elipses (no círculos)
- Planetas con tamaño proporcional (pero exagerado para visibilidad)
- Sol con efecto de glow

## Convenciones
- Tema oscuro (fondo negro/azul muy oscuro)
- Color dorado (#fbbf24) para acentos y UI
- Planetas con colores realistas
- Tipografía Inter, peso ligero
- UI minimalista, foco en la simulación

## Contexto Histórico (para tutorial)
Incluir explicación de:
- Quién fue Kepler y qué es Harmonices Mundi (1619)
- Las tres leyes de Kepler
- La "música de las esferas" como concepto filosófico
- Cómo Kepler asignó intervalos musicales a cada planeta
```

---

## Tags
`canvas` `webaudio` `astronomía` `música` `kepler` `simulación`

## Complejidad
Media (~800 LOC) - Física orbital + síntesis de audio

## Fecha
Diciembre 2024
