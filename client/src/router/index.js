import Vue from 'vue';
import Router from 'vue-router';
import WhatsOnMenu from '@/components/WhatsOnMenu';
import Menu from '@/components/Menu';
import Account from '@/components/Account';
import Steps from '@/components/Steps';
import Contact from '@/components/Contact';



Vue.use(Router);

export default new Router({
  routes: [
      {
        path: '/account/:email',
        name: 'Account',
        component: Account,
      },
    {
      path: '/parsedmenu',
      name: 'Menu',
      component: Menu,
    },
    {
      path: '/menu/:email',
      name: 'WhatsOnMenu',
      component: WhatsOnMenu,
    },
    {
      path: '/steps',
      name: 'steps',
      component: Steps,
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact,
    },
  ],
  mode: 'history',

});
