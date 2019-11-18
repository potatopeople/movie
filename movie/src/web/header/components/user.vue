<template>
  <section @mouseleave="none_box" class="user_box" @mouseenter="show_box">
    <img :src="user_intro.avatar || default_img" @click="toLogin">
    <!-- <span class="iconfont" v-if="user_intro">&#xe64a;</span> -->
    <div @mouseover="show_box" ref="box" class="box" v-show="tf">
      <ul>
        <li @click="to_link(item.ticps,item.path)" v-for="item of text" :key="item.id">
          {{item.text}}
        </li>
      </ul>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeaderUser',
  computed: {
    user_intro () {
      return this.$store.state.user.header_user_intro
    }
  },
  data () {
    return {
      default_img: require('@/assets/images/user.png'),
      tf: false,
      text: [
        {id:1,text:'个人信息',ticps:'intro',path:'/center/intro'},
        {id:2,text:'订单信息',ticps:'order',path:'/center/order'},
        {id:3,text:'退出登陆',ticps:'exit',path:'/'}
      ]
    }
  },
  methods: {
    to_link (value, path) {
      this.tf = false
      if (value === 'exit') {
        this.$store.dispatch('get_user_intro',{})
        window.localStorage.removeItem('_AMap_vectoruser')
        this.$router.push(path)
      } else {
        this.$router.push({
          path,
          query: {
            cat:value
          }
        })
      }
    },
    toLogin () {
      if (window.localStorage.getItem('_AMap_vectoruser')) {
        return 0
      } else {
        this.$router.push('/login')
      }
    },
    none_box () {
      this.tf = false
    },
    show_box () {
      if (window.localStorage.getItem('_AMap_vectoruser')) {
        this.tf = true
      } else {
        this.tf = false
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  .user_box{
    cursor: pointer
    padding: .1rem .3rem 0 .3rem
    margin: auto 0 auto auto
    height: auto
    position: relative
    img{
      width: 1rem
      height: 1rem
      border-radius: 50%
      overflow: hidden
    }
    .iconfont{
      position: absolute
      bottom: -10px
      left: calc(40px - 8px)
      color: rgb(200,200,200)
      transform: rotate(180deg)
    }
    .box{
      background: white
      border-radius: 4px
      padding: .2rem
      position: absolute
      font-size: 16px
      top: 55px
      left: calc(-50px + 40px)
      width: 100px
      ul{
        padding: 0
        cursor: default
        margin: 0
        list-style: none
        li{
          text-align: center
          padding: .1rem 0
        }
        li:hover{
          color: rgb(15,153,213)
          text-decoration: underline
          cursor: pointer
        }
      }
    }
  }
  .user_box:hover{
    // .iconfont{
    //   transform: rotate(360deg)
    // }
  }
</style>
