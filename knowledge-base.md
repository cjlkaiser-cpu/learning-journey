# Knowledge Base 2026

> **Filosofía**: "Piano piano se arriva lontano" - KISS - Salud por delante
> **Principio #0**: MEMORIA EVOLUTIVA - Cada proyecto alimenta al siguiente
> **Última actualización**: 10 enero 2026
>
> **Background**: Lic. Física Teórica (UAM) + Lic. Farmacia 
> **Location**: Madrid, España
>
> **Meta-objetivo:** Los proyectos son vehículos, no destinos.

---

## Estadísticas Acumuladas

| Métrica | Total | Detalle |
|---------|-------|---------|
| Proyectos | 56 | Labs + Plugins + Standalone |
| Simulaciones | 128+ | EigenLab (14 labs) |
| Plugins Audio | 13 | 7 JUCE + 6 MuseScore |
| Tools Rust | 11 | EigenTools (Dual UI) |
| Tools documentadas | 68 | |
| Patterns documentados | 43 | |

### Desglose de Proyectos

| Categoría | Cuenta |
|-----------|--------|
| Labs EigenLab | 14 |
| Plugins JUCE | 7 |
| Plugins MuseScore | 6 |
| Tools EigenTools | 11 |
| Standalone | ~20 |

### Stack Dominado

| Área | Tecnologías |
|------|-------------|
| **Rust** | Tokio, Axum, Ratatui, WASM |
| **C++** | JUCE, Emscripten, WebAssembly |
| **Web** | Canvas, Three.js, Web Audio, PWA |
| **Python** | FastAPI, Flask, Ollama |
| **IA/ML** | RAG, Embeddings, LLMs locales |

---

## Metodologías Propias

### minerOS
ORO → GEMAS → TESORO
```
Tunnels   → Scanner (encuentra)
Pickaxe   → Extractor (extrae)
Gemcutter → Clasificador (genera metadatos)
Pipeline  → IA profunda
Vault     → Base de datos
Compass   → Interfaz web
DirectOS  → Centro de operaciones
```

### Dual UI Pattern
Web + TUI desde estado compartido `Arc<RwLock<State>>`
- Axum para API REST
- Ratatui para terminal
- Sincronización automática

### HITL (Human-in-the-Loop)
Agentes con aprobación humana para tareas críticas.

### Arquitectura Híbrida
Router + Plantillas + LLM fallback = 100% accuracy con 7ms/query.

---

## Ecosistemas Activos

### EigenTools
10 herramientas educativas de monitoreo + TUI launcher
- GitHub: https://github.com/cjlkaiser-cpu/eigentools
- Ubicación: `~/Projects/eigentools/`

### EigenLab
150+ simulaciones educativas (física, química, biología, astronomía, matemáticas)
- Ubicación: `~/Projects/EigenLab/`

### EigenLab Instruments
7 plugins JUCE de síntesis física
- Ubicación: `~/Projects/eigenlab-instruments/`
- GitHub Pages: https://cjlkaiser-cpu.github.io/eigenlab-instruments/

### Physics Sound Lab
Instrumentos generativos de música (Tonnetz, Kepler, Orbifold)
- Ubicación: `~/Projects/physics-sound-lab/`

---

## Proyectos en Desarrollo

| Proyecto | Ubicación | Estado |
|----------|-----------|--------|
| DirectOS | `~/Desktop/DirectOS/` | Evolución continua |
| EigenLab Generative | `~/Projects/eigenlab-generative/` | v0.7.0 + Web App |
| Paper Tonnetz | `~/Desktop/Physics Sound Lab/paper-tonnetz-atractor/` | Redacción |
| Harmonic Groove Engine | `~/Projects/eigenlab-instruments/` | WIP |

---

## Changelog 2026

