export default {
  state: {
    movie_rank_list: []
  },
  mutations: {
    get_movie_rank_list(state, val) {
      val[0]['page'] = val[0].pageSum
      if (parseInt(val[0].pageSum) <= 6) {
        val[0].pageSum = 7
      }
      val[0].data.forEach((item, index) => {
        if (item.rank === 1) {
          item['style'] = 'first'
        } else if (item.rank === 2 || item.rank === 3) {
          item['style'] = 'secend'
        } else {
          item['style'] = ''
        }
      })
      val[0]['catgory'] = val[1];
      state.movie_rank_list = val[0];
    }
  },
  actions: {
    get_movie_rank_list(ctx, val) {
      ctx.commit('get_movie_rank_list', val)
    }
  }
}