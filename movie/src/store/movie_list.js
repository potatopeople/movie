export default {
  state: {
    movie_list: []
  },
  mutations: {
    get_movie_list(state, val) {
      val[0]['page'] = val[0].pageSum
      if (parseInt(val[0].pageSum) <= 6) {
        val[0].pageSum = 7
      }
      val[0]['catgory'] = val[1];
      state.movie_list = val[0];
    }
  },
  actions: {
    get_movie_list(ctx, val) {
      ctx.commit('get_movie_list', val);
    }
  },
  getters: {
    get_movie_list (state) {
      return state.movie_list
    }
  }
}
