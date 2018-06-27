export default {
  jwt: localStorage.getItem('eh-token'),
  endpoints: {
    obtainJWT: '/api/v1/login/',
    refreshJWT: '/api/v1/refresh/',
    signUp: '/api/v1/register/'
  },
}
