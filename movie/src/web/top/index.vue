<template>
  <section class="movie_top_box">
    <top-type />
    <movie-list @success_data="success_data" />
    <movie-page />
    <data-mask v-show="tf"></data-mask>
  </section>
</template>

<script>
import TopType from './components/type'
import MovieList from './components/movie'
import MoviePage from './components/page'
export default {
  name: 'MovieTop',
  data () {
    return {
      tf: true
    }
  },
  methods: {
    success_data () {
      setTimeout(() => {
        this.tf = false
      }, 1000)
    }
  },
  components: {
    TopType,
    MovieList,
    MoviePage
  }
}
</script>

<style lang="stylus" scoped>
  .movie_top_box{
    background: white
  }
</style>
