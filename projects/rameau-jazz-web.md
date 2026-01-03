---
id: rameau-jazz-web
name: RameauJazz Web
status: production
stack: [vue, tone.js, d3, vite, pinia]
---

# RameauJazz Web

Generador de progresiones armónicas jazz con motor de Markov, visualización interactiva y síntesis de audio en tiempo real.

## Links

- **Demo**: https://cjlkaiser-cpu.github.io/rameau-jazz-web/
- **GitHub**: https://github.com/cjlkaiser-cpu/rameau-jazz-web
- **Local**: `~/Projects/rameau-jazz-web/`

## Stack

| Componente | Tecnología |
|------------|------------|
| Framework UI | Vue.js 3 (Composition API) |
| State | Pinia |
| Audio | Tone.js (FM synth, walking bass, drums) |
| Visualización | D3.js (force graph) + Canvas (piano roll) |
| Build | Vite |
| Export | midi-writer-js, jsPDF |

## Características v0.2.5

### AI Solo Generation
- 3050 licks extraídos de Impro-Visor (Parker, Coltrane, Clifford Brown, Miles Davis)
- Categorías: ii-V-I (515), blues (123), bebop (2412)
- Selección inteligente con chord tone matching y proximity scoring
- Sintetizador MonoSynth tipo trompeta jazz
- Toggle ON/OFF durante playback

### Export iReal Pro
- Genera URLs compatibles con iReal Pro
- Copia al clipboard para importar en la app
- Mapeo de 38 tipos de acordes a notación iReal

### Motor de Armonía
- 38 grados de acordes jazz (diatónicos, secundarios, tritono subs, borrowed, Coltrane)
- Matriz de Markov con transiciones probabilísticas
- 8 targets de modulación (incluido Giant Steps cycle)
- 5 estilos de voicing (shell, drop2, rootless A/B, block)
- Control de gravedad tonal (caos ↔ estructura)

### Audio
- Piano FM estilo Rhodes con tremolo, chorus y reverb
- Walking bass con 4 patrones (Blue Note, Oleaje, Escalar, Cromático)
- Drummer con ride y hi-hat
- Tap tempo y swing ajustable (0-100%)

### Visualización
- Force graph D3.js (nodos = acordes, links = transiciones)
- Piano roll Canvas con playhead animado
- Círculo de quintas interactivo

### Export
- MIDI (multi-track: piano, bass, drums)
- Audio WAV (grabación directa)
- PDF Lead Sheet (estilo Real Book)

### Persistencia
- Guardar/cargar progresiones (LocalStorage)
- Presets: Standard, Bebop, Bossa Nova, Modal, Ballad

## Arquitectura

```
src/
├── engine/          # Motor Markov (38 acordes, modulaciones)
├── audio/           # Tone.js (synth, bass, drums)
├── visualization/   # D3 force graph, Canvas piano roll
├── export/          # MIDI, WAV, PDF
├── storage/         # LocalStorage
├── components/      # Vue components
└── stores/          # Pinia state
```

## Relación con otros proyectos

- Separado de **eigenlab-generative** (que son plugins MuseScore)
- Motor basado en **RameauJazz plugin** (QML) pero reimplementado en JS
- Inspirado en **Rameau Machine** (proyecto original web)

## Changelog

- **03 ene 2026**: v0.2.5 - AI Solo con licks (3050), selección inteligente, export iReal Pro
- **02 ene 2026**: v0.2.0 - Export MIDI/WAV/PDF, guardar progresiones, GitHub Pages
- **02 ene 2026**: Separado en repo propio desde eigenlab-generative
- **02 ene 2026**: v0.1.0 - Motor Markov, audio Tone.js, visualización D3
