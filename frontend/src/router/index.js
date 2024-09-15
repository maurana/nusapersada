import { createRouter, createWebHistory } from 'vue-router'
import Sales from '../views/Sales.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'sales',
      component: Sales
    },
    {
      path: '/report',
      name: 'report',
      component: () => import('../views/Report.vue')
    }
  ]
})

export default router