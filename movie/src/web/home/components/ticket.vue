<template>
  <section class="movie_ticket">
    <p class="prompt">
      <span>上映票房</span>
      <span class="iconfont" @click="ticket_introduction">详情&#xe6ec;</span>
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
          <p>{{item.ticketRank}}</p>
        </div>
      </li>
      <li
        class="movie_list"
        v-for="(item, index) of movie_list"
        :key="item.id"
      >
        <span  >{{(index + 2)}}</span>
        <span :title="item.name">{{item.name}}</span>
        <span>{{item.ticketRank}}</span>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieTicket',
  data () {
    return {
      first_movie: [], // 第一名
      movie_list: [] // 2-10名
    }
  },
  methods: {
    ticket_introduction () { // 票房详情
      console.log('详情')
    },
    async get_movie_ticket_rank (type, page=1, size=10) { // 发起请求
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
        if (response.data.code == 200) {
          this.handle_movie_list(response.data)
        }
      } catch (error) {
        console.log('电影票房数据请求失败：', error)
      }
    },
    handle_movie_list (data) { // 数据赋值
      let arr = data.data.data
      this.movie_list = arr.slice(1, arr.length)
      this.first_movie = arr.slice(0, 1)
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_movie_ticket_rank('release', 1, 10)
    })
  }
}
</script>

<style lang="stylus" scoped>
  @import '~style/fontFamily.styl'
  .movie_ticket{
    fontFamily()
    flex: .5
    margin-left: 1rem
    .prompt{
      font-size: .45rem
      display: flex
      justify-content: space-between
      color: #ef4238
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
          background: url('../../../../static/images/release_rank.png')
        }
        .intro{
          flex: 1
          display: flex
          flex-direction: column
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
            line-height: 90px
            color: #ef4238
          }
        }
      }
      .movie_list{
        color: rgb(50,50,50)
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
          color: #ef4238
        }
      }
      li:nth-child(2),li:nth-child(3){
        span:first-child{
          color: #ef4238
        }
      }
      li:hover{
        background: rgb(240,240,240)
      }
    }
  }
</style>
