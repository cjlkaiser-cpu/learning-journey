# Obsidian Dataview

> Prompt de reproducción - Plugin para tratar Obsidian Vault como base de datos

## Descripción
Plugin de Obsidian que permite hacer queries tipo SQL sobre el vault de Markdown. Extrae metadatos de frontmatter e inline fields, y los presenta en tablas, listas, calendarios y vistas personalizadas.

## Fuente
- **Repo:** https://github.com/blacksmithgu/obsidian-dataview
- **Autor:** Michael Brenan
- **Licencia:** MIT

---

## Prompt

```
Crea un plugin de Obsidian que trate el vault como una base de datos consultable
con las siguientes especificaciones:

## Stack
- TypeScript 5.x
- Rollup como bundler
- Jest para testing
- Preact para componentes UI
- Luxon para manejo de fechas
- Parsimmon para parsing de queries
- CodeMirror 6 para extensiones del editor
- API de Obsidian (Plugin, MarkdownPostProcessor, etc.)

## Estructura del Proyecto
```
src/
├── main.ts              # Entry point del plugin, extiende Plugin
├── settings.ts          # Configuración del plugin
├── index.ts             # Exports públicos de la API
├── api/                 # API pública (DataviewApi, DataviewInlineApi)
├── query/               # Parser y estructura de queries DQL
├── expression/          # Parser de expresiones inline
├── data-model/          # Tipos de datos (Link, Literal, PageMetadata)
│   └── serialized/      # Versiones serializadas para cache
├── data-index/          # Índice del vault (FullIndex, PrefixIndex)
├── data-import/         # Importación de datos
│   └── web-worker/      # Worker para indexación en background
├── ui/                  # Componentes de UI
│   ├── views/           # Vistas (inline, JS, calendar)
│   ├── export/          # Exportación a markdown
│   └── render.ts        # Funciones de renderizado
├── util/                # Utilidades (locale, normalize, paths)
└── test/                # Tests unitarios
```

## Lenguaje de Queries (DQL)
Implementar un DSL pipeline-based similar a SQL:
- TABLE: Muestra resultados en tabla
- LIST: Lista simple con links
- TASK: Lista de tareas
- CALENDAR: Vista calendario

Sintaxis:
```
TABLE campo1, campo2
FROM "carpeta" OR #tag
WHERE condicion
SORT campo DESC
GROUP BY campo
LIMIT n
```

## Tipos de Datos
Interface Literal con tipos:
- string, number, boolean, null
- date (DateTime de Luxon)
- duration
- link (referencia a archivo)
- array, object
- function, widget

## Fuentes de Metadatos
1. YAML Frontmatter:
   ```yaml
   ---
   rating: 8
   author: "Nombre"
   ---
   ```

2. Inline Fields (sintaxis propia):
   ```markdown
   Campo:: Valor
   [campo:: valor inline]
   (campo:: valor oculto)
   ```

## Modos de Query
1. Codeblocks DQL:
   ```dataview
   TABLE rating FROM #book
   ```

2. Codeblocks JavaScript:
   ```dataviewjs
   dv.table(["Name"], dv.pages("#book").map(p => [p.file.name]))
   ```

3. Inline DQL: `= this.file.name`

4. Inline JS: `$= dv.current().rating`

## API JavaScript (DataviewApi)
Métodos principales:
- pages(source): DataArray de páginas
- pagePaths(source): Array de rutas
- page(path): Página individual
- current(): Página actual
- table(headers, rows): Renderiza tabla
- list(items): Renderiza lista
- taskList(tasks): Lista de tareas
- paragraph(text): Párrafo
- header(level, text): Encabezado
- execute(query): Ejecuta DQL
- executeJs(code): Ejecuta JavaScript

## Sistema de Índice
- FullIndex: Índice completo del vault
- Actualización reactiva cuando cambian archivos
- Persistencia con localforage
- Web Worker para indexación en background
- Debounced refresh de vistas

## Configuración (Settings)
- enableInlineDataview: boolean
- enableDataviewJs: boolean
- inlineQueryPrefix: "=" por defecto
- inlineJsQueryPrefix: "$=" por defecto
- refreshEnabled: boolean
- refreshInterval: ms
- defaultDateFormat: formato Luxon
- taskCompletionTracking: auto-completar tareas
- prettyRenderInlineFields: renderizado bonito

## Comandos
- Force refresh all views
- Drop cached metadata
- Rebuild current view

## Integración con CodeMirror 6
- Syntax highlighting para dataviewjs
- Live preview de inline fields
- Extensiones de editor personalizadas

## Convenciones
- TypeScript estricto
- Prettier para formateo
- Tests con Jest
- Documentación con MkDocs
- Versionado semántico

## Archivos de Configuración Obsidian
manifest.json:
{
  "id": "dataview",
  "name": "Dataview",
  "version": "x.x.x",
  "minAppVersion": "0.13.11",
  "isDesktopOnly": false
}

## Características Avanzadas
- DataArray: wrapper funcional sobre arrays con métodos chainables
- Grouping y agregación
- Funciones built-in (date, duration, link, etc.)
- Soporte para CSV
- Exportación a markdown
- Calendar UI component
```

---

## Complejidad
Alta - Este es un proyecto de ~15k LOC con parser propio, sistema de indexación,
integración profunda con Obsidian API, y múltiples modos de renderizado.

## Fecha de Análisis
Diciembre 2024
