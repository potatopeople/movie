<template>
  <div class="email_box">
    <div class="email">
      <div class="user">邮箱</div>
      <div class="input">
        <input
          @focus="email_focus('email')"
          @blur="email_blur('email')"
          v-model="email"
          maxlength="30"
          placeholder="验证邮箱"
          type="text"
        />
        <div class="iconfont" @click="clear" v-if="email">&#xe609;</div>
      </div>
    </div>
    <p :class="['intro',email_caveat]">
      <span class="iconfont">&#xe635;</span>
      {{email_intro}}
    </p>
    <transition
      enter-active-class='animated fadeIn'
      @before-enter=spider_before
      @enter="spider_enter"
      @after-enter="spider_after"
    >
      <div class="spider_box" v-if="success_spider" ref="spider">
      <div class="mask">向右拖动发送邮件</div>
      <slider-pips
        :min="0"
        :max="spider"
        :step="1"
        labels range
        :values="[0]"
        :email="email"
        @verify_email="verify_email"
        @post_email="post_success"
      >
      </slider-pips>
      <transition
        enter-active-class='animated fadeIn'
      >
        <div class="iconfont" v-show="success_email">&#xe607;</div>
      </transition>
      <transition
        enter-active-class='animated fadeIn'
      >
        <div class="iconfont" style="color:red" v-show="error_email">&#xe60b;</div>
      </transition>
    </div>
    </transition>
    <transition
      enter-active-class='animated fadeIn'
      leave-active-class='animated fadeOut'
    >
      <div class="verify" v-if="verify_show">
        <div class="user">验证码</div>
        <div class="input">
          <input
            v-model="verify"
            maxlength="8"
            placeholder="邮箱接收的验证码"
            type="text"
            @focus="email_focus('verify')"
            @blur="email_blur('verify')"
          />
          <div class="iconfont" @click="newPost">重新发送</div>
        </div>
      </div>
    </transition>
    <p :class="['intro',verify_caveat]">
      <span class="iconfont">&#xe635;</span>
        {{verify_text}}
    </p>
    <div class="next_step" @click="next_step">
      <p>下一步</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RegisterEmail',
  data () {
    return {
      spider: 20,
      success_spider: true,
      success_email: false,
      error_email: false,
      verify_show: false,
      email: '',
      verify: '',
      verify_text: '',
      verify_caveat: 'introThree',
      email_caveat: 'introThree',
      email_intro: ''
    }
  },
  methods: {
    verify_email (text='邮箱不能为空！',color='introTwo') {
      this.email_intro = text
      this.email_caveat = color
    },
    email_focus (val) {
      if (val === 'email') {
        this.email_intro = '请输入您的邮箱！'
        this.email_caveat = 'introOne'
      } else if (val === 'verify') {
        this.verify_text = '请输入您的验证码!'
        this.verify_caveat = 'introOne'
      }
    },
    email_blur (val) {
      if (val === 'email') {
        this.email_caveat = 'introThree'
      } else if (val === 'verify') {
        this.verify_caveat = 'introThree'
      }
    },
    next_verify () {
      if (this.email === '') {
        this.verify_email()
        return false
      } else {
        if (this.verify === '') {
          this.verify_text = '验证码不能为空!'
          this.verify_caveat = 'introTwo'
          return false
        } else {
          return true
        }
      }
    },
    async next_step () { // 发送验证码给后端
      if (this.next_verify()) {
        let email = {
          random: this.verify,
          email: this.email
        }
        try {
          let response = await this.$http.postHttp('api/emailVerify', email)
          this.verify_success(response.data.message)
        } catch (error) {
          console.log(error)
        }        
      }
    },
    verify_success (val) { // 判断是否验证成功
      if (val === '验证成功！') {
        this.$router.replace({
          path: '/register/input',
          query: {
            step: 'information',
            email: this.email
          }
        })
        alert('验证成功')
      } else if (val === '验证码错误！') {
        this.verify_caveat = 'introTwo'
        this.verify_text = val
      } else if (val === '验证码已过期，请重新发送邮件！') {
        this.verify_caveat = 'introTwo'
        this.verify_text = val
      } else {
        this.verify_caveat = 'introTwo'
        this.verify_text = val
      }
    },
    newPost () { // 重新发送邮件
      this.verify_text = ''
      this.verify_caveat = 'introThree'
      this.verify = ''
      this.success_spider = true
      this.verify_show = false
      this.bus.$emit('new_post_email')
    },
    clear () {
      this.email = ''
    },
    post_email_success (val) {
      this.success_email = val
      setTimeout(() => {
        this.success_spider = false
        this.success_email = false
        this.verify_show = true
      },1000)
    },
    post_email_error (val) {
      this.error_email = true
      if (val === '抱歉！您的邮件发送失败，请重试') {
        this.email_intro = val
        this.email_caveat = 'introTwo'
      } else if (val === '该邮箱已被注册！') {
        this.email_intro = val
        this.email_caveat = 'introTwo'
      } else if (val === '错误字段') {
        this.email_intro = val
        this.email_caveat = 'introTwo'
      } else if (val === '没有该验证类型') {
        this.email_intro = val
        this.email_caveat = 'introTwo'
      } else {
        this.email_intro = '服务器出错！'
        this.email_caveat = 'introTwo'
      }
      setTimeout(() => {
        this.error_email = false
        this.bus.$emit('post_email_error')
      }, 1000)
    },
    async post_success (val) {
      let email = {
        email: this.email,
        type: 'createUser'
      }
      try {
        let responsoe = await this.$http.postHttp('api/emailVerify', email)
        if (responsoe.data.message === '发送成功！') {
          this.post_email_success(val)
        } else {
          this.post_email_error(responsoe.data.message)
        }
      } catch (error) {
        this.post_email_error(error)
      }
    },
    spider_before (el) {
      el.style.position = 'absolute'
      el.style.display = 'none'
    },
    spider_enter (el,done) {
      setTimeout(() => {
        done()
      }, 1000)
    },
    spider_after (el) {
      el.style.position = 'relative'
      el.style.display = 'block'
    }
  }
}
</script>

