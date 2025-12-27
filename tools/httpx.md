---
id: httpx
name: httpx
category: Backend
icon: fa-solid fa-globe
color: text-cyan-500
tag: HTTP Client
status: available
level: learning
next: Async streams
---

# httpx

Cliente HTTP moderno con soporte async. Reemplazo de requests.

## Por qué en minerOS

Async nativo, ideal para FastAPI. API compatible con requests pero mejor.

## Casos de uso

- Llamadas a APIs externas
- Web scraping async
- Testing de endpoints

## Código ejemplo

```python
import httpx

# Sync
r = httpx.get("https://api.github.com/users/octocat")
print(r.json())

# Async
async with httpx.AsyncClient() as client:
    r = await client.get("https://api.github.com/users/octocat")
    print(r.json())
```

## Instalación

```bash
pip install httpx
```
