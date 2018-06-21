import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import auth from './modules/auth/index'
import users from './modules/users/index'

export const store = new Vuex.Store({
  modules: {
    auth,
    users,
  },
})
