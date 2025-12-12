# Physics Sound Lab

> Colección de metrónomos físicos interactivos donde la física genera música

## Descripción
7 simulaciones de física que convierten ecuaciones del movimiento en sonido.
Cada metrónomo resuelve ecuaciones diferenciales con métodos numéricos
precisos (Runge-Kutta, Newton-Raphson) y genera beats en tiempo real.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/physics-sound-lab
- **Demo:** https://cjlkaiser-cpu.github.io/physics-sound-lab/
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT (código), CC BY 4.0 (contenido)

---

## Prompt

```
Crea una colección de simulaciones de física sonificadas con las siguientes
especificaciones:

## Stack
- HTML5 single-file por simulación
- Canvas 2D para renderizado
- Web Audio API para síntesis
- Tailwind CSS (landing) o CSS vanilla (simulaciones)
- JavaScript ES6+ vanilla
- Google Fonts (Inter)

## Estructura del Proyecto
```
physics-sound-lab/
├── index.html              # Landing page con previews animados
├── pendulo-simple/index.html
├── oscilador-armonico/index.html
├── pendulos-acoplados/index.html
├── lissajous/index.html
├── onda-estacionaria/index.html
├── rebote-elastico/index.html
└── harmonices-mundi/index.html
```

## Las 7 Simulaciones

### 1. Péndulo Simple
- **Ecuación:** θ'' + (g/L)sin(θ) = 0
- **Método:** Runge-Kutta 4º orden
- **Física:** Ecuación completa (no lineal), período depende de amplitud
- **Sonido:** Click en paso por equilibrio

### 2. Oscilador Armónico (Masa-Resorte)
- **Ecuación:** ẍ + (k/m)x = 0
- **Método:** Analítico (MAS puro)
- **Física:** Movimiento armónico simple, período independiente de amplitud
- **Sonido:** Tono continuo proporcional a posición

### 3. Péndulos Acoplados (Polirritmos)
- **Ecuación:** T₁/T₂ = √(L₁/L₂)
- **Física:** Múltiples péndulos con longitudes diferentes
- **Sonido:** Polirritmos naturales por superposición de períodos

### 4. Figuras de Lissajous
- **Ecuación:** x = sin(ωₓt), y = sin(ωᵧt + δ)
- **Física:** Oscilaciones perpendiculares con ratios de frecuencia
- **Sonido:** Dos osciladores con ratio ajustable

### 5. Onda Estacionaria
- **Ecuación:** fₙ = n·v/(2L)
- **Física:** Modos normales de vibración, serie armónica
- **Sonido:** Armónicos según modo seleccionado

### 6. Rebote Elástico
- **Ecuación:** v' = -e·v (coef. restitución)
- **Física:** Progresión geométrica de impactos, disipación
- **Sonido:** Click en cada rebote, frecuencia/volumen decreciente

### 7. Harmonices Mundi (Kepler)
- **Ecuación:** T² = a³, M = E - e·sin(E)
- **Método:** Newton-Raphson para ecuación de Kepler
- **Física:** Órbitas elípticas, velocidad variable
- **Sonido:** Frecuencia proporcional a velocidad orbital

## Arquitectura Común

### Loop de Simulación
```javascript
let lastTime = 0;
function animate(timestamp) {
    const dt = (timestamp - lastTime) / 1000;
    lastTime = timestamp;

    // 1. Física: actualizar estado con dt
    updatePhysics(dt);

    // 2. Audio: generar sonido según estado
    updateAudio();

    // 3. Render: dibujar en canvas
    render();

    requestAnimationFrame(animate);
}
```

### Runge-Kutta 4 (para ODEs)
```javascript
function rk4Step(state, dt, derivative) {
    const k1 = derivative(state);
    const k2 = derivative(addStates(state, scaleState(k1, dt/2)));
    const k3 = derivative(addStates(state, scaleState(k2, dt/2)));
    const k4 = derivative(addStates(state, scaleState(k3, dt)));

    return addStates(state, scaleState(
        addStates(k1, scaleState(k2, 2), scaleState(k3, 2), k4),
        dt/6
    ));
}
```

### Web Audio Setup
```javascript
const audioCtx = new AudioContext();
const oscillator = audioCtx.createOscillator();
const gainNode = audioCtx.createGain();

oscillator.connect(gainNode);
gainNode.connect(audioCtx.destination);

// Click sound para eventos discretos
function playClick(freq = 800, duration = 0.05) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.frequency.value = freq;
    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + duration);
    osc.connect(gain).connect(audioCtx.destination);
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
}
```

## Landing Page

### Grid de Cards
- Preview animado (mini-canvas con simulación)
- Título y descripción
- Ecuación en formato matemático (font-style: italic)
- Botón "Abrir Demo"
- Hover con borde dorado animado

### Tema
- Fondo oscuro (#0a0a0a)
- Acento dorado/ámbar (#fbbf24)
- Cards con borde sutil, hover elevado

## Controles Comunes (por simulación)
- Play/Pause
- Reset
- Sliders para parámetros físicos (longitud, masa, gravedad, etc.)
- Toggle sonido on/off
- Velocidad de simulación

## Convenciones
- Tema oscuro en todas las simulaciones
- Color ámbar/dorado para acentos
- Ecuaciones con formato matemático
- Código documentado con la física
- Sin frameworks, vanilla JS
- Cada simulación es independiente (single-file)
```

---

## Tags
`física` `simulación` `canvas` `webaudio` `runge-kutta` `educación`

## Complejidad
Media-Alta (~3k LOC total) - 7 simulaciones con física real

## Fecha
Diciembre 2024
