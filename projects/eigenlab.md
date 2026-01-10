---
id: eigenlab
name: EigenLab
status: production
stack: [JavaScript, Canvas 2D, Three.js, Web Audio API, WebAssembly, Tailwind CSS]
---

# EigenLab

> Ecosistema de laboratorios virtuales educativos que convierte ecuaciones y conceptos científicos en experiencias visuales, interactivas y sonoras.

## Información General

- **Repositorio**: https://github.com/cjlkaiser-cpu/eigenlab
- **Ubicación**: `~/Projects/EigenLab/`
- **Filosofía**: Educación científica a través de experimentación interactiva
- **Arquitectura**: HTML autocontenido (no build tools)

## Estadísticas (10 ene 2026)

| Métrica | Valor |
|---------|-------|
| **Simulaciones** | 128+ |
| **Laboratorios** | 14 |
| **Disciplinas** | 9 |
| **Conexiones** (Knowledge Graph) | 240+ |
| **Líneas de código** | ~50,000+ |
| **CLAUDE.md** | 8 archivos (~2,800 líneas documentación) |

## Estructura de Laboratorios

### Physics (2 labs)
- **Physics Visual Lab** - 19 simulaciones (mecánica, ondas, termodinámica, relatividad)
- **Physics Sound Lab** - 19 simulaciones (7 metronomos físicos + 6 generativos sonoros)

### Chemistry (1 lab)
- **Chemistry Visual Lab** - 17 simulaciones (estructura atómica, reacciones, termodinámica)

### Biochemistry (1 lab)
- **Biochem Visual Lab** - 16 simulaciones (metabolismo, síntesis proteica, ADN)

### Biology (1 lab)
- **Biology Visual Lab** - 9 simulaciones (Hodgkin-Huxley, Lotka-Volterra, Boids WASM)

### Geology (1 lab)
- **Geology Visual Lab** - 8 simulaciones (ondas sísmicas, volcanes VEI, tectónica)

### Mathematics (4 labs)
- **Math Visual Lab** - 27 simulaciones (fractales, caos, topología)
- **Math Generative Art Lab** - 7 simulaciones (Gray-Scott, L-Systems, Penrose)
- **Math Sound Lab** - 8 simulaciones (Game of Life musical, Fourier, Markov)
- **Euler Lab** - 100 problemas de Project Euler (Pyodide)

### Astronomy (2 labs)
- **Astronomy Visual Lab** - 8 simulaciones (Schwarzschild, Hubble, H-R diagram)
- **Astronomy Sound Lab** - 3 simulaciones (pulsares, ondas LIGO, música esferas)

### Computation (1 lab)
- **Computation Lab** - 6 simulaciones (algoritmos, BST, DFA, perceptrón)

## Stack Tecnológico

### Core
- **HTML5/CSS3/JS ES6+** - Vanilla, sin frameworks
- **Google Fonts: Inter** - Tipografía principal
- **Tailwind CSS** (CDN) - Solo para índices

### Rendering
- **Canvas 2D** - Mayoría de simulaciones
- **Three.js** - Visualizaciones 3D (Lorenz, moléculas, órbitas)
- **SVG** - Diagramas vectoriales

### Audio
- **Web Audio API** - Síntesis nativa
- **ADSR Envelopes** - Modelado de notas
- **Síntesis FM/Aditiva** - Timbres complejos

### Avanzado
- **WebAssembly** - Boids (Biology Lab)
- **Pyodide** - Python en browser (Euler Lab)

## Métodos Numéricos Implementados

- **RK4 (Runge-Kutta 4)**: Péndulos, órbitas, Lorenz
- **Euler**: Simulaciones simples
- **Newton-Raphson**: Ecuaciones trascendentes
- **Diferencias Finitas**: Difusión térmica, ecuación de onda
- **Gray-Scott**: Reacción-difusión (patterns de Turing)
- **Monte Carlo**: Distribuciones, integrales
- **FFT**: Análisis espectral
- **Barnes-Hut**: N-body problem (O(n log n))

## Documentación Técnica

