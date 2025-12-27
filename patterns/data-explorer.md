---
id: data-explorer
name: Explorador de Datos
emoji: 🔬
category: data-eng
problem: Tienes un CSV/Excel y no sabes qué contiene ni cómo está.
prompt: |
  Analiza este dataset y dame un informe exploratorio:

  1. **Estructura**: filas, columnas, tipos de datos
  2. **Estadísticas**: media, mediana, std, min, max por columna numérica
  3. **Valores faltantes**: qué columnas tienen NaN y cuántos
  4. **Valores únicos**: para columnas categóricas
  5. **Correlaciones**: entre variables numéricas
  6. **Anomalías**: outliers o valores sospechosos
  7. **Código**: script de Pandas para generar este análisis
  8. **Siguiente paso**: qué harías con estos datos

  Si me das el archivo, analízalo. Si no, dame el código para hacerlo yo.
flow:
  - python
  - pandas
flowDesc: Datos crudos → Análisis exploratorio → Insights → Siguiente paso
---

# Explorador de Datos

Tienes un CSV/Excel y no sabes qué contiene ni cómo está.

## Ejemplo de uso

"Tengo este CSV de ventas, ¿qué puedo sacar de él?"

O pega las primeras filas:
```
fecha,producto,cantidad,precio
2024-01-01,Widget A,10,25.50
2024-01-02,Widget B,5,
```
