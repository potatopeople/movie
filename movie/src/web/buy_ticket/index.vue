<template>
  <section class="box">
    <div class="main">
      <box-header />
      <movie-screen />
      <movie-seat :movie_seat="movie_seat" @error_ticps="error_ticps" :seat="seat" @drop_seat="drop_seat" @chose_seat="chose_seat"/>
    </div>
    <movie-intro @error_ticps="error_ticps" :seat="seat" />
    <screen-mask @error_ticps="error_ticps" :ticps="ticps" v-if="ticps_mask" />
  </section>
</template>

<script>
import ScreenMask from '@/public/mask'
import MovieSeat from './components/seat'
import MovieScreen from './components/screen'
import BoxHeader from './components/header'
import MovieIntro from './components/intro'
export default {
  name: 'BuyTicket',
  components: {
    BoxHeader,
    MovieScreen,
    MovieSeat,
    MovieIntro,
    ScreenMask
  },
  data () {
    return {
      seat: [], // 选中座位信息
      ticps: '',
      ticps_mask: false,
      movie_seat: {}
    }
  },
  computed: {
    intro () {
      return JSON.parse(this.$route.query.movie)
    }
  },
  methods: {
    error_ticps (value,ticps='') { // 錯誤提示
      if (value === 'close') {
        this.ticps = ''
        this.ticps_mask = false
      } else if (value === 'error') {
        this.ticps = ticps
        this.ticps_mask = true
      }
    },
    chose_seat (id,seat_intro) { // 添加座位
      this.seat.push({
        id,
        text: seat_intro
      })
    },
    drop_seat (intro) { // 删除座位
      this.seat.forEach((item,index) => {
        if (item.text === intro) {
          this.seat.splice(index, 1)
        }
      })
    },
    async get_movie_seat (cid,nid,mid) {
      var data = {
        city_id: cid,
        cinemas_id: nid,
        movie_id: mid
      }
      try {
        let response = await this.$http.postHttp('api/movie/seat', data)
        if (response.data.code === 200) {
          this.movie_seat = response.data.data
        }
      } catch (error) {
        console.log(error,'获取seat数据失败')
      }
    }
  },
  created () {
    this.$nextTick(() => {
      var intro = this.intro
      this.get_movie_seat(intro.city_id,intro.cinemas_id,intro.movie_id)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .box{
    border: 1px solid #e5e5e5
    width: 100%
    padding: .3rem .2rem
    background: white
    margin-top: .5rem
    display: flex
    justify-content: space-between
    .main{
      flex: 1
    }
  }
</style>
