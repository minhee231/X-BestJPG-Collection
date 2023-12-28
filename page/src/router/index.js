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
    path: '/project-sekai',
    name: 'prsk',
    component: () => import('@/views/ProjectSekai.vue'),
    children: [
      {
        path: 'best/:likes',
        name: 'sekai-best',
        component: () => import('@/views/ProjectSekai.vue'),
        props: true
      },
      
    ]
  },
  {
    path: '/mygo',
    name: 'mygo',
    component: () => import('@/views/Mygo.vue'),
    children: [
      {
        path: 'best/:likes',
        name: 'mygo-best',
        component: () => import('@/views/Mygo.vue'),
        props: true
      },
    ]
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
