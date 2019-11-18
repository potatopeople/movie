<template>
  <section class="type_box">
    <i class="point" ref="point"></i>
    <ul class="type">
      <li
        ref="type"
        v-for="(item, index) of movie_type"
        :key="item.id"
        @click="chose_type(index, item.catgory)"
        :class="item.chose"
      >
        {{item.name}}
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'TopType',
  data () {
    return {
      movie_type: [
        {id: 1, name: '热映口碑榜', catgory:'release', chose: 'active'},
        {id: 2, name: '最受期待榜', catgory:'soon', chose: 'no_active'},
        {id: 3, name: '经典TOP100', catgory:'classic', chose: 'no_active'}
      ],
      catgory: '',
      curren: ''
    }
  },
  computed: {
    start () {
      this.curren = this.$refs.type[0]
      return this.$refs.type[0]
    }
  },
  methods: {
    mouse_hover (indexs) { // 鼠标移入变色
      this.movie_type.forEach((item, index) => {
        if (indexs === index) {
          item.chose = 'active'
        } else {
          item.chose = 'no_active'
        }
      })
    },
    chose_type (index,catgory) { // 指标移动
      if (this.catgory !== catgory) {
        this.curren = event.target
        this.catgory = catgory
        this.mouse_hover(index)
        this.bus.$emit('http_movie_top', catgory,1)
        let movie_long = this.calc_long(event.target, this.$refs.point)
        this.$refs.point.style.left =  movie_long
      }
    },
    movie_point (dom,dom2) { // 初始化指标位置
      let movie_long = this.calc_long(dom2, dom)
      dom.style.left =  movie_long
    },
    calc_long (dom1, dom2) {
      return dom1.offsetLeft + (dom1.offsetWidth / 2) - (dom2.offsetWidth / 2) + 'px'
    }
  },
  mounted() {
    this.movie_point(this.$refs.point,this.start)
    window.addEventListener('resize',() => {
      this.movie_point(this.$refs.point,this.curren)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .type_box{
    margin-top: .3rem
    position: relative
    .point{
      display: inline-block
      position: absolute
      border: 10px solid rgb(240,240,240)
      border-color: transparent transparent white transparent
      z-index: 1
      bottom: 0
      transition: left .5s
    }
    .type{
      width: 100%
      height: 60px
      background: rgb(80,80,80)
      color: rgb(200,200,200)
      font-size: .4rem
      position: relative
      list-style: none
      padding: 0
      margin: 0
      display: flex
      box-sizing: border-box
      li{
        font-size: .35rem
        cursor: pointer
        padding: .3rem
        margin: auto
      }
      .active{
        color: rgb(245,26,52)
      }
      .no_active:hover{
        color: rgb(255,255,255)
      }
    }
  }
</style>

