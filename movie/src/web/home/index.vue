<template>
  <section class="main_box">
    <marquee
      behavior="scroll"
      direction="left"
      loop="infinite"
      scrollamount="3px"
      class="prompt"
      v-text="prompt"
      v-if="prompt"
    />
    <home-swiper />
    <release-movie @success_movie="success_movie" />
    <soon-movie />
    <classic-movie />
    <data-mask v-show="tf"></data-mask>
  </section>
</template>

<script>
import HomeSwiper from './components/swiper'
import ReleaseMovie from './components/release'
import SoonMovie from './components/soon'
import ClassicMovie from './components/classic'
export default {
  name: 'WebHome',
  data () {
    return {
      prompt: '本网站正在开发中，敬请期待！',
      tf: true
    }
  },
  methods: {
    success_movie () {
      setTimeout(() => {
        this.tf = false
      }, 1000)
    }
  },
  components: {
    HomeSwiper,
    ReleaseMovie,
    SoonMovie,
    ClassicMovie
  }
}
</script>

<style lang="stylus" scoped>
  @import '~style/scrwidth.styl'
  .main_box{
    position: relative
    margin: auto
    width: 1100px
    .prompt{
      color: rgb(15,153,213)
      font-size: .3rem
    }
  }
  @media only screen and (min-width:1900px){
    .main_box{
      scrWidth()
    }
  }
</style>
