import App from './App.vue'
import {createApp} from 'vue'
import BootstrapVue3 from 'bootstrap-vue-3'
import Router from './router'
// import Vue from 'vue'
// Optional, since every component import their Bootstrap functionality
// the following line is not necessary
// import 'bootstrap'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'

const app = createApp(App)
app.use(BootstrapVue3)
app.use(Router)
app.mount('#app')

// Vue.config.productionTip = false



