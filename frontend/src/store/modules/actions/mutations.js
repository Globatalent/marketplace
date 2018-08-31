export default {
  notifications (state, notifications) {
    state.notifications = notifications
  },
  pushNotifications (state, notifications) {
    state.notifications = state.notifications.concat(notifications)
  },
  unread (state, unread) {
    state.unread = unread
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
}
