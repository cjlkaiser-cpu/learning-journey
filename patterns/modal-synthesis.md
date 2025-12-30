---
id: modal-synthesis
name: Modal Synthesis vs Karplus-Strong
problem: Karplus-Strong siempre suena a "pluck", no a "struck"
flow: [cpp, juce, dsp]
---

# Modal Synthesis vs Karplus-Strong

## El Problema

Karplus-Strong (delay + lowpass) produce sonido de cuerda pulsada.
Para instrumentos golpeados (marimba, vibraphone, bells) se necesita Modal Synthesis.

## La Solución

### Resonador 2-Pole (NO delay lines)

```cpp
y[n] = x[n] + 2r·cos(ω)·y[n-1] - r²·y[n-2]
```

Donde:
- `ω = 2π × freq / Fs` (frecuencia angular)
- `r = 10^(-3 / (T60 × Fs))` (decay mapeado a T60)

### Banco de Resonadores

```
excitation ──┬──► Resonador (f₁) ──►┐
             ├──► Resonador (f₂) ──►┤
             ├──► Resonador (f₃) ──►├──► Σ ──► output
             └──► Resonador (fₙ) ──►┘
```

### Inharmonicidad

```
f_n = n × f_1 × √(1 + B × n²)
```

El coeficiente B varía por registro:
- Graves: B ≈ 0.0004
- Agudos: B ≈ 0.000005

## Comparación

| Karplus-Strong | Modal Synthesis |
|----------------|-----------------|
| Delay + Lowpass | Resonadores 2-pole |
| Suena a "pluck" | Suena a "struck" |
| Agudos decaen rápido | Decay controlado por T60 |
| Simple | Más control tímbrico |

## Aplicación

- **ModalKeys**: Marimba, Vibraphone, Rhodes, Celesta, Bells
- **ModalPercussion**: Campanas, gongs, gamelan

## Referencias

- Smith, J.O. - Physical Audio Signal Processing
- Fletcher & Rossing - The Physics of Musical Instruments
