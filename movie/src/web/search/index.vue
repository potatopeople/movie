<template>
 <section class="search_box">
   <search-input />
   <movie-list @success_data="success_data" />
   <movie-page />
   <data-mask v-show="tf"></data-mask>
 </section>
</template>

<script>
import SearchInput from './components/input'
import MovieList from './components/movie'
import MoviePage from './components/page'
export default {
  name: 'MovieSearch',
  components: {
    SearchInput,
    MovieList,
    MoviePage
  },
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
  }
}
</script>

<style lang="stylus" scoped>
  .search_box{
    background: white
  }
</style>
