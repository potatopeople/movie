<template>
  <section class="input_box">
    <p class="title">账号登录</p>
    <div class="box">
      <div class="user_name">
        <div :class="['img','iconfont',isChangeName]">&#xe611;</div>
        <div class="input">
          <input @focus="focus_name" @blur="blur_name" v-model="user_name" placeholder="手机号/账号" type="text" ref="user_name">
          <div @click="clear_username" class="iconfont" v-show="user_name">&#xe609;</div>
        </div>
      </div>
      <p class="intro">{{name_verify}}</p>
      <div class="user_password">
        <div @click="send_code" :class="['img','iconfont',isChangePassword]" ref="password">
          <div class="send" v-html="send_ico"></div>
        </div>
        <div class="input">
          <input @focus="focus_password" v-model="user_password" placeholder="验证码" type="password" ref="user_password">
          <div @click="clear_password" class="iconfont" v-show="user_password">&#xe609;</div>
        </div>
      </div>
      <p class="intro">{{password_verify}}</p>
      <div class="sure_login">
        <!-- <p>
          <router-link tag="span" to="/login">忘记密码</router-link> 
        </p> -->
        <div class="sure_login_btn" @click="login">登录</div>
      </div>
    </div>
  </section>
</template>

<script>
import Verification from '@/public/verification'
export default {
  name: 'LoginInput',
  data () {
    return {
      user_name: '',
      user_password: '',
      verification: '',
      name_verify: '',
      password_verify: '',
      isChangeName: 'change2',
      send_ico: '&#xe617;',
      tf: true,
      token: ''
    }
  },
  computed: {
    user_name_verify () { //账号验证
      return /^1(3|4|5|7|8)\d{9}$/.test(this.user_name)
    },
    isChangePassword () {
      if (this.user_name_verify && this.tf) {
        return 'change'
      } else {
        return 'change2'
      }
    }
  },
  methods: {
    login () {
      if (this.user_name && this.user_name_verify) {
        if (this.user_password) {
          this.loginPost()
        }
        else {
          this.password_verify = '密码不能为空'
        }
      } else {
        this.name_verify = '请输入正确的手机号'
      }
    },
    async send_code () {
      if (this.user_name) {
        try {
          let data = {
            type: 'send',
            code: ''
          }
          let response = await this.$http.getHttp('api/send_code/'+this.user_name,data)
          if (response.data.code === 200) {
            this.token = response.data.data.token
            this.send_code_style()
          } else {
            this.password_verify = response.data.message
          }
        } catch (error) {
          this.password_verify = error
        } 
      }
    },
    send_code_style () {
      this.send_ico = 60
      this.tf = false
      var timer = setInterval(() => {
        if (this.send_ico <= 0) {
          clearInterval(timer)
          this.send_ico = '&#xe617;'
          this.tf = true
          return 0
        }
        this.send_ico -= 1
      }, 1000)
    },
    async loginPost () {
      if (this.token) {
        let data = {
          type: 'verify',
          code: this.user_password
        }
        let response = await this.$http.getHttp('api/send_code/'+this.user_name,data)
        let code = response.data.code
        if (code === 200) {
          this.verification = ''
          data = {version:`#@SED2341%RTYG32135IUH1324IJ$${this.token}$#@SE12341D%R413TYGIUHIJ`}
          window.localStorage.setItem('_AMap_vectoruser',JSON.stringify(data))
          this.$store.dispatch('get_user_intro',response.data.data)
          this.$router.push('/home')
        } else if (code === 500) {
          this.password_verify = '系统发生错误'
        }
      } else {
        this.password_verify = '验证码失去效性，请重新发送！'
      }
    },
    focus_name () {
      this.name_verify = ''
      this.isChangeName = 'change'
    },
    blur_name () {
      this.isChangeName = 'change2'
    },
    focus_password () {
      this.password_verify = ''
      this.isChangePassword = 'change'
    },
    clear_username () { // 清空账户
      this.user_name = ''
    },
    clear_password () { // 清空密码
      this.user_password = ''
    }
  }
}
</script>

<style lang="stylus" scoped>
  borders(){
    border: 1px solid rgb(140,140,140)
  }
  inputs(){
    flex: 1
    display: flex
    justify-content: center
    margin-top: .1rem
    .img{
      font-size: .5rem
      padding: .1rem
      borders()
      padding-left: .2rem
      padding-right: .2rem
      border-right: 0
      margin: auto 0
      width: 37px
      box-sizing: content-box
      text-align: center
    }
    .input{
      position: relative
      display: flex
      margin: auto 0
      box-sizing: border-box
      borders()
      input{
        color: rgb(100,100,100)
        box-sizing: border-box
        border: 0px solid white
        padding: .24rem
        padding-right: .7rem
        flex: 1
        font-size: .4rem
        outline: none
      }
      .iconfont{
        cursor: pointer
        position: absolute
        font-size: .5rem
        right: 5px
        top: .12rem
      }
      .iconfont:hover{
        color: red
      }
    }
  }
  .change{
    color: rgb(15,153,213)
    cursor: pointer
    pointer-events: auto
    overflow: hidden
    .send{
      animation: 1s linear infinite address
    }
    .send:hover{
      animation-play-state: paused
    }
  }
  @keyframes address{
    0%{
      transform: scale(1)
    }
    50%{
      transform: scale(1.3)
    }
    100%{
      transform: scale(1)
    }
  }
  .change2{
    color: rgb(100,100,100)
    cursor: default
    pointer-events: none
  }
  .input_box{
    position: absolute
    right: 1rem
    bottom: .5rem
    padding: 0 1rem
    box-shadow: 0 0 .15rem rgb(200,200,200)
    background: white
    .title{
      font-size: .5rem
      text-align: center
      padding: .3rem
    }
    .box{
      padding-top: .6rem
      margin: auto
      display: flex
      flex-direction: column
      .intro{
        height: .35rem
        color: red
        font-size: .25rem
        margin-top: .13rem
      }
      .user_name{
        inputs()
      }
      .user_password{
        inputs()
      }
      .sure_login{
        flex: 1
        margin-bottom: 1rem
        .sure_login_btn{
          user-select: none
          cursor: pointer
          margin-top: .2rem
          box-sizing: border-box
          color: white
          border: 1px solid white
          padding: .1rem
          font-size: .4rem
          text-align: center
          background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                      )
        }
        .sure_login_btn:active{
          border: 1px solid rgb(15,153,213)
        }
        p{
          font-size: .3rem
          margin-top: .1rem
          text-align: right
          color: rgb(50,50,50)
          span:hover{
            cursor: pointer
            color: rgb(15,153,213)
            text-decoration: underline
          }
        }
      }
    }
  }
</style>
