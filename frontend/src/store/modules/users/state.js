export default {
  user: null,
  userType: null,
  endpoints: {
    getUser: '/api/v1/users/me/',
    users: '/api/v1/users/',
    verifyEmail: '/api/v1/verify_email/',
  },
  userTypes: {
    athlete: 'athlete',
    supporter: 'supporter',
  },
}
