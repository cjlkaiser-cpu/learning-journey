---
id: python-bug-buster
name: Python Bug Buster
emoji: 🐛
category: debug
problem: Tu código Python tiene un bug y no sabes dónde está.
prompt: |
  Analiza el código Python que te paso. Identifica bugs o errores y dame:
  1. El código corregido
  2. Explicación de qué estaba mal
  3. Cómo evitarlo en el futuro

  El código corregido debe ser funcional y seguir buenas prácticas de Python.
flow:
  - python
flowDesc: Código con bug → Análisis → Código corregido → Explicación
---

# Python Bug Buster

Tu código Python tiene un bug y no sabes dónde está.

## Prompt

Analiza el código Python que te paso. Identifica bugs o errores y dame:
1. El código corregido
2. Explicación de qué estaba mal
3. Cómo evitarlo en el futuro

## Ejemplo de uso

Pega tu código con el error:
```python
def calculate_average(nums):
    sum = 0
    for num in nums:
        sum += num
    average = sum / len(nums)
    return average

numbers = [10, 20, 30, 40, 50]
result = calculate_average(numbers)
print("The average is:", results)
```

## Flujo

Código con bug → Análisis → Código corregido → Explicación

## Fuente

[Anthropic Prompt Library](https://platform.claude.com/docs/en/prompt-library/python-bug-buster)
