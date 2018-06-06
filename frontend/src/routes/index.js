import Login from '@/auth/pages/Login.vue'
import Registration from '@/auth/pages/Registration.vue'
import AthleteProfile from '@/athletes/pages/AthleteProfile.vue'
import AthleteList from '@/athletes/pages/AthleteList.vue'

export default [
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'registration',
    component: Registration
  },

  // Athletes
  {
    path: '/athlete-profile',
    name: 'athlete.profile',
    component: AthleteProfile
  },
  {
    path: '/athletes',
    name: 'athlete.list',
    component: AthleteList
  },

  // 404
  {
    path: '/404',
    name: 'not-found',
    component: resolve => require(['@/pages/NotFound.vue'], resolve),
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
