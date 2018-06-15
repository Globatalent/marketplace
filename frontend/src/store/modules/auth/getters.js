export default {
  isAuthenticated(state) {
    return !!state.jwt
  },
  token(state) {
    return state.jwt
  },
  header(state) {
    const token = state.jwt
    return token ? `jwt ${token}` : null
  }
}
