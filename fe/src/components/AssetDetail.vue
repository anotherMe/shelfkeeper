<!-- src/components/AssetDetail.vue -->
<template>
  <div>
    <h1>{{ asset?.name }}</h1>
    <p>{{ asset?.description }}</p>
    <img :src="asset?.main_image_url" alt="Main Image" v-if="asset?.main_image_url" />

    <h2>Additional Images</h2>
    <div v-if="asset?.images && asset.images.length">
      <img v-for="image in asset.images" :key="image.id" :src="image.url" alt="Additional Image" />
    </div>

    <router-link to="/">Back to list</router-link>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { fetchAssetById, Asset } from '../api';
import { useRoute } from 'vue-router';

// Access the route to get asset ID
const route = useRoute();
const asset = ref<Asset | null>(null);

// Fetch the asset by ID when component mounts
onMounted(async () => {
  const id = Number(route.params.id);
  if (!isNaN(id)) {
    asset.value = await fetchAssetById(id);
  }
});
</script>

<style scoped>
img {
  max-width: 100%;
  border-radius: 8px;
}
</style>
