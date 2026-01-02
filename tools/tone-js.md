---
id: tone-js
name: Tone.js
category: Audio
level: solid
---

# Tone.js

Framework Web Audio para música interactiva en el browser.

## Uso en proyectos

- **RameauJazz Web App** - Síntesis FM, walking bass, drums

## Conceptos clave

### Sintetizadores
```javascript
import * as Tone from 'tone'

// FM Synth (Rhodes-like)
const synth = new Tone.PolySynth(Tone.FMSynth, {
  harmonicity: 3.01,
  modulationIndex: 14,
  envelope: { attack: 0.01, decay: 0.2, sustain: 0.2, release: 0.8 }
})

// Mono synth (bass)
const bass = new Tone.MonoSynth({
  oscillator: { type: 'triangle' },
  envelope: { attack: 0.02, decay: 0.1, sustain: 0.4, release: 0.3 }
})
```

### Effects Chain
```javascript
const tremolo = new Tone.Tremolo(4, 0.3).start()
const reverb = new Tone.Reverb({ decay: 2.5, wet: 0.3 })
const compressor = new Tone.Compressor(-20, 4)

synth.chain(tremolo, reverb, compressor, Tone.Destination)
```

### Transport
```javascript
await Tone.start() // Requiere user gesture

Tone.Transport.bpm.value = 120
Tone.Transport.swing = 0.3

Tone.Transport.scheduleRepeat((time) => {
  synth.triggerAttackRelease('C4', '8n', time)
}, '4n')

Tone.Transport.start()
```

### Draw (sync con animación)
```javascript
Tone.Draw.schedule(() => {
  // Actualizar UI en sync con audio
  updateVisuals()
}, time)
```

## Recursos

- [Tone.js Docs](https://tonejs.github.io/)
