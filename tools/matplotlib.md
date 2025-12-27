---
id: matplotlib
name: Matplotlib
category: Backend
icon: fa-solid fa-chart-line
color: text-orange-400
tag: Visualización
status: available
level: learning
next: Subplots y estilos
---

# Matplotlib

Gráficos estáticos de calidad publicación. El estándar de Python.

## Por qué usarlo

Crear cualquier tipo de gráfico: líneas, barras, scatter, histogramas, heatmaps...

## Casos de uso

- Gráficos para papers/reportes
- Visualización de datos
- Debugging visual de algoritmos

## Código ejemplo

```python
import matplotlib.pyplot as plt
import numpy as np

# Datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Gráfico simple
plt.plot(x, y)
plt.title("Seno")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.savefig("grafico.png", dpi=300)
plt.show()

# Múltiples gráficos
fig, axes = plt.subplots(2, 2)
axes[0, 0].plot(x, y)
axes[0, 1].bar([1,2,3], [4,5,6])
```

## Instalación

```bash
pip install matplotlib
```
