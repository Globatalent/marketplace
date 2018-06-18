export default {
  jwt: localStorage.getItem('eh-token'),
  endpoints: {
    obtainJWT: 'http://localhost:8000/api/v1/login/',
    refreshJWT: 'http://localhost:8000/api/v1/refresh/',
    signUp: 'http://localhost:8000/api/v1/register/'
  },
}