<style lang="stylus" scoped>
  widths(){
    margin: 0 auto
    width: 65%
  }
  input_style(){
    widths()
    position:relative
    border: 1px solid rgb(180,180,180)
    padding: .2rem
    display: flex
    justify-content: center
    .user{
      font-size: .43rem
      position: absolute
      z-index: 999
      left: .3rem
      letter-spacing: .7rem
    }
    .input{
      position: relative
      display: flex
      left: .65rem
      input{
        color: rgb(50,50,50)
        border: 0px solid red
        box-sizing: border-box
        padding: .1rem
        padding-top: .15rem
        flex: 1
        width: 230px
        font-size: .32rem
        outline: none
      }
      .iconfont{
        cursor: pointer
        position: absolute
        font-size: .35rem
        right: -.6rem
        top: .1rem
      }
      .iconfont:hover{
        color: red
      }
    }
  }
  .email_box{
    position:relative
    display: flex
    flex-direction: column
    .email{
      input_style()
    }
    .email:hover{
      border: 1px solid rgb(15,153,213)
    }
    .spider_box{
      position: relative
      width: 65%
      margin: 0 auto
      .mask{
        user-select: none
        position: absolute
        display: flex
        align-items: center
        justify-content: center
        color: rgb(15,153,213)
        font-size: .3rem
        letter-spacing: .1rem
        top: .2rem
        width: 390px
        height: 45px
        border-radius: .5rem
        background: rgb(226,245,242)
        box-shadow: 0 0 .25rem rgb(150,245,242) inset
        z-index: 1
      }
      .iconfont{
        position: absolute
        right: 2.9%
        top: .34rem
        font-size: .45rem
        color: green
        z-index: 1000
      }
    }
    .verify{
      input_style()
      margin-top: .18rem
      .user{
        letter-spacing: .15rem
      }
      .input{
        .iconfont{
          top: .17rem
          right: -.8rem
          font-size: .2rem
        }
        .iconfont:hover{
          color: rgb(15,153,213)
        }
      }
    }
    .verify:hover{
      border: 1px solid rgb(15,153,213)
    }
    .next_step{
      position: absolute
      top: 3.6rem
      left: 2.1rem
      user-select: none
      width: 65%
      border: 1px solid white
      text-align: center
      color: black
      font-size: .38rem
      padding: .25rem
      cursor: pointer
      background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                    )
    }
    .next_step:active{
      border: 1px solid rgb(15,200,213)
    }
    .intro{
      widths()
      margin-top: .1rem
    }
    .introOne{
      color: rgb(150,150,150)
    }
    .introTwo{
      color: red
    }
    .introThree{
      color: white
    }
    .introFour{
      color: rgb(15,153,213)
    }
  }
</style>
