<template>
  <section class="movie_box">
    <p class="prompt" v-if="!movie_list.length">
      抱歉，没有找到相关结果，请尝试用其他条件筛选。
    </p>
    <ul class="movie_list">
      <li
        class="movie"
        v-for="item of movie_list"
        :key="item.id"
        @click="watch_movie_intro(item)"
      >
        <div class="movie_main">
          <i v-if="item.cat" class="cat">
            {{item.cat | cat_text}}
          </i>
          <img :src="item.img" class="movie_img">
          <p class="movie_name" :title="item.name">{{item.name}}</p>
          <p class="movie_score">
            <span>{{item.score | score_filter}}</span>
            <span>{{item.score | scored_filter}}</span>
            <span v-if="item.people">
              {{item.people + '人想看'}}
            </span>
          </p>
        </div>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieLists',
  data () {
    return {
      catgory: ''
    }
  },
  computed: {
    movie_list () {
      return this.$store.state.movieList.movie_list.data || []
    }
  },
  filters: {
    cat_text (cat) {
      let type = ''
      if (cat === 'imax3d') {
        type = '3DIMAX'
      } else if (cat === 'm3d') {
        type = '3D'
      } else if (cat === 'imax2d') {
        type = '2DIMAX'
      }
      return type
    },
    score_filter (score) {
      if (score) {
        return score.substring(0,2)
      } else if (score === '') {
        return '暂无评分'
      }
    },
    scored_filter (score) {
      if (score) {
        return score.substring(2,3)
      } else {
        return ''
      }
    }
  },
  methods: {
    watch_movie_intro (data) {
      this.$router.push({
        path: '/releasemovie',
        query: {
          item: JSON.stringify(data)
        }
      })
    },
    async get_movie_data (orderBy='0',type='release', page=1, size=30) {
      let data = {
        orderBy, // 排序类型
        showType: type, // 电影数据类型
        page, // 页数
        pageSize: size, // 每页数据量
        catgory: this.catgory.catgorys || 'all',
        years: this.catgory.years || 'all',
        region: this.catgory.region || 'all'
      }
      try {
        let response = await this.$http.postHttp('api/movie', data)
        if (response.data.code === 200) {
          this.$store.dispatch('get_movie_list', [response.data.data,type])
        }
      } catch (error) {
        console.log('电影数据请求出错：', error)
      }
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_movie_data('0','release',1,30)
    })
  },
  mounted () {
    this.bus.$on('movie_catgory', (value) => {
      this.catgory = value
      this.get_movie_data('0',this.$store.state.movieList.movie_list.catgory,1,30)
    })
    this.bus.$on('movie_orderby', (value) => {
      this.get_movie_data(value,this.$store.state.movieList.movie_list.catgory,1,30)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .movie_box{
    .prompt{
      font-size: .35rem
      color: rgb(50,50,50)
    }
    .movie_list{
      margin: 0 -25px 0 -25px
      color: black
      list-style: none
      padding: 0
      display: flex
      flex-wrap: wrap
      justify-content: flex-start
      .movie{
        margin: 25px -4px 0 30px
        .movie_main{
          position: relative
          .cat{
            padding: .05rem .05rem .05rem 0
            display: block
            width: 69px
            height: 25px
            position: absolute
            left: -.03rem
            top: .1rem
            font-size: .3rem
            font-weight: 600
            text-align: center
            color: rgb(255,255,255)
            background: rgb(15,153,213)
            box-shadow: 0 0 .04rem rgb(90,90,90)
          }
          .movie_img{
            width: 160px
            height: 220px
          }
          .movie_name{
            cursor: default
            width: 160px
            text-overflow: ellipsis
            overflow: hidden
            white-space: nowrap
            font-size: .35rem
            text-align: center
          }
          .movie_score{
            margin-top: .15rem
            font-size: .32rem
            text-align: center
            span:nth-child(1){
              font-size: .38rem
              color: rgb(15,153,213)
            }
            span:nth-child(2){
              color: rgb(15,153,213)
            }
            span:nth-child(3){
              color: red
            }
          }
        }
      }
      @media only screen and (min-width:1900px){
        .movie{
          margin: 25px 30px 0 35px
        }
      }
    }
  }
</style>
