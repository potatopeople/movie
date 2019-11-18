<template>
  <section class="screen">
    银幕中央
  </section>
</template>

<script>
export default {
  name: 'MovieScreen'
}
</script>

<style lang="stylus" scoped>
  .screen{
    padding-top: 50px
    position: relative
    width: 550px
    text-align: center
    font-size: 16px
    margin: 0 auto
    color: #666
    background: url('../../../../static/images/screen.png') no-repeat
    background-position-x: center
  }
  .screen:after{
    content: ''
    position: absolute
    height: 500px
    border-left: 1px dashed #e5e5e5
    left: 50%
    top: 90px
  }
</style>
