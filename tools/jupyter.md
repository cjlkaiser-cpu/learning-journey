---
id: jupyter
name: Jupyter Notebook
category: Backend
icon: fa-solid fa-book-open
color: text-orange-500
tag: Entorno Interactivo
status: available
level: learning
next: JupyterLab y extensiones
---

# Jupyter Notebook

Documentos interactivos con código, texto y visualizaciones.

## Por qué usarlo

Exploración de datos, prototipos rápidos, documentación ejecutable. Ideal para aprender y experimentar.

## Casos de uso

- Análisis exploratorio
- Tutoriales interactivos
- Prototipos de ML
- Reportes con código

## Código ejemplo

```python
# En una celda de Jupyter:

import pandas as pd
import matplotlib.pyplot as plt

# Los gráficos aparecen inline
df = pd.read_csv("datos.csv")
df.plot(kind="bar")
plt.show()

# Markdown entre celdas para explicaciones
# Exportar a HTML o PDF para compartir
```

## Instalación

```bash
pip install jupyterlab
jupyter lab  # Abre en navegador
```
