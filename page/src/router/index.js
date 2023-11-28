// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/Leoneed',
    name: 'Leoneed',
    component: () => import('../views/Leoneed.vue'),
  },
  {
    path: '/Sekai',
    name: 'SekaiPage',
    component: () => import('../views/Sekai.vue')
  },
  {
    path: '/MoreMoreJump',

  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;
