import Vue from 'vue';
import Router from 'vue-router';
import Locations from '@/components/Locations';
import Menu from '@/components/Menu';
import Filters from '@/components/Filters';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/locations',
      name: 'Locations',
      component: Locations,
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
