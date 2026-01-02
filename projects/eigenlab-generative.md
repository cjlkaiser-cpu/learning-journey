---
id: eigenlab-generative
name: EigenLab Generative
status: active
stack: [qml, javascript, musescore]
---

# EigenLab Generative

Plugins generativos para MuseScore 4 (QML/JavaScript).

## Filosofía

```
eigenlab-instruments/     → Plugins de AUDIO (VST3/AU, JUCE/C++)
eigenlab-generative/      → Plugins de PARTITURA (MuseScore, QML/JS)
rameau-jazz-web/          → Web app generativa (Vue/Tone.js) [repo separado]
```

## Links

- **GitHub**: https://github.com/cjlkaiser-cpu/eigenlab-generative
- **Local**: `~/Projects/eigenlab-generative/`

## Plugins MuseScore

| Plugin | Descripción | Estado |
|--------|-------------|--------|
| **RameauGenerator** | Progresiones SATB con Markov | v0.2.0 |
| **RameauGuitar** | Voicings guitarra + arpegios | v0.3.0 |
| **RameauPiano** | Grand staff con patrones LH/RH | v0.3.0 |
| **RameauJazz** | Jazz: 38 acordes, modulaciones, Coltrane | v0.7.0 |

## Motor de Markov (común)

### Características
- Cadenas de Markov con matrices de transición empíricas
- Gravedad tonal (caos ↔ estructura)
- Modos mayor y menor armónico
- Voice leading SATB con evitación de paralelas
- Cadencia auténtica V-I opcional

### Matriz de transición (fragmento)

```javascript
'I':  { 'I': 0.05, 'ii': 0.15, 'IV': 0.25, 'V': 0.30, 'vi': 0.15 }
'V':  { 'I': 0.70, 'vi': 0.14, ... }  // V→I dominante
```

## Análisis Profundo: Estilos

### Decisiones clave

1. **No usar épocas falsas**: "Barroco" ≠ slider. Bach es más complejo que V→I.
2. **Jazz requiere arquitectura diferente**: 7as obligatorias, voicings específicos.
3. **Estructura de frase antes de modulación**: Sin frase = modulaciones sin sentido.

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

## Relacionados

- **[RameauJazz Web](rameau-jazz-web.md)** - Webapp separada (Vue + Tone.js + D3)

## Changelog

- **02 ene 2026**: Webapp separada a repo propio (rameau-jazz-web)
- **02 ene 2026**: RameauJazz plugin v0.7.0 - 38 acordes, Coltrane changes
- **02 ene 2026**: RameauGuitar v0.3.0 - Arpegios y patrones p-i-m-a
- **02 ene 2026**: RameauPiano v0.3.0 - Patrones RH
- **01 ene 2026**: Análisis profundo estilos, ROADMAP completo
- **01 ene 2026**: Plugin RameauSATB v0.2.0 funcional
- **01 ene 2026**: Proyecto creado, portado motor Markov de Rameau Machine
