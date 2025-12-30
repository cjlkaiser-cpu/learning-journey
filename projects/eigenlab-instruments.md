---
id: eigenlab-instruments
name: EigenLab Instruments
status: active
stack: [cpp, juce, cmake]
---

# EigenLab Instruments

7 sintetizadores de modelado físico en C++/JUCE.

## Links

- **GitHub**: https://github.com/cjlkaiser-cpu/eigenlab-instruments
- **Pages**: https://cjlkaiser-cpu.github.io/eigenlab-instruments/
- **Local**: `~/Projects/eigenlab-instruments/`

## Plugins

| Plugin | Algoritmo | Estado |
|--------|-----------|--------|
| ResonantGraphSynth | Karplus-Strong + grafos | Alpha |
| HarmonicGrooveEngine | Game of Life | WIP |
| ModalPercussion | Síntesis modal (metales) | Pending |
| **ModalKeys** | Resonadores 2-pole | Alpha |
| GravityWell | RK4 orbital | In Dev |
| MembraneSynth | Bessel membranes | In Dev |
| FluidHarmonicField | Navier-Stokes | In Dev |

## Algoritmos Clave

### Modal Synthesis (ModalKeys)
```
y[n] = x[n] + 2r·cos(ω)·y[n-1] - r²·y[n-2]
```
- Resonadores 2-pole sin delay lines
- T60 decay mapping
- Inharmonicidad: `f_n = n × f_1 × √(1 + B × n²)`

### Karplus-Strong (ResonantGraphSynth)
```
y[n] = (y[n-L] + y[n-L-1]) / 2 × g
```

## Changelog

- **30 dic 2025**: ModalKeys completado, publicado en GitHub Pages
- **26 dic 2025**: Showcase page con animaciones canvas
- **24 dic 2025**: 6 plugins base implementados
