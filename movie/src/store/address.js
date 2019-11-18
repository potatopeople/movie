
export default {
    state: {
      user_address: {
        id: 1,
        name: '北京'
      } // 用户地址
    },
    mutations: {
      get_user_address(state, val) {
        window.localStorage.setItem('userAddress', JSON.stringify(val))
        state.user_address = val
      }
    },
    actions: {
      get_user_address(ctx, val) {
        ctx.commit('get_user_address', val)
      }
    }
  }