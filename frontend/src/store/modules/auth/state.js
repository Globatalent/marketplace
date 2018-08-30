export default {
  jwt: localStorage.getItem('eh-token'),
  endpoints: {
    obtainJWT: '/api/v1/login/',
    refreshJWT: '/api/v1/refresh/',
    signUp: '/api/v1/register/',
    requestRestoreCode: '/api/v1/request_restore_code/',
    restorePassword: '/api/v1/restore_password/',
    registerAthlete: '/api/v1/register/athletes/',
    registerSupporter: '/api/v1/register/supporter/'
  }
}
