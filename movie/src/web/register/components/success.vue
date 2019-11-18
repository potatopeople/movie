<template>
  <section>
    <div class="tips_box">
      <span class="tips">恭喜您完成注册!</span>
    </div>
    <p>尊敬的用户，您已成功注册土豆电影网账号，请
      <router-link
        tag="span"
        to="/login"
      >
        点击登录
      </router-link>！
    </p>
    <router-link
      tag="div"
      to="/login"
      class="login_btn"
    >
      立即登录
    </router-link>
  </section>
</template>

<script>
export default {
  name: 'RegisterSuccess',
  data () {
    return {
    }
  },
  methods: {
    setp_success (val) {
      if (val === 'success') {
        this.$emit('steptwo','topLinet','stept')
        this.$emit('step', 'topLine', 'step')
      }
    }
  },
  mounted () {
    
    this.setp_success(this.$route.query.step)
  }
}
</script>

<style lang="stylus" scoped>
  .tips_box{
    width: 100%
    height: 115px
    .tips{
      display: table-cell
      text-align: right
      vertical-align: middle
      width: 150px
      font-size: .7rem
      width: 520px
      color: rgb(15,153,213)
      height: 115px
      background: url('../../../../static/images/gougou2.png') 0 no-repeat
      background-position: 1.8rem
    }
  }
  p{
    //border-top: 1px dashed black
    margin-top: .5rem
    font-size: .35rem
    text-align: center
    padding-top: .5rem
    span{
      color: rgb(15,103,213)
      font-weight: 600
      cursor: pointer
    }
  }
  .login_btn{
    margin: auto
    display: flex
    align-items: center
    justify-content: center
    margin-top: .5rem
    border: 1px solid rgb(15,153,213)
    width: 300px
    cursor: pointer
    user-select: none
    color: black
    font-size: .45rem
    height: 50px
    background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                  )
    }
    .login_btn:active{
      border: 1px solid rgb(15,50,213)
    }
</style>

