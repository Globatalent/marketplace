import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import auth from './modules/auth/index'

export const store = new Vuex.Store({
  modules: {
    auth,
  },
})
