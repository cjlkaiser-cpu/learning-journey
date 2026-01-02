---
id: eigenlab-generative
name: EigenLab Generative
status: active
stack: [qml, javascript, musescore, vue, tone.js, d3]
---

# EigenLab Generative

Plugins generativos para MuseScore 4 + Web apps de armonía generativa.

## Filosofía

```
eigenlab-instruments/     → Plugins de AUDIO (VST3/AU, JUCE/C++)
eigenlab-generative/      → Plugins de PARTITURA (MuseScore, QML/JS)
                          → Web apps generativas (Vue/Tone.js)
```

## Links

- **GitHub**: https://github.com/cjlkaiser-cpu/eigenlab-generative
- **Local**: `~/Projects/eigenlab-generative/`

## Plugins

### MuseScore Plugins

| Plugin | Descripción | Estado |
|--------|-------------|--------|
| **RameauSATB** | Progresiones armónicas SATB con Markov | v0.2.0 |
| **RameauJazz** | Jazz con 38 acordes, modulaciones, Coltrane | v0.7.0 |
| RameauAnalysis | Análisis armónico de partituras | Roadmap |
| RameauGuitar | Voicings de guitarra + tablatura | Roadmap |
| RameauPiano | Grand staff con patrones LH/RH | Roadmap |

### Web Apps

| App | Stack | Descripción | Estado |
|-----|-------|-------------|--------|
| **RameauJazz Web** | Vue 3 + Tone.js + D3 | Generador jazz interactivo | v0.1.0 |

## Motor de Markov (RameauSATB)

### Características v0.2.0

- Cadenas de Markov con matrices de transición empíricas
- Gravedad tonal (caos ↔ estructura)
- Modos mayor y menor armónico
- Voice leading SATB con evitación de paralelas
- Cadencia auténtica V-I opcional
- 10 tonalidades, hasta 32 acordes

### Matriz de transición (fragmento)

```javascript
'I':  { 'I': 0.05, 'ii': 0.15, 'IV': 0.25, 'V': 0.30, 'vi': 0.15 }
'V':  { 'I': 0.70, 'vi': 0.14, ... }  // V→I dominante
```

## Análisis Profundo: Estilos

### Decisiones clave

1. **No usar épocas falsas**: "Barroco" ≠ slider. Bach es más complejo que V→I.
2. **Jazz requiere plugin separado**: Arquitectura diferente (7as obligatorias).
3. **Estructura de frase antes de modulación**: Sin frase = modulaciones sin sentido.

### Por qué Bach ≠ "Barroco estricto"

| Lo que esperamos | Lo que Bach realmente hace |
|------------------|---------------------------|
| V→I 80% | V→I ~55-60%, V→vi ~20% |
| Solo triadas | Dominantes secundarias, cromatismo |
| Simple | Secuencias, retardos, suspensiones |

## Roadmap

```
v0.2 ✓ SATB funcional
v0.3   Honestidad (renombrar gravedad, presets)
v0.4   Estructura de frase (antecedente-consecuente)
v0.5   Modulación (pivot chords)
v0.6   Acordes de 7a
v0.7   Presets completos
v1.0   Release estable
```

## RameauJazz Web App

### Stack
- **Frontend**: Vue 3 (Composition API) + Pinia
- **Audio**: Tone.js (FM synth, walking bass, drums)
- **Visualización**: D3.js (force graph) + Canvas (piano roll)
- **Build**: Vite

### Características v0.1.0
- 38 grados de acordes (diatónicos, secundarios, tritono subs, Coltrane)
- Matriz de Markov con transiciones probabilísticas
- 8 targets de modulación (incluido Giant Steps cycle)
- 5 estilos de voicing (shell, drop2, rootless A/B, block)
- Tap tempo y swing ajustable
- Force graph interactivo (click para preview)
- Piano roll con playhead animado
- Presets: Standard, Bebop, Bossa Nova, Modal, Ballad

### Ubicación
`~/Projects/eigenlab-generative/web/rameau-jazz/`

## Changelog

- **02 ene 2026**: RameauJazz Web App v0.1.0 - Vue 3 + Tone.js + D3
- **02 ene 2026**: RameauJazz plugin v0.7.0 - 38 acordes, Coltrane changes
- **01 ene 2026**: Análisis profundo estilos, ROADMAP completo con dependencias
- **01 ene 2026**: Plugin RameauSATB v0.2.0 funcional, 32 acordes max
- **01 ene 2026**: Proyecto creado, portado motor Markov de Rameau Machine
