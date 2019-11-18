<template>
  <section>
    <movie-type />
    <movie-catgory @success_data="success_data" />
    <movie-orderby />
    <movie-lists />
    <movie-page />
    <data-mask v-show="tf"></data-mask>
  </section>
</template>

<script>
import MovieType from './components/type'
import MovieCatgory from './components/catgory'
import MovieOrderby from './components/orderBy'
import MovieLists from './components/movie'
import MoviePage from './components/page'
export default {
  name: 'MovieList',
  data () {
    return {
      tf: true
    }
  },
  methods: {
    success_data () {
      setTimeout(() => {
        this.tf = false
      }, 2000)
    }
  },
  components: {
    MovieType,
    MovieCatgory,
    MovieOrderby,
    MovieLists,
    MoviePage
  },
  mounted () {
    window.scroll(0,0)
  }
}
</script>