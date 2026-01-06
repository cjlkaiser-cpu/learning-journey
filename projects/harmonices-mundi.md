---
id: harmonices-mundi
name: Harmonices Mundi
status: production
stack: [web-audio-api, canvas, javascript]
---

# Harmonices Mundi

Sistema solar sonificado en tiempo real según Kepler (1619).

## Ubicación
- Local: `~/Projects/EigenLab/Physics/Physics Sound Lab/generativos/harmonices-mundi/`
- GitHub: https://github.com/cjlkaiser-cpu/harmonices-mundi
- Demo: https://cjlkaiser-cpu.github.io/harmonices-mundi/

## Características

### Modos de Sonificación
1. **Kepler 1619** - Intervalos históricos (min/max por excentricidad)
2. **Tiempo Real** - Frecuencia proporcional a velocidad orbital
3. **Musical** - Escala Do mayor (Tierra = La4 440Hz)
4. **NASA Voyager** - Picos espectrales reales de Voyager PWS

### Física
- Ecuación de Kepler resuelta con Newton-Raphson
- 8 planetas con parámetros orbitales reales
- Escalas: lineal, logarítmica, adaptativa

### Audio
- Web Audio API con OscillatorNode + GainNode
- Analyser FFT para espectro en tiempo real
- Multi-oscillator para picos NASA simultáneos

## NASA Mode (06 ene 2026)
Síntesis basada en picos detectados en análisis PSD de Voyager:
- Júpiter: 258.4, 409.1 Hz
- Saturno: 247.6, 53.8, 360.7 Hz
- Urano: 199.2, 59.2, 403.7 Hz
- Neptuno: 199.2, 398.4 Hz

Planetas interiores: síntesis atenuada 30% (sin datos Voyager).

## Proyecto Hermano
→ [kepler-vs-voyager](./kepler-vs-voyager.md) - Comparativa Kepler vs NASA
