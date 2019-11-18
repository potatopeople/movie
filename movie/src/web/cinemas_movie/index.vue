<template>
  <section>
    <movie-header @success_data="success_data" @cinemas_movie="cinemas_movie" />
    <movie-list @chose_movie="chose_movie" :movie_list="movie" />
    <movie-intro :movie_intro="movie_intro" />
    <data-mask v-show="tf"></data-mask>
  </section>
</template>

<script>
import MovieHeader from './components/header'
import MovieList from './components/movie'
import MovieIntro from './components/intro'
export default {
  name: 'CinemasMovie',
  components: {
    MovieHeader,
    MovieList,
    MovieIntro
  },
  computed: {
    cinemas () {
      return JSON.parse(this.$route.query.cinemas)
    }
  },
  data () {
    return {
      movie: [],
      movie_intro: {},
      money: '',
      room: '',
      tf: true
    }
  },
  methods: {
    success_data () {
      setTimeout(() => {
        this.tf = false
      }, 1000)
    },
    chose_movie (index=0,name='') { // 选中电影
      this.movie.forEach((item, indexs) => {
        if (index === indexs || name === item.name) {
          item.active = 'active'
          this.movie_intro = this.movie[indexs]
        } else {
          item.active = ''
        }
      })
    },
    cinemas_movie (value) {
      var new_value = value.forEach((item, index) => {
        if (index === 0) {
          item['active'] = 'active'
          this.movie_intro = item
        } else {
          item['active'] = ''
        }
      })
      this.movie = value
    }
  }
}
</script>

<style lang="stylus" scoped>

</style>
