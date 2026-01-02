---
id: vue
name: Vue.js
category: Frontend
level: solid
---

# Vue.js

Framework progresivo para construir interfaces de usuario.

## Versión

Vue 3 con Composition API

## Uso en proyectos

- **RameauJazz Web App** - Generador jazz interactivo

## Conceptos clave

### Composition API
```javascript
import { ref, computed, watch, onMounted } from 'vue'

const count = ref(0)
const doubled = computed(() => count.value * 2)

watch(count, (newVal) => console.log(newVal))

onMounted(() => { /* init */ })
```

### Pinia (State Management)
```javascript
import { defineStore } from 'pinia'

export const useStore = defineStore('name', () => {
  const state = ref(0)
  function action() { state.value++ }
  return { state, action }
})
```

### Single File Components
```vue
<template>
  <div>{{ message }}</div>
</template>

<script setup>
import { ref } from 'vue'
const message = ref('Hello')
</script>

<style scoped>
div { color: blue; }
</style>
```

## Recursos

- [Vue.js Docs](https://vuejs.org/)
- [Pinia Docs](https://pinia.vuejs.org/)
