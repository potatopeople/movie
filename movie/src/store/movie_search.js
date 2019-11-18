export default {
  state: {
    movie_search_list: []
  },
  mutations: {
    get_movie_search_list(state, val) {
      if (val.hasOwnProperty('data')) {
        val['page'] = val.pageSum
        if (parseInt(val.pageSum) <= 6) {
          val.pageSum = 7;
        }
        state.movie_search_list = val;
      } else {
        state.movie_search_list = [];
      }
    }
  },
  actions: {
    get_movie_search_list(ctx, val) {
      ctx.commit('get_movie_search_list', val);
    }
  }
}