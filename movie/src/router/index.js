import Vue from 'vue';
import Router from 'vue-router';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/', // header
      name: 'webs',
      redirect: '/home',
      component: () => import('@/web/header/index'),
      children: [
        {
          path: '/home', // 主页
          name: 'home',
          component: () => import('@/web/home/index'),
        },
        {
          path: '/movie_list',
          name: 'MovieList',
          component: () => import('@/web/movie/index'),
        },
        {
          path: '/movie_top',
          name: 'MovieTop',
          component: () => import('@/web/top/index'),
        },
        {
          path: '/movie_search',
          name: 'MovieSearch',
          component: () => import('@/web/search/index'),
        },
        {
          path: '/cinemas',
          name: 'Cinemas',
          component: () => import('@/web/cinemas/index'),
        },
        {
          path: '/cinemas_movie',
          name: 'CinemasMovie',
          component: () => import('@/web/cinemas_movie/index'),
        },
        {
          path: '/releasemovie',
          name: 'ReleaseMovie',
          component: () => import('@/web/release_movie'),
        },
        {
          path: '/movie/buy_ticket',
          name: 'BuyTicket',
          component: () => import('@/web/buy_ticket'),
        },
        {
          path: '/movie/pay',
          name: 'OrderPay',
          component: () => import('@/web/pay_money/index'),
        },
        {
          path: '/center',
          name: 'UserCenter',
          redirect: '/center/intro',
          component: () => import('@/web/center/index'),
          children: [
            {
              path: '/center/intro',
              name: 'IntroBox',
              component: () => import('@/web/center/components/intro'),
            },
            {
              path: '/center/order',
              name: 'OrderBox',
              component: () => import('@/web/center/components/order'),
            },
          ],
        },
      ],
    },
    {
      path: '/login', // 登录
      name: 'UserLogin',
      component: () => import('@/web/login/index'),
    },
    {
      path: '/admin/home',
      name: 'WebHome',
      component: () => import('@/web/admin_home/index'),
      children: [
        {
          path: '/admin/home/user',
          name: 'UserIntro',
          component: () => import('@/web/admin_user/index'),
        },
        {
          path: '/admin/home/talk',
          name: 'UserTalk',
          component: () => import('@/web/admin_talk/index'),
        },
      ],
    },
    {
      path: '/admin', // 后台登陆
      name: 'WebLogin',
      component: () => import('@/web/admin/index'),
    },
    {
      path: '/register', // 注册
      name: 'Register',
      redirect: '/register/input',
      component: () => import('@/web/register/index'),
      children: [
        {
          path: '/register/email', // 邮箱验证
          name: 'RegisterEmail',
          component: () => import('@/web/register/components/email'),
        },
        {
          path: '/register/input', // 输入信息
          name: 'RegisterInput',
          component: () => import('@/web/register/components/input'),
        },
        {
          path: 'register/success', // 注册成功
          name: 'RegisterSuccess',
          component: () => import('@/web/register/components/success'),
        },
      ],
    },
  ],
});
