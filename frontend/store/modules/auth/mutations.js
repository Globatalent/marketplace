
export default {

  updateToken (state, newToken) {
    localStorage.setItem('gb-token', newToken)
    state.jwt = newToken
  },
  cleanToken (state) {
    localStorage.removeItem('gb-token')
    state.jwt = null
  },
}
