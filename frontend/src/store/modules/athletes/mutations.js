export default {
  athlete (state, athlete) {
    state.athlete = athlete
  },
  athletes (state, athletes) {
    state.athletes = athletes
  },
  pushAthletes (state, athletes) {
    state.athletes = state.athletes.concat(athletes)
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
}
