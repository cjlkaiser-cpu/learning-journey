---
id: bd-parafarmacia
name: BD Parafarmacia + Dashboard
status: active
stack:
  - sqlite
  - streamlit
  - plotly
  - pandas
  - python
repo: ~/Desktop/scripts_python/database/
description: Base de datos SQLite + Dashboard Streamlit para análisis de parafarmacia (22K productos, 18 familias, 771 laboratorios).
---

# BD Parafarmacia + Dashboard

De Excel a base de datos relacional con dashboard interactivo.

## Contexto

Farmacia Zafra Colón tiene un Excel con 22,417 productos de parafarmacia en 18 hojas (una por familia). Se creó una BD SQLite normalizada y un dashboard Streamlit para consultar y analizar los datos.

## Datos de origen

| Dato | Valor |
|------|-------|
| **Fuente** | `Ventas por familias referencia PVP ZAFRA COLÓN.xlsx` |
| **Productos** | 22,417 |
| **Familias** | 18 (Dermo, Nutrición, Capilar, Ocular, Solar...) |
| **Laboratorios** | 771 |
| **Grupos terapéuticos** | 525 |
| **Ventas** | Acumulado 2025 |
| **BD resultante** | 6.4 MB SQLite |

## Arquitectura

```
database/
├── schema.sql          # 6 tablas + índices
├── db.py               # Conexión y helpers
├── importar_excel.py   # Excel → SQLite
├── consultas.py        # 9 consultas CLI
├── dashboard.py        # Dashboard Streamlit (8 tabs)
├── requirements.txt
└── datos/parafarmacia.db
```

### Esquema relacional

- `familias` → `productos` ← `laboratorios`
- `productos` → `precios` (con flag puc_fiable)
- `productos` → `stock`
- `productos` → `ventas` (periodo 2025)

### Dashboard (8 tabs)

1. **Familias** - Facturación, treemap, eficiencia €/SKU
2. **Laboratorios** - Top N, cuota, scatter
3. **Top Productos** - Ranking filtrable por familia
4. **Pareto ABC** - Curva Pareto con umbrales ajustables
5. **Alertas** - Stock muerto (16K€), bajo mínimo, calidad PUC
6. **Ficha Producto** - Buscador + ficha completa
7. **Duplicados** - Detección de productos similares
8. **Consola SQL** - Queries libres con exportación

## Aprendizajes clave

### Lo que funcionó bien

1. **Normalización relacional**: De 27 columnas planas a 6 tablas relacionadas
2. **Flag puc_fiable**: Detectar automáticamente PUC=0 o PUC=PVP (60.4% no fiable)
3. **Streamlit + Plotly**: Dashboard profesional en ~400 líneas de Python
4. **INSERT OR IGNORE + cache**: Manejar duplicados entre hojas del Excel (195 productos)
5. **Filtros globales sidebar**: Un solo WHERE builder para todas las tabs
6. **.command en Desktop**: Doble clic para arrancar dashboard

### Problemas resueltos

- **FK constraint failed**: `INSERT OR IGNORE` silencioso dejaba productos sin insertar → try/except + continue
- **PUC no fiable**: 60% de los datos con PUC=0 o PUC=PVP → flag automático
- **sql() sin params**: Wrapper de pd.read_sql_query necesitaba params=None por defecto
- **Duplicados entre hojas**: 195 productos en múltiples familias → primera aparición gana

### Hallazgos de negocio

- **Stock muerto**: 277 productos, 16K€ inmovilizados (SkinCeuticals domina)
- **Dermocosmética**: 127K€ facturación pero 87% de productos sin venta
- **Eficiencia**: Digestivo tiene mejor €/SKU que Dermocosmética
- **Top labs**: Pierre Fabre (34K€), La Roche Posay (31K€), IFC Cantabria (28K€)

## Roadmap

- **Fase 3**: Calidad datos (afinar scraper, importar Fenix, CIMA/CN)
- **Fase 4**: Scraping a escala (precios online, tab dashboard)
- **Fase 5**: Inteligencia negocio (cruces, alertas compuestas, simulador P&L)
- **Fase 6**: Operativa Colón (datos reales, multi-farmacia)

## Stack técnico

- **BD**: SQLite 3 (incluido en Python)
- **Dashboard**: Streamlit 1.54
- **Gráficos**: Plotly 6.5
- **Datos**: Pandas + openpyxl
- **Arranque**: `.command` en Desktop → Brave Browser

## Relación con otros proyectos

- **scripts_python**: Módulo `database/` dentro del repo principal
- **Análisis Parafarmacia Colón**: Los 10 Excels que este proyecto digitaliza
- **comparador_pvp**: Scraper que alimentará tabla `precios_online`
- **farmaIA**: Mismo dominio (farmacia) pero distinto enfoque (IA vs datos)
