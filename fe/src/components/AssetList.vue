<!-- src/components/AssetList.vue -->
<template>
    <div>
      <h1>Assets</h1>
      <ul>
        <li v-for="asset in assets" :key="asset.id">
          <router-link :to="{ name: 'AssetDetail', params: { id: asset.id }}">{{ asset.name }}</router-link>
        </li>
      </ul>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import { fetchAssets, Asset } from '../api';
  
  // Reactive state for assets
  const assets = ref<Asset[]>([]);
  
  // Fetch assets when the component mounts
  onMounted(async () => {
    assets.value = await fetchAssets();
  });
  </script>
  
  <style scoped>
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    margin: 0.5em 0;
  }
  </style>
  