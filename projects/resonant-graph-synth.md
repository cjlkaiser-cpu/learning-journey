---
id: resonant-graph-synth
name: Resonant Graph Synth
status: active
stack: [cpp, juce, cmake, karplus-strong]
repo: https://github.com/cjlkaiser-cpu/resonant-graph-synth
---

# Resonant Graph Synth

Sintetizador fisico-armonico basado en una red de resonadores acoplados.

## Concepto

Cada nota es un **nodo** en un grafo musical. Cuando tocas una nota:
1. Se inyecta energia en ese nodo
2. La energia se propaga por las conexiones del grafo
3. Los nodos vecinos resuenan simpaticamente
4. El timbre emerge de la topologia

## Stack

- **C++17** - Motor DSP
- **JUCE 7.x** - Framework audio/GUI
- **CMake** - Build system
- **Karplus-Strong** - Modelo de cuerdas

## Caracteristicas

- 12 nodos (una octava) con resonadores Karplus-Strong
- Topologias: Chromatic, Fifths, Tonnetz, Harmonic
- Visualizacion en tiempo real del grafo de energia
- Teclado MIDI integrado
- Builds: Standalone + VST3 + AU

## Origen

Evolucion de Sympathetic-12 (Rust/WASM) a una aplicacion nativa JUCE.
Primera incursion en desarrollo de plugins de audio profesionales.

## Aprendizajes

- Arquitectura de plugins JUCE (AudioProcessor, AudioProcessorEditor)
- CMake con JUCE como submodulo
- DSP en tiempo real con buffers de audio
- Creacion de iconos para macOS (.icns)

## Roadmap

Ver ROADMAP.md en el repo para milestones M0-M8.
