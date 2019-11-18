<template>
  <section class="people_rank">
    <p class="prompt">
      <span>最受期待</span>
      <span class="iconfont" @click="rank_introduction">
        详情&#xe6ec;
      </span>
    </p>
    <ul>
      <li
        v-for="item of first_movie"
        :key="item.id"
        class="first"
      >
        <div class="img">
          <img :src="item.img">
        </div>
        <div class="intro">
          <p class="name">{{item.name}}</p>
          <p class="time">上映时间：{{item.releaseTime}}</p>
          <p class="people">{{item.people}}人想看</p>
        </div>
      </li>
      <!-- <li class="third">
        <div
          v-for="item of sec_thir_movie"
          :key="item.id"
          class="box"
        >
          <div class="img">
            <img :src="item.img">
          </div>
          <p class="name">{{item.name}}</p>
          <p class="people">{{item.people}}人想看</p>
        </div>
      </li> -->
      <li
        v-for="(item, index) of movie_list"
        :key="item.id"
        class="movie_list"
      >
        <span>{{(index + 2)}}</span>
        <span :title="item.name">{{item.name}}</span>
        <span>{{item.people}}人想看</span>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'PeopleRank',
  data () {
    return {
      movie: []
    }
  },
  computed: {
    first_movie () { // 第一名
      return this.movie.slice(0, 1)
    },
    // sec_thir_movie () { // 2-3名
    //   return this.movie.slice(1, 3)
    // },
    movie_list () { // 3-10名
      return this.movie.slice(1, this.movie.length)
    }
  },
  methods: {
    rank_introduction () {
    },
    async get_soon_rank (type, page=1, size=10) {
      let data = {
        orderBy: '1', // 排序类型
        showType: type, // 电影数据类型
        page: page, // 页数
        pageSize: size, // 每页数据量
        catgory: 'all',
        years: 'all',
        region: 'all'
      }
      try {
        let response = await this.$http.postHttp('api/movie', data)
        this.movie = response.data.data.data
      } catch (error) {
        console.log('soon排行查询失败：', error)
      }
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_soon_rank('soon', 1, 10) 
    })
  }
}
</script>

<style lang="stylus" scoped>
  .people_rank{
    fontFamily()
    flex: .5
    margin-left: 1rem
    .prompt{
      font-size: .45rem
      display: flex
      justify-content: space-between
      color: rgb(15,153,213)
      span{
        cursor: pointer
      }
      span:nth-child(2){
        display: flex
        align-items: flex-end
      }
    }
    ul{
      list-style: none
      padding: 0
      margin: .3rem 0 0 0
      li + li{
        marging-top: .2rem
      }
      .first{
        border: 1px solid rgb(235,235,235)
        display: flex
        .img{
          height: 194px
          img{
            height: 100%
          }
        }
        .img::before{
          content: ''
          position: absolute
          width: 22px
          height: 25px
          background: url('../../../../static/images/soon_first.png')
        }
        .intro{
          padding-left: .25rem
          display: flex
          flex-direction: column
          justify-content: center
          .name{
            font-size: .35rem
            color: rgb(0,0,0)
          }
          .time{
            margin-top: .2rem
            font-size: .32rem
            color: rgb(150,150,150)
          }
          .people{
            margin-top: .1rem
            font-size: .3rem
            color: rgb(15,153,213)
          }
        }
      }
      .movie_list{
        color: rgb(30,30,30)
        cursor: pointer
        position: relative
        padding: .2rem 0
        display: flex
        span{
          margin: auto 0
        }
        span:nth-child(1){
          vertical-align: top
          font-size: .38rem
          color: #999
          font-style: oblique
        }
        span:nth-child(2){
          font-size: .3rem
          vertical-align: top
          display: inline-block
          width: 150px
          margin-left: .25rem
          text-overflow: ellipsis
          overflow: hidden
          white-space: nowrap
        }
        span:nth-child(3){
          display: inline-block
          position: absolute
          right: 0
          top: calc(50% - 11px)
          font-size: .3rem
          color: rgb(15,153,213)
        }
      }
      li:nth-child(2),li:nth-child(3){
        span:first-child{
          color: rgb(15,153,213)
        }
      }
      li:hover{
        cursor: pointer
        background: rgb(240,240,240)
      }
    }
  }
</style>
