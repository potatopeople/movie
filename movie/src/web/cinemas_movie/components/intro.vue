<template>
  <section class="intro_box">
    <div class="header">
      {{movie_intro.name}}
      <span class="score">
        {{movie_intro.score | score_filter}}
        <span>{{movie_intro.score | score_filter_word}}</span>
      </span>
    </div>
    <p class="mation">
      <span class="time" v-if="movie_intro.play_time">时长：<span style="color:#151515">{{movie_intro.play_time}}</span> </span>
      <span class="cat" v-if="movie_intro.catgory">类型：<span style="color:#151515">{{movie_intro.catgory}}</span></span>
      <span class="star" v-if="movie_intro.star">主演：<span style="color:#151515">{{movie_intro.star}}</span></span>
    </p>
    <table>
      <thead>
        <tr>
          <th>放映时间</th>
          <th>语言版本</th>
          <th>放映厅</th>
          <th>售价（元）</th>
          <th>选座购票</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td class="time">
            <p>{{movie_intro.movie_time}}</p>
            <p>{{movie_intro.movie_leave}}散场</p>
          </td>
          <td>{{movie_intro.lang}}</td>
          <td>{{movie_intro.movie_room}}</td>
          <td class="money">￥{{movie_intro.movie_money}}</td>
          <td><div class="buy_btn" @click="buy_ticket">选座购票</div></td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script>
export default {
  name: 'MovieIntro',
  props: {
    movie_intro: {
      type: Object,
      default: {
        name: '',
        score: '',
        play_time: '',
        catgory: '',
        star: '',
        movie_time: '',
        movie_leave: ''
      }
    }
  },
  computed: {
    cinemas () {
      return JSON.parse(this.$route.query.cinemas)
    }
  },
  filters: {
    score_filter (value) {
      var patter = /\./
      if (patter.test(value)) {
          return value
      }
      return '暂无'
    },
    score_filter_word (value) {
      var patter = /\./
      if (patter.test(value)) {
          return '分'
      }
      return ''
    }
  },
  methods: {
    buy_ticket () {
      var cinemas = {
        name: this.cinemas.name
      }
      this.$router.push({
        path:'/movie/buy_ticket',
        query: {
          movie: JSON.stringify(this.movie_intro),
          cinemas: JSON.stringify(cinemas)
        }
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
  .intro_box{
    background: white
    padding: .4rem .25rem
    .header{
      color: #333
      font-size: .55rem
      margin-bottom: 20px
      .score{
        color: rgb(15,153,213)
        font-size: .55rem
        margin-left: .5rem
        span{
          font-size: .3rem
        }
      }
    }
    .mation{
      margin-bottom: 20px
      font-size: .3rem
      span{
        margin-right: 40px
        color: #999
      }
      .time{}
    }
    table{
      width: 100%
      font-size: .32rem
      border-spacing: 0
      border: none
      thead{
        background: #f7f7f7
        border-color:inherit
        color: #333
        tr{
          height: 53px
          th{
            vertical-align: middle
          }
        }
      }
      tbody{
        tr{
          height: 80px
          td{
            text-align: center
            vertical-align: middle
          }
          .money{
            color: #f03d37
            font-weight: 600
            font-size: .36rem
          }
          .time{
            font-weight: 600
            color: black
            font-size: .36rem
            p:last-child{
              font-weight: 100
              color: #999
              font-size: .26rem
            }
          }
          .buy_btn{
            background-color: rgb(15,153,213)
            margin: 0 auto
            height: 30px
            color: #fff
            width: 80px
            text-align: center
            line-height: 30px
            font-size: .29rem
            box-shadow: 0 2px 10px -2px rgb(15,153,213)
            border-radius: 100px
          }
          .buy_btn:hover{
            background-color: rgb(15,173,213)
            cursor: pointer
          }
        }
        tr:nth-child(even){
          background: #f7f7f7
        }
      } 
    }
  }
</style>
