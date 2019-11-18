<template>
  <section class="input_box">
    <div class="username">
      <div class="user">用户名</div>
      <div class="input">
        <input
          v-model="username"
          maxlength="10"
          placeholder="您的登录账号"
          type="text"
          @focus="input_focus('name')"
          @blur="input_blur('name')"
        />
        <div class="iconfont" @click="clear('name')" v-show="username">&#xe609;</div>
      </div>
    </div>
    <p :class="['intro',name_caveat]">
      <span class="iconfont">&#xe635;</span>
      {{name_intro}}
    </p>
    <div class="password">
      <div class="user">密码</div>
      <div class="input">
        <input
          v-model="password"
          maxlength="20"
          placeholder="10-20个字符"
          type="password"
          @focus="input_focus('password')"
          @blur="input_blur('password')"
        />
        <div class="iconfont" @click="clear('password')" v-show="password">&#xe609;</div>
      </div>
    </div>
    <p :class="['intro',pass_caveat]">
      <span class="iconfont">&#xe635;</span>
      {{pass_intro}}
    </p>
    <div class="password_s">
      <div class="user">确认密码</div>
      <div class="input">
        <input
          v-model="passwords"
          maxlength="20"
          placeholder="请再次输入密码"
          type="password"
          @focus="input_focus('passwords')"
          @blur="input_blur('passwords')"
        />
        <div class="iconfont" @click="clear('passwords')" v-show="passwords">&#xe609;</div>
      </div>
    </div>
    <p :class="['intro',passs_caveat]">
      <span class="iconfont">&#xe635;</span>
      {{passs_intro}}
    </p>
    <div class="verifytion">
      <div class="user">验证码</div>
      <div class="input">
        <input
          v-model="verifytion"
          maxlength="8"
          placeholder="请输入验证码"
          type="text"
          @focus="input_focus('verify')"
          @blur="input_blur('verify')"
        />
        <div class="verify_code" id="verification"></div>
      </div>
    </div>
    <p :class="['intro',verifytion_caveat]">
      <span class="iconfont">&#xe635;</span>
      {{verify_intro}}
    </p>
    <div class="next_Step" @click="confirm_handle">
      确认
    </div>
  </section>
</template>

