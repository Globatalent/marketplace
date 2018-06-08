// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store/index'
import VueMoment from 'vue-moment'
import VueI18n from 'vue-i18n'
import './scss/theme.scss'

Vue.config.productionTip = false

Vue.use(VueMoment)
Vue.use(VueI18n)

/** Theme & UI **/
import ElementUI from 'element-ui'

Vue.use(ElementUI)

/** Axios **/
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
// csrf settings
Vue.axios.defaults.baseURL = process.env.BASE_URL
Vue.axios.defaults.xsrfCookieName = 'csrftoken'
Vue.axios.defaults.xsrfHeaderName = 'X-CSRFToken'
Vue.axios.defaults.headers.common['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.post['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.put['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.patch['Content-Type'] = 'application/json'

// Ready translated locale messages
const messages = {
  en: {
    message: {
      SignIn: 'Sign In',
      Email: 'Email',
      Password: 'Password',
      RememberMe: 'Remember me',
      LogIn: 'Log in',
      ForgotYourPassword: 'Forgot your password?',
      DontHaveAccount: 'Don\'t have an account?',
      SignUp: 'Sign Up'
    }
  },
  es: {
    message: {
      SignIn: 'Registro',
      Email: 'Email',
      Password: 'Contraseña'
    }
  }
}

// Create VueI18n instance with options
const i18n = new VueI18n({
  locale: 'en', // set locale
  fallbackLocale: 'en',
  messages, // set locale messages
})

/* eslint-disable no-new */
new Vue({
  i18n,
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
