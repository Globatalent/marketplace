// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store/index'
import VueMoment from 'vue-moment'
import VueI18n from 'vue-i18n'
// import FlagIcon from 'vue-flag-icon';
import './scss/theme.scss'
import { messages } from './translations/translations'
/** Theme & UI **/
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import VueMasonry from 'vue-masonry-css'
/** Axios **/
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueScrollTo from 'vue-scrollto'

Vue.config.productionTip = false

Vue.use(VueMoment)
Vue.use(VueI18n)
Vue.use(FlagIcon);
Vue.use(ElementUI, { locale })
Vue.use(VueMasonry)
Vue.use(VueAxios, axios)
Vue.use(VueScrollTo)

// csrf settings
Vue.axios.defaults.baseURL = process.env.BASE_URL
Vue.axios.defaults.headers.common['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.post['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.put['Content-Type'] = 'application/json'
Vue.axios.defaults.headers.patch['Content-Type'] = 'application/json'

Vue.axios.interceptors.request.use(request => {
  const header = store.getters['auth/header']

  if (header) {
    request.headers.common['Authorization'] = header
  }
  return request
})

// Create VueI18n instance with options
const numberFormats = {
  'en-US': {
    currency: {
      style: 'currency', currency: 'USD'
    }
  },
}
const i18n = new VueI18n({
  locale: 'en-US', // set locale
  fallbackLocale: 'en-US',
  numberFormats,
  messages // set locale messages
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
