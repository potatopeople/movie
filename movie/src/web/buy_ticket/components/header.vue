<template>
  <section class="header">
    <div class="seat">
      <span>可选座位</span>
    </div>
    <div class="seat_down">
      <span>已售座位</span>
    </div>
    <div class="seat_chose">
      <span>已选座位</span>
    </div>
  </section>
</template>

<script>
export default {
  name: 'BoxHeader'
}
</script>

<style lang="stylus" scoped>
  .header{
    display: flex
    justify-content: center
    margin-top: 30px
    margin-bottom: 30px
    color: #666
    font-size: 16px
    div{
      padding-left: 38px
      height: 26px
      margin-left: 50px
    }
    .seat{
      background: url('../../../../static/images/seat.png') no-repeat
    }
    .seat_down{
      background: url('../../../../static/images/seat_down.png') no-repeat
    }
    .seat_chose{
      background: url('../../../../static/images/seat_chose.png') no-repeat
    }
    span{
      line-height: 26px
    }
  }
</style>
