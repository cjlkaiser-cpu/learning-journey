---
id: process-watcher
name: Process Watcher
status: production
stack: [rust, axum, ratatui, sysinfo, tokio]
---

# Process Watcher v1.0

Monitor de procesos educativo con interfaz web profesional estilo EigenLab. Visualiza CPU, memoria, árbol de procesos, y ofrece experimentos interactivos para entender cómo funcionan los procesos en sistemas Unix.

## Ubicación

`~/Projects/eigentools/tools/process-watcher/`

## Características

### Overview
- Gauges de CPU, Memoria, Swap con animaciones
- Sparklines de histórico (últimos 60 segundos)
- Top 5 procesos por CPU y Memoria
- Alertas automáticas (CPU > 80%, zombies, memoria crítica)

### Procesos
- Lista completa con PID, nombre, usuario, estado
- Ordenamiento por cualquier columna
- Búsqueda por nombre, PID o usuario
- Acción Kill con confirmación

### Árbol
- Jerarquía padre-hijo de procesos
- Visualización del linaje desde init/launchd

### Lab Mode (6 experimentos)
1. **Árbol de Procesos** - Visualiza fork() y jerarquía
2. **Detalles de Proceso** - Examina PID específico (exe, cmd, fds)
3. **Señales Unix** - Aprende SIGTERM, SIGKILL, SIGHUP...
4. **Threads vs Procesos** - Compara concurrencia
5. **Procesos Zombie** - Detecta y aprende sobre zombies
6. **Historial de Recursos** - Monitoreo temporal (próximamente)

## Stack Técnico

| Componente | Tecnología |
|------------|------------|
| Runtime | Tokio (async) |
| Web | Axum + tower-http |
| TUI | Ratatui + Crossterm |
| Sistema | sysinfo (CPU, memoria, procesos) |
| Usuarios | users (UID → username) |
| DB | SQLite (rusqlite) |
| Config | TOML |

## Diseño UI

Estilo EigenLab profesional:
- Tipografía: Playfair Display (headings), Inter (body), JetBrains Mono (code)
- Paleta: Purple (#a855f7) + Cyan (#06b6d4) + Green (#22c55e)
- Gradientes sutiles, bordes que brillan al hover
- Animaciones fluidas, sparklines SVG

## Endpoints API

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | HTML Dashboard |
| `/api/state` | GET | Estado completo (procesos, sistema, histórico) |
| `/api/kill` | POST | Terminar proceso (SIGTERM/SIGKILL) |
| `/api/tree` | GET | Árbol de procesos |
| `/api/process/{pid}` | GET | Detalles de proceso específico |

## Ejecución

```bash
# Web UI
cargo run --release -p process_watcher
# Abre http://localhost:3001

# TUI
cargo run --release -p process_watcher -- --tui
```

## Aprendizajes

- sysinfo crate para info de sistema
- Árbol de procesos con HashMap recursivo
- Señales Unix (kill, SIGTERM, SIGKILL)
- Sparklines SVG generadas dinámicamente
- Sistema de alertas basado en umbrales

## Changelog

**27 dic 2025**: v1.0 - Producción
- Username resolution (UID → username)
- Start time real de procesos
- Búsqueda/filtro en Web UI
- Ordenamiento por columna (click header)
- Alertas funcionales (CPU>80%, zombies, memoria)
- Lab: Señales Unix completo con documentación
- Kill desde TUI (tecla x + confirmación y/n)
- Endpoint /api/signals con docs
- Endpoint /api/alerts
- Toast notifications en Web UI
- TUI: búsqueda, mensajes de estado

**27 dic 2025**: v0.1 - Scaffold inicial, UI EigenLab
