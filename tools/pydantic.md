---
id: pydantic
name: Pydantic
category: Backend
icon: fa-solid fa-check-double
color: text-red-500
tag: Validación
status: available
level: learning
next: Validadores custom
---

# Pydantic

Validación de datos con tipado Python. Base de FastAPI.

## Por qué en minerOS

Valida datos de entrada, genera JSON schemas, y es el core de FastAPI.

## Casos de uso

- Validar datos de API
- Configuración de apps
- Serialización JSON

## Código ejemplo

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

user = User(name="Carlos", email="carlos@example.com", age=30)
print(user.model_dump_json())
```

## Instalación

```bash
pip install pydantic[email]
```
