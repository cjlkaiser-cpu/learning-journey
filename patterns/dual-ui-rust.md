---
id: dual-ui-rust
name: Dual UI Pattern (Rust)
problem: Ofrecer interfaz Web y Terminal desde el mismo backend sin duplicar lógica
flow: [rust, axum, ratatui, tokio]
---

# Dual UI Pattern en Rust

## Problema

Crear aplicaciones que funcionen tanto como:
- **Web UI**: Dashboard accesible desde navegador
- **TUI**: Interfaz de terminal para usuarios avanzados

Sin duplicar la lógica de negocio ni el estado.

## Solución

Arquitectura con estado compartido (Arc<RwLock>) que alimenta ambas interfaces:

```
┌─────────────────────────────────────────┐
│              AppState                   │
│  - data: Vec<T>                         │
│  - stats: Stats                         │
│  - config: Config                       │
│  - history: History                     │
└───────────────┬─────────────────────────┘
                │
                ▼
┌─────────────────────────────────────────┐
│         Arc<RwLock<AppState>>           │
│            SharedState                  │
└───────────────┬─────────────────────────┘
                │
        ┌───────┴───────┐
        ▼               ▼
    ┌───────┐       ┌───────┐
    │ Axum  │       │Ratatui│
    │ :3001 │       │ --tui │
    └───────┘       └───────┘
        │               │
        ▼               ▼
    ┌───────┐       ┌───────┐
    │Browser│       │Terminal│
    └───────┘       └───────┘
```

## Implementación

### 1. Estado compartido

```rust
use std::sync::Arc;
use tokio::sync::RwLock;

#[derive(Debug, Clone, Default)]
struct AppState {
    items: Vec<Item>,
    stats: Stats,
    config: Config,
}

type SharedState = Arc<RwLock<AppState>>;
```

### 2. Update loop (background task)

```rust
async fn update_loop(state: SharedState, interval: u64) {
    loop {
        {
            let mut guard = state.write().await;
            guard.items = collect_data();
            guard.stats = calculate_stats(&guard.items);
        }
        tokio::time::sleep(Duration::from_secs(interval)).await;
    }
}
```

### 3. Web handlers (Axum)

```rust
async fn get_state(State(state): State<SharedState>) -> Json<AppState> {
    let guard = state.read().await;
    Json(guard.clone())
}

async fn index_html() -> Html<&'static str> {
    Html(include_str!("index.html"))
}
```

### 4. TUI rendering (Ratatui)

```rust
fn draw_tui(frame: &mut Frame, state: &AppState) {
    let chunks = Layout::default()
        .direction(Direction::Vertical)
        .constraints([Constraint::Length(3), Constraint::Min(10)])
        .split(frame.area());

    // Render using state.items, state.stats, etc.
}
```

### 5. Main con flag CLI

```rust
#[derive(Parser)]
struct Args {
    #[arg(long)]
    tui: bool,
}

#[tokio::main]
async fn main() {
    let args = Args::parse();
    let state = Arc::new(RwLock::new(AppState::default()));

    // Start update loop
    let update_state = state.clone();
    tokio::spawn(async move {
        update_loop(update_state, 2).await;
    });

    if args.tui {
        run_tui(state).await;
    } else {
        run_web(state).await;
    }
}
```

## Beneficios

| Aspecto | Beneficio |
|---------|-----------|
| **DRY** | Lógica de negocio en un solo lugar |
| **Flexibilidad** | Usuario elige interfaz preferida |
| **Testing** | Un solo estado a testear |
| **Mantenimiento** | Cambios en lógica afectan ambas UIs |

## Casos de Uso

- Herramientas de monitoreo (network-watcher, process-watcher)
- CLIs con dashboard opcional
- Aplicaciones de administración de sistemas
- DevTools locales

## Stack Recomendado

```toml
[dependencies]
tokio = { version = "1", features = ["full"] }
axum = "0.7"
tower-http = { version = "0.5", features = ["cors"] }
ratatui = "0.28"
crossterm = "0.28"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
clap = { version = "4", features = ["derive"] }
```

## Proyectos que usan este patrón

- Network Watcher
- Process Watcher
- (Futuro) File Watcher, Log Viewer, etc.
