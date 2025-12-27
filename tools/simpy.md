---
id: simpy
name: SimPy
category: Backend
icon: fa-solid fa-clock-rotate-left
color: text-yellow-500
tag: Simulación Discreta
status: available
level: learning
next: Recursos y colas
---

# SimPy

Simulación de eventos discretos. Modela colas, procesos, sistemas.

## Por qué usarlo

Simular sistemas reales: colas en banco, líneas de producción, tráfico de red, procesos hospitalarios.

## Casos de uso

- Colas de espera (bancos, hospitales)
- Líneas de producción
- Logística y transporte
- Sistemas de inventario

## Código ejemplo

```python
import simpy
import random

def cliente(env, nombre, cajero):
    llegada = env.now
    print(f"{nombre} llega en {llegada:.1f}")
    
    with cajero.request() as req:
        yield req  # Espera cajero libre
        espera = env.now - llegada
        print(f"{nombre} espera {espera:.1f} min")
        
        yield env.timeout(random.uniform(1, 5))  # Tiempo servicio
        print(f"{nombre} termina en {env.now:.1f}")

def generador(env, cajero):
    for i in range(10):
        yield env.timeout(random.expovariate(1/2))  # Llegadas
        env.process(cliente(env, f"Cliente {i}", cajero))

# Correr simulación
env = simpy.Environment()
cajero = simpy.Resource(env, capacity=2)  # 2 cajeros
env.process(generador(env, cajero))
env.run(until=50)
```

## Instalación

```bash
pip install simpy
```
