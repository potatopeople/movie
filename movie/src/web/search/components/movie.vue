<template>
  <section class="movie_list_box">
    <div class="null_movie" v-if="!tf">
      <p class="title">很抱歉，没找到相关的影视剧</p>
      <p class="promt">
        <span class="one">土豆建议您：</span>
        <span class="two">1. 请检查输入的关键词是否有误</span>
        <span class="three">2. 请缩短关键词</span>
      </p>
    </div>
    <ul class="movie_list">
      <li
        v-for="item of movie_list.data"
        :key="item.id"
        class="movie"
      >
        <img :src="item.img" @click="to_intro(item)">
        <div class="intro">
          <p class="name" :title="item.name">{{item.name}}</p>
          <p class="elname" :title="item.elname">{{item.elname}}</p>
          <p class="score">{{item.score | filter_score}}</p>
          <p class="catgory" :title="item.catgory">
            {{item.catgory}}
          </p>
          <p class="time" :title="item.catgory + item.address">
            {{item.releaseTime + item.address}}
          </p>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieList',
  computed: {
    movie_list () {
      return this.$store.state.movieSearch.movie_search_list
    },
    tf () {
      return this.$store.state.movieSearch.movie_search_list.hasOwnProperty('data')
    },
    kw () {
      return this.$route.query.kw
    }
  },
  watch: {
    kw () {
      this.http(this.kw,1)
    }
  },
  filters: {
    filter_score (score) {
      if (score){
        return score
      } else{
        return '暂无评分'
      }
    }
  },
  methods: {
    to_intro (item) {
      this.$router.push({
        path: '/releasemovie',
        query: {
          item: JSON.stringify(item)
        }
      })
    },
    async http (keywords='',page='1',pageSize='20') {
      let data = {
        keywords,
        page,
        pageSize
      }
      try {
        let response = await this.$http.postHttp('api/movie/search', data)
        if (response.data.code === 200) {
          this.$store.dispatch('get_movie_search_list',response.data.data)
        } else {
          this.$store.dispatch('get_movie_search_list',[])
        }
        this.$emit('success_data')
      } catch (error) {
        this.$emit('success_data')
        console.log('搜索失败',error)
      }
    }
  },
  mounted () {
    this.http(this.$route.query.kw,1)
    this.bus.$on('http_movie_search',(kw,page) => {
      this.http(kw,page)
    })
  }
}
</script>

<style lang="stylus" scoped>
  introStyle(col=rgb(80,80,80),size=.35rem){
    color: col
    font-size: size
  }
  .movie_list_box{
    .null_movie{
      margin-left: 5%
      margin-top: 6%
      .title{
        introStyle(rgb(153,153,153),.5rem)
      }
      .promt{
        display: flex
        flex-direction: column
        margin-top: .4rem
        span{
          margin-bottom: .2rem
        }
        .one{
          introStyle(rgb(242,66,56),.33rem)
        }
        .two{
          introStyle(rgb(60,60,60),.33rem)
        }
        .three{
          introStyle(rgb(60,60,60),.33rem)
        }
      }
    }
    .movie_list{
      padding: 0
      margin: 0
      list-style: none
      display: flex
      flex-wrap: wrap
      justify-content: space-between
      .movie:nth-child(odd){
        margin-left: 5%
      }
      .movie:nth-child(even){
        margin-right: 5%
      }
      .movie{
        display: flex
        width: 40%
        margin-top: .8rem
        p{
          margin: 0
          font-size: .35rem
        }
        .intro{
          margin-left: .6rem
          display: flex
          width: 100%
          flex-direction: column
          justify-content:center
          border-bottom: 1px solid rgb(200,200,200)
          .name{
            max-width: 245px
            text-overflow: ellipsis
            overflow: hidden
            white-space: nowrap
            introStyle(rgb(10,10,10),.5rem)
          }
          .elname{
            max-width: 245px
            text-overflow: ellipsis
            overflow: hidden
            white-space: nowrap
            introStyle()
          }
          .score{
            introStyle(rgb(242,185,3),.4rem)
            margin-top: .3rem
            margin-bottom: .25rem
          }
          .catgory{
            introStyle(rgb(50,50,50),.38rem)
          }
          .time{
            max-width: 227px
            text-overflow: ellipsis
            overflow: hidden
            white-space: nowrap
            introStyle(rgb(140,140,140),size=.34rem)
          }
        }
      }
    }
  }
</style>
