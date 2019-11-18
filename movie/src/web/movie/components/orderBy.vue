<template>
  <section class="movie_orderby">
    <div
      v-for="(item, index) of order"
      :key="item.id"
      @click="chose_orderby(item.style,index,item.order)"
      :class="item.style"
    >
      <span :class="item.active"><i></i></span>
      <span>{{item.text}}</span>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MovieOrderby',
  data () {
    return {
      order: [
        {id:1,style:'hot',text:'按热门排序',active:'active',order:'0'},
        {id:2,style:'time',text:'按时间排序',active:'',order:'2'}
      ],
      curren: ''
    }
  },
  methods: {
    chose_orderby (cat,indexs,order) { // 选中事件
      if (!(cat === this.curren)) {
        this.curren = cat
        this.bus.$emit('movie_orderby', order)
        this.order.forEach((item,index) => {
          if (index === indexs) {
            item.active = 'active'
          } else {
            item.active = ''
          }
        })
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
  piont(){
    cursor: pointer
    font-size: .3rem
    display: flex
    span:first-child{
      position: relative
      display: inline-block
      width: 16px
      height: 16px
      border: 1px solid rgb(50,50,50)
      border-radius: 50%
      margin: auto
      i{
        position: absolute
        top: calc(50% - 4px)
        left: calc(50% - 4px)
        display: inline-block
        background: rgb(240,240,240)
        width: 8px
        height: 8px
        border-radius: 50%
      }
    }
    span:last-child{
      color: rgb(0,0,0)
      margin-left: .15rem
      display: inline-block
    }
  }
  .active{
    border: 0px solid red!important
    background: red
  }
  .movie_orderby{
    margin-top: .7rem
    display: flex
    .hot{
      margin-left: .1rem
      piont()
    }
    .time{
      margin-left: .6rem
      piont()
    }
  }
</style>
