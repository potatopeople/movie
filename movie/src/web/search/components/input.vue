<template>
  <section class="search_input_box">
    <div class="input_box">
      <input @keydown="keydow" v-model="input_text" type="text">
      <div @click="search_movie" class="iconfont">&#xe6a8;</div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'SearchInput',
  data () {
    return {
      input_text: '' // 搜索关键字
    }
  },
  computed: {
    kw () {
      return this.$route.query.kw
    }
  },
  watch:  {
    kw () {
      this.input_text = this.kw
    }
  },
  methods: {
    keydow (e) {
     if (e.key === 'Enter') {
       this.search_movie()
     }
    },
    search_movie () {
      this.$router.push({
        path: '',
        query: {
          kw: this.input_text
        }
      })
      this.bus.$emit('http_movie_searchs')
    }
  },
  mounted () {
    this.input_text = this.kw
  }
}
</script>

<style lang="stylus" scoped>
  .search_input_box{
    background: rgb(80,80,80)
    padding: .5rem 0
    display: flex
    justify-content: center
    .input_box{
      position: relative
      width: 600px
      input{
        padding: .2rem 1rem .2rem .3rem
        width: 100%
        height: 100%
        border: 0px solid red
        color: rgb(100,100,100)
        font-size: .4rem
        outline: none
        border-radius: .4rem
      }
      .iconfont{
        position: absolute
        right: .25rem
        cursor: pointer
        bottom: 0
        font-size: .6rem
        color: red
        font-weight: 600
      }
    }
  }
</style>
