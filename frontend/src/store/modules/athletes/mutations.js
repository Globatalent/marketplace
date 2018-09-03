export default {
  athlete (state, athlete) {
    state.athlete = athlete
  },
  athletes (state, athletes) {
    state.athletes = athletes
  },
  reviews (state, reviews) {
    state.reviews = reviews
  },
  pushAthletes (state, athletes) {
    state.athletes = state.athletes.concat(athletes)
  },
  pushReviews (state, reviews) {
    state.reviews = state.reviews.concat(reviews)
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
  reviewsPagination(state, pagination) {
    state.reviewsPagination.count = pagination.count;
    state.reviewsPagination.next = pagination.next;
    state.reviewsPagination.previous = pagination.previous;
  },
}
