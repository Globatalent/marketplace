export default {
  jwt: localStorage.getItem('gb-token'),
  endpoints: {
    obtainJWT: '/api/v1/login/',
    refreshJWT: '/api/v1/refresh/',
    signUp: '/api/v1/register/'
  },
}
