// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Introduction.vue'),
  },
  {
    path: '/introduction',
    name: 'introduction',
    component: () => import('@/views/Introduction.vue'),
  },
  {
    path: '/project-sekai/:likes',
    name: 'prsk',
    component: () => import('@/views/ProjectSekai.vue'),
    props: true
      
  },
  {
    path: '/mygo/:likes',
    name: 'mygo',
    component: () => import('@/views/Mygo.vue'),
    props: true
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/Profile.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;
