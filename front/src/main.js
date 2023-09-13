import './assets/main.css'

import { createApp } from 'vue';
import App from './App.vue';
import axios from "axios";

const Vue = createApp(App);
//Адрес API
Vue.config.globalProperties.$HttpApiAddress = import.meta.env.VITE_API_URL;
Vue.config.globalProperties.$axios = axios;
Vue.config.globalProperties.$loadComponent = (componentPromise) => {
    componentPromise.then(component => {
        Vue.component(component.name, component)
    })
}
Vue.mount('#app');
