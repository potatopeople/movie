<template>
  <section class="input_box">
    <div class="create step">
      <div>
        <div class="iconfont">&#xe61c;</div>
        <div class="text">邮箱验证</div>
      </div>
      <div :class="['line',steps]"></div>
    </div>
    <div :class="['phone','iconfont',stepsc]">
      <div>
        <div class="iconfont">&#xe642;</div>
        <div class="text">填写信息</div>
      </div>
      <div :class="['line', stepsT]"></div>
    </div>
    <div :class="['success','iconfont', stepscT]">
      <div>
        <div class="iconfont">&#xe607;</div>
        <div class="text">完成注册</div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'RegisterStep',
  props: {
    steps: {
      type: String,
      required: false,
      default: ''
    },
    stepsc: {
      type: String,
      required: false,
      default: ''
    },
    stepsT: {
      type: String,
      required: false,
      default: ''
    },
    stepscT: {
      type: String,
      required: false,
      default: ''
    }
  }
}
</script>

<style lang="stylus" scoped>
  fontSize() {
    flex: 1
    display: flex
    .iconfont{
      margin-left: .4rem
      font-size: .55rem
    }
    .text{
      font-size: .35rem
    }
    .line{
      flex: 1
      border-top: 2px dashed black
      margin: auto 0
    }
  }
  .topLinet {
    border-top: 2px dashed rgb(15,153,213)!important
  }
  .stept{
    color: rgb(15,153,213)!important
  }
  .step{
    color: rgb(15,153,213)!important
  }
  .topLine{
    border-top: 2px dashed rgb(15,153,213)!important
  }
  .input_box{
    margin: auto
    display: flex
    .create{
      fontSize()
    }
    .phone{
      fontSize()
    }
    .success{
      fontSize()
      flex: none
    }
  }
</style>
