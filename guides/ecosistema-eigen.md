# Ecosistema Eigen

> Un universo de proyectos educativos conectados por la curiosidad

---

## Vista General

```
                         EIGEN ECOSYSTEM
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   SIMULACIONES            AUDIO               EDUCATIVO
        │                     │                     │
   ┌────┴────┐           ┌────┴────┐          ┌────┴────┐
   │         │           │         │          │         │
EigenLab  eigenlab    EigenLab  EigenLab   EigenLab  Eigen
 (Labs)    -core     Instruments Genertic   Odyssey  Robotics
   │         │           │         │          │         │
 150+     C++/WASM    7 JUCE    6 Muse-    Juego    11 Arduino
 sims     engine     plugins    Score     narrativo  +LEGO
```

---

## 1. EigenLab (Simulaciones)

**Qué es**: 12 laboratorios con 150+ simulaciones interactivas de ciencia.

**Ubicación**: `~/Projects/EigenLab/`

**Laboratorios**:

| Lab | Sims | Tecnología | Highlights |
|-----|------|------------|------------|
| Physics Visual Lab | 25+ | Canvas | Relatividad, Lagrangiana, N-cuerpos |
| Physics Sound Lab | 19 | Web Audio | 11 generativos + 8 metrónomos |
| Chemistry Visual Lab | 17 | Three.js | Orbitales 3D, reacciones |
| Math Visual Lab | 22 | Canvas | Topología, fractales, grupos |
| Math Generative Art | 7 | Canvas | Perlin, IFS, Gray-Scott |
| Euler Lab | 20 | Pyodide | Project Euler con Python |
| Biology Visual Lab | 6 | Canvas | Hodgkin-Huxley, Lotka-Volterra |
| Biochem Visual Lab | 16 | Canvas | Michaelis-Menten, genética |
| Astronomy Visual Lab | 6 | Canvas | Órbitas, estrellas |
| Astronomy Sound Lab | 3 | Web Audio | Púlsares, ondas gravitacionales |
| Geology Visual Lab | 6 | Canvas | Tectónica, volcanes |
| Computation Lab | 6 | Canvas | BST, DFA, Perceptrón |

**GitHub Pages**:
- https://cjlkaiser-cpu.github.io/physics-visual-lab/
- https://cjlkaiser-cpu.github.io/chemistry-visual-lab/
- https://cjlkaiser-cpu.github.io/math-visual-lab/

---

## 2. eigenlab-core (Motor C++/WASM)

**Qué es**: Motor de alto rendimiento compilado a WebAssembly.

**Ubicación**: `~/Projects/EigenLab/eigenlab-core/`

**Specs**:
- 158KB compilado
- 5 simulaciones pesadas @ 60fps
- Algoritmos: Navier-Stokes, Boids, N-body Barnes-Hut, Erosion, Cloth PBD

**Uso**: Se importa en labs que necesitan rendimiento extremo.

---

## 3. EigenLab Instruments (Plugins JUCE)

**Qué es**: 7 plugins de síntesis física para DAWs.

**Ubicación**: `~/Projects/eigenlab-instruments/`

**Plugins**:

| Plugin | Síntesis | Estado |
|--------|----------|--------|
| ResonantGraphSynth | Karplus-Strong + grafos | Activo |
| GravityWell | RK4 + Karplus-Strong | Producción |
| MembraneSynth | Bessel membrane physics | Producción |
| ModalPercussion | Modal 2-pole resonators | Producción |
| ModalKeys | Modal (Marimba, Rhodes) | Producción |
| FluidHarmonicField | Fluidos + armonía | Producción |
| HarmonicGrooveEngine | Autómata celular | WIP |

**Stack**: C++17 + JUCE + CMake

**GitHub Pages**: https://cjlkaiser-cpu.github.io/eigenlab-instruments/

---

## 4. EigenLab Generative (Plugins MuseScore)

**Qué es**: 6 plugins de composición algorítmica para MuseScore 4.

**Ubicación**: `~/Projects/eigenlab-generative/`

**Plugins**:

