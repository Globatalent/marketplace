import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/auth/components/Login.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },


  // 404
  {
    path: '/404',
    name: 'not-found',
    component: resolve => require(['@/pages/not-found/index.vue'], resolve),
  },
  // Redirects
  {
    path: '/',
    redirect: '/projects',
  },
  {
    path: '/*',
    redirect: '/404',
  },
  ]
})
