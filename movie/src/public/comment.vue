<template>
  <section class="comment_assembly_box">
    <div class="big_send_message">
      <div class="img">
        <img :src="user_intro.avatar || default_img">
      </div>
      <div class="textarea-container">
        <div class="input_mask" v-if="!token">
          <router-link tag="span" to="/login" class="login_btn">请登录</router-link>
        </div>
        <textarea
          placeholder="请自觉遵守互联网相关的政策法规,严禁发布色情，暴力，反动的言论"
          rows="5"
          :id="textarea_active"
          v-model.trim="container"
          ref="big_iput"
          maxlength="300"
        >
        </textarea>
        <span class="iconfont" @click.stop="expression_show_event">
          <span class="si">&#xe612;</span>
          <span class="s">表情</span>
          <span @click.stop="" class="expression" v-show="expression_show">
            <img v-for="item of expression_data"
            :key="item.id" :src="item.url" :title="item.title"
            @click.stop="add_expression(item.title)">
          </span>
        </span>
        <span :class="[flow,'text_total']">{{container.length + '/' + 300}}</span>
      </div>
      <div ref="sure_send" @click="check_send_container" @mouseout="out_sure_send" :class="[sure_send_token,'sure_send']" @mouseenter="enter_sure_send">发表评论</div>
      <transition
        enter-active-class='animated fadeInUp'
        leave-active-class='animated fadeOutDown'
        :duration="{enter:800,leave:500}"
      >
        <div class="send_error" v-show="error_tips">{{error_ticps_text}}</div>
      </transition>
    </div>
    <comment-talk
      :expression_data="expression_data"
      :comment_data="comment_data"
    />
  </section>
</template>

<script>
import CommentTalk from './talk'
export default {
  name: 'CommentAssembly',
  components: {
    CommentTalk
  },
  data () {
    return {
      textarea_active: '',
      container: '',
      error_ticps_text:'请不要发送0字的评论',
      error_tips: false,
      expression_show: false
    }
  },
  props: {
    comment_data: {
      type: Array,
      default:[]
    },
    user_intro: {
      type: Object
    },
    default_img: {
      type: String
    }
  },
  computed: {
   token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      if (token) {
        return reg.exec(token.version)[1]
      } else {
        return ''
      }
    },
    sure_send_token () {
      if (this.token) {
        return 'sure_send_token'
      } else {
        return ''
      }
    },
    flow () {
      if (this.container.length >= 300) {
        return 'flow'
      } else {
        return ''
      }
    },
    expression_data () {
      var i = 1,
          img_title= ['微笑','嫌弃','喜欢','呆','大哭','害羞','无语','委屈','尴尬','生气','奸笑','大笑','惊讶','囧','捂脸','灵魂出窍','吐','抠鼻','惊喜','傲娇','疼','阴险','画风突变','妙啊','doge','滑稽','吃瓜','笑哭','支持','吓','点赞'],
          img_obj = []
      for (i;i <= 31; i++) {
        img_obj.push(
          {
            id:i,url:'../../static/images/expression_'+i+'.webp',
            title: img_title[i - 1]
          }
        )
      }
      return img_obj
    }
  },
  methods: {
    expression_show_event () { // 表情框显示隐藏
      let show = this.expression_show
      if (show === false) {
        this.textarea_active = 'text_active'
        this.$refs.big_iput.focus()
      } else {
        this.textarea_active = ''
      }
      this.expression_show = show === false ? true : false
    },
    add_expression (text) { // 点击表情
      this.focus_add_container(this.$refs.big_iput,`[${text}]`)
    },
    focus_add_container (dom, text) { // 插入表情
      if (document.selection) {
       dom.focus()
       sel = document.selection.createRange()
       sel.text = text
       sel.select()
      } else if (dom.selectionStart || dom.selectionStart == '0') {
       // 得到光标前的位置
       var startPos = dom.selectionStart
       // 得到光标后的位置
       var endPos = dom.selectionEnd
       // 在加入数据之前获得滚动条的高度
       var restoreTop = dom.scrollTop
       this.container = this.container.substring(0, startPos) + text + this.container.substring(endPos, this.container.length)
       // 如果滚动条高度大于0
       if (restoreTop > 0) {
         // 返回
         dom.scrollTop = restoreTop
       }
       dom.focus()
       dom.selectionStart = startPos + text.length
       dom.selectionEnd = startPos + text.length
      } else {
        this.container += text
        dom.focus()
      }
      this.expression_show_event()
    },
    enter_sure_send () { // 发送按钮hover样式
      this.textarea_active = 'text_active'
    },
    out_sure_send () { // 发送按钮hover样式
      this.textarea_active = ''
    },
    filter_expression (text) { // 匹配表情
      let reg = text.replace(/[\[\]]/g, '')
      for (var item of this.expression_data) {
        if (reg === item.title) {
          return `<img style="display:inline-block;height:20px;width:20px" src=${item.url} />`
        }
      }
      return text
    },
    send_container (text) { // 发送内容
      text = text.replace(/\[.*?\]/g, function () {
        return this.filter_expression(arguments[0])
      }.bind(this))
      text = text.replace(/\n/g,'<br />')
      text = text.replace(/<[a-zA-Z]>/g,' ')
      text = text.replace(/<\/[a-zA-Z]>/g,' ')
      this.container = ''
      this.$emit('send_container', text)
    },
    check_send_container () { // 检查发送内容
      let text = this.container
      if (text === '') {
        this.show_error('请不要发送 0 字的评论')
      } else if (this.container.length > 300) {
        this.show_error('最多 300 字得评论')
      } else {
        this.send_container(text)
      }
    },
    show_error (text) { //提示错误信息
      this.error_tips = true
      this.error_ticps_text = text
      setTimeout(() => {
        this.error_tips = false
      }, 3000)
    },
    ex_show () { // 全屏点击事件
      this.expression_show = false
      this.textarea_active = ''
    }
  },
  mounted () {
    window.addEventListener('click',this.ex_show)
  }
}
</script>

