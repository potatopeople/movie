<template>
  <transition
    enter-active-class="animated fadeInDown"
  >
  <section class="box" ref="log_box"
    @mouseup="putdown_log_box"
    @mousedown="drap_log_box"
    @mouseout="putdown_log_box"
  >
    <p
      class="system"
      @mousedown="drap_log_box"
      @mouseup="putdown_log_box"
      @mousemove="start_drap_log_box"
      title="可拖动"
    >
      系统登录
    </p>
    <input placeholder="账号" v-model.trim="username" type="text" class="user_name">
    <input placeholder="密码" v-model.trim="password" type="password" class="user_password">
    <p class="remenber">
      <span @click.stop="remenber_password" :class="[active_point,'point','iconfont']"></span>
      <span @click.stop="remenber_password" class="password">记住账号</span>
    </p>
    <p @click.stop="text_verify" class="login_btn">登录</p>
    <div class="login_mask iconfont" v-if="login_mask">
      <span :class="['text',login_mask]">&#xe625;</span>
    </div>
    <verify-silde
      @close_verify="close_verify"
      :silde_option="silde_option"
      :user_login="user_login"
    />
    <message-box
      :option="option"
    />
  </section>
  </transition>
</template>

<script>
import MessageBox from '@/public/message'
import VerifySilde from './solide'
export default {
  name: 'LoginBox',
  components: {
    MessageBox,
    VerifySilde
  },
  data () {
    return {
      option: {
        show: false,
        position: 'absolute',
        tiSize: '.35rem',
        messSize: '.3rem',
        message: '请输入账号！',
        catgory: 'tips',
        animatedIn: 'animated fadeInUp',
        animatedOut: 'animated fadeOut',
        top: '63%',
        enterTime: 600, // 进入动画时间
        leaveTime: 600 // 离开动画时间
      },
      silde_option: {
        show: false
      },
      active_point: '',
      username: '',
      password: '',
      timer: '',
      login_mask: '',
      drap: false,
      disX: '',
      disY: ''
    }
  },
  computed: {
    user_login () {
      return {
        username: this.username,
        password: this.password
      }
    }
  },
  methods: {
    // 拖动登录框
    drap_log_box (e) {
      this.drap = true
      let left = this.$refs.log_box.offsetLeft,
          top = this.$refs.log_box.offsetTop
      this.disX = e.clientX - left
      this.disY = e.clientY - top
      this.$refs.log_box.style.position = 'absolute'
    },
    // 开始拖动
    start_drap_log_box (e) {
      if (this.drap) {
        let l = e.clientX - this.disX,
            t = e.clientY - this.disY,
            winW = document.documentElement.clientWidth, // 页面宽
            winH = document.documentElement.clientHeight, // 页面高
            maxMoveW = winW - this.$refs.log_box.offsetWidth, // 可移动X
            maxMoveH = winH - this.$refs.log_box.offsetHeight // 可移动Y
        if (l < 0) {
          l = 0
        } else if ( l > maxMoveW) {
          l = maxMoveW
        }
        if (t < 0){
          t = 0
        } else if ( t > maxMoveH) {
          t = maxMoveH
        }
        this.$refs.log_box.style.left = l + 'px'
        this.$refs.log_box.style.top = t + 'px'
      }
    },
    // 释放登录框
    putdown_log_box (e) {
      this.drap = false
    },
    // 验证输入文本
    close_verify (show) {
      this.silde_option.show = show
    },
    async send_login () {
      let data = {
        username: this.username,
        password: this.password
      }
      try {
        let response = await this.$http.postHttp('api/admin/login', data)
        if (response.data.code === 200) {
          this.login_success()
          this.handel_storage()
          this.$store.dispatch('get_admin_user_intro', response.data.data)
          window.sessionStorage.setItem('admin_name',response.data.data.name)
          window.sessionStorage.setItem('admin_token',response.data.data.token)
        } else {
          this.login_error('warning', '账号错误!')
        }
      } catch (error) {
        this.login_error('error', '服务器错误!')
        console.log('登录失败：',error)
      }
    },
    login_error (cat, intro) { //登录失败
      setTimeout(() => {
        this.login_mask = ''
        this.option.message = intro
        this.option.catgory = cat
        this.option.show = true
      }, 1000)
      this.tips()
    },
    login_success () { // 登录成功
      setTimeout(() => {
        this.login_mask = ''
        this.silde_option.show = true
      }, 1000)
    },
    text_verify () { // 验证文本
      if (this.username === '') {
        this.option.message = '请输入账号！'
        this.option.catgory = 'tips'
        this.option.show = true
      } else if (this.password === '') {
        this.option.message = '请输入密码！'
        this.option.catgory = 'tips'
        this.option.show = true
      } else {
        this.login_mask = 'stop'
        this.send_login()
      }
        this.tips()
    },
    tips () { // 输入异常提示
      this.timer = setTimeout(() => {
        this.option.show = false
      }, 2500)
    },
    // 给localStorage赋值
    handel_storage () {
      if (this.active_point && this.username) {
        localStorage.setItem('username', this.username)
      } else {
        localStorage.setItem('username', '')
      }
    },
    // 网页刷新判断是否记住账号
    handel_username () {
      let username = localStorage.getItem('username')
      if (username) {
        this.username = username
        this.remenber_password(0)
      }
    },
    // 记住账号
    remenber_password (state=1) {
      if (state) {
        this.active_point = this.active_point == 'point_active' ? '' : 'point_active'
      } else {
        this.active_point = 'point_active'
      }
    }
  },
  created () {
    this.$nextTick(this.handel_username)
  }
}
</script>

