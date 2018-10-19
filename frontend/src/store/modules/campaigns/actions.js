import Vue from 'vue'
import CampaignTransformer from '../../../campaigns/transformers/CampaignTransformer'


export default {
  list({commit, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters, push } = payload
      let endpoint = state.endpoints.campaigns
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results, count, next, previous } = response.data;
        const campaigns = results.map(item => CampaignTransformer.fetch(item));
        if (push) {
          commit('pushCampaigns', campaigns)
        } else {
          commit('campaigns', campaigns)
        }
        commit('pagination', {count, next, previous})
        resolve(campaigns)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  fetch({commit, state}, id) {
    return new Promise((resolve, reject) => {
      Vue.axios.get(`${state.endpoints.campaigns}${id}/`).then((response) => {
        const campaign = CampaignTransformer.fetch(response.data);
        commit('campaign', campaign)
        resolve(campaign)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  delete({commit, state}, data) {
    return new Promise((resolve, reject) => {
      const payload = CampaignTransformer.send(data)
      Vue.axios.delete(`${state.endpoints.campaigns}${payload.id}/`, payload).then( response => {
        commit('campaign', {})
        resolve()
      }).catch((error) => {
        reject(error)
      })
    })
  },
  create({commit, state}, data) {
    return new Promise((resolve, reject) => {
      const payload = CampaignTransformer.send(data)
      Vue.axios.post(state.endpoints.campaigns, payload).then( response => {
        const campaign = CampaignTransformer.fetch(response.data);
        commit('campaign', campaign)
        resolve(campaign)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  update({commit, state}, data) {
    return new Promise((resolve, reject) => {
      const { links, revenues, incomes } = data
      const payload = CampaignTransformer.send(data)
      Vue.axios.patch(`${state.endpoints.campaigns}${payload.id}/`, payload).then( response => {
        const campaign = CampaignTransformer.fetch(response.data);
        let requests = []  // All extra requests needed
        // Check for links
        if (typeof links !== "undefined" && links.length > 0) {
          const toCreateLinks = links.filter( link => !link.id && link.url !== "")
          const toEditLinks = links.filter( link => !!link.id && link.url !== "")
          requests = requests.concat(
            toCreateLinks.map(linkPayload => {
              return Vue.axios.post(`${state.endpoints.links}`, linkPayload)
            })
          ).concat(
            toEditLinks.map(linkPayload => {
              return Vue.axios.patch(`${state.endpoints.links}${linkPayload.id}/`, linkPayload)
            })
          )
        }
        // Check for revenues
        if (typeof revenues !== "undefined" && revenues.length > 0) {
          const toCreateRevenues = revenues.filter( revenue => !revenue.id && !!revenue.amount)
          const toEditRevenues = revenues.filter( revenue => !!revenue.id && !!revenue.amount)
          requests = requests.concat(
            toCreateRevenues.map(revenuePayload => {
              return Vue.axios.post(`${state.endpoints.revenues}`, revenuePayload)
            })
          ).concat(
            toEditRevenues.map(revenuePayload => {
              return Vue.axios.patch(`${state.endpoints.revenues}${revenuePayload.id}/`, revenuePayload)
            })
          )
        }
        // Check for incomes
        if (typeof incomes !== "undefined" && incomes.length > 0) {
          const toCreateIncomes = incomes.filter( income => !income.id && !!income.amount)
          const toEditIncomes = incomes.filter( income => !!income.id && !!income.amount)
          requests = requests.concat(
            toCreateIncomes.map(incomePayload => {
              return Vue.axios.post(`${state.endpoints.incomes}`, incomePayload)
            })
          ).concat(
            toEditIncomes.map(incomePayload => {
              return Vue.axios.patch(`${state.endpoints.incomes}${incomePayload.id}/`, incomePayload)
            })
          )
        }
        // If there are some external requests, wait for all of them
        if (requests.length > 0) {
          Vue.axios.all(requests).then( () => {
            commit('campaign', campaign)
            resolve(campaign)
          })
        } else {
          commit('campaign', campaign)
          resolve(campaign)
        }
      }).catch((error) => {
        reject(error)
      })
    })
  },
  follow({state}, id) {
    return new Promise((resolve, reject) => {
      Vue.axios.post(`${state.endpoints.campaigns}${id}/follow/`).then((response) => {
        resolve(response)
      }).catch((error) => {
        reject(error)
      })
    })
  },
  createPicture({state}, payload) {
    return new Promise((resolve, reject) => {
      const config = { headers: { 'Content-Type': 'multipart/form-data' } };
      const formData = new FormData();
      Object.keys(payload).forEach((key) => {
        const value = data[key];
        if (!!value) {
          formData.append(key, value);
        }
      });
      return Vue.axios.post(state.endpoints.pictures, formData, config).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  updatePicture({state}, payload) {
    return new Promise((resolve, reject) => {
      const config = { headers: { 'Content-Type': 'multipart/form-data' } };
      const formData = new FormData();
      Object.keys(payload).forEach((key) => {
        const value = data[key];
        if (!!value) {
          formData.append(key, value);
        }
      });
      return Vue.axios.patch(`${state.endpoints.pictures}${payload.id}/`, formData, config).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  deletePicture({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.delete(`${state.endpoints.pictures}${payload.id}/`).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  createLink({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.post(state.endpoints.links, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  updateLink({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.patch(`${state.endpoints.links}${payload.id}/`, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  deleteLink({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.delete(`${state.endpoints.links}${payload.id}/`).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  createRevenue({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.post(state.endpoints.revenues, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  updateRevenue({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.patch(`${state.endpoints.revenues}${payload.id}/`, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  deleteRevenue({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.delete(`${state.endpoints.revenues}${payload.id}/`).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  createIncomes({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.post(state.endpoints.incomes, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  updateIncomes({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.patch(`${state.endpoints.incomes}${payload.id}/`, payload).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  deleteIncomes({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.delete(`${state.endpoints.incomes}${payload.id}/`).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  createRecommendation({state}, payload) {
    return new Promise((resolve, reject) => {
      const config = { headers: { 'Content-Type': 'multipart/form-data' } };
      const formData = new FormData();
      Object.keys(payload).forEach((key) => {
        const value = data[key];
        if (!!value) {
          formData.append(key, value);
        }
      });
      return Vue.axios.post(state.endpoints.recommendations, formData, config).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  updateRecommendation({state}, payload) {
    return new Promise((resolve, reject) => {
      const config = { headers: { 'Content-Type': 'multipart/form-data' } };
      const formData = new FormData();
      Object.keys(payload).forEach((key) => {
        const value = data[key];
        if (!!value) {
          formData.append(key, value);
        }
      });
      return Vue.axios.patch(`${state.endpoints.recommendation}${payload.id}/`, formData, config).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  deleteRecommendation({state}, payload) {
    return new Promise((resolve, reject) => {
      return Vue.axios.delete(`${state.endpoints.recommendation}${payload.id}/`).then(response => {
        resolve(response)
      }).catch(error => {
        reject(error)
      })
    })
  },
  sports({commit, state}, payload={}) {
    return new Promise((resolve, reject) => {
      const { url, filters } = payload
      let endpoint = state.endpoints.sports
      if (!!url) {
        endpoint = url
      } else if (!!filters) {
        const query = Object.keys(filters).map(key => `${key}=${filters[key]}`).join('&')
        endpoint = [endpoint, query].join('?')
      }
      Vue.axios.get(endpoint).then((response) => {
        const { results } = response.data;
        const sports = results;
        commit('sports', sports)
        resolve(sports)
      }).catch((error) => {
        reject(error)
      })
    })
  },
}
