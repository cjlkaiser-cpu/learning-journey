---
id: sprite-workflow
name: Workflow Sprite Art → Juego Web
problem: Crear personajes animados y usarlos en un juego web
flow: [aseprite, phaser]
---

# Workflow: Sprite Art → Juego Web

Patron para crear pixel art animado en Aseprite e integrarlo en juegos Phaser.js.

## El flujo completo

```
1. CREAR en Aseprite
   └─ Nuevo sprite → Paleta → Dibujar → Animar
              ↓
2. ORGANIZAR con tags
   └─ Run, Idle, Jump, Fall (cada animacion)
              ↓
3. EXPORTAR como sprite sheet
   └─ File → Export Sprite Sheet → PNG + JSON
              ↓
4. REGISTRAR en Phaser
   └─ CHARACTERS object con frameWidth, scale, hitbox
              ↓
5. CARGAR en preload()
   └─ this.load.spritesheet('player', 'assets/sprite.png', {...})
              ↓
6. ANIMAR en create()
   └─ this.anims.create({ key: 'run', frames: [...] })
              ↓
7. USAR en update()
   └─ player.anims.play('run', true)
```

## Configuracion de sprite en Phaser

```javascript
const CHARACTERS = {
    mi_personaje: {
        name: 'Nombre Display',
        file: 'assets/nombre.png',
        frameWidth: 32,      // Ancho de cada frame
        frameHeight: 32,     // Alto de cada frame
        scale: 2,            // Escala visual (x2, x3...)
        hitbox: {
            width: 20,       // Ancho del hitbox
            height: 28,      // Alto del hitbox
            offsetX: 6,      // Offset X desde esquina
            offsetY: 4       // Offset Y desde esquina
        }
    }
};
```

## Scripts Lua utiles

| Script | Uso |
|--------|-----|
| `paleta_personaje.lua` | Crea paleta optimizada |
| `animacion_correr.lua` | Genera frames + tags |
| `exportar_spritesheet.lua` | Exporta a Phaser |

## Ubicacion scripts

```bash
~/aseprite-scripts/           # Fuente
~/Library/Application Support/Aseprite/scripts/  # Instalados
```

## Tamaños recomendados

| Tipo | Tamaño | Uso |
|------|--------|-----|
| Retro simple | 16x16 | NES-style |
| Platformer | 32x32 | Balance detalle/simplicidad |
| Detallado | 64x64 | Mas expresivo |

## Frames por animacion

| Animacion | Frames | Notas |
|-----------|--------|-------|
| Idle | 2-4 | Respiracion sutil |
| Run | 4-6 | Ciclo de carrera |
| Jump | 1-2 | Pose ascendente |
| Fall | 1-2 | Pose descendente |

## Conexion con EigenLab

Este workflow aplica los principios de EigenLab:
- **Visual State**: El sprite ES el estado visible del personaje
- **Manipulacion directa**: Editar → Ver resultado inmediato
- **Modularidad**: Cada animacion es independiente

## Fuentes de sprites gratuitos

| Sitio | Licencia |
|-------|----------|
| itch.io/game-assets | Varía |
| OpenGameArt.org | CC0/GPL |
| Kenney.nl | CC0 (100% libre) |
