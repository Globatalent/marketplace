import Vue from 'vue'


import TokenTransformer from '../../../tokens/transformers/TokenTransformer'
import PurchaseTransformer from '../../../purchases/transformers/PurchaseTransformer'


export default {

  create({state}, data) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(state.endpoints.tokens, data).then((response) => {
        const token = TokenTransformer.fetch(response.data)
        resolve(token)
      }).catch((error) => {
        reject(error)
      })
    })
  },

  purchase({state}, data) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(state.endpoints.purchases, data).then((response) => {
        const purchase = PurchaseTransformer.fetch(response.data)
        resolve(purchase)
      }).catch((error) => {
        reject(error)
      })
    })
  },

  purchases({state, commit}) {
    return new Promise((resolve, reject) => {
      Vue.axios.get(state.endpoints.purchases).then((response) => {
        const { results, count, next, previous } = response.data;
        const purchases = results.map(item => PurchaseTransformer.fetch(item));
        commit('purchases', purchases)
        resolve(purchases)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  fetchPurchase({dispatch, state, commit}, id) {
    return new Promise((resolve, reject) => {
      Vue.axios.get(`${state.endpoints.purchases}${id}/`).then((response) => {
        const purchase = PurchaseTransformer.fetch(response.data);
        dispatch('athletes/fetch', purchase.token.athlete, {root: true}).then( () => {
          commit('purchase', purchase)
          resolve(purchase)
        })
      }).catch((error) => {
        reject(error)
      })
    })
  }
}
