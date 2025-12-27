---
id: aseprite
name: Aseprite
category: Frontend
level: learning
---

# Aseprite

Editor de pixel art y animaciones 2D para desarrollo de videojuegos.

## Instalacion

Compilado desde GitHub (gratuito y legal para uso personal):

```bash
# Dependencias
brew install cmake ninja

# Clonar
git clone --recursive https://github.com/aseprite/aseprite.git

# Descargar Skia
# https://github.com/aseprite/skia/releases (m124 para macOS ARM64)

# Compilar
cd aseprite && mkdir build && cd build
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_OSX_ARCHITECTURES=arm64 \
      -DLAF_BACKEND=skia \
      -DSKIA_DIR=$HOME/deps/skia \
      -G Ninja ..
ninja aseprite

# Instalar
cp -R bin/Aseprite.app /Applications/
```

## Ubicacion local

- Source: `~/aseprite-source/`
- Scripts Lua: `~/aseprite-scripts/`
- App: `/Applications/Aseprite.app`

## Scripts Lua creados

| Script | Funcion |
|--------|---------|
| `paleta_personaje.lua` | Crea paleta 11 colores para pixel art |
| `animacion_correr.lua` | Genera 4 frames de ciclo de carrera + tags |
| `exportar_spritesheet.lua` | Exporta PNG + JSON para Phaser.js |

## Atajos importantes

- **B** = Pincel
- **E** = Borrador
- **G** = Bote de pintura
- **M** = Seleccion rectangular
- **Alt+N** = Nuevo frame
- **Enter** = Play/Stop animacion
- **< >** = Navegar frames
- **Cmd+Shift+E** = Export Sprite Sheet

## Workflow tipico

1. New Sprite → 32x32 px, transparente
2. Crear paleta (o usar script)
3. Dibujar frame idle
4. Duplicar frames para animacion
5. Crear tags (Run, Idle, Jump, Fall)
6. Export Sprite Sheet → PNG + JSON

## Aprendido

- Scripting Lua para automatizacion
- Export para Phaser.js
- Animacion por frames
- Paletas indexadas
