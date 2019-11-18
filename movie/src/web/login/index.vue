<template>
  <div class="login_box">
    <login-header/>
    <div class="main">
      <div class="center">
        <login-input/>
      </div>
    </div>
    <div class="nu"></div>
    <footer>
      <login-footer/>
    </footer>
  </div>
</template>

<script>
import LoginHeader from './components/header'
import LoginInput from './components/input'
import LoginFooter from './components/footer'
export default {
  name: 'UserLogin',
  components: {
    LoginHeader,
    LoginInput,
    LoginFooter
  }
}
</script>

<style lang="stylus" scoped>
  .login_box{
    overflow: hidden
    background: white
    min-height: 100vh
    display: flex
    flex-direction: column
    .main{
      margin-top: .5rem
      .center{
        position: relative
        margin: 0 auto
        max-width: 1300px
        min-width: 1000px
        background: url('../../../static/images/login_back2.png') no-repeat
        background-size: auto
        height: 500px
        display: flex
      }
    }
    .nu{
      flex: 1
    }
  }
</style>
