// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import { store } from './store/index'
import VueMoment from 'vue-moment'
import './scss/theme.scss'

Vue.config.productionTip = false

Vue.use(VueMoment)

/** Theme & UI **/
import ElementUI from 'element-ui'
import VueMasonry from 'vue-masonry-css'

Vue.use(ElementUI)
Vue.use(VueMasonry)

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

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
