export default {
    state: {
      header_user_intro: ''
    },
    mutations: {
      get_user_intro(state, val) {
        state.header_user_intro = val
      }
    },
    actions: {
      get_user_intro(ctx, val) {
        ctx.commit('get_user_intro', val)
      }
    }
  }