### CLAUDE.md Files (2,800 líneas)
Creados en **Documentation Sprint** (10 ene 2026):

1. **Biology Visual Lab** - Hodgkin-Huxley, Lotka-Volterra, Hardy-Weinberg
2. **Geology Visual Lab** - Ondas P/S, VEI scale, tectónica
3. **Astronomy Visual Lab** - Schwarzschild, lensing, nucleosíntesis
4. **Astronomy Sound Lab** - Pulsares (Joy Division), ondas LIGO, Kepler 1619
5. **Computation Lab** - Complejidad algorítmica, BST, DFA
6. **Physics Sound Lab** - 7 metronomos + 6 generativos (Tonnetz, Rameau)
7. **Math Generative Art Lab** - Gray-Scott PDEs, L-Systems, Perlin noise
8. **Biochemistry Visual Lab** - Metabolismo, respiración celular

### Knowledge Graph
- **110+ nodos** (simulaciones + conceptos transversales)
- **240+ conexiones** (intra e inter-disciplina)
- **D3.js force-directed graph**
- Filtros por disciplina
- Búsqueda con highlight

### Caminos de Aprendizaje
5 rutas interdisciplinarias:
- Entender el Caos
- Oscilaciones Universales
- Estados y Transiciones
- Algoritmos en Acción
- Emergencia

## Hitos Principales

### 2026
- **10 ene**: Documentation Sprint - 8 CLAUDE.md, actualización knowledge graph
- **10 ene**: Sincronización portal (showcase + index) con conteos correctos

### 2025
- **Dic**: Math Sound Lab (8 sims) - Game of Life musical, Fourier, Lorenz
- **Nov**: Math Generative Art Lab (7 sims) - Reacción-difusión, L-Systems
- **Oct**: Astronomy Sound Lab (3 sims) - Pulsares, ondas gravitacionales
- **Sep**: Biology Visual Lab expandido - Boids WASM
- **Ago**: Computation Lab (6 sims) - Algoritmos, estructuras de datos
- **Jul**: Geology Visual Lab (8 sims)
- **Jun**: Portal unificado con knowledge graph D3.js
- **May**: Biochemistry Visual Lab (16 sims)
- **Abr**: Chemistry Visual Lab (17 sims)
- **Mar**: Physics Sound Lab - Harmonices Mundi, Tonnetz Atractor
- **Feb**: Math Visual Lab (27 sims)
- **Ene**: Physics Visual Lab (19 sims) - Base del proyecto

## Patrón: Documentación Modular Jerárquica

**Problema**: CLAUDE.md monolítico se volvió unwieldy con 128+ simulaciones

**Solución**: Arquitectura de documentación en tres niveles:

1. **`CLAUDE.md` maestro** (raíz) - Overview general, referencias a labs
2. **Lab-specific `CLAUDE.md`** - Detalles técnicos de cada laboratorio (5+ sims)
3. **Inline comments** - Documentación en código para sims individuales

**Beneficios**:
- Git diffs más claros
- Lectura modular y focalizada
- Escalabilidad sin límite
- Claude Code puede leer solo lo necesario

## Siguientes Pasos

- [ ] Crear CLAUDE.md para Physics Visual Lab (19 sims)
- [ ] Crear CLAUDE.md para Chemistry Visual Lab (17 sims)
- [ ] Crear CLAUDE.md para Math Visual Lab (27 sims)
- [ ] Crear CLAUDE.md para Biochemistry Visual Lab (16 sims)
- [ ] Añadir tests automatizados (simulaciones críticas)
- [ ] PWA support (offline usage)
- [ ] Implementar búsqueda global cross-lab

## Enlaces Relacionados

- **GitHub**: https://github.com/cjlkaiser-cpu/eigenlab
- **EigenLab Instruments**: https://cjlkaiser-cpu.github.io/eigenlab-instruments/
- **Physics Sound Lab**: Submodule con generativos sonoros
- **Math Generative Art Lab**: Submodule con arte algorítmico

---

**Última actualización**: 10 ene 2026
