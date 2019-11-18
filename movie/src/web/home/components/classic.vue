<template>
  <section class="classic_movie">
    <div class="movie_list">
      <div class="header">
        <div class="count">
          <span>经典电影</span>
        </div>
        <div class="all iconfont" @click="to_movie_list">
          <span>全部&#xe6ec;</span>
        </div>
      </div>
      <div class="movie">
        <ul>
          <li
            v-for="item of movie_list"
            :key="item.id"
          >
            <div class="box">
              <div class="img_box" @click="watch_movie(item)">
                <img :src="item.img">
                <span class="name" :title="item.name">
                    {{item.name}}
                </span>
                <span class="score" :title="'评分：' + item.score">
                  <span>{{item.score | score_one}}</span>
                  <span>{{item.score | score_two}}</span>
                </span>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <movie-top />
  </section>
</template>

<script>
import MovieTop from './top'
export default {
  name: 'ClassicMovie',
  components: {
    MovieTop
  },
  data () {
    return {
      movie_count: 0, // 总数
      movie_list: [] // 列表
    }
  },
  filters: {
    score_one (text) {
      return text.substr(0,2)
    },
    score_two (text) {
      return text.substr(2,1)
    }
  },
  methods: {
    watch_movie (data) {
      this.$router.push({
        path: '/releasemovie',
        query: {
          item: JSON.stringify(data)
        }
      })
    },
    to_movie_list () {
      this.$router.push('/movie_list')
    },
    buy_ticket () { // 买票
      console.log('买票')
    },
    async get_movie_list (type, page=1, size=10) { // 发起请求
      let data = {
        orderBy: '0', // 排序类型
        showType: type, // 电影数据类型
        page: page, // 页数
        pageSize: size, // 每页数据量
        catgory: 'all',
        years: 'all',
        region: 'all'
      }
      try{
        let response = await this.$http.postHttp('api/movie', data)
        if (response.data.code === 200) {
          this.handle_movie_list(response.data)
        }
      } catch (error) {
        console.log('上映电影请求失败：', error)
      }
    },
    handle_movie_list (data) { // 电影列表赋值
      this.movie_count = data.data.total
      this.movie_list = data.data.data
    }
  },
  created () { // 运行请求方法
    this.get_movie_list('classic', 1, 8)
  }
}
</script>

<style lang="stylus" scoped>
  @import '~style/fontFamily.styl'
  fl(){
    cursor: pointer
    display: flex
    align-items: flex-end
  }
  .classic_movie{
    max-height: 562px
    overflow: hidden
    margin-top: .5rem
    back()
    display: flex
    padding: .25rem
    .movie_list{
      flex: 1
      .header{
        display: flex
        justify-content: space-between
        color: rgb(250,156,6)
        .count{
          font-size: .45rem
          fl()
          cursor: default
        }
        .all{
          fl()
        }
      }
      .movie{
        ul{
          padding: 0
          margin: 0
          list-style: none
          display: flex
          justify-content: space-between
          flex-wrap: wrap
          li{
            border: 1px solid rgb(230,230,230)
            cursor: pointer
            margin: .3rem .1rem
            .box{
              display: flex
              flex-direction: column
              .img_box{
                position: relative
                display: flex
                flex-direction: column
                .name{
                  display: inline-block
                  position: absolute
                  padding-left: .2rem
                  bottom: .1rem
                  width: 2.4rem
                  color: white
                  font-size: .32rem
                  text-overflow: ellipsis
                  overflow: hidden
                  white-space: nowrap
                  z-index: 1
                }
                .score{
                  display: inline-block
                  position: absolute
                  bottom: .06rem
                  right: .2rem
                  font-size: .35rem
                  color: rgb(250,156,6)
                  text-overflow: ellipsis
                  overflow: hidden
                  white-space: nowrap
                  span:last-child{
                    font-size: .3rem
                  }
                }
              }
              .img_box::before{
                content: ''
                position: absolute
                left: 0
                right: 0
                bottom: 0
                top: 50%
                background: linear-gradient(to top, rgb(10,10,10), transparent)
              }
            }
          }
        }
      }
    }
  }
  .release_movie::after{
    content: " "
    display: table
    clear: both
  }
</style>

