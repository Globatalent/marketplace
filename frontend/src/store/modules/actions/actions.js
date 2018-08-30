import Vue from 'vue'
import NotificationTransformer from '../../../actions/transformers/NotificationTransformer'


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
}
