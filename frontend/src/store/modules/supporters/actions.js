import Vue from 'vue'
import AlertTransformer from '../../../supporters/transformers/AlertTransformer'
import SupporterTransformer from '../../../supporters/transformers/SupporterTransformer'
import { store } from '../../index'


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
          dispatch('athletes/fetch', alert.athlete, {root: true}).then(athlete => {
            alert.athlete = athlete
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
  update({commit, state}, data) {
    return new Promise((resolve, reject) => {
      const payload = SupporterTransformer.send(data)
      Vue.axios.patch(`${state.endpoints.supporters}${payload.id}/`, payload).then( response => {
        const supporter = SupporterTransformer.fetch(response.data);
        resolve(supporter)
      }).catch((error) => {
        reject(error)
      })
    })
  },
}
