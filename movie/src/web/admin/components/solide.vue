<template>
  <section class="silde_box" v-show="silde_option.show">
    <p class="header">
      <span class="tips">完成拼图验证</span>
      <span class="iconfont" @click="close_verify">&#xe60d;</span>
    </p>
    <slide-verify
      :l="42"
      :r="10"
      :w="410"
      :h="250"
      :slider-text="text"
      @success="success"
      @fail="fail"
    ></slide-verify>
  </section>
</template>

<script>
export default {
  name: 'VerifySilde',
  data () {
    return {
      text: '向右滑动',
      img: [
        {url:require('@/assets/images/silde_one.jpg')}
      ]
    }
  },
  props: {
    silde_option: {
      type: Object,
      default: {
        show: true
      }
    },
    user_login: {
      type: Object,
      default: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    success () { // 拼图验证成功
      setTimeout(() => {
        this.$router.push('/admin/home')
      },1000)
    },
    fail () { // 拼图验证错误
      console.log('验证错误')
    },
    close_verify () {
      this.$emit('close_verify', false)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .silde_box{
    position: absolute
    z-index: 1
    background: white
    bottom: 2.1rem
    box-shadow: 0 -.05rem .05rem rgb(150,150,150)
    filter: drop-shadow(0 .07rem .05rem rgb(150,150,150))
    font-size: .3rem
    box-sizing: content-box
    padding: .2rem .4rem
    width: calc(450px - .8rem)
    left: 0
    .header{
      margin: 0 0 .2rem 0
      display: flex
      justify-content: space-between
      display: flex
      align-items: center
      .iconfont{
        font-size: .45rem
        cursor: pointer
        margin-right: -.1rem
      }
    }
  }
  .silde_box:before{
    content: ''
    bottom: -.4rem
    left: calc((450px - .4rem) / 2 - 3px)
    position: absolute
    border: 10px solid white
    border-color: white transparent transparent transparent
  }
</style>