| Plugin | Función |
|--------|---------|
| RameauJazz | Generador jazz con Markov chains |
| RameauBach | Estilo Bach con voice leading |
| RameauPiano | Texturas pianísticas |
| RameauGuitar | Patrones guitarra |
| RameauGenerator | Generador base |
| DeepBach | Coral estilo Bach |

**Stack**: QML + JavaScript

**Web App**: https://cjlkaiser-cpu.github.io/rameau-jazz-web/ (Vue + Tone.js)

---

## 5. EigenLab Odyssey (Juego Narrativo)

**Qué es**: Juego que conecta las 150+ simulaciones en una narrativa.

**Ubicación**: `~/Projects/eigenlab-odyssey/`

**Concepto**:
- 9 reinos (uno por disciplina)
- 12 eigenvalores que desbloquear
- Sistema de exploración
- Conecta con simulaciones reales

**Stack**: Phaser.js + Vite + Web Audio

---

## 6. EigenRobotics (Arduino + LEGO)

**Qué es**: 11 proyectos para aprender robótica en familia.

**Ubicación**: `~/Projects/eigenrobotics/`

**Proyectos**:

| # | Proyecto | Conceptos |
|---|----------|-----------|
| P0 | Blink | digitalWrite, delay |
| P1 | Semáforo | Secuencias, timing |
| P2 | Nave Luces | PWM, efectos |
| P3 | Alarma | PIR, buzzer |
| P4 | Girasol | LDR, servo |
| P5 | Robot | Motores DC, L298N |
| P6 | Control Remoto | IR, VS1838B |
| P7 | Brazo Robótico | 3 servos, potenciómetros |
| P8 | Seguidor Línea | IR reflectivo, PID básico |
| P9 | LCD | I2C, caracteres custom |
| P10 | Comunicación | Serial, protocolo comandos |

**Stack**: Arduino C++ + HTML/CSS/JS (showcase)

**GitHub Pages**: https://cjlkaiser-cpu.github.io/eigenrobotics/

---

## 7. EigenTools (Herramientas Rust)

**Qué es**: 11 herramientas educativas de monitoreo con Dual UI (Web + TUI).

**Ubicación**: `~/Projects/eigentools/`

**Tools**:

| Tool | Función |
|------|---------|
| eigentools-launcher | TUI central |
| network-watcher | Monitor de red |
| process-watcher | Monitor procesos |
| disk-watcher | Monitor disco |
| memory-lab | Explorador memoria |
| crypto-lab | Criptografía interactiva |
| http-lab | Cliente HTTP educativo |
| json-explorer | Visualizador JSON |
| regex-lab | Tester regex |
| sql-lab | Sandbox SQL |
| auth-playground | Lab autenticación |

**Stack**: Rust + Axum + Ratatui + Tokio

**Patrón**: Dual UI - `Arc<RwLock<State>>` compartido entre Web y TUI

---

## Conexiones Entre Proyectos

```
EigenLab Odyssey ──────► EigenLab (150+ sims)
        │                      │
        │                      ▼
        │               eigenlab-core (rendimiento)
        │
        ▼
EigenRobotics ◄──────── Conceptos físicos de EigenLab
        │
        ▼
EigenTools ◄─────────── Patrón Dual UI reutilizable

EigenLab Instruments ◄── Física del sonido (Physics Sound Lab)
        │
        ▼
EigenLab Generative ◄─── Teoría musical aplicada
```

---

## Filosofía Común

1. **Educativo primero**: Todo debe enseñar algo
2. **Interactivo**: No solo leer, experimentar
3. **Progresivo**: De simple a complejo
4. **Conectado**: Los proyectos se alimentan entre sí
5. **Open source**: Compartir conocimiento

---

## Estadísticas

| Métrica | Total |
|---------|-------|
| Simulaciones | 150+ |
| Plugins Audio | 13 |
| Tools Rust | 11 |
| Proyectos Arduino | 11 |
| Labs | 12 |

---

## Próximos Pasos

- [ ] Publicar más labs en GitHub Pages
- [ ] Integrar eigenlab-core en más simulaciones
- [ ] Completar HarmonicGrooveEngine
- [ ] Expandir EigenLab Odyssey
- [ ] Documentar patrones reutilizables

---

> "Piano piano se arriva lontano"
>
> El ecosistema Eigen crece poco a poco, pero cada pieza encaja.
