# Dashboard Trebol Farmacias

> Prompt de reproducción para recrear el dashboard de objetivos de ventas

## Descripción
Dashboard single-file HTML para visualizar objetivos de ventas de una farmacia, con comparativas interanuales, exportación a CSV/Excel, y diseño dark mode responsive.

---

## Prompt

```
Crea un dashboard de objetivos de ventas para una cadena de farmacias con las
siguientes especificaciones:

## Stack
- HTML5 single-file (todo en un archivo .html)
- CSS3 con variables CSS (custom properties)
- JavaScript vanilla (ES6+)
- Librería externa: SheetJS (xlsx.full.min.js) vía CDN para exportar a Excel
- Google Fonts: Inter

## Estructura/Módulos
Un único archivo HTML que contiene:
1. Estilos CSS inline (<style>) con diseño dark mode
2. Markup HTML semántico
3. JavaScript inline (<script>) para lógica y datos

## Diseño Visual
- Tema oscuro: fondo #0a0a0a, texto #ffffff
- Acento rojo: #ff4444 (botones, highlights)
- Colores semánticos: verde (#22c55e) éxito, amarillo (#eab308) warning
- Tipografía: Inter, fuente monoespaciada para números
- Responsive con CSS Grid y media queries (breakpoint 768px)
- Animaciones CSS (fadeInUp) al scroll con IntersectionObserver

## Componentes UI
1. Navbar sticky con logo, selectores (farmacia, año) y botones exportar
2. Header con badge, título y subtítulo dinámicos
3. Grid de stats cards (5): Venta Anual, Objetivo, Media Diaria, %SOE, %Libre
4. Tabla de desglose mensual con 11 columnas, indicadores de colores
5. Sección de gráficos (6 chart-cards):
   - Barras horizontales ventas mensuales
   - Anillos comparativos cumplimiento (2024 vs 2025)
   - Barras evolución venta media diaria (2023→2025)
   - Distribución SOE vs Libre
   - Comparativa 2024 vs 2025 (barras superpuestas)
   - Crecimiento mensual vs año anterior
6. Footer con créditos
7. Toast notifications para feedback de exportación

## Modelos de Datos
Objeto allData con estructura por año:
{
  año: {
    comparaConAno: number,
    cumplioObjetivo: boolean,
    nota?: string,
    totales: { ventaAA, objetivo, pctObjetivo, ventaMes, objMediaDia,
               ventaMediaDia, pctSOE, pctLibre, crecimiento },
    meses: [{ mes, ventaAA, objetivo, pctObjetivo, pctCrecDia, pctCrecMes,
              ventaMes, objMediaDia, ventaMediaDia, pctSOE, pctLibre }]
  }
}

## Features
- Selector de año (2023, 2024, 2025) que actualiza todo el dashboard dinámicamente
- Exportación a CSV (con BOM UTF-8, separador ;)
- Exportación a Excel (.xlsx) con SheetJS
- Formateo de números al estilo español (1.234.567)
- Indicadores visuales de cumplimiento (círculos verde/amarillo/rojo)
- Highlight automático para crecimientos >25%
- Notas contextuales cuando hay datos parciales

## Convenciones
- Idioma: español (UI y comentarios)
- Números formateados con locale es-ES
- Porcentajes con coma decimal (ej: 108,66%)
- Nombres descriptivos en español: formatNumber, changeYear, updateDashboard
- CSS BEM-like simplificado: .stat-card, .chart-card, .bar-fill

## Variables de Entorno
Ninguna - todo autocontenido en el HTML

## Características Técnicas
- Zero dependencies server-side (funciona abriendo el .html directamente)
- CDN para SheetJS y Google Fonts
- IntersectionObserver para animaciones on-scroll
- Event delegation mínimo, listeners en DOMContentLoaded
```

---

## Proyecto Original
`/Users/carlos/dashboard-trebol-farmacias/`

## Fecha
Diciembre 2024
