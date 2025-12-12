# Factoría Demo

> Sistema de gestión para escuela de artes con datos sintéticos

## Descripción
Demo funcional de un sistema de gestión académica para escuelas de artes.
Incluye dashboard, alumnos, inscripciones, horarios, ausencias y pagos con
7 tipos de cálculo diferentes.

## Fuente
- **Repo:** https://github.com/cjlkaiser-cpu/factoria-demo
- **Autor:** Carlos (cjlkaiser-cpu)
- **Licencia:** MIT

---

## Prompt

```
Crea un sistema de gestión para escuela de artes con las siguientes especificaciones:

## Stack
- Python 3.9+ con Flask
- SQLite como base de datos
- Jinja2 para templates
- Bootstrap 5 para UI
- Faker (español) para datos sintéticos

## Estructura del Proyecto
```
factoria-demo/
├── app/
│   ├── main.py              # Aplicación Flask principal
│   ├── templates/
│   │   ├── base.html        # Layout base con navbar
│   │   ├── dashboard.html   # Estadísticas generales
│   │   ├── alumnos/
│   │   │   ├── list.html    # Listado con filtros
│   │   │   └── detail.html  # Ficha completa
│   │   ├── inscripciones/list.html
│   │   ├── horarios/view.html
│   │   ├── ausencias/list.html
│   │   └── pagos/list.html
│   └── static/css/style.css
├── database/
│   ├── schema.sql           # Modelo de datos completo
│   ├── seed_real_data.sql   # Datos reales (profesores, actividades)
│   └── factoria_demo.db     # SQLite generado
├── scripts/
│   ├── init_database.py     # Crea BD y carga datos iniciales
│   └── generate_students.py # Genera alumnos sintéticos con Faker
└── requirements.txt
```

## Modelo de Datos (schema.sql)
```sql
-- Entidades principales
sedes (id, nombre, direccion, telefono)
areas (id, nombre, icono, descripcion)  -- Música, Danza, Robótica, etc.
actividades (id, nombre, area_id, sede_id, precio_mensual, activa)
profesores (id, nombre, email, telefono, tipo_pago, valor_pago, activo)
alumnos (id, nombre, apellidos, fecha_nacimiento, email, telefono, activo)
tutores (id, alumno_id, nombre, relacion, telefono, email)

-- Relaciones
inscripciones (id, alumno_id, actividad_id, fecha_inicio, estado, precio_especial)
horarios (id, actividad_id, profesor_id, dia_semana, hora_inicio, hora_fin, aula)
ausencias (id, alumno_id, inscripcion_id, fecha, justificada, motivo)
pagos_profesores (id, profesor_id, mes, año, horas, alumnos, importe, estado)
```

## Tipos de Pago para Profesores
| Tipo | Cálculo |
|------|---------|
| `hora` | horas_trabajadas × valor_hora |
| `alumno` | num_alumnos × valor_por_alumno |
| `fijo` | cantidad_fija mensual |
| `mixto_alumno` | fijo + (alumnos × valor) |
| `mixto_porcentaje` | fijo + (ingresos × porcentaje) |
| `mixto_hora_alumno` | (horas × valor) + (alumnos × valor) |

## Módulos/Vistas

### Dashboard (/)
- Cards con KPIs: alumnos activos, profesores, inscripciones, ausencias mes
- Ingresos mensuales estimados
- Distribución por área (gráfico o lista)
- Últimas inscripciones
- Próximas clases del día

### Alumnos (/alumnos)
- Listado con búsqueda y filtros (sede, área, estado)
- Detalle con: datos personales, tutor (si menor), inscripciones, historial ausencias
- Indicador visual de edad (adulto/menor)

### Inscripciones (/inscripciones)
- Listado con filtros por estado (activa/baja/pendiente)
- Alta rápida: seleccionar alumno → actividad → precio
- Soporte para precio especial (descuentos)

### Horarios (/horarios)
- Vista semanal tipo calendario
- Filtro por sede y área
- Muestra actividad, profesor, aula, hora

### Ausencias (/ausencias)
- Registro por alumno y fecha
- Campo justificada (sí/no) y motivo
- Estadísticas por alumno

### Pagos (/pagos)
- Cálculo automático según tipo de pago del profesor
- Vista mensual con desglose
- Estados: pendiente, pagado

## Scripts de Inicialización

### init_database.py
1. Crear tablas desde schema.sql
2. Insertar datos reales: sedes, áreas, actividades, profesores
3. Configurar tipos de pago

### generate_students.py
1. Usar Faker('es_ES') para nombres españoles
2. Generar 50 alumnos con datos realistas
3. Crear tutores para menores de edad
4. Asignar inscripciones aleatorias (1-3 por alumno)
5. Generar historial de ausencias

## Filtros Jinja2 Personalizados
- `currency`: formatea como "1.234,56 €"
- `fecha`: formatea como "DD/MM/YYYY"

## Rutas Flask
| Ruta | Método | Descripción |
|------|--------|-------------|
| `/` | GET | Dashboard |
| `/alumnos` | GET | Listado alumnos |
| `/alumnos/<id>` | GET | Detalle alumno |
| `/inscripciones` | GET | Listado inscripciones |
| `/horarios` | GET | Vista semanal |
| `/ausencias` | GET | Listado ausencias |
| `/pagos` | GET | Cálculo de pagos |

## Convenciones
- Idioma UI: Español
- Moneda: EUR con formato español
- Fechas: DD/MM/YYYY
- Bootstrap 5 con tema claro
- Iconos: Font Awesome o Bootstrap Icons
```

---

## Tags
`flask` `sqlite` `escuela` `gestión` `bootstrap` `faker`

## Complejidad
Media (~1k LOC) - CRUD completo con cálculos de pago

## Fecha
Diciembre 2024
