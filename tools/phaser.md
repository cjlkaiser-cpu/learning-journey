---
id: phaser
name: Phaser.js
category: Frontend
level: learning
---

# Phaser.js

Framework de desarrollo de videojuegos 2D para web (HTML5 + Canvas/WebGL).

## Stack

- **Lenguaje**: JavaScript
- **Fisica**: Arcade Physics (integrada)
- **Render**: Canvas/WebGL automatico
- **Version**: 3.60+

## Instalacion

Via CDN (mas simple):
```html
<script src="https://cdn.jsdelivr.net/npm/phaser@3.60.0/dist/phaser.min.js"></script>
```

## Estructura basica

```javascript
const config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: { gravity: { y: 800 } }
    },
    scene: [MenuScene, GameScene, WinScene],
    pixelArt: true  // Importante para pixel art
};

const game = new Phaser.Game(config);
```

## Metodos clave por escena

```javascript
class GameScene extends Phaser.Scene {
    preload() { }  // Cargar assets
    create() { }   // Inicializar objetos
    update() { }   // Loop del juego
}
```

## Cargar sprites

```javascript
// Sprite sheet
this.load.spritesheet('player', 'assets/personaje.png', {
    frameWidth: 32,
    frameHeight: 32
});

// Con JSON de Aseprite
this.load.aseprite('player', 'assets/personaje.png', 'assets/personaje.json');
```

## Crear animaciones

```javascript
this.anims.create({
    key: 'run',
    frames: this.anims.generateFrameNumbers('player', { start: 0, end: 3 }),
    frameRate: 10,
    repeat: -1
});
```

## Fisica basica

```javascript
// Crear sprite con fisica
player = this.physics.add.sprite(100, 500, 'player');
player.setBounce(0.1);
player.setCollideWorldBounds(true);

// Colisiones
this.physics.add.collider(player, platforms);
this.physics.add.overlap(player, coins, collectCoin, null, this);
```

## Controles

```javascript
cursors = this.input.keyboard.createCursorKeys();

// En update()
if (cursors.left.isDown) {
    player.setVelocityX(-180);
    player.setFlipX(true);
}
```

## Servidor local

```bash
cd mi-juego && python3 -m http.server 8888
```

## Proyecto ejemplo

- Ubicacion: `~/Projects/mi-juego-plataformas/`
- Features: Menu, selector personajes, enemigos, monedas, victoria
- 5 personajes con sistema de registro

## Aprendido

- Escenas y transiciones
- Arcade Physics
- Sprite sheets y animaciones
- Colisiones y overlaps
- Sistema de registro de personajes (CHARACTERS object)
