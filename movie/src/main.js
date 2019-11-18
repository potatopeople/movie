// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import iView from 'iview';
import 'swiper/dist/css/swiper.min.css';
import 'iview/dist/styles/iview.css';
import 'style/animate.css';
import 'style/border.css';
import 'style/nomalize.css';
import 'style/iconfont.css';
import 'style/spider.css';
import '@/public/spider';
import App from './App';
import router from './router';
import http from './axios/http';
import store from './store/index';
import  './public/data_mask.js';
import SlideVerify from 'vue-monoplasty-slide-verify';

Vue.use(SlideVerify);
Vue.config.productionTip = false;
Vue.use(iView);
Vue.prototype.$http = http;
Vue.prototype.bus = new Vue();
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
