import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import auth from './modules/auth/index'
import users from './modules/users/index'
import alerts from './modules/alerts/index'
import tokens from './modules/tokens/index'
import actions from './modules/actions/index'
import campaigns from './modules/campaigns/index'

export const store = new Vuex.Store({
  modules: {
    auth,
    users,
    alerts,
    tokens,
    actions,
    campaigns,
  },
})