- **10 ene 2026**: 📚 **EigenLab Documentation Sprint** - Documentación técnica masiva para EigenLab. Creados 8 archivos CLAUDE.md detallados (Biology, Geology, Astronomy Visual/Sound, Computation, Physics Sound, Math Generative Art). Total ~2,800 líneas de documentación técnica. Actualizado knowledge graph (+8 nodos Math Sound Lab, +14 conexiones). Sincronizado showcase + portal con conteos correctos (128+ sims, 14 labs, 9 disciplinas). Commits a 3 repositorios (main + 2 submodules). Patrón: **Documentación Modular Jerárquica**.
- **06 ene 2026**: 🛰️ **Kepler vs Voyager** - Comparativa empírica Kepler (1619) vs NASA Voyager PWS. Pipeline: yt-dlp → ffmpeg → scipy PSD Welch → find_peaks. 4 planetas analizados (Júpiter, Saturno, Urano, Neptuno). Web comparativa con A/B test audio. Conclusión: fenómenos físicamente diferentes (cinemática vs electromagnetismo).
- **06 ene 2026**: 🪐 **Harmonices Mundi NASA Mode** - Nuevo modo de sonificación usando picos espectrales reales de Voyager. Multi-oscillator synthesis (2-3 picos simultáneos por planeta). Síntesis atenuada 30% para planetas interiores. GitHub: https://github.com/cjlkaiser-cpu/harmonices-mundi
- **04 ene 2026**: 🤖 **EigenRobotics** - 11 proyectos Arduino+LEGO para aprender robótica en familia. Showcase interactivo con demos Canvas, diagramas SVG, simuladores Wokwi. P0-P10: Blink, Semáforo, Nave, Alarma, Girasol, Robot, Control IR, Brazo, Seguidor Línea, LCD I2C, Comunicación Serial. GitHub Pages: https://cjlkaiser-cpu.github.io/eigenrobotics/
- **03 ene 2026**: 🎷 **RameauJazz Web v0.2.5** - AI Solo con licks (3050 patrones de Parker, Coltrane, Clifford Brown). Selección inteligente (chord tones, proximity). Export iReal Pro. Sin dependencia TensorFlow (~1MB vs 46MB).
- **02 ene 2026**: 🚀 **RameauJazz Web v0.2.0** - Separado en repo propio. Export MIDI/WAV/PDF, guardar progresiones, GitHub Pages: https://cjlkaiser-cpu.github.io/rameau-jazz-web/
- **02 ene 2026**: 🎹 **RameauJazz Web App v0.1.0** - Generador jazz con Vue 3 + Tone.js + D3.js. Motor Markov (38 acordes, Coltrane changes), FM synth Rhodes, walking bass, drums. Visualización: force graph + piano roll. Tap tempo, swing, 5 voicings, 5 presets.
- **02 ene 2026**: 🎷 **RameauJazz plugin v0.7.0** - 38 acordes jazz (diatónicos, secundarios, tritono subs, borrowed, Coltrane). Modulaciones a 8 targets incluyendo Giant Steps cycle.
- **01 ene 2026**: 🎼 Creado **EigenLab Generative** - Plugins de partitura para MuseScore 4 (QML/JS). RameauSATB v0.2.0: Markov chains + voice leading SATB. Análisis profundo: Bach ≠ "Barroco", Jazz requiere plugin separado (7as). ROADMAP completo v0.2→v1.0 con dependencias (frase→modulación→7as).
- **30 dic 2025**: 🎹 Creado **ModalKeys** - Plugin JUCE de síntesis modal con resonadores 2-pole. Presets: Marimba, Vibraphone, Rhodes, Celesta, Bells. Fórmula: `y[n] = x[n] + 2r·cos(ω)·y[n-1] - r²·y[n-2]`. Publicado eigenlab-instruments en GitHub Pages.
- **28 dic 2025**: Creado **Euler Lab** - 20 problemas de Project Euler con Pyodide (Python en browser), 2-4 niveles pedagógicos cada uno, animaciones Canvas, filtros por categoría. Publicado en GitHub.

---

## Archivo Histórico

- [2025 Year in Review](./archive/2025-year-in-review.md) - Resumen completo + changelog

---

> "Piano piano se arriva lontano"
>
> No es la velocidad, es la dirección.
> No es memorizar, es entender.
> No es que funcione, es que aporte valor.
