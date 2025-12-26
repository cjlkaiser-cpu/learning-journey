---
id: eigentools
name: EigenTools
status: active
stack: [rust, axum, ratatui, tokio, sysinfo, pcap]
---

# EigenTools

Ecosistema de herramientas educativas de monitoreo de sistemas en Rust. Monorepo con arquitectura de workspace compartido.

## Ubicación

`~/Projects/eigentools/`

## Estructura

```
eigentools/
├── Cargo.toml              # Workspace config
├── README.md
├── ROADMAP.md              # 16 herramientas planificadas
├── shared/
│   └── eigentools-core/    # Traits y utilidades comunes
│       ├── Cargo.toml
│       └── src/lib.rs
└── tools/
    ├── network-watcher/    # Monitor de red v1.0
    └── process-watcher/    # Monitor de procesos v0.1
```

## Filosofía

- **Educativo**: Cada herramienta enseña conceptos de sistemas operativos
- **Lab Mode**: Experimentos interactivos para aprender haciendo
- **Dual UI**: Web (Axum) + Terminal (Ratatui) desde el mismo código
- **Monorepo**: Código compartido, dependencias unificadas

## Herramientas

| Tool | Versión | Estado | Descripción |
|------|---------|--------|-------------|
| Network Watcher | v1.0 | Producción | Monitor de red, dispositivos, paquetes |
| Process Watcher | v0.1 | Desarrollo | Monitor de procesos, CPU, memoria |

## Roadmap (16 herramientas)

### Prioridad Alta
- File Watcher - Monitor de cambios en filesystem
- Log Viewer - Visor de logs con filtros y búsqueda
- Port Scanner - Escáner de puertos educativo

### Sistema
- Disk Analyzer - Visualizador de uso de disco
- Memory Inspector - Análisis de memoria en tiempo real
- CPU Profiler - Profiling de CPU por proceso

### Seguridad
- Firewall Monitor - Monitor de reglas de firewall
- Permission Auditor - Auditoría de permisos

### Web/APIs
- HTTP Inspector - Análisis de tráfico HTTP
- DNS Explorer - Explorador de DNS

## Stack Técnico

```
┌─────────────────────────────────────────┐
│            eigentools-core              │
│   ToolConfig, ToolState, format_bytes   │
└─────────────────────────────────────────┘
              ▲           ▲
              │           │
    ┌─────────┴───┐   ┌───┴─────────┐
    │   network   │   │   process   │
    │   watcher   │   │   watcher   │
    └─────────────┘   └─────────────┘
```

## Dependencias Compartidas

- tokio 1.40 (async runtime)
- axum 0.7 (web framework)
- ratatui 0.28 (TUI)
- serde 1.0 (serialization)
- rusqlite 0.31 (database)
- chrono 0.4 (time)

## Changelog

**27 dic 2024**: Scaffold Process Watcher con UI profesional estilo EigenLab
**26 dic 2024**: Monorepo creado, Network Watcher v1.0 completado
