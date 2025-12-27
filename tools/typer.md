---
id: typer
name: Typer
category: Backend
icon: fa-solid fa-terminal
color: text-green-500
tag: CLI Framework
status: available
level: learning
next: Subcomandos y grupos
---

# Typer

Framework para crear CLIs profesionales con tipado Python.

## Por qué en minerOS

Convierte scripts sueltos en herramientas CLI con --help automático, validación y colores.

## Casos de uso

- CLIs para automatización
- Herramientas de línea de comandos
- Scripts con argumentos tipados

## Código ejemplo

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1):
    for _ in range(count):
        typer.echo(f"Hello {name}!")

if __name__ == "__main__":
    app()
```

## Instalación

```bash
pip install typer[all]
```