<style lang="stylus" scoped>
  .box{
    position: relative
    box-shadow: 0 0 .3rem rgb(210,210,210)
    width: 370px
    font-size: .4rem
    display: flex
    border-radius: 10px
    flex-direction: column
    z-index: 1
    justify-content: center
    padding: .3rem .8rem
    box-sizing: content-box
    .system{
      cursor: move
      text-align: center
      font-weight: 600
      color: rgb(80,80,80)
      margin: 0
      padding: 20px 0
    }
    .user_name{
      margin: .4rem 0rem
      padding: .2rem .2rem
      border: 1px solid rgb(190,190,190)
      border-radius: 5px
    }
    .user_password{
      margin: .4rem 0rem
      padding: .2rem .2rem
      border: 1px solid rgb(190,190,190)
      border-radius: 5px
    }
    .remenber{
      user-select: none
      margin: .2rem 0
      display: flex
      justify-content: flex-end
      cursor: default
      .point{
        display: inline-block
        height: 17px
        width: 15px
        color: white
        border: 1px solid rgb(15,153,213)
        border-radius: 3px
        overflow: hidden
      }
      .point_active{
        background: url('../../../../static/images/rember.png')
        background-repeat: no-repeat
        background-size: 100% 100%
        background-position: center
      }
      .password{
        margin-left: .2rem
        color: rgb(15,153,213)
        font-size: .32rem
      }
    }
    .login_mask{
      user-select: none
      position: absolute
      width: 100%
      height: 100%
      left: 0
      top: 0
      display: flex
      align-items: center
      justify-content: center
      font-size: .5rem
      color: rgb(15,153,213)
      background: rgba(220,220,220,.5)
      .text{
        animation: 2s linear infinite loginWait
        animation-play-state: paused
      }
      .stop{  
        animation-play-state: running
      }
      @keyframes loginWait{
        to {
          transform: rotate(360deg)
        }
      }
    }
    .login_btn{
      margin: .3rem 0
      display: flex
      justify-content: center
      align-items: center
      padding: .25rem 0
      border-radius: 5px
      cursor: pointer
      font-size: .33rem
      color: white
      user-select: none
      border: 1px solid transparent
      background: rgb(64,159,255) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                      )
      background-clip: padding-box
    }
    .login_btn:active{
      border: 1px solid rgb(15,153,213)
    }
  }
</style>
