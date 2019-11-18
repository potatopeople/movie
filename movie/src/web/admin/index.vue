<template>
  <section class="login_box">
    <login-box @regstir_user="regstir_user" v-show="login" />
  </section>
</template>

<script>
import LoginBox from './components/box'
export default {
  name: 'WebLogin',
  components: {
    LoginBox
  },
  data () {
    return {
      login: true
    }
  },
  methods: {
    login_user (val1, val2) {
      this.regstir = val1
      this.login = val2
    }
  }
}
</script>

<style lang="stylus" scoped>
  .login_box{
    position: fixed
    height: 100%
    width: 100%
    display: flex
    align-items: center
    background: white
    justify-content: center
  }
</style>
