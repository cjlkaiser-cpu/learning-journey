---
id: plotly
name: Plotly
category: Data
icon: fa-chart-bar
color: text-violet-300
tag: Visualización
status: used
level: solid
next: Dash (framework completo), animaciones temporales
---

# Plotly

Librería de gráficos interactivos para Python. Hover, zoom, tooltips nativos.

## Por qué lo uso

Gráficos profesionales con interactividad sin escribir JavaScript. Perfecto con Streamlit.

## Casos de uso

- Bar charts horizontales con gradientes de color
- Treemaps proporcionales (facturación por familia)
- Scatter plots con burbujas (tamaño = variable)
- Pie charts de cuota de mercado
- Area charts para curvas de Pareto
- Barras apiladas (ABC, fiabilidad PUC)

## Código ejemplo

```python
import plotly.express as px

# Bar horizontal con gradiente
fig = px.bar(df, x="venta", y="familia", orientation="h",
             color="venta", color_continuous_scale=["#E8F4FD", "#2E86AB"])
fig.update_traces(texttemplate="%{x:,.0f} €", textposition="outside")

# Treemap
fig = px.treemap(df, path=["familia"], values="venta",
                 color="venta", color_continuous_scale=["#F0E6F6", "#A23B72"])

# Scatter con burbujas
fig = px.scatter(df, x="productos", y="venta", size="unidades",
                 color="familia", hover_data=["margen"])
```

## Aprendizajes clave

- `color_continuous_scale` para gradientes sin leyenda
- `coloraxis_showscale=False` limpia el layout
- `yaxis=dict(autorange="reversed")` para barras top→bottom
- Paleta personalizada con lista de hex colors
- `texttemplate` para valores dentro de barras

## Proyectos que lo usan

- BD Parafarmacia Dashboard (12+ gráficos interactivos)
