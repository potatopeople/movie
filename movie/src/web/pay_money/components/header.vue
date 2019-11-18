<template>
  <section class="header_box">
    <p class="time_box">
      <span>请在</span>
      <span class="time">{{minutes}}</span>
      <span>分钟</span>
      <span class="time">{{second}}</span>
      <span>秒内完成支付</span>
    </p>
    <p>超时订单会自动取消，如遇支付问题，请致电土豆客服：17381198366</p>
  </section>
</template>

<script>
export default {
  name: 'PayHeader',
  data () {
    return {
      minutes: 0,
      second: 0
    }
  },
  props: {
    buy_date: {
      type: String
    },
    tf:{
      type: Boolean,
      default: false
    }
  },
  watch:{
    tf () {
      if (this.tf) {
        this.computer_time()
      }
    }
  },
  computed: {
    buy_date_formats () { //this.buy_date
      let date = new Date(this.buy_date)
      return date
    }
  },
  methods: {
    computer_time () { //计算时间
      let cur_date = new Date(),
          interval = cur_date.getTime() - this.buy_date_formats.getTime(),
          minutes = 15 - parseInt(interval / 1000 / 60),
          second = 60 - (parseInt(parseFloat(interval / 1000) % 60));
      if (minutes >= 0 & second >= 0) {
        this.minutes = minutes // 秒
        this.second = second // 分钟
        this.time_runer()
      }
    },
    time_runer () { //时间运行
      var timer
      timer = setInterval(() => {  
        if (this.second <= 0) {
          this.minutes -= 1
          this.second = 60
        }
          this.second -= 1
        if (this.minutes <= 0 && this.second <= 0) {
          this.$emit('error_ticps','error','订单超时未支付，请重新选择！')
          this.$emit('exit_web')
          clearInterval(timer)
          return 0
        }   
      },1000)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .header_box{
    padding: 20px 0 25px 75px
    margin: 40px 0
    color: #f03d37
    font-size: 14px
    background: url('../../../../static/images/time.png') no-repeat
    background-color: #fff3f3
    background-position: left 25px top 40px
    .time_box{
      color: #666
      font-size: 16px
      margin-bottom: 4px
      .time{
        font-size: 32px
        color: #f03d37
        margin: 0 5px
      }
    }
  }
</style>
