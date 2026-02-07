---
id: streamlit
name: Streamlit
category: Data
icon: fa-chart-line
color: text-red-300
tag: Dashboard
status: used
level: solid
next: Multi-page apps, deploy en Streamlit Cloud
---

# Streamlit

Framework Python para crear dashboards web interactivos sin HTML/CSS/JS.

## Por qué lo uso

Dashboards profesionales en Python puro. Ideal para análisis de datos con visualización inmediata.

## Casos de uso

- Dashboard Parafarmacia (8 tabs, filtros globales, exportación Excel)
- Visualización de datos con Plotly integrado
- Consola SQL interactiva
- Buscadores con fichas de producto

## Código ejemplo

```python
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Mi Dashboard", layout="wide")

# KPIs
c1, c2 = st.columns(2)
c1.metric("Productos", "22,417")
c2.metric("Facturación", "486K €")

# Sidebar filtros
with st.sidebar:
    familia = st.multiselect("Familia", opciones)

# Gráficos Plotly
fig = px.bar(df, x="familia", y="venta")
st.plotly_chart(fig, use_container_width=True)

# Tablas con formato
st.dataframe(df.style.background_gradient(cmap="Blues"))

# Exportar Excel
st.download_button("Descargar", to_excel(df), "datos.xlsx")
```

## Aprendizajes clave

- `st.cache_resource` para conexiones BD persistentes
- `st.tabs()` para organizar contenido
- Plotly se integra nativamente con `st.plotly_chart()`
- `sql()` wrapper con params para queries parametrizadas
- `.command` file en macOS para arranque con doble clic

## Proyectos que lo usan

- BD Parafarmacia Dashboard (8 tabs, 22K productos, Streamlit + Plotly + SQLite)
