<template>
  <section class="top_movie_box">
    <p class="text">{{currenDate}}<span>已更新</span></p>
    <p class="text">榜单规则：{{text}}</p>
    <ul class="top_movie">
      <li
        class="movie"
        v-for="item of movie_list.data"
        :key="item.id"
      >
        <p :class="['rank',item.style]"><i>{{item.rank | filter_rank}}</i></p>
        <div class="img_box">
          <img :src="item.img">
        </div>
        <div class="movie_intro">
          <div class="intro">
            <p class="name">{{item.name}}</p>
            <p class="star">主演 &nbsp;: &nbsp;{{item.star}}</p>
            <p class="time">上映时间 &nbsp;: &nbsp;{{item.releaseTime}}</p>
          </div>
          <div class="score" v-if="item.score">
            <span class="one">
              <i>{{item.score | filter_score_one}}</i>
            </span>
            <span class="two">
              <i>{{item.score | filter_score_two}}</i>
            </span>
          </div>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieList',
  data () {
    return {
      text: '将国内热映的影片，按照评分从高到低排列取前10名，每天上午10点更新。相关数据来源于“土豆专业版”及“土豆电影库”。'
    }
  },
  filters: {
    filter_rank (rank) {
      if (rank === 1) {
        return ''
      } else {
        return rank
      }
    },
    filter_score_one (score) {
      return score.substring(0,2)
    },
    filter_score_two (score) {
      return score.substring(2,3)
    }
  },
  computed: {
    movie_list () { // 电影数据
      return this.$store.state.movieTop.movie_rank_list
    },
    currenDate () { // 当前时间
      let date = new Date(),
          year = date.getFullYear(),
          month = date.getMonth() + 1,
          day = date.getDate()
      return year + ' -' + month + ' -' + day
    }
  },
  methods: {
    async getData (type='release',page=1,pageSize=10) { // 发起数据请求
      let data = {
        type,
        page,
        pageSize,
      }
      try {
        let response = await this.$http.postHttp('api/movieTop', data)
        if (response.data.code == 200) {
          this.$store.dispatch('get_movie_rank_list', [response.data.data,type])
        }
        this.$emit('success_data')
      } catch (error) {
        this.$emit('success_data')
        console.log('movieTop',error)
      }
    },
    movie_catgory_verify (catgory,page) {
      if (catgory === 'release') {
        this.text = '将国内热映的影片，按照评分从高到低排列取前10名，每天上午10点更新。相关数据来源于“土豆专业版”及“土豆电影库”。'
      } else if (catgory === 'soon') {
        this.text = '将昨日国内待映影片，按照之前30天的想看数总量从高到低排列取前50名，每天上午10点更新。相关数据来源于“猫眼电影库”。'
      } else if (catgory === 'classic') {
        this.text = '将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库“。'
      }
      this.getData(catgory,page)
    }
  },
  created () {
    this.$nextTick(this.getData)
    this.bus.$on('http_movie_top',(val,val2) => {
      this.movie_catgory_verify(val,val2)
    })
    this.bus.$on('https_movie_top',(val,val2) => {
      this.movie_catgory_verify(val,val2)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .top_movie_box{
    .text{
      text-align: center
      margin-top: .7rem
      color: rgb(160,160,160)
      font-size: .25rem
      span{
        color: #ffb400
        margin-left: .1rem
      }
    }
    .text:nth-child(2){
      margin-top: .1rem
      letter-spacing: 1px
    }
    .top_movie{
      list-style: none
      padding: 0
      margin: 0
      min-height: 2520px
      margin-top: 1rem
      .movie{
        margin-top: .6rem
        display: flex
        align-items: center
        .rank{
          margin: 0 0 0 40px
          width: 50px
          font-size: .5rem
          font-weight: 600
          justify-content: center
          display: flex
          align-items: center
          height: 50px
          color: rgb(160,160,160)
          background: rgb(230,230,230)
        }
        .first{
          background: url('../../../../static/images/movie_top_one.png')
        }
        .secend{
          background: #ffb400
          color: white
        }
        .img_box{
          margin-left: 40px
        }
        .movie_intro{
          border-bottom: 1px solid rgb(225,225,225)
          box-sizing: border-box
          padding-right: 2rem
          height: 220px
          flex: 1
          margin-left: 30px
          display: flex
          align-items:center
          justify-content: space-between
          .intro{
            .name{
              font-size: .5rem
              color: rgb(10,10,10)
            }
            .star{
              margin-top: .15rem
              font-size: .35rem
              color: rgb(60,60,60)
            }
            .time{
              font-size: .35rem
              color: rgb(150,150,150)
            }
          }
          .score{
            color: #ffb400
            font-weight: 600
            .one{
              font-size: 1.1rem
            }
            .two{
              font-size: .6rem
            }
          }
        }
      }
    }
  }
</style>
