---
id: numpy
name: NumPy
category: Backend
icon: fa-solid fa-calculator
color: text-blue-400
tag: Computación Numérica
status: available
level: learning
next: Broadcasting y vectorización
---

# NumPy

El MATLAB de Python. Arrays multidimensionales y operaciones matemáticas rápidas.

## Por qué usarlo

Es la base de TODO el stack científico de Python. Pandas, SciPy, TensorFlow... todos usan NumPy por debajo.

## Casos de uso

- Operaciones con matrices
- Álgebra lineal
- Estadística básica
- Procesamiento de señales

## Código ejemplo

```python
import numpy as np

# Crear array
arr = np.array([1, 2, 3, 4, 5])

# Operaciones vectorizadas (sin loops!)
arr * 2  # [2, 4, 6, 8, 10]

# Matrices
matrix = np.array([[1, 2], [3, 4]])
np.linalg.inv(matrix)  # Inversa

# Estadística
np.mean(arr), np.std(arr), np.median(arr)
```

## Instalación

```bash
pip install numpy
```
