import Vue from 'vue'


export default {
  create({state}, data) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(state.endpoints.tokens, data).then((response) => {
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  purchase({state}, data) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(state.endpoints.purchases, data).then((response) => {
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
}
