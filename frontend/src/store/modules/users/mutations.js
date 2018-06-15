export default {
  setUser (state, user) {
    state.user = user
    if (user.athlete) {
      state.userType = state.userTypes.athlete
    } else if (user.supporter) {
      state.userType = state.userTypes.supporter
    }
  },
  clearUser (state) {
    state.user = null
    state.userType = null
  },
}
