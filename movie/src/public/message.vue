<template>
  <transition
    :enter-active-class="option.animatedIn"
    :leave-active-class="option.animatedOut"
    :duration="{'enter': option.enterTime, 'leave': option.leaveTime }"
  >
    <section
      :style="`position:${option.position};
               right:${option.right};
               top:${option.top};
               left:${option.left};
               bottom:${option.bottom};
               width:${option.width};
               height:${option.heignt};
               z-index:${option.zIndex}`"
      ref="message_box"
      class="message_box"
      v-show="option.show"
    >
      <div class="img_prompt" v-html="message_catgory[option.catgory]"></div>
      <div class="text_prompt">
        <p class="title" ref="title" v-show="option.title">{{option.title}}</p>
        <p class="message" ref="message">{{option.message}}</p>
        <p class="tf_btn" v-show="option.btn_show">
          <span @click="sure_btn" class="sure iconfont">&#xe60c;</span>
          <span @click="close_btn" class="close iconfont">&#xe60d;</span>
        </p>
      </div>
    </section>
  </transition>
</template>

<script>
export default {
  name: 'MessageBox',
  data () {
    return {
      message_catgory: {
        tips: `<p class="iconfont" style="margin:0;color:rgb(15,153,213);font-size:${this.option.tiSize}">&#xe606;</p>`,
        warning: `<p class="iconfont" style="margin:0;color:rgb(245,245,13);font-size:${this.option.tiSize}">&#xe736;</p>`,
        success: `<p class="iconfont" style="margin:0;color:rgb(53,216,26);font-size:${this.option.tiSize}">&#xeaca;</p>`,
        error: `<p class="iconfont" style="margin:0;color:rgb(242,8,8);font-size:${this.option.tiSize}">&#xe60b;</p>`
      }
    }
  },
  props: {
    option: {
      type: Object,
      default: {
        show: true, // 是否显示
        btn_show: false, // 确认、取消按钮显示
        position: 'relative', // 定位
        zIndex: '0', // 层级
        tiSize: '.3rem', // 图标大小
        titSize: '.5rem', // 标题大小
        messSize: '.3rem', // 消息大小
        title: '', // 标题内容
        message: '消息', // 消息内容
        catgory: 'tips', // 图标类型
        animatedIn: '', // 出现时动画效果
        animatedOut: '', // 退出时动画效果
        width: 'auto', // 宽度
        height: 'auto', // 高度
        center: '',  // 水平居中
        parentDom: '', // 根据该元素进行水平居中
        right: '', // 右定位
        top: '', //上定位
        left: '', //左定位
        bottom: '', //下定位
        enterTime: 500, // 进入动画时间
        leaveTime: 500 // 离开动画时间
      }
    }
  },
  methods: {
    sure_btn () {
      this.$emit('sure_btn')
    },
    close_btn () {
      this.$emit('close_btn')
    },
    style_application () { // 样式应用
      this.$refs.title.style.fontSize = this.option.titSize
      this.$refs.message.style.fontSize = this.option.messSize
    }
  },
  mounted () {
    this.$nextTick(this.style_application)
  }
}
</script>

<style lang="stylus" scoped>
  .message_box{
    user-select: none
    box-shadow: 0 0 .1rem rgb(150,150,150)
    border-radius: .07rem
    display: flex
    align-items: center
    background: white
    padding: .2rem .3rem
    .img_prompt{
      color: rgb(40,40,40)
    }
    .text_prompt{
      margin-left: .35rem
      color: rgb(100,100,100)
      p{
        margin: 0
      }
      .tf_btn{
        height: 20px
        display: flex
        justify-content: space-between
        span{
          padding: .18rem .2rem
          display: flex
          font-size: .35rem
          align-items: center
          cursor: pointer
          margin-top: .1rem
        }
        .sure{
          background: rgb(15,153,213)
          color: white
        }
        .close{
          background: rgb(227,13,23)
          color: white
        }
      }
    }
  }
</style>
