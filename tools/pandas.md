---
id: pandas
name: Pandas
category: Backend
icon: fa-solid fa-table
color: text-green-400
tag: Análisis de Datos
status: available
level: learning
next: GroupBy y merge
---

# Pandas

DataFrames para análisis de datos. Como Excel pero con superpoderes.

## Por qué usarlo

Cargar CSVs, limpiar datos, filtrar, agrupar, exportar. Todo en pocas líneas.

## Casos de uso

- Leer/escribir CSV, Excel, JSON
- Limpiar y transformar datos
- Análisis exploratorio
- Preparar datos para ML

## Código ejemplo

```python
import pandas as pd

# Leer CSV
df = pd.read_csv("datos.csv")

# Explorar
df.head()           # Primeras 5 filas
df.describe()       # Estadísticas
df.info()           # Tipos de columnas

# Filtrar
mayores = df[df["edad"] > 30]

# Agrupar
df.groupby("ciudad")["ventas"].sum()

# Exportar
df.to_excel("resultado.xlsx")
```

## Instalación

```bash
pip install pandas openpyxl
```
