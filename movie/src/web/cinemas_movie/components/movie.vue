<template>
  <section ref="box" class="movie_list">
    <div ref="movie_box" class="movie_box">
      <div
        :class="['movie', item.active]"
        v-for="(item, index) of movie_list"
        :key="item.id"
        @click="chose_movie(index,item.id,item.city_id,item.cinemas_id)"
      >
        <img :src="item.movie_img">
      </div>
    </div>
    <span @click="prev_btn" class="prev_btn"></span>
    <span @click="next_btn" class="next_btn"></span>
  </section>
</template>

<script>
export default {
  name: 'MovieList',
  props: {
    movie_list: {
      type: Array,
      default: []
    }
  },
  methods: {
    prev_btn () { // 上一页
      var dom = this.$refs.movie_box,
          left = parseFloat(window.getComputedStyle(dom).left.replace('px','')),
          box_w = this.$refs.box.offsetWidth, // 外容器宽
          movie_w = dom.offsetWidth, // 电影容器宽
          max_l = movie_w - box_w; // 最大移动left
      this.dom_move('L',dom,147,left,max_l)
    },
    dom_move (direction,dom,size,curreen_left,max_l) { // 移动电影列表
      if (max_l <= 0) {
        max_l = 0
      }
      if (size+curreen_left <= (-max_l) && direction === 'R') {
        dom.style.left = -max_l + 'px'
      } else if (direction === 'L' && curreen_left + size >= 0) {
        dom.style.left = '0px'
      } else {
        dom.style.left = curreen_left + size +'px'
      }
    },
    next_btn () { // 下一页
      var dom = this.$refs.movie_box,
          left = parseFloat(window.getComputedStyle(dom).left.replace('px','')),
          box_w = this.$refs.box.offsetWidth, // 外容器宽
          movie_w = dom.offsetWidth, // 电影容器宽
          max_l = movie_w - box_w; // 最大移动left
      this.dom_move('R',dom,-147,left,max_l)
    },
    chose_movie (index, id, cid, nid) {
      this.$emit('chose_movie', index)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .movie_list{
    background: rgb(220,220,220)
    width: 100%
    height: 236px
    margin-top: 120px
    padding: 22px 0
    box-sizing: content-box
    overflow: hidden
    position: relative
    .movie_box{
      position: absolute
      display: flex
      align-items: center
      top: calc(50% - 97px)
      left: 0
      padding: 0 .2rem
      transition: left .3s
      .movie{
        height: 186px
        width: 139px
        border: 4px solid #fff
        box-sizing: content-box
        box-shadow: 0 1px 3px 0 hsla(0,0%,66%,.5)
        margin: 0 .3rem
        transform: scale(1)
        transition: transform .3s
        img{
          height: 100%
          width: 100%
        }
      }
      .active{
        transform: scale(1.2)
        box-sizing: content-box
        border: 4px solid rgb(15,183,213)
      }
    }
    span{
      display: inline-block
      position: absolute
      width: 30px
      height: 100%
      top: 0
      cursor: pointer
    }
    .prev_btn{
      left: 0
      background: url('../../../../static/images/prev.png') no-repeat center
    }
    .next_btn{
      right: 0
      background: url('../../../../static/images/next.png') no-repeat center
    }
  }
</style>
