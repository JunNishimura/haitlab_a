import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import BaseButton from '@/components/UI/BaseButton.vue';
import BaseCheckBox from '@/components/UI/BaseCheckBox.vue';

const app = createApp(App);
app.component('BaseButton', BaseButton);
app.component('BaseCheckBox', BaseCheckBox);
app.use(store);
app.use(router);
app.mount('#app');