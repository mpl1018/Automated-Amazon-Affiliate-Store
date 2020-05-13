import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import { BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import firebase from "firebase/app";
import 'firebase/firestore';
import store from './store';
import {configOptions} from './keys.js';

Vue.use(BootstrapVueIcons)
Vue.config.productionTip = false


firebase.initializeApp(configOptions);
export const db = firebase.firestore(); 

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

