<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Главная</RouterLink>
      <RouterLink to="/about">О проекте</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>

<style>
/* Здесь можно написать самые базовые стили для всего сайта */
nav {
  display: flex;
  gap: 20px;
  padding: 20px;
  background: #f4f4f4;
}
</style>
