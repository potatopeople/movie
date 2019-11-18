<template>
  <section class="seat">
    <div class="mask" v-show="loading"></div>
    <div class="seat_num">
      <span v-for="(item,index) of seat_nums" :key="index">
        {{item}}
      </span>
    </div>
    <div class="seat_box">
      <div class="row_front" v-for="(b_item,index) of row_fronts" :key="index">
        <span 
          v-for="item of b_item"
          :key="item.id"
          @click="chose_seat(item.id,item.clumn,index+1)"
          :chose="item.chose"
          :class="'chose' + item.chose"
        >
        </span>
      </div>
      <div class="xian"></div>
      <div ref="seat_row" class="row_after" v-for="(b_item,index) of row_afters" :key="index">
        <span 
          v-for="item of b_item"
          ref="seat_after"
          :key="item.id"
          :chose="item.chose"
          :class="'chose' + item.chose"
          @click="chose_seat(item.id,item.clumn,index+6)"
        >
        </span>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MovieSeat',
  data () {
    return {
    }
  },
  props: {
    seat: {
      type: Array
    },
    movie_seat: {
      type: Object
    }
  },
  computed: {
    loading () {
      if (this.row_fronts.length) {
        return false
      } else {
        return true
      }
    },
    row_fronts () { // 前排
      var data = []
      for (let i in this.movie_seat) {
        if (parseInt(i) <= 5) {
          data.push(
            this.movie_seat[i]
          )
        }
      }
      return data
    },
    row_afters () { // 后排
      var data = []
      for (let i in this.movie_seat) {
        if (parseInt(i) >= 6) {
          data.push(
            this.movie_seat[i]
          )
        }
      }
      return data
    },
    seat_nums () { // 行
      var seat_num = []
      for (let i in this.movie_seat) {
        seat_num.push(i)
      }
      return seat_num
    }
  },
  methods: {
    chose_seat (id,clumn, row) {
      var seat_dom = event.target
      switch (seat_dom.getAttribute('chose')) {
        case '0': if (this.seat.length < 5) {
                    seat_dom.style.backgroundImage = "url('../../../../static/images/seat_chose.png')"
                    seat_dom.setAttribute('chose','1')
                    this.$emit('chose_seat', id,`${row}排${clumn}座`)
                  } else {
                    this.$emit('error_ticps', 'error','一次最多购买5张票')
                  }
                  break
        case '1': seat_dom.style.backgroundImage = "url('../../../../static/images/seat.png')"
                  seat_dom.setAttribute('chose','0')
                  this.$emit('drop_seat', `${row}排${clumn}座`)
                  break
        case '2': break
        default : break
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  seat(){
    width: 30px
    height: 26px
    margin: 0 5px
    display: inline-block
    background: url('../../../../static/images/seat.png') no-repeat
    background-position: 0 1px
  }
  .seat{
    margin-top: 30px
    position: relative
    min-height: 455px
    .mask{
      position: absolute
      width: 100%
      height: 100%
      background: url('../../../../static/images/loading2.png') no-repeat center
      animation: 2s linear infinite loading
      z-index: 100
    }
    @keyframes loading {
      to {
        transform: rotate(360deg)
      }
    }
    .seat_num{
      font-size: 16px
      color: #999
      width: 20px
      white-space: normal
      margin-left: 80px
      span{
        display: inline-block
        height 26px
        width: 20px
        line-height: 29px
        margin-right: 40px
        margin-bottom: 10px
        text-align: center
      }
      span:nth-child(5){
        margin-bottom: 33px
      }
    }
    display: flex
    @media only screen and (max-width:1900px){
      .seat_num{
        font-size: 16px
        color: #999
        width: 20px
        white-space: normal
        margin-left: 15px
        span{
          display: inline-block
          height 26px
          width: 20px
          line-height: 29px
          margin-right: 40px
          margin-bottom: 10px
          text-align: center
        }
        span:nth-child(5){
          margin-bottom: 33px
        }
      }
    }
    .xian{
      margin-top: 30px
    }
    .seat_box{
      margin-left: 50px
      .row_front{
        margin-bottom: 10px
        white-space: nowrap
        height: 26px
        span{
          seat()
        }
      }
      .row_after{
        white-space: nowrap
        height: 26px
        margin-bottom: 10px
        span{
          seat()
        }
        span:first-child{
          margin-left: 45px
        }
        span:nth-child(6){
          margin-right: 85px
        }
      }
      .chose2{
        background: url('../../../../static/images/seat_down.png')!important
      }
    }
     @media only screen and (max-width:1900px) {
      .seat_box{
        margin-left: 15px
        .row_front{
          margin-bottom: 10px
          white-space: nowrap
          height: 26px
          span{
            seat()
          }
        }
        .row_after{
          white-space: nowrap
          height: 26px
          margin-bottom: 10px
          span{
            seat()
          }
          span:first-child{
            margin-left: 45px
          }
          span:nth-child(6){
            margin-right: 85px
          }
        }
      }
    }
  }
</style>
