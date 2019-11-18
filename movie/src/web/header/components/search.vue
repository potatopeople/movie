<template>
  <section class="search_box">
    <input v-model="search_text" type="text" placeholder="搜索电影.......">
    <div class="search iconfont" @click="search">&#xe6a8;</div>
  </section>
</template>

<script>
export default {
  name: 'HeaderSearch',
  data () {
    return {
      search_text: ''
    }
  },
  methods: {
    search () {
      this.$router.push({
        path: '/movie_search',
        query: {
          kw: this.search_text
        }
      })
      this.search_text = ''
    }
  }
}
</script>

<style lang="stylus" scoped>
  .search_box{
    margin: auto
    margin-right: 1.5rem
    position: relative
    input{
      color: rgb(80,80,80)
      font-size: .25rem
      padding: .2rem
      width: 250px
      background: rgb(248,248,248)
      padding-right: 1rem
      border: 1px solid rgb(200,200,200)
      outline: none
      border-radius: .5rem
    }
    input:hover{
      border: 1px solid rgb(200,200,200)
    }
    .search{
      cursor: pointer
      position: absolute
      color: black
      font-size: .5rem
      right: .2rem
      top: .05rem
    }
    .search:hover{
      transform: scale(1.1)
    }
  }
</style>
