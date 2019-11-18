<template>
  <section class="swiper_box">
    <div class="swiper-container">
      <div class="swiper-wrapper">
        <div
          class="swiper-slide swiper-no-swiping"
          v-for="item of imgs"
          :key="item.id"
        >
          <img :src="item.url">
        </div>
      </div>
      <div class="swiper-pagination"></div>
      <div class="swiper-scrollbar"></div>
    </div>
  </section>
</template>

<script>
import Swiper from 'swiper'
export default {
  name: 'HomeSwiper',
  data () {
    return {
      swiperConfig: {
        pagination : '.swiper-pagination', // 分页器类名
        paginationType : 'custom', // 分页器样式
        scrollbar: '.swiper-scrollbar' , // 滚动条
        scrollbarHide: false, // 显示滚动条
        scrollbarDraggable : true , // 拖动滚动条
        scrollbarSnapOnRelease : true , // 释放滚动条，贴合slide
        effect: 'slide', // 切换方式
        loop: true, // 开启环路
        autoplay: 3000, // 自动播放间隔时间 ms
        autoHeight: true, // 自适应高度
        autoplayDisableOnInteraction: true, // 操作后依然播放
        speed: 500 // 切换间隔的时间 ms
      },
      imgs: [ // 轮播图片
        {id: 1, url: require('images/home1.jpg')},
        {id: 2, url: require('images/home2.jpg')},
        {id: 3, url: require('images/home3.jpg')},
        {id: 4, url: require('images/home4.jpg')},
      ]
    }
  },
  mounted () {
    let mySwiper = new Swiper(
      '.swiper-container',
      this.swiperConfig
    )
  }
}
</script>

<style lang="stylus" scoped>
  .swiper_box{
    margin-top: .3rem
    height: 8.2rem
    background: rgb(150,150,150)
    overflow: hidden
    img{
      width: 100%
    }
  }
  @media only screen and (max-width:1900px){
    .swiper_box{
      height: 6.95rem
    }
  }
</style>
