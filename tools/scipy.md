---
id: scipy
name: SciPy
category: Backend
icon: fa-solid fa-flask
color: text-blue-500
tag: Computación Científica
status: available
level: learning
next: Optimización y señales
---

# SciPy

Algoritmos científicos: optimización, integración, álgebra lineal, estadística.

## Por qué usarlo

Extiende NumPy con funciones científicas avanzadas. El equivalente a los toolboxes de MATLAB.

## Casos de uso

- Optimización de funciones
- Procesamiento de señales
- Interpolación
- Tests estadísticos
- Resolver ecuaciones

## Código ejemplo

```python
from scipy import optimize, stats, signal
import numpy as np

# Optimización: encontrar mínimo
def f(x):
    return x**2 + 10*np.sin(x)
result = optimize.minimize(f, x0=0)

# Estadística: test t
t_stat, p_value = stats.ttest_ind(grupo1, grupo2)

# Señales: filtro paso bajo
b, a = signal.butter(4, 0.1)
filtered = signal.filtfilt(b, a, data)
```

## Instalación

```bash
pip install scipy
```
