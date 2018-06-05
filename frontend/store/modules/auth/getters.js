export default {
  isAuthenticated(state) {
    return !!state.jwt
  },
  token(state) {
    return state.jwt
  },
  header(state) {
    return `jwt ${state.jwt}`
  }
}
