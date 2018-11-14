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
  update({commit, state}, data) {
    return new Promise((resolve, reject) => {
      const payload = UserTransformer.sendPartial(data)
      Vue.axios.patch(`${state.endpoints.users}me/`, payload).then( response => {
        const supporter = UserTransformer.fetch(response.data);
        resolve(supporter)
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
  verify({state}, verificationCode ) {
    return new Promise((resolve, reject) => {
      const payload = {verification_code: verificationCode}
      Vue.axios.post(state.endpoints.verifyEmail, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      });
    })
  },
  clearUser ({commit}) {
    commit('clearUser')
  },
}
