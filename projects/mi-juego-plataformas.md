---
id: mi-juego-plataformas
name: Mi Juego de Plataformas
status: prototype
stack: [phaser, javascript, aseprite]
---

# Mi Juego de Plataformas

Juego de plataformas 2D creado con Phaser.js como proyecto de aprendizaje.

## Ubicacion

`~/Projects/mi-juego-plataformas/`

## Stack

- **Frontend**: HTML5 + JavaScript
- **Motor**: Phaser.js 3.60
- **Arte**: Aseprite (compilado desde source)
- **Servidor**: Python http.server

## Estructura

```
mi-juego-plataformas/
├── index.html          # Pagina principal
├── js/
│   └── game.js         # Logica del juego (590+ lineas)
└── assets/
    ├── personaje.png   # Sprite propio (Aseprite)
    ├── hero.png        # Heroe verde
    ├── ninja.png       # Ninja
    ├── robot.png       # Robot
    └── phaser_dude.png # Phaser Dude
```

## Features

- **3 escenas**: Menu, Juego, Victoria
- **Selector de personajes**: 5 personajes con preview
- **Sistema de registro**: Objeto CHARACTERS con config por sprite
- **Fisica arcade**: Gravedad, colisiones, rebote
- **Enemigos**: Slimes con patrullaje
- **Monedas**: 8 monedas con animacion flotante
- **Controles**: Flechas/WASD + Espacio
- **Reinicio**: R = Reiniciar, ESC = Menu

## Sistema de personajes

```javascript
const CHARACTERS = {
    player_hero: {
        name: 'Heroe Verde',
        file: 'assets/hero.png',
        frameWidth: 16,
        frameHeight: 18,
        scale: 3,
        hitbox: { width: 12, height: 16, offsetX: 2, offsetY: 2 }
    },
    // ... mas personajes
};
```

## Como ejecutar

```bash
cd ~/Projects/mi-juego-plataformas
python3 -m http.server 8888
# Abrir http://localhost:8888
```

## Relacion con EigenLab

Este proyecto comparte la filosofia de EigenLab:
- **Aprendizaje visual**: Ver el resultado inmediatamente
- **Interactividad**: Manipular para entender
- **Progresion gradual**: De simple a complejo

## Aprendido

- Compilar Aseprite desde source
- Scripting Lua para automatizacion
- Workflow Aseprite → Phaser.js
- Escenas y transiciones en Phaser
- Sistema de registro modular para personajes
- Fisica arcade basica
