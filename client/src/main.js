// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import SignIn from './components/SignIn'
import Footer from './components/Footer'
import LandingPage from '@/components/LandingPage';

import router from './router'
import Buefy from "buefy"
import GAuth from 'vue-google-oauth2'
const gauthOption = {
  clientId: '179670366717-te5ijr0k13g7rptku9jomkk1s96ehsgi.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'select_account'
}
Vue.use(GAuth, gauthOption)
Vue.use(Buefy)
Vue.config.productionTip = false;


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
new Vue({
  el: '#signin',
  router,
  components: { SignIn },
  template: '<SignIn/>',
});
new Vue({
  el: '#footer',
  router,
  components: { Footer },
  template: '<Footer/>',
});
/* new Vue({
  el: '#landing',
  router,
  components: { LandingPage },
  template: '<LandingPage/>',
}); */
