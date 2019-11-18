<template>
  <section class="order_box">
    <p class="promt">请仔细核对场次信息，出票后将<span>无法退票和改签</span></p>
    <table class="order_table">
      <thead class="title">
        <tr>
          <th>影片</th>
          <th>时间</th>
          <th>影院</th>
          <th>座位</th>
        </tr>
      </thead>
      <tbody class="body">
        <tr>
          <td class="movie_name">{{order_data.movie_name}}</td>
          <td class="movie_date">{{order_data.movie_date | date_filter}}</td>
          <td class="cinemas_name">{{order_data.cinemas_name}}</td>
          <td class="seat_box">
            <span class="room">{{order_data.room}}</span>
            <div class="seat">
                <span :key="index" class="intro" v-for="(item,index) in order_data.seat">
                  <i>{{item.row}}</i>
                    排
                  <i>{{item.clumn}}</i>
                    座
                </span>
            </div>
          </td>
        </tr>
        <tr class="id_box">
          <td>身份证:</td>
          <td colspan="3">
            <input v-model="id_card" placeholder="该身份证用于验票" type="text" class="input">
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
export default {
  name: 'OrderBody',
  props: {
    order_data: {
      type: Object
    }
  },
  data () {
    return {
      id_card: ''
    }
  },
  watch: {
    id_card () {
      this.$emit('id_card_handel',this.id_card)
    }
  },
  computed : {
    null_date () {
      if (this.order_data) {
        return ''
      } else {
        return '.'
      }
    }
  },
  filters: {
    date_filter (time) {
      if (time) {
        var cur_date = new Date()
        return '今日 ' + (cur_date.getMonth() + 1) +'月'+cur_date.getDate() +'日 ' + time
      } else {
        return ''
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .order_box{
    .promt{
      margin: 5px 0
      padding-left: 18px
      background: url('../../../../static/images/error.png') no-repeat
      background-size: 12px
      background-position-y: 2px
      color:#666
      font-size: 12px
      span{
        color: #faaf00
      }
    }
    .order_table{
      width: 100%
      border: 1px solid rgb(200,200,200)
      border-spacing: 0
      .title{
        background: #f7f7f76
        font-size: 16px
        th{
          width: 25%
          font-weight: 400
          color: #333
          padding: 14px 0
        }
      }
      .body{
        background: white
        .movie_date{
          color: #f03d37
        }
        .id_box{
          td + td{
            text-align: left
          }
          .input{
            width: 200px
            display: inline-block
            height: 100%
            padding: .2rem .1rem
            outline: none
            border: 0px solid white
          }
        }
        td{
          text-align: center
          font-size: 16px
          color: #333
          padding: 20px 0
        }
        .seat_box{
          .room{
            display: inline-block
            font-weight: 700
            margin-right: 10px
          }
          .seat{
            text-align: left
            display: inline-block
            font-size: 12px
            i{
              font-weight: 600
              font-style: normal
              font-size: 16px
            }
            span{
              margin:5px 5px
              position: relative
            }
            span:after{
              content: ''
              position: absolute
              height: 100%
              top: 0
              right: -5px
              border-right: 1px solid #e5e5e5
              z-index: 5
            }
          }
        }
      }
    }
  }
</style>
