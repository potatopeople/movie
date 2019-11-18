<template>
  <section class="soon_movie">
    <div class="movie_list">
      <div class="header">
        <div class="count">
          <span>{{'即将上映 ( ' + movie_count + '部 )'}}</span>
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
              </div>
              <p>{{item.people + '人想看'}}</p>
            </div>
            <p>{{item.releaseTime | refine_date}}&nbsp;上映</p>
          </li>
        </ul>
      </div>
    </div>
    <people-rank/>
  </section>
</template>

<script>
import PeopleRank from './people'
export default {
  name: 'SoonMovie',
  components: {
    PeopleRank
  },
  data () {
    return {
      movie_count: 0, // 电影总数
      movie_list: [],  // 电影列表
      movie: []
    }
  },
  filters: {
    refine_date (data) {
      var year = data.substring(0,4)
      var mounth
      var day
      if (data.substring(5,6) === '0') {
        mounth = data.substring(6,7)
      } else{
        mounth = data.substring(5,7)
      }
      if (data.substring(8,9) === '0') {
        day = data.substring(9,10)
      } else {
        day = data.substring(8,10)
      }
      return year + '年 ' +mounth + '月 ' + day + '日 '
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
    async get_movie_data (type, page=1, size=10) {  // 请求数据
      let data = {
        orderBy: '1', // 排序类型
        showType: type, // 电影数据类型
        page: page, // 页数t
        pageSize: size, // 每页数据量
        catgory: 'all',
        years: 'all',
        region: 'all'
      }
      try {
        let response = await this.$http.postHttp('api/movie', data)
        if (response.data.code == 200) {
          this.handle_movie_data(response.data)
        }
      } catch (error) {
        console.log('soon电影数据请求失败：', error)
      }
    },
    handle_movie_data (data) {
      let arr = data.data
      this.movie_count = arr.total
      this.movie_list = arr.data.slice(0, 8)
      this.movie = arr.data
    }
  },
  created () {
    this.$nextTick(() => {
      this.get_movie_data('soon', 1, 10)
    })
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
  .soon_movie{
    margin-top: .5rem
    max-height: 706px
    overflow: hidden
    back()
    display: flex
    padding: .25rem
    .movie_list{
      flex: 1
      .header{
        display: flex
        justify-content: space-between
        color: rgb(15,153,213)
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
            cursor: pointer
            margin: .3rem .1rem
            .box{
              border: 1px solid rgb(230,230,230)
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
                  width: 2.5rem
                  color: white
                  font-size: .32rem
                  text-overflow: ellipsis
                  overflow: hidden
                  white-space: nowrap
                  z-index: 1
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
              p{
                color: rgb(15,153,213)
                padding: .2rem
                text-align: center
                font-size: .27rem
                background: rgb(250,250,250)
              }
            }
            p{
              text-align: center
              font-size: .3rem
              padding-top: .2rem
            }
          }
        }
      }
    }
  }
</style>

