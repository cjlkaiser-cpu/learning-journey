# MathKids

> Juego educativo de matemáticas para niños con gamificación

## Descripción
App web de juegos matemáticos para niños con múltiples módulos:
sumas, restas, multiplicaciones, divisiones, contar, comparar,
formas, series, reloj, dinero. Sistema de estrellas y modo examen.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/math-kids
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un juego educativo de matemáticas para niños con las siguientes
especificaciones:

## Stack
- HTML5 single-file (~1500 líneas)
- CSS3 con variables y animaciones
- JavaScript ES6+ vanilla
- Google Fonts (Comic Neue - infantil)
- LocalStorage para progreso

## Estructura
```
math-kids/
└── index.html    # Aplicación completa
```

## Paleta de Colores (Infantil)
```css
:root {
    --primary: #FF6B6B;       /* Coral - sumas */
    --secondary: #4ECDC4;     /* Turquesa - restas */
    --accent: #FFE66D;        /* Amarillo - contar */
    --success: #95E1A3;       /* Verde - correcto */
    --error: #FFB3BA;         /* Rosa - error */
    --background: #FFF5E6;    /* Crema */
    --text: #5D4E6D;          /* Púrpura oscuro */
}
```

## Módulos de Juego (12 total)

| Módulo | Color | Descripción |
|--------|-------|-------------|
| Sumas | Coral | Operaciones de suma básicas |
| Restas | Turquesa | Operaciones de resta |
| Multiplicar | Rosa | Tablas de multiplicar |
| Dividir | Morado | División básica |
| Contar | Amarillo | Contar objetos (emojis) |
| Comparar | Lavanda | Mayor/menor/igual |
| Formas | Naranja | Identificar figuras geométricas |
| Series | Verde | Completar secuencias numéricas |
| Reloj | Celeste | Leer la hora |
| Dinero | Dorado | Contar monedas/billetes |
| Paridad | Teal | Par o impar |
| Problemas | Índigo | Problemas de texto simples |

## Interfaz

### Header
- Logo con emoji (🧮)
- Título "MathKids"
- Stats: ⭐ Estrellas totales, 🔥 Racha

### Dashboard (Pantalla Principal)
- Grid responsive de cards de módulos
- Cada card muestra:
  - Icono/emoji del módulo
  - Título
  - Descripción breve
  - Estrellas conseguidas (⭐⭐⭐)
  - Barra de color superior identificativa
- Card especial "Examen" (gradiente multicolor)
- Cards bloqueadas hasta conseguir estrellas

### Pantalla de Juego
- Botón volver (←)
- Barra de progreso (10 preguntas)
- Timer (modo examen)
- Contenedor de pregunta:
  - Visualización con emojis (ej: 🍎🍎 + 🍎 = ?)
  - Texto de la pregunta
  - Opciones de respuesta (4 botones)
- Feedback visual (verde/rojo) con animación

### Pantalla de Resultados
- Estrellas conseguidas (animadas)
- Puntuación: X/10
- Tiempo (si aplica)
- Botón "Jugar de nuevo"
- Botón "Volver al menú"

## Lógica de Juego

### Generador de Preguntas
```javascript
function generateQuestion(module, difficulty) {
    switch(module) {
        case 'sumas':
            const a = random(1, 10 * difficulty);
            const b = random(1, 10 * difficulty);
            return {
                visual: '🍎'.repeat(a) + ' + ' + '🍎'.repeat(b),
                text: `${a} + ${b} = ?`,
                answer: a + b,
                options: generateOptions(a + b)
            };
        // ... otros módulos
    }
}

function generateOptions(correct) {
    const options = [correct];
    while (options.length < 4) {
        const wrong = correct + random(-3, 3);
        if (wrong > 0 && !options.includes(wrong)) {
            options.push(wrong);
        }
    }
    return shuffle(options);
}
```

### Sistema de Estrellas
- ⭐ = 6-7 correctas
- ⭐⭐ = 8-9 correctas
- ⭐⭐⭐ = 10/10 perfectas

### Modo Examen
- 20 preguntas mezcladas de todos los módulos
- Timer de 5 minutos
- Desbloquea con 15 estrellas totales

### Progreso (LocalStorage)
```javascript
const progress = {
    stars: { sumas: 2, restas: 3, ... },
    totalStars: 15,
    streak: 5,
    lastPlayed: "2024-12-12"
};
localStorage.setItem('mathkids-progress', JSON.stringify(progress));
```

## Animaciones

### CSS Keyframes
```css
@keyframes popIn {
    from { transform: scale(0); }
    to { transform: scale(1); }
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-10px); }
    75% { transform: translateX(10px); }
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-20px); }
}

@keyframes starSpin {
    from { transform: rotate(0deg) scale(0); }
    to { transform: rotate(360deg) scale(1); }
}
```

### Feedback Visual
- Respuesta correcta: fondo verde, confetti de emojis
- Respuesta incorrecta: shake, fondo rojo breve
- Nueva estrella: animación de giro y brillo

## Responsive
- Mobile-first
- Cards en grid auto-fit
- Botones grandes para táctil
- Fuente legible (Comic Neue, tamaños grandes)

## Sonido (Opcional)
- Sonido de acierto (campana)
- Sonido de error (buzzer suave)
- Aplausos al completar

## Convenciones
- Idioma: Español
- Tipografía infantil (Comic Neue)
- Colores brillantes y alegres
- Emojis para visualización
- Bordes redondeados (25px)
- Sombras suaves
- Sin anuncios ni distracciones
```

---

## Tags
`educación` `niños` `matemáticas` `juego` `gamificación` `responsive`

## Complejidad
Media (~1.5k LOC) - Múltiples módulos con generación procedural

## Fecha
Diciembre 2024
