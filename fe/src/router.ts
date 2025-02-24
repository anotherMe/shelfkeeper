// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import AssetList from './components/AssetList.vue';
import AssetDetail from './components/AssetDetail.vue';

const routes = [
  { path: '/', component: AssetList, name: 'AssetList' },
  { path: '/assets/:id', component: AssetDetail, name: 'AssetDetail', props: true },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
