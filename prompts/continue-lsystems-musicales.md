# L-Systems Musicales - Continuación

> Prompt de continuación para implementar L-Systems Musicales en Math Sound Lab

## Descripción
Implementación de gramáticas de Lindenmayer con síntesis de audio sincronizada. Parte del Math Sound Lab de EigenLab. El plan de implementación ya existe y está completo, solo falta ejecutar las 5 fases secuenciales.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/eigenlab
- **Path:** `Mathematics/Math Sound Lab/l-systems-musicales.html`
- **Plan:** `~/.claude/plans/fluttering-pondering-meteor.md`

---

## Contexto Previo

### ✅ Completado (10 ene 2026)

**Documentation Sprint de EigenLab:**
- ✅ 8 archivos CLAUDE.md creados (~2,800 líneas)
- ✅ Knowledge graph actualizado (+8 nodos Math Sound Lab, +14 conexiones)
- ✅ Showcase + portal sincronizados (128+ sims, 14 labs)
- ✅ Vault actualizado (knowledge-base, dashboard, graph, projects/eigenlab.md)
- ✅ 5 commits exitosos (3 repos: main + 2 submodules + vault)

**Math Sound Lab Status:**
- 📊 8 simulaciones documentadas en CLAUDE.md
- 📍 Ubicación: `~/Projects/EigenLab/Mathematics/Math Sound Lab/`
- 🎯 Siguiente simulación: **L-Systems Musicales** (pendiente implementación)

---

## Prompt

```
Vamos a implementar L-Systems Musicales para Math Sound Lab. Tengo el plan completo en `~/.claude/plans/fluttering-pondering-meteor.md`.

## Contexto Rápido

**Plan mode ya ejecutado anteriormente:**
- Plan file existe y está completo
- 5 fases de implementación definidas
- Especificaciones técnicas detalladas

**Simulación a crear:**
- **Archivo**: `~/Projects/EigenLab/Mathematics/Math Sound Lab/l-systems-musicales.html`
- **Concepto**: Gramáticas de Lindenmayer + síntesis de audio sincronizada
- **Features**: 6 presets (Árbol Binario, Planta Fractal, Helecho, Alga, Arbusto, Sierpinski)
- **Stack**: Canvas 2D + Web Audio API (ADSR envelopes)
- **Líneas estimadas**: ~1,400-1,600 (autocontenido)

## Instrucciones

1. **Lee el plan completo** en `~/.claude/plans/fluttering-pondering-meteor.md`

2. **Implementa las 5 fases secuencialmente:**
   - Fase 1 (25%): Backend L-System (clase + expand + test)
   - Fase 2 (25%): Visualización estática (drawTree + auto-scaling)
   - Fase 3 (20%): Audio engine (generateAudioEvents + playNote)
   - Fase 4 (20%): Sincronización (playLoop + animación progresiva)
   - Fase 5 (10%): UI completa (sidebar + presets + controles)

3. **Referencias para copiar patrones:**
   - `Mathematics/Math Sound Lab/game-of-life-musical.html` - Audio properties
   - `Mathematics/Math Sound Lab/cadenas-markov-generativas.html` - UI completa
   - `Mathematics/Math Generative Art Lab/l-systems.html` - Algoritmo visual (sin audio)

4. **Checkpoints de verificación:**
   - ✅ String se expande correctamente (test en consola)
   - ✅ Árbol fractal visible con colores graduales
   - ✅ Melodía suena correctamente (sin visual)
   - ✅ Visual y audio sincronizados
   - ✅ Flujo completo funcional (preset → reproducir → cambiar preset)

5. **Después de implementar:**
   - Actualizar `Mathematics/Math Sound Lab/index.html`:
     - Badge: 7 sims → **8 sims**
     - Agregar card para L-Systems Musicales
   - Commit y push:
     ```bash
     cd ~/Projects/EigenLab/Mathematics/Math\ Sound\ Lab/
     git add l-systems-musicales.html index.html
     git commit -m "feat(math-sound): add L-Systems Musicales simulation

     Gramáticas de Lindenmayer con síntesis de audio sincronizada.
     6 presets, editor de reglas, animación progresiva, escalas pentatónicas.

     Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
     git push origin main
     ```

## Especificaciones Técnicas (del plan)

**Clase LSystem:**
- `expand(iterations)` - Genera string expandido
- `generateSegments()` - Convierte string a segmentos visuales con auto-scaling
- `generateAudioEvents()` - Mapea símbolos a eventos musicales

**Mapeo Símbolos → Audio:**
- `F` → tocar nota (pitch según profundidad de stack)
- `+` → transponer arriba (2 semitonos)
- `-` → transponer abajo (2 semitonos)
- `[` → push stack (subir registro +5 semitonos)
- `]` → pop stack (restaurar registro)

**Escalas:**
- Pentatónica menor: [0, 3, 5, 7, 10]
- Pentatónica mayor: [0, 2, 4, 7, 9]

**ADSR Envelope:**
```javascript
gain.gain.setValueAtTime(0, now)
gain.gain.linearRampToValueAtTime(volume * 0.3, now + 0.01)  // Attack
gain.gain.exponentialRampToValueAtTime(0.001, now + duration) // Release
```

## Quick Start

```bash
# Navegar
cd ~/Projects/EigenLab/Mathematics/Math\ Sound\ Lab/

# Leer plan
cat ~/.claude/plans/fluttering-pondering-meteor.md

# Después de implementar
git status
git add l-systems-musicales.html index.html
git commit -m "feat(math-sound): add L-Systems Musicales"
git push
```

Comienza leyendo el plan y ejecutando fase por fase. Pregúntame si algo no está claro.
```

---

## Variables
- `{math-sound-lab-path}` - `~/Projects/EigenLab/Mathematics/Math Sound Lab/`
- `{plan-file}` - `~/.claude/plans/fluttering-pondering-meteor.md`

## Tags
`eigenlab` `math-sound-lab` `l-systems` `web-audio-api` `generative-music` `canvas-2d` `continuation`

## Complejidad
Media-Alta (5 fases, sincronización audio-visual, gramáticas formales)

## Fecha
Enero 2026

## Notas

**Patrón:** Este es un prompt de **continuación**, no de arranque desde cero. El plan mode ya fue ejecutado y el plan está completo en el archivo referenciado. Solo falta implementación.

**Estado previo necesario:**
- Plan file debe existir en `~/.claude/plans/fluttering-pondering-meteor.md`
- Math Sound Lab debe tener 7 simulaciones previas
- CLAUDE.md de Math Sound Lab debe estar documentado

**Output esperado:**
- Archivo HTML autocontenido (~1,500 líneas)
- 6 presets de L-Systems funcionales
- Audio sincronizado con animación visual progresiva
- UI completa con controles y estadísticas
