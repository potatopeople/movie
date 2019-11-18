<template>
  <section class="order_box">
    <ul>
      <li
        class="option"
        v-if="order_data"
      >
        <p class="title">
          <span class="date">{{order_data.buy_date}}</span>
          <span class="batch">土豆订单号：{{order_data.batch}}</span>
          <span @click="drop_order" title="删除订单" class="iconfont">&#xe665;</span>
        </p>
        <div class="main">
          <div>
            <img :src="order_data.img">
          </div>
          <div class="intro">
            <p class="movie_title">《{{order_data.movie_name}}》</p>
            <p class="c_name">{{order_data.cinemas_name}}</p>
            <p class="seat">
              <span>{{order_data.room}}</span>
              <span v-for="item of order_data.seat" :key="item.id">
                {{item.row}}排{{item.clumn}}座
              </span>
            </p>
            <p class="play_time">今日 {{date_time}} {{order_data.movie_date}}</p>
          </div>
          <div class="money">￥{{order_data.money}}</div>
          <div class="tf">{{order_data.tf | tf_filter}}</div>
          <div class="buy" @click="pay_order">付款</div>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'OrderBox',
  data () {
    return {
      order_data: ''
    }
  },
  filters: {
    tf_filter (value) {
      if (value === '0') {
        return '待支付'
      } else if (value === '2') {
        return '已支付'
      }
    }
  },
  computed: {
    token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      return reg.exec(token.version)[1]
    },
    date_time () {
      return this.order_data.buy_date.substr(5,5)
    }
  },
  methods: {
    pay_order () {
      this.$router.push('/movie/pay')
    },
    async get_order_data () {
      try {
        let data = {
          type: '0',
          date: '10:30'
        }
        let response = await this.$http.get_http_auth('api/movie/seat/order/get_order',data,this.token)
        if (response.data.code === 200) {
          this.order_data = response.data.data
        }
      } catch (error) {
        this.$emit('error_ticps','error',error)
      }
    },
    async drop_order () {
      try {
        let data = {
          type: '1',
          date: ''
        }
        let response = await this.$http.get_http_auth('api/movie/seat/order/get_order',data,this.token)
        if (response.data.code === 200) {
          this.order_data = ''
          this.$emit('error_ticps','error','订单删除完成！')
        }
      } catch (error) {
        this.$emit('error_ticps','error',error)
      }
    },
  },
  created () {
    this.$nextTick(this.get_order_data)
  }
}
</script>

<style lang="stylus" scoped>
  .order_box{
    margin-left: 40px
    ul{
      list-style: none
      padding: 0
      margin: 0
      .option{
        margin: 15px 60px 15px 0
        border: 1px solid #e5e5e5
        .title{
          padding: 16px 20px
          background: #f7f7f7
          font-size: 15px
          position: relative
          span{
            display: inline-block
            color: #333
          }
          .date{
            margin-right: 30px
          }
          .batch{
            color:#999
          }
          .iconfont{
            position: absolute
            right: 20px
            cursor: pointer
          }
        }
        .main{
          padding: 20px
          img{
            width: 66px
            height: 91px
            border: 2px solid #fff
            margin-right: 11px
            box-shadow: 0 1px 4px 0 hsla(0,0%,53%,.5)
          }
          display: flex
          .intro{
            margin-left: 10px
            width: 49%
            .movie_title{
              font-size: 17px
              font-weight: 700
              color: #333
              margin: 4px 0 7px -6px
            }
            .c_name{
              color: #999
              font-size: 13px
              margin-bottom: 4px
            }
            .seat{
              color: #999
              font-size: 13px
              margin-bottom: 4px
              span +span{
                margin-left: 5px 
              }
            }
            .play_time{
              color:#f03d37
              font-size: 12px
            }
          }
          .money{
            display: flex
            align-items: center
            width: 12%
            font-size: 15px
            color: #333
          }
          .tf{
            display: flex
            align-items: center
            color: #333
            width: 15%
            font-size: 15px
          }
          .buy{
            display: flex
            align-items: center
            justify-content: center
            font-size: 15px
            width: 80px
            height: 30px
            margin-top: 32px
            cursor: pointer
            text-align: center
            background-color: #f03d37
            color: #fff
            box-shadow: 0 2px 10px -2px #f03d37
            border-radius: 15px
          }
        }
      }
    }
  }
</style>
