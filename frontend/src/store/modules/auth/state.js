export default {
  jwt: localStorage.getItem('eh-token'),
  endpoints: {
    obtainJWT: '/api/v1/auth/jwt/token/',
    refreshJWT: '/api/v1/auth/jwt/refresh/',
    signUp: '/api/v1/register/',
    users: '/api/v1/users/',
    requestRestoreCode: '/api/v1/request_restore_code/',
    restorePassword: '/api/v1/restore_password/',
    registerAthlete: '/api/v1/register/athletes/',
    registerSupporter: '/api/v1/register/supporter/'
  }
}
