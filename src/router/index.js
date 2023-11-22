import { createRouter, createWebHistory } from 'vue-router'


const routes = [
  {
    name:'adList',
    path:'/adList',
    component: () => import("@/views/adList.vue")
  },
  {
    name:'homepage',
    path:'/',
    component: () => import("@/views/homepage.vue")
  },
  {
    name:'createAd',
    path:'/createAd',
    component: () => import("@/views/createAd.vue")
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
