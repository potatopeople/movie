<template>
  <section class="home_box" @click.stop="screen_click">
    <home-header />
    <home-list />
  </section>
</template>

<script>
import HomeHeader from './components/header'
import HomeList from './components/list'
export default {
  name: 'WebHome',
  components: {
    HomeHeader,
    HomeList
  },
  methods: {
    screen_click () {
      this.bus.$emit('screen_click')
    }
  }
}
</script>

<style lang="stylus" scoped>
  .home_box{
    min-height: 100vh
    display: flex
    background: white
    flex-direction: column
  }
</style>

