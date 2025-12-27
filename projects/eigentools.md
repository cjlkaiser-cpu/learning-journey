---
id: eigentools
name: EigenTools
status: production
stack: [rust, axum, ratatui, tokio, sysinfo, pcap, jwt, bcrypt, argon2, totp]
---

# EigenTools v1.0

Ecosistema de 10 herramientas educativas de monitoreo de sistemas en Rust.

## Ubicación

- Local: `~/Projects/eigentools/`
- GitHub: https://github.com/cjlkaiser-cpu/eigentools (privado)

## Herramientas

| Tool | Puerto | Categoría | Descripción |
|------|--------|-----------|-------------|
| Network Watcher | 3000 | Red | Captura paquetes, DNS, ARP, traceroute |
| Process Watcher | 3001 | Sistema | Procesos, CPU, señales Unix, árbol |
| Disk Watcher | 3002 | Sistema | Almacenamiento, I/O, filesystems |
| Crypto Lab | 3003 | Seguridad | AES, ChaCha20, hashes, firmas |
| HTTP Lab | 3004 | Web | Métodos, headers, cookies, CORS |
| SQL Lab | 3005 | Datos | SQLite, JOINs, índices, EXPLAIN |
| Regex Lab | 3006 | Datos | Tester, patrones, explain engine |
| JSON Explorer | 3007 | Datos | JSON/YAML/TOML, JSONPath, diff |
| Memory Lab | 3008 | Sistema | Stack/heap, pressure, page faults |
| Auth Playground | 3009 | Seguridad | JWT, bcrypt, argon2, TOTP, OAuth2 |

## TUI Launcher

Gestor central para todas las herramientas:
```bash
./target/release/eigentools
```
- ↑↓ navegar
- Enter iniciar/detener
- q salir
- Estado en vivo (●/○)

## Filosofía

1. **Educativo**: Cada herramienta enseña conceptos de sistemas
2. **Lab Mode**: Experimentos interactivos
3. **Dual UI**: Web (Axum) + Terminal (Ratatui)
4. **10 herramientas consolidadas**: No se añaden más

## Quick Start

```bash
cd ~/Projects/eigentools
cargo build --release
./target/release/eigentools
```

## Stack

- Rust + Tokio (async runtime)
- Axum (web framework)
- Ratatui (TUI)
- SQLite (persistencia)

## Changelog

- **27 dic 2025**: v1.0 - 10 herramientas + TUI launcher + GitHub
- **27 dic 2025**: Auth Playground v1.0 (JWT, bcrypt, TOTP)
- **26 dic 2025**: Consolidación a 10 herramientas
