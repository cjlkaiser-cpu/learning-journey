---
id: network-watcher
name: Network Watcher
status: production
stack: [rust, axum, ratatui, pcap, tokio]
---

# Network Watcher v1.0

Monitor de red educativo con interfaz web y terminal. Captura paquetes, detecta dispositivos, y ofrece experimentos interactivos para aprender networking.

## Ubicación

`~/Projects/eigentools/tools/network-watcher/`

## Características

### Monitoreo
- Captura de paquetes en tiempo real (pcap)
- Detección automática de dispositivos en la red
- Estadísticas de tráfico por protocolo
- Histórico de conexiones

### Interfaz Dual
- **Web UI**: Dashboard en http://localhost:3001
- **TUI**: Interfaz de terminal con tabs

### Lab Mode (5 experimentos)
1. **DNS Explorer** - Resuelve dominios y aprende sobre DNS
2. **ARP Table** - Visualiza la tabla ARP del sistema
3. **Traceroute Visual** - Traza rutas con visualización
4. **Latency Comparator** - Compara latencias entre hosts
5. **Port Scanner** - Escaneo educativo de puertos

## Stack Técnico

| Componente | Tecnología |
|------------|------------|
| Runtime | Tokio (async) |
| Web | Axum + tower-http (CORS) |
| TUI | Ratatui + Crossterm |
| Paquetes | pcap (libpcap) |
| DB | SQLite (rusqlite) |
| Config | TOML |

## Arquitectura

```
┌─────────────────────────────────────────┐
│           SharedState                   │
│      Arc<RwLock<AppState>>              │
│  ┌─────────┬─────────┬─────────┐        │
│  │ devices │ packets │  lab    │        │
│  └─────────┴─────────┴─────────┘        │
└───────────────┬─────────────────────────┘
                │
    ┌───────────┴───────────┐
    ▼                       ▼
┌─────────┐           ┌─────────┐
│  Axum   │           │ Ratatui │
│ Web UI  │           │   TUI   │
│ :3001   │           │ --tui   │
└─────────┘           └─────────┘
```

## Endpoints API

| Endpoint | Método | Descripción |
|----------|--------|-------------|
| `/` | GET | HTML Dashboard |
| `/api/state` | GET | Estado completo JSON |
| `/api/lab/dns` | POST | Resolver DNS |
| `/api/lab/arp` | GET | Tabla ARP |
| `/api/lab/traceroute` | POST | Traceroute |
| `/api/lab/ping` | POST | Ping host |
| `/api/lab/portscan` | POST | Escanear puertos |

## Ejecución

```bash
# Web UI (requiere sudo para pcap)
sudo cargo run --release -p network_watcher

# TUI
sudo cargo run --release -p network_watcher -- --tui
```

## Aprendizajes

- Captura de paquetes con libpcap
- Parsing de headers Ethernet/IP/TCP/UDP
- Detección de dispositivos via ARP
- Arquitectura dual UI en Rust
- Estado compartido async con RwLock

## Changelog

**27 dic 2024**: Integrado en monorepo EigenTools
**26 dic 2024**: v1.0 - Lab Mode con 5 experimentos, README completo
**25 dic 2024**: ARP Table, dispositivos con MAC, fix version display
