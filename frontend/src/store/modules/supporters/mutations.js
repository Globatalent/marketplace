export default {
  alerts (state, alerts) {
    state.alerts = alerts
  },
  pushAlerts (state, alerts) {
    state.alerts = state.alerts.concat(alerts)
  },
  pagination(state, pagination) {
    state.pagination.count = pagination.count;
    state.pagination.next = pagination.next;
    state.pagination.previous = pagination.previous;
  },
}
