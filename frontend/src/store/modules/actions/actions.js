import Vue from 'vue'
import NotificationTransformer from '@/actions/transformers/NotificationTransformer'


export default {
  notifications({commit, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters, push } = payload
      let endpoint = state.endpoints.notifications
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results, count, next, previous } = response.data;
        const notifications = results.map(item => NotificationTransformer.fetch(item));
        if (push) {
          commit('pushNotifications', notifications)
        } else {
          commit('notifications', athletes)
        }
        commit('pagination', {count, next, previous})
        resolve(notifications)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  updateNotification({dispatch, state}, payload) {
    return new Promise((resolve, reject) => {
      Vue.axios.patch(`${state.endpoints.notifications}${payload.id}/`, payload).then(response => {
        const notification = NotificationTransformer.fetch(response.data)
        dispatch('unread').then( () => {
          resolve(notification)
        }).catch( error => {
          reject(error)
        })
      }).catch((error) => {
        reject(error)
      })
    })
  },
  unread({commit, state}) {
    return new Promise((resolve, reject) => {
      const endpoint = `${state.endpoints.notifications}count/?read=False`
      Vue.axios.get(endpoint).then((response) => {
        const { count } = response.data;
        commit('unread', count)
        resolve(count)
      }).catch((error) => {
        reject(error)
      })
    })
  }
}
