import Vue from 'vue';
import Router from 'vue-router';
import WhatsOnMenu from '@/components/WhatsOnMenu';
import Menu from '@/components/Menu';
import Account from '@/components/Account';
import Steps from '@/components/Steps';



Vue.use(Router);

export default new Router({
  routes: [
      {
        path: '/account/:email',
        name: 'account',
        component: Account,
      },
    {
      path: '/parsedmenu',
      name: 'Menu',
      component: Menu,
    },
    {
      path: '/menu',
      name: 'WhatsOnMenu',
      component: WhatsOnMenu,
    },
    {
      path: '/steps',
      name: 'steps',
      component: Steps,
    },
  ],
  mode: 'history',

});
