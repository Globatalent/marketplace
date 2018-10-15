export default {
  alerts (state, alerts) {
    state.alerts = alerts
  },
  updateAlert(state, alert) {
    state.alerts = state.alerts.map(originalAlert => {
      if (originalAlert.id = alert.id) {
        return alert
      }
      return originalAlert
    })
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
