---
id: montecarlo
name: Monte Carlo
category: Backend
icon: fa-solid fa-dice
color: text-red-500
tag: Simulación Estocástica
status: available
level: learning
next: Cadenas de Markov
---

# Monte Carlo

Simulaciones basadas en números aleatorios para estimar probabilidades y valores.

## Por qué usarlo

Cuando el problema es demasiado complejo para resolver analíticamente. Simula miles de escenarios y calcula estadísticas.

## Casos de uso

- Estimación de riesgos financieros
- Propagación de incertidumbre
- Optimización estocástica
- Cálculo de integrales complejas

## Código ejemplo

```python
import numpy as np

# Estimar Pi con Monte Carlo
n_puntos = 1_000_000
x = np.random.uniform(-1, 1, n_puntos)
y = np.random.uniform(-1, 1, n_puntos)
dentro = (x**2 + y**2) <= 1
pi_estimado = 4 * dentro.sum() / n_puntos
print(f"Pi ≈ {pi_estimado}")  # ~3.1416

# Simulación financiera
dias = 252  # Días de trading
simulaciones = 10_000
precio_inicial = 100
volatilidad = 0.2
retorno_medio = 0.05

retornos = np.random.normal(
    retorno_medio/dias, 
    volatilidad/np.sqrt(dias), 
    (simulaciones, dias)
)
precios = precio_inicial * np.cumprod(1 + retornos, axis=1)

# Estadísticas
print(f"Precio medio final: {precios[:,-1].mean():.2f}")
print(f"VaR 95%: {np.percentile(precios[:,-1], 5):.2f}")
```

## Instalación

```bash
pip install numpy  # Ya incluido en NumPy
```
