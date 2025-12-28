---
id: euler-lab
name: Euler Lab
status: active
stack: [HTML, Tailwind, Pyodide, Python, Canvas]
---

# Euler Lab

Plataforma pedagógica de soluciones a Project Euler con ejecución de Python en navegador.

## Ubicación

`~/Projects/EigenLab/Mathematics/Euler Lab`

## GitHub

https://github.com/cjlkaiser-cpu/euler-lab

## Características

- **20 problemas** (001-020) implementados
- **Pyodide** para ejecutar Python directamente en el navegador
- **2-4 niveles por problema** según complejidad pedagógica
- **Animaciones Canvas** en cada card del index
- **Navegación** con links prev/next entre problemas
- **Filtros** por categoría (Números, Secuencias, Primos, Combinatoria, Strings)

## Filosofía Pedagógica

Cada problema tiene niveles flexibles (2-4) según lo que enseña:

| Nivel | Enfoque | Ejemplo |
|-------|---------|---------|
| 1 | Entendimiento - visualización, intuición | Por qué greedy falla |
| 2 | Fuerza bruta - implementación directa | Bucles anidados |
| 3 | Pythónico - idiomático, generators, stdlib | `math.comb()`, `datetime` |
| 4 | Matemático - fórmulas cerradas, historia | Gauss, Euler, combinatoria |

## Problemas Completados

| # | Problema | Niveles | Concepto Principal |
|---|----------|---------|-------------------|
| 001 | Múltiplos de 3 y 5 | 4 | Aritmética, Gauss |
| 002 | Fibonacci pares | 3 | Secuencias, generadores |
| 003 | Factor primo mayor | 3 | Factorización |
| 004 | Palíndromo más grande | 3 | Strings, optimización |
| 005 | MCM 1-20 | 3 | GCD, Euclides |
| 006 | Suma vs cuadrado | 3 | Series, fórmulas |
| 007 | Primo 10001 | 3 | Criba, primalidad |
| 008 | Producto en serie | 3 | Sliding window |
| 009 | Triplete pitagórico | 3 | Geometría, Euclides |
| 010 | Suma de primos | 3 | Criba Eratóstenes |
| 011 | Producto en cuadrícula | 2 | Matrices, direcciones |
| 012 | Número triangular | 3 | Divisores, factorización |
| 013 | Suma grande | 2 | BigInt |
| 014 | Secuencia Collatz | 3 | Memoización, caché |
| 015 | Caminos en cuadrícula | 3 | Combinatoria, DP |
| 016 | Suma dígitos potencia | 2 | BigInt |
| 017 | Letras en números | 3 | Diccionarios, hash tables |
| 018 | Ruta máxima triángulo | 3 | DP bottom-up |
| 019 | Contando domingos | 3 | datetime, modular |
| 020 | Suma dígitos factorial | 2 | Factorial |

## Stack Técnico

- **HTML5** - Estructura semántica
- **Tailwind CSS** - Estilos via CDN
- **Pyodide 0.24.1** - Python en WebAssembly
- **Canvas API** - Animaciones en cards
- **JetBrains Mono** - Tipografía código

## Estructura

```
euler-lab/
├── index.html              # Landing con 20 cards animadas
├── problems/
│   ├── 001/index.html      # Múltiplos de 3 y 5
│   ├── 002/index.html      # Fibonacci pares
│   └── ...                 # Hasta 020
└── CLAUDE.md               # Contexto del proyecto
```

## Changelog

- **28 dic 2024**: Proyecto creado con 20 problemas completos
