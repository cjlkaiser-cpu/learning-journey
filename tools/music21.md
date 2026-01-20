---
id: music21
name: music21
category: Audio
level: solid
---

# music21

Toolkit de Python para análisis computacional musical. Desarrollado por MIT. Usado para parsing MIDI y análisis armónico.

## Primer uso

**Proyecto:** GPT Bach WTC (20 ene 2026)
**Contexto:** Parser MIDI → tokens, export tokens → MIDI/MusicXML

## Conceptos Básicos

### Load MIDI
```python
import music21 as m21

# Cargar MIDI
score = m21.converter.parse('prelude.mid')

# Analizar estructura
parts = score.parts  # Lista de Part objects
for part in parts:
    print(part.id, len(part.notes))
```

### Stream Hierarchy
```
Score
├── Part 1 (Piano right hand)
│   ├── Measure 1
│   │   ├── Note C4
│   │   ├── Note E4
│   │   └── Rest
│   └── Measure 2
└── Part 2 (Piano left hand)
```

### Notes and Rests
```python
# Crear nota
note = m21.note.Note('C4')
note.quarterLength = 1.0  # Duration
note.offset = 0.0  # Position

# Crear rest
rest = m21.note.Rest()
rest.quarterLength = 0.5

# Chord (multiple notes simultaneous)
chord = m21.chord.Chord(['C4', 'E4', 'G4'])
```

### Extract Notes from MIDI
```python
def extract_notes(midi_path):
    """Extract all notes from MIDI file."""
    score = m21.converter.parse(midi_path)

    notes = []
    for element in score.flatten().notesAndRests:
        if isinstance(element, m21.note.Note):
            notes.append({
                'pitch': element.pitch.nameWithOctave,  # 'C4'
                'midi': element.pitch.midi,  # 60
                'duration': element.quarterLength,
                'offset': element.offset
            })
        elif isinstance(element, m21.note.Rest):
            notes.append({
                'pitch': 'REST',
                'duration': element.quarterLength,
                'offset': element.offset
            })

    return notes
```

### Harmonic Analysis
```python
# Detectar tonalidad
key = score.analyze('key')
print(key.tonic, key.mode)  # C major

# Transpose
transposed = score.transpose('P5')  # Perfect 5th up

# Normalize to C major/A minor
if key.mode == 'major':
    interval = m21.interval.Interval(
        key.tonic,
        m21.pitch.Pitch('C')
    )
else:  # minor
    interval = m21.interval.Interval(
        key.tonic,
        m21.pitch.Pitch('A')
    )

normalized = score.transpose(interval)
```

### Voice Tracking
```python
# Detectar voces en música polifónica
for part in score.parts:
    for voice in part.voices:
        print(f"Voice {voice.id}")
        for note in voice.notes:
            print(f"  {note.nameWithOctave}")
```

## Caso de Uso: GPT Bach WTC

### Parse MIDI → MusicEvents
```python
def parse_midi_to_events(midi_path: Path):
    """Convert MIDI to structured music events."""

    score = m21.converter.parse(midi_path)

    events = []
    bar_offsets = []

    # Get all parts
    for part in score.parts:
        voice_id = 1

        # Track voices
        for element in part.flatten().notesAndRests:
            if isinstance(element, m21.note.Note):
                events.append(MusicEvent(
                    note=element.pitch.nameWithOctave,
                    voice=voice_id,
                    duration=element.quarterLength,
                    time_offset=element.offset,
                    is_rest=False
                ))

            elif isinstance(element, m21.note.Rest):
                events.append(MusicEvent(
                    note='REST',
                    voice=voice_id,
                    duration=element.quarterLength,
                    time_offset=element.offset,
                    is_rest=True
                ))

    # Extract bar boundaries
    for measure in score.parts[0].getElementsByClass(
        m21.stream.Measure
    ):
        bar_offsets.append(measure.offset)

    return events, bar_offsets
```

### MusicEvents → Score (Export)
```python
def events_to_score(events: List[MusicEvent]) -> m21.stream.Score:
    """Convert music events back to music21 Score."""

    score = m21.stream.Score()

    # Metadata
    score.metadata = m21.metadata.Metadata()
    score.metadata.title = "Generated Prelude"
    score.metadata.composer = "MusicGPT (trained on J.S. Bach)"

    # Group by voice
    voices = {}
    for event in events:
        if event.voice not in voices:
            voices[event.voice] = []
        voices[event.voice].append(event)

    # Create parts
    for voice_id, voice_events in voices.items():
        part = m21.stream.Part()
        part.id = f"voice{voice_id}"

        # Add time/key signatures
        part.insert(0, m21.meter.TimeSignature('4/4'))
        part.insert(0, m21.key.Key('C'))

        # Add notes
        current_offset = 0.0
        for event in sorted(voice_events, key=lambda e: e.time_offset):
            if event.is_rest:
                rest = m21.note.Rest()
                rest.quarterLength = event.duration
                part.insert(current_offset, rest)
            else:
                note = m21.note.Note(event.note)
                note.quarterLength = event.duration
                part.insert(current_offset, note)

            current_offset += event.duration

        score.append(part)

    return score
```

### Export Formats
```python
# Export to MIDI
score.write('midi', fp='output.mid')

# Export to MusicXML (MuseScore)
score.write('musicxml', fp='output.musicxml')

# Export to LilyPond
score.write('lilypond', fp='output.ly')

# Show in default viewer
score.show()

# Show in MuseScore specifically
score.show('musicxml.pdf')
```

### Musical Analysis
```python
from music21 import analysis

# Harmonic analysis
chords = score.chordify()
for c in chords.flatten().getElementsByClass(m21.chord.Chord):
    print(c.pitchedCommonName)  # 'C major triad'

# Melodic analysis
melody = score.parts[0].flatten().notes
intervals = []
for i in range(len(melody) - 1):
    interval = m21.interval.Interval(
        melody[i],
        melody[i+1]
    )
    intervals.append(interval.name)  # 'M3', 'P5', etc.

# Rhythm analysis
durations = [n.quarterLength for n in score.flatten().notes]
print(f"Rhythmic variety: {len(set(durations))}")
```

## Integración con Otros Tools

### pretty-midi
```python
# music21 → pretty-midi
import pretty_midi

midi_data = pretty_midi.PrettyMIDI('output.mid')
```

### mido (low-level MIDI)
```python
import mido

# Read MIDI messages
mid = mido.MidiFile('output.mid')
for msg in mid:
    print(msg)
```

### matplotlib (visualization)
```python
import matplotlib.pyplot as plt

# Piano roll from music21
notes = score.flatten().notes
times = [n.offset for n in notes]
pitches = [n.pitch.midi for n in notes]

plt.scatter(times, pitches)
plt.xlabel('Time (quarters)')
plt.ylabel('MIDI Pitch')
plt.show()
```

## Limitaciones

- Lento para archivos MIDI muy grandes
- Parsing puede fallar con MIDIs mal formados
- Voice tracking no siempre es perfecto
- Requiere MuseScore instalado para `show()`

## Recursos

- **Documentación:** https://web.mit.edu/music21/doc/
- **User's Guide:** https://web.mit.edu/music21/doc/usersGuide/
- **Corpus:** Incluye miles de piezas (Bach, Beethoven, etc.)

## Proyectos

- [GPT Bach WTC](../projects/gpt-bach-wtc.md) - MIDI parsing y export

---

**Estado:** Solid - Parsing, análisis y export completo
**Próximo:** Análisis armónico avanzado, detección de patterns
