<template>
  <section>
    <movie-header :movie_data="movie_intro" @look_intro="look_intro" />
    <cinemas-list @success_list="success_list" v-show="!intro" />
    <movie-intro v-if="intro" :movie_data_intro="movie_data_intro"/>
    <user-talk v-show="intro" @send_talk="send_talk" :comment_data="comment_data" />
    <data-mask v-show="tf"></data-mask>
  </section>
</template>

<script>
import MovieHeader from './components/header'
import CinemasList from './components/cinemas_list'
import MovieIntro from './components/intro'
import UserTalk from './components/talk'
export default {
  name: 'ReleaseMovie',
  components: {
    MovieHeader,
    CinemasList,
    MovieIntro,
    UserTalk
  },
  computed: {
    movie_data_intro () {
      return JSON.parse(this.$route.query.item).introduction
    },
    movie_intro () {
      return JSON.parse(this.$route.query.item)
    },
    token () {
      let token = JSON.parse(window.localStorage.getItem('_AMap_vectoruser')),
          reg = /\$(.*)\$/g;
      return reg.exec(token.version)[1]
    }
  },
  data () {
    return {
      intro: false,
      comment_data: [],
      tf: true
    }
  },
  methods: {
    success_list () {
      setTimeout(() => {
        this.tf = false
      },2000)
    },
    look_intro () {
      this.intro = !this.intro
    },
    async send_talk (main) { // 发送评论
      try {
        let data = {
          cat: this.movie_intro.play_cat,
          mid: this.movie_intro.id,
          main: main.main
        }
        let response = await this.$http.put_http_auth('api/movie/send_talk',data,this.token)
        if (response.data.code === 200) {
          this.comment_data.unshift(main)
        } else {
          alert(response.data.message)
        }
      } catch (error) {
        alert(error)
      }
    },
    async get_talk () {
      try {
        let data = {
          cat: this.movie_intro.play_cat,
          mid: this.movie_intro.id
        }
        let response = await this.$http.postHttp('api/movie/get_talk',data)
        if (response.data.code === 200 || response.data.code === 300) {
          this.comment_data = response.data.data
          this.tf = false
        }
      } catch (error) {
        console.log(error)
      }
    }
  },
  created () {
    this.$nextTick(this.get_talk)
  }
}
</script>