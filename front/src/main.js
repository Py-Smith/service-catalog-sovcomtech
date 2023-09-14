import './assets/main.css'

import { createApp } from 'vue';
import App from './App.vue';
import axios from "axios";

const Vue = createApp(App);
//Адрес API
Vue.config.globalProperties.$HttpApiAddress = 'http://localhost:8011/api/v1/';
Vue.config.globalProperties.$axios = axios;
Vue.config.globalProperties.$loadComponent = (componentPromise) => {
    componentPromise.then(component => {
        Vue.component(component.name, component)
    })
}
Vue.mount('#app');
