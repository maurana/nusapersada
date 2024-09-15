import { createApp } from 'vue'
import VueApexCharts from 'vue3-apexcharts'
import App from './App.vue'
import router from './router'
import './index.css'
import '../node_modules/flowbite-vue/dist/index.css'

const app = createApp(App)
app.use(router)
app.use(VueApexCharts)
app.component('apexchart', VueApexCharts)
app.mount('#app')