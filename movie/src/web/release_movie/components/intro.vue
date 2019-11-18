<template functional>
  <section class="intro_box">
    <p class="title">电影介绍</p>
    <div class="text_o" v-if="!props.movie_data_intro">
      该电影暂无介绍
    </div>
    <div class="text">
      {{props.movie_data_intro}}
    </div>
  </section>
</template>

<style lang="stylus" scoped>
  .intro_box{
    background: white
    .text{
      padding: .25rem
      font-size: 15px
      line-height: 26px
    }
    .text_o{
      text-align: center
      font-size: .4rem
      padding: .3rem 0
      color: black 
    }
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


