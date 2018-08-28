import Vue from 'vue'
import AthleteTransformer from '../../../athletes/transformers/AthleteTransformer'
import { store } from '../../index'

export default {
  list({commit, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters, push } = payload
      let endpoint = state.endpoints.athletes
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results, count, next, previous } = response.data;
        const athletes = results.map(item => AthleteTransformer.fetch(item));
        if (push) {
          commit('pushAthletes', athletes)
        } else {
          commit('athletes', athletes)
        }
        commit('pagination', {count, next, previous})
        resolve(athletes)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  fetch({commit, state}, id) {
    return new Promise((resolve, reject) => {
      Vue.axios.get(`${state.endpoints.athletes}${id}/`).then((response) => {
        const athlete = AthleteTransformer.fetch(response.data);
        commit('athlete', athlete)
        resolve(athlete)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  follow({state}, id) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(`${state.endpoints.athletes}${id}/follow/`).then((response) => {
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
}