<style lang="stylus" scoped>
  #text_active{
    background: white
    border-color: #00b5e5
    position: relative
  }
  .comment_assembly_box{
    display: flex
    flex-direction: column
    justify-content: flex-start
    .big_send_message{
      margin: auto
      display: flex
      min-width: 1000px
      position: relative
      justify-content: space-between
      .img{
        img{
          width: 48px
          height: 48px
          border-radius: 50%
          margin-top: .1rem
        }
      }
      .textarea-container{
        display: flex
        flex: 1
        flex-direction: column
        justify-content: space-between
        font-size: .3rem
        margin: 0 10px 0 37px
        position: relative
        .input_mask{
          position: absolute
          left: 0
          top: 0
          right: 0
          bottom: 0
          background: rgba(150,150,150,.7)
          z-index: 10
          border-radius: 5px
          text-align: center
          display: flex
          align-items: center
          .login_btn{
            display: inline-block
            color: white
            border-radius: 5px
            cursor: pointer
            margin: auto
            padding: .1rem .2rem
            background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.6),
                        transparent
                      )
          }
          .login_btn:active{
            background: rgb(15,153,213)
          }
        }
        .text_total{
          position: absolute
          color: rgb(15,153,213)
          font-size: 16px
          bottom: 3px
          left: 80px
        }
        .flow{
          color: red
        }
        textarea{
          color: rgb(100,100,100)
          padding: .1rem .25rem
          outline: none
          resize: none
          height: 65px
          border: 1px solid #e5e9ef
          border-radius: 4px
          background: #f4f5f7
          box-sizing: border-box
        }
        textarea:hover,textarea:focus{
          background: white
          border: 1px solid #00b5e5
        }
        .iconfont{
          display: inline-block
          user-select: none
          position: relative
          margin-top: .15rem
          padding: .1rem 0
          text-align: center
          width: 64px
          background: white
          border-radius: 4px
          color: rgb(170,170,170)
          border: 1px solid rgb(230,230,230)
          cursor: pointer
          font-size: 13px
          letter-spacing: 1px
          .si{
            font-size: 15px
          }
          .expression{
            position: absolute
            background: white
            z-index: 1
            border: 1px solid rgb(229,233,239)
            width: 341px
            padding: .2rem .05rem
            left: 0
            top: 40px
            border-radius: 6px
            box-shadow: 0 .2rem .2rem  .1rem #e5e9ef
            display: flex
            justify-content: flex-start
            flex-wrap: wrap
            img{
              padding: 4px
              width: 30px
              height: 30px
              outline: none
            }
            img:hover{
              background-color: #ddd
            }
          }
          .expression::after{
            position: absolute
            top: -4.7px
            left: 20px
            content: ''
            width: 8px
            height: 5px
            background: url('../../static/images/arrow.png') 0 -49px no-repeat
          }
        }
        .iconfont:hover{
          color: rgb(100,100,100)
        }
      }
      .sure_send{
        pointer-events: none
        background: #00a1d6
        border-color: #00a1d6
        border: 1px solid #00a1d6
        width: 70px
        height: 65px
        line-height: 25px
        display: flex
        align-items: center
        cursor: pointer
        text-align: center
        border-radius: 4px
        font-size: 15px
        outline: none
        user-select: none
        color: white
        margin-left: .35rem
        padding: .1rem .3rem
        box-sizing: border-box
        transition: .2s
      }
      .sure_send_token{
        pointer-events: auto
      }
      .sure_send:hover{
        background: #00b5e5
        border-color: #00b5e5
      }
      .send_error{
        position: absolute
        font-size: 15px
        color: white
        padding: .2rem .25rem
        top: -45px
        right: -54px
        background: rgba(233,61,61,.9)
        border-radius: 4px
        transition: .3s
      }
    }
  }
</style>
