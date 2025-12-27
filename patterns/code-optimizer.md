---
id: code-optimizer
name: Code Optimizer
emoji: 🚀
category: refactoring
problem: Tu código funciona pero quieres que sea más rápido o eficiente.
prompt: |
  Analiza el código Python que te paso y sugiere mejoras de rendimiento:
  1. Identifica partes ineficientes
  2. Propón optimizaciones específicas
  3. Explica por qué cada cambio mejora el rendimiento
  4. Dame el código optimizado

  El código optimizado debe mantener la misma funcionalidad.
flow:
  - python
flowDesc: Código lento → Análisis → Optimizaciones → Código eficiente
---

# Code Optimizer

Tu código funciona pero quieres que sea más rápido o eficiente.

## Prompt

Analiza el código Python que te paso y sugiere mejoras de rendimiento:
1. Identifica partes ineficientes
2. Propón optimizaciones específicas
3. Explica por qué cada cambio mejora el rendimiento
4. Dame el código optimizado

## Ejemplo de uso

```python
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
```

## Flujo

Código lento → Análisis → Optimizaciones → Código eficiente

## Fuente

[Anthropic Prompt Library](https://platform.claude.com/docs/en/prompt-library/code-consultant)
