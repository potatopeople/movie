export default {
    state: {
      cinemas: [] // 用户地址
    },
    mutations: {
      get_cinemas_data(state, val) {
        state.cinemas = val
      }
    },
    actions: {
      get_cinemas_data(ctx, val) {
        ctx.commit('get_cinemas_data', val)
      }
    }
  }