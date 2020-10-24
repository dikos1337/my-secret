import Vue from "vue";
import Vuelidate from "vuelidate";
import App from "./App.vue";
import axios from 'axios'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

Vue.config.productionTip = false;
Vue.use(Vuelidate)

new Vue({
  render: h => h(App),
}).$mount("#app");