
export default {
    state: {
      user_intro: ''
    },
    mutations: {
      get_admin_user_intro(state, val) {
        state.user_address = val
      }
    },
    actions: {
      get_admin_user_intro(ctx, val) {
        ctx.commit('get_admin_user_intro', val)
      }
    }
  }