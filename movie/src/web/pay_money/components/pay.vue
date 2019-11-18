<template>
  <section class="pay_box">
    <p>
      <span>实际支付：</span>
      <span class="money">{{total}}</span>
    </p>
    <div class="sure">
      <div @click="sure_pay" class="sure_pay">确认支付</div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'PayBtn',
  props: {
    total: {
      type: Number,
      default: 0
    },
    batch:{
      type: String,
      default: ''
    },
    id_card: {
      type: String,
      default: ''
    }
  },
  computed: {
    id_card_verify () {
      let reg = /^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$/
      return reg.test(this.id_card)
    }
  },
  methods: {
    date_verify () { 
      if (this.id_card && this.id_card_verify) {
        return true
      } else {
        return false
      }
    },
    async sure_pay () {
      if (this.date_verify()) {
        try {
          let data = {
            money: this.total,
            batch: this.batch,
            id_card: this.id_card
          }
          let response = await this.$http.putHttp('api/movie/pay',data)
          if (response.data.code === 200) {
            window.location.href = response.data.data; 
          } else {
            this.$emit('error_ticps','error',response.data.data)
            this.$emit('exit_web')
          }
        } catch (error) {
          console.log(error)
          this.$emit('error_ticps','error',error)
        }
      } else {
        this.$emit('error_ticps','error','请填写正确的身份证！')
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .pay_box{
    margin-top: 60px
    p{
      text-align: right
      span{
        display: inline-block
        font-size: 14px
        color: #333
      }
      .money{
        color:#f03d37
        font-size: 36px
      }
      .money:before{
        content: "\FFE5"
        font-size: 24px
      }
      margin-bottom: 20px
    }
    .sure{
      text-align: right
      .sure_pay{
        cursor: pointer
        display: inline-block
        width: 190px
        height: 42px
        line-height: 42px
        font-size: 16px
        text-align: center
        color: #fff
        background-color: #f03d37
        border-radius: 100px
        box-shadow: 0 2px 10px -2px #f03d37
      }
    }
  }
</style>
