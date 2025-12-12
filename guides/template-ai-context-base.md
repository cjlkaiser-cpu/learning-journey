# Proyecto: [NOMBRE]

## Stack
- Backend: [Python/Node/Go...]
- Frontend: [React/Vue/Vanilla...]
- DB: [SQLite/PostgreSQL/MongoDB...]
- Hosting: [Local/Vercel/Railway...]

## Estructura
```
proyecto/
├── src/           # Código fuente
├── tests/         # Tests
├── docs/          # Documentación
└── scripts/       # Utilidades
```

## Convenciones
- Idioma código: [español/inglés]
- Formato: [tabs/spaces, comillas]
- Nombres: [camelCase/snake_case]

## Reglas
1. Código funcional, no placeholders
2. [Regla específica del proyecto]
3. [Otra regla]

## Contexto
[Descripción breve del proyecto y su objetivo]

---
# Notas de uso

## Niveles de contexto
- **Nivel 0**: Nada (scripts one-shot)
- **Nivel 1**: Solo este archivo (proyectos pequeños)
- **Nivel 2**: + patterns.md (proyectos medianos)
- **Nivel 3**: + decisions.md + memory.md (proyectos largo plazo)

## Archivos por motor
| Motor | Archivo |
|-------|---------|
| Claude Code | `CLAUDE.md` |
| Cursor | `.cursorrules` |
| Copilot | `.github/copilot-instructions.md` |
| Gemini | `.gemini.md` (no oficial) |

## Generar para todos los motores
```bash
# Crear estructura
mkdir -p .ai-context .github
cp template-ai-context-base.md .ai-context/base.md

# Editar .ai-context/base.md con datos del proyecto

# Generar archivos
cp .ai-context/base.md CLAUDE.md
cp .ai-context/base.md .cursorrules
cp .ai-context/base.md .github/copilot-instructions.md
```
