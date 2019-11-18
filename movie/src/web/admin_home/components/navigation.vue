<template>
  <section class="nav_box">
    <div class="nav">
      <span class="home">首页</span>
      <span class="point iconfont">&#xe6ec;</span>
      <span>{{curren_list || querys.ptext}}</span>
      <span v-if="curren_chlid || querys.text" class="point iconfont">&#xe6ec;</span>
      <span>{{curren_chlid || querys.text}}</span>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ListNav',
  computed: {
    querys () {
      return this.$route.query
    }
  },
  props: {
    curren_list: {
      type: String,
      default: ''
    },
    curren_chlid: {
      type: String,
      default: ''
    }
  }
}
</script>

<style lang="stylus" scoped>
  .nav_box{
    flex: 1
    display: flex
    .nav{
      cursor: default
      flex: 1
      font-size: .32rem
      display: flex
      box-sizing: border-box
      span{
        display: flex
        align-items: center
      }
      .point{
        color: rgb(200,200,200)
        margin: 0 .2rem
      }
      .home{
        font-weight: 600
      }
    }
  }
</style>
