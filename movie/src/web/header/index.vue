<template>
  <div class="home_box">
    <nav-address v-show="address" @close_address="control_address" />
    <header class="header_box">
      <div class="header_main" ref="header">
        <header-nav @open_address="control_address" />
        <header-search/>
        <header-user/>
      </div>
    </header>
    <div class="main" ref="main">
      <main>
        <router-view></router-view>
      </main>
      <footer>
        <movie-footer></movie-footer>
      </footer>
    </div>
  </div>
</template>

<script>
import HeaderUser from './components/user'
import HeaderSearch from './components/search'
import HeaderNav from './components/nav'
import MovieFooter from './components/footer'
import NavAddress from './components/address'
export default {
  name: 'HeaderMain',
  components: {
    HeaderNav,
    HeaderSearch,
    HeaderUser,
    MovieFooter,
    NavAddress
  },
  data () {
    return {
      address: false
    }
  },
  computed: {
    token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      return reg.exec(token.version)[1]
    },
    user_intro () {
      return this.$store.state.user.header_user_intro
    }
  },
  methods: {
    control_address (tf) { // 控制地址菜单
      this.address = tf
    },
    async get_user_intro () {
      try {
        let response = await this.$http.get_http_auth('api/user/verifyToken','',this.token)
        if (response.data.code === 200) {
          this.$store.dispatch('get_user_intro',response.data.data)
        } else {
          alert('请重新登录')
        }
      } catch (error) {
        console.log(error)
      }
    },
    check_token () {
      if (!this.user_intro && this.token) {
        this.get_user_intro()
      } else {
        console.log('游客')
      }
    }
  },
  created () {
    this.$nextTick(this.check_token)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~style/scrwidth.styl'
  @import '~style/fontFamily.styl'
  .home_box{
    position: relative
    fontFamily()
    min-height: 100vh
    display: flex
    flex-direction: column
    .header_box{
      z-index: 99
      background: white
      padding-top: .15rem
      padding-bottom: .15rem
      box-shadow: .1rem 0 .07rem rgb(150,150,150)
      .header_main{
        width: 1100px
        margin: auto
        font-size: .45rem
        display: flex
      }
      @media only screen and (min-width:1900px){
        .header_main{
          scrWidth()
        }
      }
    }
    .main{
      flex: 1
      display: flex
      flex-direction: column
      justify-content: space-around
      main{
        flex: 1
        width: 1100px
        margin: auto
      }
      @media only screen and (min-width:1900px){
        main{
          scrWidth()
        }
      }
      footer{
        margin-top: 2rem
        padding: 1rem 0 1.2rem 0
        background: rgb(38,38,38)
      }
    }
  }
</style>
