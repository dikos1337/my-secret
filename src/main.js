import Vue from "vue";
import Vuelidate from "vuelidate";
import App from "./App.vue";
import axios from "axios"
import router from "./router"

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"

Vue.config.productionTip = false;
Vue.use(Vuelidate)


new Vue({
  router,
  render: h => h(App),
}).$mount("#app");