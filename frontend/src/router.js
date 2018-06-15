import Vue from 'vue'
import VueRouter from 'vue-router'

import routes from './routes'
import { store } from './store'

Vue.use(VueRouter)
const router = new VueRouter({
  scrollBehavior (to, from, savedPosition) { return {x: 0, y: 0} },
  mode: 'history',
  routes,
})

router.beforeEach((to, from, next) => {
  store.dispatch('auth/inspectToken').then(() => {
    store.dispatch('users/checkUser').then(() => {
      if (to.matched.some(m => m.meta.userType !== undefined && m.meta.userType !== store.getters['users/userType'])) {
        next('/')
      }
      next()
    }).catch(() => {
      next()
      console.log('error getting user')
    })
  }).catch(() => {
    if (to.matched.some(m => m.meta.auth)) {
      Message.error({
        message: 'You must be logged in to access this page',
        center: true,
      })
      next({name: 'login'})
    }
    next()
  })
})

export default router
