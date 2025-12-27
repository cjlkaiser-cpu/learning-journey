---
id: rich
name: Rich
category: Backend
icon: fa-solid fa-palette
color: text-purple-500
tag: Terminal UI
status: available
level: learning
next: Panels y layouts
---

# Rich

Output bonito en terminal con colores, tablas y barras de progreso.

## Por qué en minerOS

Hace que los scripts sean más legibles y profesionales. Integra perfecto con Typer.

## Casos de uso

- Logs con colores
- Tablas en terminal
- Barras de progreso

## Código ejemplo

```python
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()
console.print("[bold green]Success![/bold green]")

# Tabla
table = Table(title="Users")
table.add_column("Name")
table.add_row("Carlos")
console.print(table)

# Progress bar
for i in track(range(100), description="Processing..."):
    pass
```

## Instalación

```bash
pip install rich
```
