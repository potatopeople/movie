<template>
  <section class="intro_box">
    <div class="change_img">
      <img :src="user_img">
      <div class="input">
        <label for="file">更换头像</label>
        <input
          id="file"
          type="file"
          @change="change_img"
          accept="image/png, image/jpg, image/jpeg"
        >
      </div>
      <p>支持JPG、PNG、JPEG格式</p>
    </div>
    <div class="intro">
      <p class="name">
        <span>昵称：</span>
        <input v-model="name" type="text">
      </p>
      <p class="sex">
        <span>性别：</span>
        <input v-model="sex" value="男" type="radio" id="men">
        <label for="men">男</label>
        <input v-model="sex" value="女" type="radio" id="women">
        <label for="women">女</label>
      </p>
      <p class="btn" @click="save_data">
        保存
      </p>
    </div>
  </section>
</template>

<script>
export default {
  name: 'IntroBox',
  data () {
    return {
      sex: '',
      name: ''
    }
  },
  watch: {
    user:{
      handler () {
        this.name = this.user.name
        this.sex = this.user.sex
      },
      immediate: true
    }
  },
  computed: {
    user_img () {
      return this.$store.state.user.header_user_intro.avatar
    },
    user () {
      return this.$store.state.user.header_user_intro
    },
    token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      return reg.exec(token.version)[1]
    }
  },
  methods: {
    async save_data () { // 保存数据
      if (this.verify_data()) {
        try {
          let data = {
            name: this.name,
            sex: this.sex
          }
          let response = await this.$http.post_http_auth('api/user/save',data,this.token)
          if (response.data.code === 200) {
            this.get_user_intro()
          }
        } catch (error) {
          this.$emit('error_ticps','error',error)
        }
      } else {
        this.$emit('error_ticps','error','不要填空数据')
      }
    },
    async get_user_intro () {
      try {
        let response = await this.$http.get_http_auth('api/user/verifyToken','',this.token)
        if (response.data.code === 200) {
          this.$store.dispatch('get_user_intro',response.data.data)
          this.$emit('error_ticps','error','保存成功！')
        } else {
          this.$emit('error_ticps','error','请重新登录！')
        }
      } catch (error) {
        this.$emit('error_ticps','error',error)
      }
    },
    change_img (e) {
       if (window.FileReader) {
        var reader = new FileReader()
        var f = event.target.files[0]
        if (f.size / (1024 * 1000) > 5) { // 限制文件大小和类型
          alert('文件过大')
          return 0
        } else if ((f.type === 'image/png' || f.type === 'image/jpg' ||
          f.type === 'image/jpeg') && f.size / (1024 * 1000) < 5) {
          reader.readAsDataURL(f)
          var _this = this
          reader.onload = function (evt) {
            console.log(evt.target.result)
          }
        } else if (!(f.type === 'image/png' || f.type === 'image/jpg' ||
          f.type === 'image/jpeg')) {
          alert('文件类型错误')
          return 0
        }
      } else {
        alert('您的浏览器不支持')
        return 0
      }
    },
    verify_data () { //
      if (this.name && this.sex) {
        return true
      } else {
        return false
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .intro_box{
    margin: 40px 0 0 40px
    display: flex
    .change_img{
      flex: 1
      text-align: center
      img{
        width: 258px
        height: 258px
        overflow: hidden
      }
      .input{
        position: relative
      }
      p{
        color: #999
        line-height: 30px
        font-size: 18px
        margin-top: 10px
      }
      label{
        width: 182px
        display: inline-block
        text-align: center
        line-height: 56px
        height: 56px
        color: #5b5b5b
        margin: 20px auto 0
        background: #e6e6e6
        border-radius: 10px
        border: 1px
        cursor: pointer
        font-size: 18px
        outline: none
      }
      input[type=file]{
        display: none
      }
    }
    .intro{
      flex: 1.7
      font-size: 14px
      span{
        font-size: 18px
      }
      .btn{
        width: 100px
        height: 40px
        font-size: 18px
        user-select: none
        text-align: center
        line-height: 40px
        margin-top: 60px!important
        margin-left: 60px
        color: #fff
        background: rgb(15,153,213) linear-gradient(
                        rgba(255,255,255,.4),
                        transparent
                      )
        border-radius: 5px
        cursor: pointer
      }
      .btn:active{
        background: rgb(15,153,213)
      }
      p{
        margin: 20px 0
      }
      input[type=text]{
        width: 240px
        line-height: 30px
        font-size: 12px
        padding-left: 12px
      }
      input[type=radio]{
        margin-left: 12px
      }
    }
  }
</style>

