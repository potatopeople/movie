import Vue from 'vue';
import Vuex from 'vuex';
import movieList from './movie_list';
import movieTop from './movie_top';
import movieSearch from './movie_search';
import userAddress from './address';
import cinemas from './cinemas';
import admin from './admin';
import user from './user';

Vue.use(Vuex);

export default new Vuex.Store({
  strict: true,
  modules: {
    movieList,
    movieTop,
    movieSearch,
    userAddress,
    cinemas,
    admin,
    user,
  },
});

