import Login from '@/auth/components/Login.vue'
import Registration from '@/auth/components/Registration.vue'

export default [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Registration',
    component: Registration
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
    redirect: '/login',
  },
  {
    path: '/*',
    redirect: '/404',
  },
]
