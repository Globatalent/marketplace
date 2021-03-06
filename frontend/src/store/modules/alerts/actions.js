import Vue from 'vue'
import AlertTransformer from '../../../users/transformers/AlertTransformer'


export default {
  alerts ({commit, dispatch, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters, push } = payload
      let endpoint = state.endpoints.alerts
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results, count, next, previous } = response.data;
        const rawAlerts = results.map(item => AlertTransformer.fetch(item));
        const alerts = rawAlerts.map( alert => {
          dispatch('campaigns/fetch', alert.campaign, {root: true}).then(campaign => {
            alert.campaign = campaign
            commit('updateAlert', alert)
          }).catch( () => {
          })
          return alert
        });
        if (push) {
          commit('pushAlerts', alerts)
        } else {
          commit('alerts', alerts)
        }
        commit('pagination', {count, next, previous})
        resolve(alerts)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  createAlert({state}, payload) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(state.endpoints.alerts, AlertTransformer.send(payload)).then( response => {
        const alert = AlertTransformer.fetch(response.data)
        resolve(alert)
      }).catch( error => {
        reject(error)
      })
    })
  },
}