<script>
import Verification from '@/public/verification'
export default {
  name: 'RegisterInput',
  data () {
    return {
      username: '',
      name_reg: /^[\w]{7,10}$/,
      password: '',
      password_reg: /^[^\s]{10,20}$/,
      passwords: '',
      verifytion: '',
      name_intro: '支持英文、数字组合,7-10个字符',
      pass_intro: '支持英文、数字、符号组合,10-20个字符',
      passs_intro: '请再次输入密码',
      verify_intro: '请输入验证码',
      name_caveat: 'introThree',
      pass_caveat: 'introThree',
      passs_caveat: 'introThree',
      verifytion_caveat: 'introThree',
      verifyCode: null,
    }
  },
  watch: {
    username () {
      this.name_prompt(this.username)
    },
    password () {
      this.password_prompt(this.password)
    },
    passwords () {
      this.passwords_prompt(this.passwords)
    },
    verifytion () {
      this.verifytion_prompt(this.verifytion)
    }
  },
  methods: {
    regexp_verify (data,reg) {
      if (reg.test(data)) {
        return true
      } else {
        return false
      }
    },
    name_prompt (val) {
      if (val === '') {
        this.name_intro = '用户名不能为空'
        this.name_caveat = 'introTwo'
        return false
      } else {
        if (this.regexp_verify(val, this.name_reg)) {
          this.name_intro = '正确'
          this.name_caveat = 'introFour'
          return true
        } else {
          this.name_intro = '用户名格式错误'
          this.name_caveat = 'introTwo'
          return false
        }
      }
    },
    password_prompt (val) {
      if (val === '') {
        this.pass_intro = '密码不能为空'
        this.pass_caveat = 'introTwo'
        return false
      } else {
        if (this.regexp_verify(val, this.password_reg)) {
          this.pass_intro = '正确'
          this.pass_caveat = 'introFour'
          return true
        } else {
          this.pass_intro = '密码格式错误'
          this.pass_caveat = 'introTwo'
          return false
        }
      }
    },
    passwords_prompt (val) {
      if (val === '') {
        this.passs_caveat = 'introTwo'
        this.passs_intro = '不能为空'
        return false
      } else {
        if (val === this.password) {
          this.passs_caveat = 'introFour'
          this.passs_intro = '正确'
          return true
        } else if (val !== this.password) {
          this.passs_caveat = 'introTwo'
          this.passs_intro = '错误'
          return false
        }
      }
    },
    verifytion_prompt (val) {
      if (val === '') {
        this.verify_intro = '不能为空'
        this.verifytion_caveat = 'introTwo'
        return false
      } else if (this.verifyCode.validate(val)) {
        this.verify_intro = '正确'
        this.verifytion_caveat = 'introFour'
        return true
      } else {
        this.verify_intro = '错误'
        this.verifytion_caveat = 'introTwo'
        return false
      }
      
    },
    input_focus (val) {
      if (val === 'name') {
        this.name_intro = '支持英文、数字组合,7-10个字符'
        this.name_caveat = 'introOne'
      } else if (val === 'password') {
        this.pass_intro = '支持英文、数字、符号组合,10-20个字符'
        this.pass_caveat = 'introOne'
      } else if (val === 'passwords') {
        this.passs_intro = '请再次输入密码'
        this.passs_caveat = 'introOne'
      } else if (val === 'verify') {
        this.verify_intro = '请输入验证码'
        this.verifytion_caveat = 'introOne'
      }
    },
    input_blur (val) {
      if (val === 'name') {
        this.name_caveat = 'introThree'
      } else if (val === 'password') {
        this.pass_caveat = 'introThree'
      } else if (val === 'passwords') {
        this.passs_caveat = 'introThree'
      } else if (val === 'verify') {
        this.verifytion_caveat = 'introThree'
      }
    },
    clear (text) {
      if (text === 'name') {
        this.username = ''
      } else if (text === 'password') {
        this.password = ''
      } else if (text === 'passwords') {
        this.passwords = ''
      }
    },
    confirm_handle () {
      if (this.name_prompt(this.username)) {
        if (this.password_prompt(this.password)) {
          if (this.passwords_prompt(this.passwords)) {
            if (this.verifytion_prompt(this.verifytion)) {
              this.create_user()
            }
          }
        }
      }
    },
    async create_user () {
      let user_infor = {
        email: this.$route.query.email,
        username: this.username,
        password: this.password
      }
      let response = await this.$http.postHttp('api/registerUser', user_infor)
      this.verify_create(response.data.message)
    },
    verify_create (val) {
      if (val === '注册成功！') {
        alert('success')
        this.$emit('steptwo','topLinet','stept')
        this.$router.replace({
          path: 'register/success',
          query:{
            step: 'success'
          }
        })
      } else if (val === '该用户名已存在') {
        this.name_intro = val
        this.name_caveat = 'introTwo'
      } else if (val === '抱歉！注册失败，请重新注册') {
        this.verify_intro = val
        this.verifytion_caveat = 'introTwo'
      } else if (val === '密码格式错误') {
        this.pass_intro = val
        this.pass_caveat = 'introTwo'
      } else if (val === '用户名格式错误') {
        this.name_intro = val
        this.name_caveat = 'introTwo'
      } else {
        this.verify_intro = '发生未知错误,请重新注册'
        this.verifytion_caveat = 'introTwo'
      }
    },
    step_two (val) {
      if (val === 'information') {
        this.$emit('step', 'topLine', 'step')
      }
    }
  },
  mounted () {
    this.step_two(this.$route.query.step)
    this.verifyCode = new Verification('verification')
  }
}
</script>

<style lang="stylus" scoped>
  hover(){
    border: 1px solid rgb(15,153,213)
  }
  widths() {
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
      letter-spacing: .2rem
    }
    .input{
      position: relative
      display: flex
      left: .8rem
      input{
        color: rgb(50,50,50)
        border: 0px solid red
        box-sizing: border-box
        padding: .1rem
        padding-top: .15rem
        padding-right: .7rem
        flex: 1
        font-size: .32rem
        outline: none
      }
      .iconfont{
        cursor: pointer
        position: absolute
        font-size: .35rem
        right: -.5rem
        top: .1rem
      }
      .iconfont:hover{
        color: red
      }
    }
  }
  .input_box{
    display: flex
    flex-direction: column
    .username{
      input_style()
    }
    .username:hover{
      hover()
    }
    .password{
      input_style()
      .user{
        letter-spacing: .84rem
      }
    }
    .password:hover{
      hover()
    }
    .password_s{
      input_style()
      .user{
        letter-spacing: .005rem
      }
    }
    .password_s:hover{
      hover()
    }
    .verifytion{
      input_style()
      overflow: hidden
      .verify_code{
        position: absolute
        width: 100px
        height: 50px
        background: red
        right: -.92rem
        top: -.2rem
      }
    }
    .verifytion:hover{
      hover()
    }
    .next_Step{
      widths()
      user-select: none
      border: 1px solid white
      color: black
      display: flex
      align-items: center
      justify-content: center
      letter-spacing: .4rem
      font-size: .38rem
      padding: .25rem
      cursor: pointer
      background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                  )
    }
    .next_Step:active{
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
