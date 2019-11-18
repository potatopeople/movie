<template>
  <section>
    <pay-header @exit_web="exit_web" :tf="tf" @error_ticps="error_ticps" :buy_date="buy_date" />
    <order-body @id_card_handel="id_card_handel" :order_data="order_data" />
    <pay-btn @exit_web="exit_web" @error_ticps="error_ticps" :batch="batch" :id_card="id_card" :total="total" />
    <screen-mask @error_ticps="error_ticps" :ticps="ticps" v-if="ticps_mask" /> 
    <data-mask v-if="tfs"/>
  </section>
</template>

<script>
import ScreenMask from '@/public/mask'
import PayHeader from './components/header'
import OrderBody from './components/intro'
import PayBtn from './components/pay'
export default {
  name: 'OrderPay',
  components: {
    ScreenMask,
    PayHeader,
    OrderBody,
    PayBtn
  },
  data () {
    return {
      ticps: '',
      ticps_mask: false,
      order_data: {},
      buy_date: '',
      tf: false,
      id_card: '',
      batch: '',
      tfs: true
    }
  },
  computed: {
    user_token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      return reg.exec(token.version)[1]
    },
    total () {
      return this.order_data.money
    },
    user_intro () {
      return this.$store.state.user.header_user_intro
    }
  },
  methods: {
    id_card_handel (value) {
      this.id_card = value
    },
    async get_user_intro () {
      try {
        let response = await this.$http.get_http_auth('api/user/verifyToken','',this.token)
        if (response.data.code === 200) {
          this.$store.dispatch('get_user_intro',response.data.data)
        } else {
          alert('请重新登录')
        }
      } catch (error) {
        console.log(error)
      }
    },
    error_ticps (type,ticps) { //异常提示
      if (type === 'close') {
        this.ticps = ''
        this.ticps_mask = false
      } else if (type === 'error') {
        this.ticps = ticps
        this.ticps_mask = true
      }
    },
    exit_web () {
      console.log('exit')
      setTimeout(() => {
        this.$router.go(-1)
      },2000)
    },
    over_tf () {
      setTimeout(() => {
        this.tfs = false
      }, 1000)
    },
    async get_order_intro () { //获取订单数据
      try {
        let data = {
          type: '0',
          date: '10:30'
        }
        let response = await this.$http.get_http_auth('api/movie/seat/order/get_order',data,this.user_token)
        if (response.data.code === 200) {
          this.order_data = response.data.data
          this.buy_date = response.data.data.buy_date
          this.batch = response.data.data.batch
          this.tf = true
        } else {
          this.error_ticps('error',response.data.message)
          this.exit_web()
        }
        this.over_tf()
      } catch (error) {
        this.error_ticps('error',error)
        this.exit_web()
        this.over_tf()
      }
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_order_intro()
      if (!this.user_intro) {
        this.get_user_intro()
      }
    })
  }
}
</script>