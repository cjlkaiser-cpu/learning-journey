---
id: eigenlab-generative
name: EigenLab Generative
status: active
stack: [qml, javascript, musescore]
---

# EigenLab Generative

Plugins generativos para MuseScore 4. Generan notas y progresiones en la partitura.

## Filosofía

```
eigenlab-instruments/     → Plugins de AUDIO (VST3/AU, JUCE/C++)
eigenlab-generative/      → Plugins de PARTITURA (MuseScore, QML/JS)
```

## Links

- **GitHub**: https://github.com/cjlkaiser-cpu/eigenlab-generative
- **Local**: `~/Projects/eigenlab-generative/`

## Plugins

| Plugin | Descripción | Estado |
|--------|-------------|--------|
| **RameauSATB** | Progresiones armónicas SATB con Markov | v0.2.0 |
| RameauAnalysis | Análisis armónico de partituras | Roadmap |
| RameauJazz | Progresiones jazz con 7as/9as | Roadmap |
| RameauGuitar | Voicings de guitarra + tablatura | Roadmap |
| RameauPiano | Grand staff con patrones LH/RH | Roadmap |

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

## Changelog

- **01 ene 2026**: Análisis profundo estilos, ROADMAP completo con dependencias
- **01 ene 2026**: Plugin RameauSATB v0.2.0 funcional, 32 acordes max
- **01 ene 2026**: Proyecto creado, portado motor Markov de Rameau Machine
