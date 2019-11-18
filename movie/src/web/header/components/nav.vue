<template>
    <nav>
      <router-link tag="div" class="logo" to="/home">
        <img src="../../../assets/images/logo.png">
      </router-link>
      <ul class="list">
        <router-link tag="li" to="/home">首页</router-link>
        <router-link tag="li" to="/movie_list">电影</router-link>
        <router-link tag="li" to="/movie_top">榜单</router-link>
        <router-link tag="li" to="/cinemas">影院</router-link>
      </ul>
      <div class="address">
        <span class="iconfont" @click="open_address">&#xe67f;</span>
        <span class="city">{{user_address.name}}</span>
      </div>
    </nav>
</template>

<script>
export default {
  name: 'HeaderNav',
  computed: {
    user_address () {
      return this.$store.state.userAddress.user_address || '地点'
    }
  },
  methods: {
    open_address () {
      this.$emit('open_address', true)
    }
  }
};
</script>

<style lang="stylus" scoped>
  center(){
    margin: auto 0
  }
  nav{
    margin: auto auto auto 0
    font-size: .45rem
    display: flex
    .logo{
      center()
      padding-top: .17rem
    }
    .address{
      color: black
      margin: auto .4rem
      .iconfont{
        display: inline-block
        color: rgb(15,153,213)
        user-select: none
        cursor: pointer
        font-size: .5rem
      }
      .city{
        cursor: default
      }
      @keyframes address{
        0%{
          transform: scale(1)
        }
        50%{
          transform: scale(1.2)
        }
        100%{
          transform: scale(1)
        }
      }
      .iconfont:hover{
        animation: 1s linear infinite address
      }
      .city{
        margin-left: .1rem
        font-size: .35rem
        color: rgb(100,100,100)
      }
    }
    .list {
      list-style: none
      display: flex
      li:first-child{
        margin-left: .5rem
      }
      li{
        color: black
        cursor: pointer
        font-size: .35rem
        padding: .4rem .3rem
      }
      li:hover{
        color: rgb(203,28,15)
      }
    }
  }
</style>
