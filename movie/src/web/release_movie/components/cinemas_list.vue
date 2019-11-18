<template>
  <section class="cinemas_list">
    <p class="title">影院列表</p>
    <ul class="cinemas" v-show="cinemas_list.length">
      <li
        class="list"
        v-for="item of cinemas_list"
        :key="item.id"
      >
        <div class="cinemas_intro_name">
          <div class="name" @click="cinemas_intro(item.city_id,item.cinemas_id,item.name,item.address,item.money)">{{item.name}}</div>
          <div class="address">{{item.address}}</div>
        </div>
        <div class="cinemas_intro_money">
          <div class="money">
            <span>￥</span>
            <span>{{item.money}}</span>
            <span>起</span>
          </div>
          <div class="buy_btn" @click="cinemas_intro(item.city_id,item.cinemas_id,item.name,item.address,item.money)">选座购票</div>
        </div>
      </li>
    </ul>
    <div class="prompt" v-show="tf">本地的此电影已下映</div>
  </section>
</template>

<script>
export default {
  name: 'CinemasList',
  data () {
    return {
      cinemas_list: [],
      tf: false
    }
  },
  computed: {
    city_id () {
      return this.$store.state.userAddress.user_address.id
    },
    movie_id () {
      return JSON.parse(this.$route.query.item)
    }
  },
  watch: {
    city_id () {
      this.get_movie_cinemas()
    },
    cinemas_list:{
      handler: function () {
        if (this.cinemas_list.length) {
          this.tf = false
        } else {
          this.tf = true
        }
      },
      immediate: true
    }
  },
  methods: {
    cinemas_intro (cid,nid,name,address,money) {
      var cinemas={
        cid,
        nid,
        name,
        address,
        money
      }
      this.$router.push({
        path: '/cinemas_movie',
        query: {
          cinemas: JSON.stringify(cinemas)
        }
      })
    },
    async get_movie_cinemas () {
      var data = {
        movie_id: this.movie_id.rid,
        city_id: this.city_id
      }
      try{
        var response = await this.$http.postHttp('api/movie/cinemas_list', data)
        if (response.data.code === 200) {
          this.cinemas_list = response.data.data
        }
        this.$emit('success_list')
      } catch (error) {
        this.$emit('success_list')
        console.log('get_movie_cinemas',error)
      }
    }
  },
  created () {
    this.$nextTick(this.get_movie_cinemas)
  },
  beforeUpdate () {
  }
}
</script>

<style lang="stylus" scoped>
  .cinemas_list{
    background: #fff
    margin-top: 50px
    min-height: 500px
    .title{
      position: relative
      color: rgb(50,50,50)
      font-size: .37rem
      font-weight: 600
      padding: .3rem .3rem
    }
    .title::after{
      position: absolute
      content: ''
      left: 0
      top: calc(50% - 13.5px)
      height: 27px
      width: 7px
      background: rgb(15,153,213)
    }
    .prompt{
      text-align: center
      font-size: .5rem
      padding-bottom: .5rem
      color: #333
    }
    .cinemas{
      list-style: none
      margin: 0
      padding: 0
      .list{
        display: flex
        justify-content: space-between
        padding: 20px .3rem
        border-bottom: 1px dashed #e5e5e5
        font-size: .31rem
        .cinemas_intro_name{
          .name{
            color: #333
            margin-bottom: 10px
          }
          .name:hover{
            color: rgb(15,153,213)
            cursor: pointer
          }
          .address{
            color: #999
            font-size: .3rem
          }
        }
        .cinemas_intro_money{
          display: flex
          align-items: center
          .money{
            color: rgb(15,153,213)
            margin-right: .7rem
            padding-top: .1rem
            display: flex
            font-size: .24rem
            line-height: 28px
            span:nth-child(2){
              font-size: .31rem
              font-weight: 700
            }
            span:nth-child(3){
              color: #999
            }
          }
          .buy_btn{
            background-color: rgb(15,153,213)
            height: 30px
            color: #fff
            width: 80px
            text-align: center
            line-height: 30px
            font-size: .29rem
            box-shadow: 0 2px 10px -2px rgb(15,153,213)
            border-radius: 100px
          }
          .buy_btn:hover{
            background-color: rgb(15,173,213)
            cursor: pointer
          }
        }
      }
    }
  }
</style>
