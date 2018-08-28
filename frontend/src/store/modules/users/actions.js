import Vue from 'vue'
import UserTransformer from '../../../users/transformers/UserTransformer'
import { store } from '../../index'

export default {
  fetchUser ({commit, state}) {
    return new Promise((resolve, reject) => {
      Vue.axios.get(state.endpoints.getUser).then((response) => {
        const user = UserTransformer.fetch(response.data)
        commit('setUser', user)
        resolve(user)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  checkUser ({dispatch, state}) {
    return new Promise((resolve, reject) => {
      if (!state.user) {
        dispatch('fetchUser').then(() => {resolve()}).catch((error) => {
          if (error.response.status === 401) {
            dispatch('auth/logout', {}, {root: true})
          }
          reject(error)
        })
      }
      resolve()
    })
  },
  clearUser ({commit}) {
    commit('clearUser')
  },
}
