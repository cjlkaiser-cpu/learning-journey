---
id: statsmodels
name: Statsmodels
category: Backend
icon: fa-solid fa-chart-bar
color: text-green-500
tag: Estadística Avanzada
status: available
level: learning
next: Series temporales ARIMA
---

# Statsmodels

Estadística avanzada: regresiones, tests de hipótesis, series temporales.

## Por qué usarlo

Cuando necesitas más que media y desviación. Modelos estadísticos con p-values, intervalos de confianza, diagnósticos.

## Casos de uso

- Regresión lineal/logística con estadísticas
- Tests de hipótesis (t-test, ANOVA, chi-cuadrado)
- Series temporales (ARIMA, SARIMA)
- Análisis de varianza

## Código ejemplo

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd

# Regresión lineal con fórmula tipo R
df = pd.read_csv("datos.csv")
modelo = smf.ols("ventas ~ precio + publicidad", data=df).fit()
print(modelo.summary())  # R², p-values, coeficientes

# Test t
from scipy import stats
t_stat, p_value = stats.ttest_ind(grupo_a, grupo_b)

# Serie temporal ARIMA
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(serie, order=(1,1,1)).fit()
forecast = model.forecast(steps=10)
```

## Instalación

```bash
pip install statsmodels
```
