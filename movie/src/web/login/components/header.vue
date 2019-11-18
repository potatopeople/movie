<template>
  <div class="header_box">
    <router-link
      tag="div"
      to="/home"
    >
    <img src="../../../assets/images/loginLogo.png">
    </router-link>
    <router-link
      tag="div"
      class="iconfont"
      v-show="path"
      to="/login"
    >
     去登录&#xe6ec;
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'LoginHeader',
  computed: {
    path () {
      let curren_path = this.$route.path,
          refine = new RegExp('^/(.*?)/'),
          path = refine.exec(curren_path) || ''
      if (path[1] === 'register') {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .header_box{
    position: relative
    padding-top: .3rem
    width: 1300px
    margin: 0 auto
    img{
      cursor: pointer
    }
    .iconfont{
      position: absolute
      right: 2rem
      color: rgb(15,153,213)
      font-size: .4rem
      bottom: 0
    }
    .iconfont:hover{
      text-decoration: underline
      cursor: pointer
    }
  }
</style>
