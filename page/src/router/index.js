// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/introduction.vue'),
  },
  {
    path: '/introduction',
    name: 'introduction',
    component: () => import('@/views/introduction.vue'),
  },
  {
    path: '/project-sekai',
    name: 'prsk',
    component: () => import('@/views/project_sekai.vue'),
    children: [
      {
        path: 'best/:likes',
        name: 'sekai-best',
        component: () => import('@/views/project_sekai.vue'),
        props: true
      },
      {
        path: 'latest',
        name: 'sekai-latest',
        component: () => import('@/views/project_sekai.vue'),
        props: true
      }
    ]
  },
  {
    path: '/mygo',
    name: 'mygo',
    component: () => import('@/views/mygo'),
    children: [
      {
        path: 'best/:likes',
        name: 'mygo-best',
        component: () => import('@/views/mygo.vue'),
        props: true
      },
      {
        path: 'latest',
        name: 'mygo-latest',
        component: () => import('@/views/mygo.vue'),
        props: true
      }
    ]
  },
  {
    path: '/profile',
    name: 'profile',
    component: () => import('@/views/profile.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});


export default router;
