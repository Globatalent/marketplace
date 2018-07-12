import jwtDecode from 'jwt-decode'
import Vue from 'vue'
import VueMoment from 'vue-moment'
import router from '@/router.js'
import { Message } from 'element-ui'

export default {
  login ({commit, state}, userData) {
    /**
     * Login to backend and set the token in state
     */
    return new Promise((resolve, reject) => {
      const payload = {
        email: userData.email,
        password: userData.password,
      }
      Vue.axios.post(state.endpoints.obtainJWT, payload).then((response) => {
        commit('updateToken', response.data.token)
        Message.success('Login successful')
        resolve()
      }).catch((error) => {
        console.log(error)
        if (error.hasOwnProperty('response')) {
          const errors = error.response.data.non_field_errors
          let message = ''
          if (errors.length > 1) {
            message += '<ul>'
            errors.forEach(error => {
              message += `<li>${error}</li>`
            })
            message += '</ul>'
          } else {
            message = errors[0]
          }
          Message.error({
            dangerouslyUseHTMLString: true,
            message: message,
            center: true,
          })
        }
        reject(error)
      })
    })
  },
  signUp ({commit, state}, userData) {
    /**
     * Login to backend and set the token in state
     */
    return new Promise((resolve, reject) => {
      const payload = {
        full_name: userData.fullName,
        email: userData.email,
        password: userData.password
      }
      Vue.axios.post(state.endpoints.signUp, payload).then((response) => {
        commit('updateToken', response.data.token)
        Message.success('Sign up successful')
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  registerAthlete ({commit, state}, userData) {
    /**
     * Login to backend and set the token in state
     */
    return new Promise((resolve, reject) => {
      const payload = {
        first_name: userData.firstName,
        last_name: userData.lastName,
        email: userData.email,
        password: userData.password,
        repeat_password: userData.repeatPassword,
        country: userData.country,
        date_of_birth: Vue.moment(userData.date).format('YYYY-MM-DD'),
        sex: userData.sex,
        sport: userData.sport
      }
      Vue.axios.post(state.endpoints.registerAthlete, payload).then((response) => {
        commit('updateToken', response.data.token)
        Message.success('Sign up successful')
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  registerSupporter ({commit, state}, userData) {
    /**
     * Login to backend and set the token in state
     */
    return new Promise((resolve, reject) => {
      const payload = {
        first_name: userData.firstName,
        last_name: userData.lastName,
        email: userData.email,
        password: userData.password,
        repeat_password: userData.repeatPassword
      }
      Vue.axios.post(state.endpoints.registerSupporter, payload).then((response) => {
        commit('updateToken', response.data.token)
        Message.success('Sign up successful')
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  logout ({commit, dispatch}) {
    commit('cleanToken')
    dispatch('users/clearUser', {}, {root: true})
    router.push({name: 'project.list'})
  },
  refreshToken ({commit, state, dispatch}) {
    return new Promise((resolve, reject) => {
      const payload = {
        token: state.jwt,
      }
      Vue.axios.post(state.endpoints.refreshJWT, payload).then((response) => {
        commit('updateToken', response.data.token)
        resolve()
      }).catch((error) => {
        console.log('Refresh failed, need to login again')
        dispatch('logout')
        reject()
      })
    })
  },
  inspectToken ({commit, dispatch, state}) {
    /**
     * Checks the token and renews it if necessary. Returns true if the token is valid
     */
    return new Promise((resolve, reject) => {
      console.log('Inspecting token')
      const token = state.jwt
      if (token) {
        const decoded = jwtDecode(token)
        const expiration = decoded.exp
        const orig_iat = decoded.orig_iat
        if (expiration - (Date.now() / 1000) < 0) {
          // Token has expired
          console.log('Token expired')
          dispatch('logout')
          resolve()
        } else if (expiration - (Date.now()) / 1000 < 1800) {
          // Token expires in 30 min
          if ((Date.now() / 1000) - orig_iat < 628200) {
            // Inside refresh period - 30min
            console.log('Refreshing token')
            dispatch('refreshToken').then(() => resolve()).catch(() => reject())
          } else {
            // Outside refresh period
            console.log('Token will expire')
            resolve()
          }
        } else {
          console.log('no need to renew')
          resolve()
        }
      } else {
        console.log('no token!')
        return reject()
      }
    })
  },
  loginRequired ({state, dispatch}) {
    /**
     * If token is not valid, show login dialog
     */
    dispatch('inspectToken').catch(() => {
      dispatch('ui/showLoginDialog', {}, {root: true})
    })
  },
}
