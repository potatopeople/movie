<template>
  <section class="cinemas_list">
    <ul class="cinemas">
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
  </section>
</template>

<script>
export default {
  name: 'CinemasList',
  computed: {
    cinemas_list () {
      return this.$store.state.cinemas.cinemas
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
    }
  }
}
</script>

<style lang="stylus" scoped>
  .cinemas_list{
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
