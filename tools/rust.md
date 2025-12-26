---
id: rust
name: Rust
category: Backend
level: solid
---

# Rust

## Estado: Solid

Lenguaje de sistemas con garantías de seguridad de memoria sin garbage collector. Ideal para herramientas de alto rendimiento, CLI, y WASM.

## Conceptos Dominados

### Fundamentales
- Ownership y Borrowing
- Lifetimes
- Pattern matching
- Enums y Option/Result
- Traits y generics
- Módulos y crates

### Async/Concurrencia
- Tokio runtime
- async/await
- Channels (mpsc)
- RwLock, Mutex
- Spawning tasks

### Ecosistema
- Cargo workspaces (monorepos)
- Crates.io
- Feature flags
- Cross-compilation

## Stack Rust Dominado

| Área | Crate | Uso |
|------|-------|-----|
| **Async** | tokio | Runtime async, tasks, channels |
| **Web** | axum | Framework web, routing, extractors |
| **CLI** | clap | Parser de argumentos derive |
| **TUI** | ratatui + crossterm | Interfaces de terminal |
| **Serialización** | serde + serde_json | JSON, TOML |
| **Sistema** | sysinfo | Info de procesos, CPU, memoria |
| **Red** | pcap | Captura de paquetes |
| **DB** | rusqlite | SQLite embebido |
| **Time** | chrono | Fechas y timestamps |
| **HTTP** | tower-http | CORS, middleware |

## Proyectos con Rust

- **Network Watcher v1.0** - Monitor de red con Web UI + TUI
- **Process Watcher** - Monitor de procesos educativo
- **EigenTools** - Monorepo de herramientas educativas

## Patrones Aprendidos

### Dual UI Pattern
```
┌─────────────────────────────────────────┐
│              SharedState                │
│         Arc<RwLock<AppState>>           │
└───────────────┬─────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
    ┌───────┐       ┌───────┐
    │ Axum  │       │Ratatui│
    │Web UI │       │  TUI  │
    └───────┘       └───────┘
```

### Estado compartido async
```rust
type SharedState = Arc<RwLock<AppState>>;

async fn update_loop(state: SharedState) {
    loop {
        {
            let mut guard = state.write().await;
            guard.update();
        }
        tokio::time::sleep(Duration::from_secs(1)).await;
    }
}
```

## Changelog

**27 dic 2024**: Level solid - EigenTools monorepo, Process Watcher, arquitectura dual UI
**26 dic 2024**: Network Watcher v1.0 completado con Lab experiments
