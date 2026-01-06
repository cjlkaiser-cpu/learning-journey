---
id: kepler-vs-voyager
name: Kepler vs Voyager
status: production
stack: [python, scipy, web-audio-api, ffmpeg, yt-dlp]
---

# Kepler vs Voyager

Comparativa empírica: frecuencias teóricas de Kepler (1619) vs ondas de plasma NASA Voyager (1977-1989).

## Ubicación
- Local: `~/Projects/EigenLab/Physics/Physics Sound Lab/generativos/kepler-vs-voyager/`
- Fuente datos: https://space-audio.org/ (Universidad de Iowa)

## Pipeline de Análisis

```
YouTube (NASA oficial) → yt-dlp → WAV → scipy.signal.welch → PSD
                                           ↓
                                    find_peaks → frecuencias pico
                                           ↓
                                    JSON → Web comparativa
```

## Resultados (06 ene 2026)

| Planeta | NASA Pico (Hz) | Kepler (Hz) | Diferencia |
|---------|----------------|-------------|------------|
| Júpiter | 258.4 | 96.5 | 2.68x |
| Saturno | 247.6 | 71.2 | 3.48x |
| Urano | 199.2 | 50.3 | 3.96x |
| Neptuno | 199.2 | 40.1 | 4.97x |

## Conclusión Científica
Son fenómenos físicamente diferentes:
- **Kepler**: Metáfora matemática basada en velocidad orbital
- **NASA**: Ondas electromagnéticas reales en plasma magnetosférico

La coincidencia sería notable, la diferencia es esperada.

## Scripts
- `01_spectral_analysis.py` - PSD Welch + detección picos
- `02_extract_samples.py` - Clips 5s con fade para web
- `03_kepler_frequencies.py` - Cálculo frecuencias teóricas

## Web
- Visualización espectro (Canvas)
- Audio A/B test (Kepler oscilador vs NASA samples)
- Datos en JSON para cada planeta

## Proyecto Hermano
→ [harmonices-mundi](./harmonices-mundi.md) - Simulación orbital sonificada
