<template>
  <section class="movie_ticket">
    <p class="prompt">
      <span>Top 100</span>
      <span class="iconfont" @click="top_introduction">完整榜单&#xe6ec;</span>
    </p>
    <ul class="rank">
      <li
        class="first_movie"
        v-for="item of first_movie"
        :key="item.id"
      >
        <div class="img">
          <img :src="item.img" :alt="item.name">
        </div>
        <div class="intro">
          <p :title="item.name">{{item.name}}</p>
          <p>{{item.score}}</p>
        </div>
      </li>
      <li
        class="movie_list"
        v-for="(item, index) of movie_list"
        :key="item.id"
      >
        <span  >{{(index + 2)}}</span>
        <span :title="item.name">{{item.name}}</span>
        <span>{{item.score}}</span>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieTop',
  data () {
    return {
      first_movie: [],
      movie_list: []
    }
  },
  methods: {
    top_introduction () {
      this.$router.push('/movie_top')
      // this.$router.push({
      //   path: '/movie_top',
      //   params: {
      //     type: 'classic'
      //   }
      // })
    },
    async get_movie_rank (page=1,pageSize=10) {
      let data = {
        page,
        pageSize,
        type: 'classic'
      }
      try {
        let response = await this.$http.postHttp('api/movieTop', data)
        if (response.data.code == 200) {
          this.handle_data(response.data)
        }
      } catch (error) {
        console.log('movieRank出错：', error)
      }
    },
    handle_data (data) {
      let movie = data.data.data
      this.first_movie = movie.slice(0,1)
      this.movie_list = movie.slice(1,data.data.length)
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_movie_rank(1,10)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .movie_ticket{
    fontFamily()
    flex: .5
    margin-left: 1rem
    .prompt{
      font-size: .45rem
      display: flex
      justify-content: space-between
      color: rgb(250,156,6)
      span{
        cursor: pointer
      }
      span:nth-child(2){
        display: flex
        align-items: flex-end
      }
    }
    .rank{
      font-size: .33rem
      padding: 0
      margin: 0
      list-style: none
      .first_movie{
        cursor: pointer
        display: flex
        margin: .3rem 0
        border: 1px solid rgb(220,220,220)
        .img{
          position: relative
          height: 120px
          img{
            height: 100%
            width: 120px
          }
        }
        .img::before{
          content: ''
          position: absolute
          width: 22px
          height: 25px
          background: url('../../../../static/images/classic_top.png')
        }
        .intro{
          flex: 1
          display: flex
          flex-direction: column
          justify-content: space-around
          p{
            color: black
            width: 180px
            margin-left: calc(50% - 90px) 
            font-size: .4rem
            text-align: center
            text-overflow: ellipsis
            overflow: hidden
            white-space: nowrap
          }
          p:nth-child(2){
            color: rgb(250,156,6)
          }
        }
      }
      .movie_list{
        color: rgb(50,50,50)
        cursor: pointer
        position: relative
        padding: .1rem 0
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
          color: rgb(250,156,6)
        }
      }
      li:nth-child(2),li:nth-child(3){
        span:first-child{
          color: rgb(250,156,6)
        }
      }
      li:hover{
        background: rgb(240,240,240)
      }
    }
  }
</style>

