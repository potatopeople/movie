<template>
  <section class="cinemas_box">
    <p class="title">影院列表</p>
    <cinemas-list />
  </section>
</template>

<script>
import CinemasList from './components/cinemasList'
export default {
  name: 'Cinemas',
  components: {
    CinemasList
  }
}
</script>

<style lang="stylus" scoped>
  .cinemas_box{
    margin-top: .3rem
    background: white
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
  }
</style>

