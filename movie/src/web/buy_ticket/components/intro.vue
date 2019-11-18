<template>
  <section class="movie">
    <div class="header">
      <div class="img">
        <img :src="movie_intro.movie_img">
      </div>
      <div class="box">
        <p class="name">{{movie_intro.name}}</p>
        <p class="cat"><span style="color:#999;margin-left:2px">类型：</span>{{movie_intro.catgory}}</p>
        <p class="time"><span style="color:#999;margin-left:2px">时长：</span>{{movie_intro.play_time}}</p>
      </div>
    </div>
    <div class="information">
      <p><span>影院：</span>{{cinemas.name}}</p>
      <p><span>影厅：</span>{{movie_intro.movie_room}}</p>
      <p><span>版本：</span>{{movie_intro.lang}}</p>
      <p class="date"><span>场次：</span>{{movie_intro.movie_time | date_filter}}</p>
      <p><span>票价：</span>￥{{movie_intro.movie_money}} / 张</p>
    </div>
    <div class="seat_intro">
      <div class="prompts">座位：<span v-show="!seat_intro.length">一次最多选5个座位</span></div>
      <div class="seat">
        <div
          class="ticket"
          v-for="(item,index) of seat_intro"
          :key="index"
        >{{item.text}}</div>
      </div>
    </div>
    <div class="prompt" v-show="!seat_intro.length">请<span>点击左侧</span>座位图选择座位</div>
    <div class="total_price">
     <span>总价：</span>￥{{movie_intro.movie_money * seat_intro.length}}
    </div>
    <input v-if="!username" v-model.trim="identity" type="text" placeholder="输入手机号" class="identity">
    <div class="code" v-if="!username">
      <input maxlength="5" v-model.trim="code" type="text" class="verify" placeholder="填写验证码">
      <span :class="code_active" @click="send_code">{{code_ticps}}</span>
    </div>
    <div class="username" v-if="username">{{username | username_filter}}</div>
    <div class="sure_seat">
      <span :class="sure_style" @click="sure_seat">
        确认选座
      </span>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MovieIntro',
  props: {
    seat: { // 选中的座位信息
      type: Array
    }
  },
  data () {
    return {
      identity: '', //手机号码
      code: '',//验证码
      code_ticps: '获取验证码',
      tf: false,
      code_message: '', //验证消息
      token: '' //用户标识
    }
  },
  filters: {
    date_filter (time) {
      var date = new Date()
      return '今日  ' + (date.getMonth() + 1) + '月' + date.getDate() +'  ' +time
    },
    username_filter (value) {
      return '手机号码为：' + value.substr(0,3) + '****' + value.substr(8,3)
    }
  },
  computed: {
    code_active () { // codeddom样式
      if (this.tf) {
        return ''
      } else if (/^1(3|4|5|7|8)\d{9}$/.test(this.identity)) {
        return 'active'
      } else {
        return ''
      }
    },
    phone_verify () { // 验证电话号
      return /^1(3|4|5|7|8)\d{9}$/.test(this.identity)
    },
    sure_style () {
      if (this.seat.length) {
        return 'active'
      } else {
        return ''
      }
    },
    movie_intro () {
      return JSON.parse(this.$route.query.movie)
    },
    cinemas () {
      return JSON.parse(this.$route.query.cinemas)
    },
    seat_intro () {
      if (this.seat) {
        return this.seat
      } else {
        return []
      }
    },
    seat_id () { // 座位id
      let anchor = []
      for (let i = 0; i < this.seat.length; i++) {
        anchor.push(
          {sid:this.seat[i].id}
        )
      }
      return anchor
    },
    username () {
      if (this.$store.state.user.header_user_intro) {
        return this.$store.state.user.header_user_intro['username']
      } else {
        return ''
      }
    },
    win_token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      if (token) {
        return reg.exec(token.version)[1]
      } else {
        return ''
      }
    }
  },
  methods: {
    send_code_after () { // 发送后的样式
      this.tf = true
      this.code = ''
      this.code_ticps = 60 + 's'
      var num = 60,
          time = setInterval(() => {
            console.log(this.tf)
            if (num === 1) {
              this.code_ticps = '获取验证码'
              this.tf = false
              clearInterval(time)
            } else {
              num -= 1
              this.code_ticps = num + 's'
            }
          },1000);
    },
    sure_seat () {
      if (!this.win_token) {
        if (this.identity === '') {
          this.$emit('error_ticps', 'error','请输入11位正确的手机号码！')
        } else if (!this.phone_verify) {
          this.$emit('error_ticps', 'error','请输入11位正确的手机号码！')
        } else if (this.code === '' || this.code.length !== 5) {
          this.$emit('error_ticps', 'error','请输入5位正确的验证码！')
        } else {
          this.code_verify()
        }
      } else {
        this.movie_order(this.win_token)
      }
    },
    verify_token () { //检查token是否有值
      if (this.token) {
        return true
      } else {
        if (this.win_token) {
          return true
        } else {
          return false
        }
      }
    },
    seat_after_buy (data) {
      let message = ''
      for (let i = 0; i < data.length; i++) {
        message += `您的：${data[i].row}行${data[i].clumn}列，`
      }
      message += '已经被抢座'
      this.$emit('error_ticps', 'error',`${message}!`)
    },
    async movie_order (token='') { // 发送订单
      if (this.verify_token()) {
        try{
          let data = {
            token: token || String(this.token),
            data: this.seat_id
          }
          let response = await this.$http.putHttp('api/movie/seat/order',data)
          if (response.data.code === 200) {
            data = {version:`#@SED2341%RTYG32135IUH1324IJ$${data.token}$#@SE12341D%R413TYGIUHIJ`}
            window.localStorage.setItem('_AMap_vectoruser',JSON.stringify(data))
            this.$router.push('/movie/pay')
          } else if (response.data.message === '有座位已被购买') {
            this.seat_after_buy(response.data.data)
          } else {
            this.$emit('error_ticps', 'error',`${response.data.message}!`,)
          }
        } catch (error) {
          console.log('订单发送失败:',error)
          this.$emit('error_ticps', 'error',`${error}!`,)
        }
      } else {
        this.$emit('error_ticps', 'error',`验证码已失效,请重新发送!`,)
      }  
    },
    async code_verify () { // 验证短信
      try {
        let data = {
          type: 'verify',
          code: this.code
        }
        let response = await this.$http.getHttp('api/send_code/' + this.identity,data)
        if (response.data.code === 200) {
          this.movie_order()
        } else {
          this.$emit('error_ticps', 'error',`${response.data.message}!`,)
        }
      } catch (error) {
        console.log('验证失败：',error)
        this.$emit('error_ticps', 'error',`短信发送失败,${response.data.message}!`,)
      }
    },
    async send_code (phone) { // 发送短信
      try {
        let data = {
          type: 'send',
          code: ''
        }
        let response = await this.$http.getHttp('api/send_code/' + this.identity,data)
        if (response.data.code === 200) {
          this.token = response.data.data.token
          this.send_code_after()
        } else {
          this.$emit('error_ticps', 'error',`短信发送失败,${response.data.message}!`,)
        }
      } catch (error) {
        console.log('身份验证失败！', error)
        this.$emit('error_ticps', 'error', '短信发送失败！')
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
 .movie{
    width: 340px
    padding: 20px
    background: #f9f9f9
    display: flex
    flex-direction: column
    p{
      margin: 0
    }
    .header{
      display: flex
      .img{
        width: 115px
        height: 158px
        border: 3px solid #fff
        box-shadow: 0 2px 7px 0 hsla(0,0%,53%,.5)
        img{
          width: 100%
          height: 100%
        }
      }
      .box{
        margin-left: .4rem
        color: #333
        .name{
          font-weight: 700
          font-size: 20px
          margin-bottom: 14px
        }
        .cat{

        }
      }
    }
    .information{
      position: relative
      margin-top: 20px
      font-size: 16px
      p{
        margin-bottom: 9px
        color: #151515
      }
      .date{
        color: #f03d37
      }
      span{
        color: #999
      }
    }
    .information:after{
      content: ''
      position: absolute
      width: 100%
      border-bottom: 1px dashed #999
    }
    .seat_intro{
      font-size: 16px
      color: #999
      display: flex
      .prompts{
        margin: 30px 0 0 0
      }
      .seat{
        display: flex
        flex: 1
        margin-top: .5rem
        flex-wrap: wrap
        .ticket{
          min-width: 60px
          color: #f03d37
          font-size: 12px
          text-align: center
          margin: 0 12px 10px 0
          line-height: 30px
          height: 30px
          background-image: url('../../../../static/images/ticket.png') 
        }
      }
    }
    .prompt{
        position: relative
        color: #333
        font-size: 14px
        width: 100%
        text-align: center
        margin: 28px 0 39px
        span{
          color: #f03d37
        }
    }
    .total_price{
      position: relative
      margin-top: 20px
      font-size: 25px
      color: #f03d37
      span{
        color:#151515
        font-size: 16px
      }
    }
    .total_price:after{
      content: ''
      left: 0
      bottom: -.2rem
      position: absolute
      width: 100%
      border-bottom: 1px dashed #999
    }
    input_style(){
      width: 218px
      height: 40px
      border: 1px solid #e5e5e5
      padding: 0 20px
      color: #333
      box-sizing: content-box
      outline: none
      font-size: 14px
      border-radius: 50px
      margin: auto
      margin-top: 1rem
    }
    .identity{
      input_style()
    }
    .code{
      margin: auto
      position: relative
      .verify{
        input_style()
        margin-top: .3rem
      }
      span{
        display: inline-block
        position: absolute
        top: 26px
        right: 15px
        color: #ccc
        font-size: 14px
        pointer-events: none
        cursor: default
        z-index: 2
      }
      .active{
        color: #f03d37
        pointer-events: auto
      }
    }
    .username{
      margin: .7rem 0 .1rem 0
      text-align: center
      font-size: .35rem
    }
    .identity:focus{
      border: 1px solid rgb(240,26,18)
    }
    .sure_seat{
      margin-top: 30px
      width: 100%
      cursor: default
      display: flex
      span{
        background: #dedede
        margin: auto
        text-align: center
        line-height: 42px
        width: 260px
        display: inline-block
        border-radius: 21px
        font-size: 16px
        color: #fff
        pointer-events: none
      }
      .active{
        background: #f03d37
        box-shadow: 0 2px 10px -2px #f03d37
        cursor: pointer
        user-select: none
        pointer-events: auto
      }
      .active:active{
        background: rgb(240,26,18)
      }
    }
  }
</style>
