
export default {

  updateToken (state, newToken) {
    localStorage.setItem('eh-token', newToken)
    state.jwt = newToken
  },
  cleanToken (state) {
    localStorage.removeItem('eh-token')
    state.jwt = null
  },
}
