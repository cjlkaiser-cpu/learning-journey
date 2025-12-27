---
id: statistical-test-selector
name: Selector de Test Estadístico
emoji: 🎯
category: data-eng
problem: No sabes qué test estadístico usar para tu análisis.
prompt: |
  Necesito elegir el test estadístico correcto. Mis datos son:
  [DESCRIBE TUS DATOS Y PREGUNTA]

  Dime:
  1. **Tipo de pregunta**: ¿comparación, correlación, predicción?
  2. **Tipo de variables**: categóricas, continuas, ordinales
  3. **Supuestos a verificar**: normalidad, homogeneidad de varianza
  4. **Test recomendado** y por qué
  5. **Código Python** para ejecutarlo (scipy o statsmodels)
  6. **Cómo interpretar** el resultado (p-value, efecto)
  7. **Alternativa** si no se cumplen los supuestos

  Ejemplos de preguntas:
  - "¿Hay diferencia significativa entre dos grupos?"
  - "¿Estas dos variables están correlacionadas?"
  - "¿Este tratamiento funciona mejor que el control?"
flow:
  - python
  - scipy
  - statsmodels
flowDesc: Pregunta → Tipo de datos → Test correcto → Código → Interpretación
---

# Selector de Test Estadístico

No sabes qué test estadístico usar para tu análisis.

## Ejemplo de uso

"Tengo las notas de dos clases (A y B) y quiero saber si hay diferencia significativa"

"Quiero ver si la edad correlaciona con el salario en mi dataset"
