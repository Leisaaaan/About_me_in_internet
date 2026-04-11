<script setup>
import { ref } from 'vue'
import LawyerContent from './components/LawyerContent.vue'
import DevContent from './components/DevContent.vue'

const isDev = ref(false)
</script>

<template>
  <div id="app" :class="{ 'dev-theme': isDev, 'law-theme': !isDev }">
    <header>
      <h1>My_page_in_internet</h1>
      <button @click="isDev = !isDev">
        Переключить на {{ isDev ? 'Юриста' : 'Разработчика' }}
      </button>
    </header>
    <main>
      <LawyerContent v-if="!isDev" />
      <DevContent v-else />
    </main>
  </div>
</template>

<style>
header {
  padding: 20px;
  text-align: center;
}
button {
  padding: 10px 20px;
  cursor: pointer;
}
.dev-theme {
  background: #1e1e1e;
  color: #4fc08d;
  font-family: 'Courier New', Courier, monospace;
  min-height: 100vh;
}
.law-theme {
  background: #f4f4f4;
  color: #2c3e50;
  font-family: 'Georgia', serif;
  min-height: 100vh;
}
</style>
