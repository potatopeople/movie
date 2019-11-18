<template>
  <section class="mask">
    <div class="model">
      <div class="icon"></div>
      <div class="ticps">{{ticps}}</div>
      <div class="btn" @click="error_ticps">我知道了</div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'ScreenMask',
  props: {
    ticps: {
      type: String,
      default: ''
    }
  },
  methods: {
    error_ticps () {
      this.$emit('error_ticps','close')
    }
  }
}
</script>

<style lang="stylus" scoped>
    .mask{
      position: fixed
      left: 0
      right: 0
      top: 0
      bottom: 0
      z-index: 99998
      background: rgba(0,0,0,.4)
      .model{
        background-color: #fff
        position: absolute
        text-align: center
        left: 0
        right: 0
        top: 0
        bottom: 0
        margin: auto
        padding: 30px 0
        box-sizing: content-box
        width: 460px
        height: 155px
        .icon{
          width: 50px
          height: 50px
          margin: auto
          background: url('../../static/images/error.png') no-repeat
        }
        .ticps{
          color: #666
          font-size: 16px
          margin: 12px 0 26px 0
        }
        .btn{
          box-shadow: 0 2px 10px -2px #f03d37
          background: #f03d37
          color: #fff
          width: 260px
          height: 42px
          line-height: 42px
          font-size: 16px
          border-radius: 100px
          margin: auto
          cursor: default
        }
      }
    }
</style>

