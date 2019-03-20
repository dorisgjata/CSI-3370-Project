import Vue from 'vue';
import Router from 'vue-router';
import Locations from '@/components/Locations';
import Menu from '@/components/Menu';
import Filters from '@/components/Filters';
import SignIn from '@/components/SignIn';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/locations',
      name: 'Locations',
      component: Locations,
    },
      {
        path: '/signIn',
        name: 'SignIn',
        component: SignIn,
      },
    {
      path: '/filters',
      name: 'Filters',
      component: Filters,
    },
    {
      path: '/menu',
      name: 'Menu',
      component: Menu,
    },
  ],
  mode: 'history',

});
