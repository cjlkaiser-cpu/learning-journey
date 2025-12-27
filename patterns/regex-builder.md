---
id: regex-builder
name: Regex Builder & Explainer
emoji: 🔤
category: debug
problem: Necesitas crear o entender una expresión regular compleja.
prompt: |
  Actúa como experto en expresiones regulares. Según lo que necesite:

  **Si doy un patrón regex:**
  1. Explica paso a paso qué hace cada parte
  2. Muestra ejemplos de strings que matchean y que NO matchean
  3. Identifica edge cases problemáticos
  4. Sugiere mejoras si hay problemas de rendimiento (backtracking)

  **Si describo lo que quiero matchear:**
  1. Crea la regex óptima para mi caso
  2. Explica cada parte
  3. Dame 5 ejemplos de test (3 que matchean, 2 que no)
  4. Versión para Python (re) y JavaScript si difiere
  5. Sugiere alternativas si la regex es muy compleja

  Formato de respuesta:
  ```
  Regex: /pattern/flags

  Explicación:
  - `parte1` → qué hace
  - `parte2` → qué hace

  Tests:
  ✅ "ejemplo1" → match
  ✅ "ejemplo2" → match
  ❌ "ejemplo3" → no match

  Python: re.compile(r'pattern')
  JavaScript: /pattern/flags
  ```
flow:
  - python
  - javascript
flowDesc: Descripción/Regex → Análisis → Explicación → Tests → Código
---

# Regex Builder & Explainer

Necesitas crear o entender una expresión regular compleja.

## Prompt

Actúa como experto en expresiones regulares. Según lo que necesite:

**Si doy un patrón regex:**
1. Explica paso a paso qué hace cada parte
2. Muestra ejemplos de strings que matchean y que NO matchean
3. Identifica edge cases problemáticos
4. Sugiere mejoras si hay problemas de rendimiento (backtracking)

**Si describo lo que quiero matchear:**
1. Crea la regex óptima para mi caso
2. Explica cada parte
3. Dame 5 ejemplos de test (3 que matchean, 2 que no)
4. Versión para Python (re) y JavaScript si difiere
5. Sugiere alternativas si la regex es muy compleja

## Flujo

Descripción/Regex → Análisis → Explicación → Tests → Código

## Stack técnico

python, javascript
