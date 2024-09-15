<script setup>
import { RouterView } from 'vue-router'
import { onMounted } from 'vue'
import { initFlowbite } from 'flowbite'
import NavHead from '@/components/NavHead.vue'

onMounted(() => {
    initFlowbite();
})
</script>

<template>
  <NavHead />
  <RouterView />
</template>