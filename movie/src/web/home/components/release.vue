<template>
  <section class="release_movie">
    <div class="movie_list">
      <div class="header">
        <div class="count">
          <span>{{'正在上映 ( ' + movie_count + '部 )'}}</span>
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
              <div class="img_box" @click="buy_ticket(item)">
                <i v-if="item.cat" class="cat">
                  {{item.cat | cat_text}}
                </i>
                <img :src="item.img">
                <span class="name" :title="item.name">
                  {{item.name}}
                </span>
                <span class="score" :title="'评分：' + item.score">
                  <span>{{item.score | score_one}}</span>
                  <span>{{item.score | score_two}}</span>
                </span>
              </div>
              <p @click="buy_ticket(item)" class="buy_ticket">购票</p>
            </div>
          </li>
        </ul>
      </div>
    </div>
    <movie-ticket />
  </section>
</template>

<script>
import MovieTicket from './ticket'
export default {
  name: 'ReleaseMovie',
  components: {
    MovieTicket
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
    },
    cat_text (text) {
      let type = ''
      if (text === 'imax3d') {
        type = '3DIMAX'
      } else if (text === 'm3d') {
        type = '3D'
      } else if (text === 'imax2d') {
        type = '2DIMAX'
      }
      return type
    }
  },
  methods: {
    to_movie_list () {
      this.$router.push('/movie_list')
    },
    buy_ticket (item) { // 买票
      this.$router.push({
        path: '/releasemovie',
        query: {
          item: JSON.stringify(item)
        }
      })
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
        this.$emit('success_movie')
      } catch (error) {
        this.$emit('success_movie')
        console.log('上映电影请求失败：', error)
      }
    },
    handle_movie_list (data) { // 电影列表赋值
      this.movie_count = data.data.total
      this.movie_list = data.data.data
    }
  },
  created () { // 运行请求方法
    this.get_movie_list('release', 1, 8)
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
  .release_movie{
    margin-top: .5rem
    max-height: 642px
    min-height: 642px
    overflow: hidden
    back()
    display: flex
    padding: .25rem
    .movie_list{
      flex: 1
      .header{
        display: flex
        justify-content: space-between
        color: #ef4238
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
              position: relative
              display: flex
              flex-direction: column
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
                  color: #ef4238
                  text-overflow: ellipsis
                  overflow: hidden
                  white-space: nowrap
                  span:last-child{
                    font-size: .3rem
                  }
                }
                img{
                  height: 220px
                  width: 160px
                  background: rgb(150,150,150)
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
              .buy_ticket{
                text-align: center
                font-size: .33rem
                padding: .15rem 0
                color: #ef4238
              }
              .buy_ticket:hover{
                background: #ef4238
                color: white
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

