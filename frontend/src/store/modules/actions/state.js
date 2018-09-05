export default {
  unread: 0,
  notifications: [],
  loadingNotifications: false,
  pagination: {
    count: 0,
    next: null,
    previous: null,
  },
  endpoints: {
    notifications: '/api/v1/notifications/',
  },
}
