<template>
  <section class="talk_box">
    <p class="title">用户短评</p>
    <comment-assembly 
      :comment_data="comment_data"
      @send_container="send_container"
      :user_intro="user_intro"
      :default_img="default_img"
    />
    <div class="promt" v-if="!comment_data.length">暂无评论</div>
  </section>
</template>

<script>
import CommentAssembly from '@/public/comment'
export default {
  name: 'UserTalk',
  components: {
    CommentAssembly
  },
  props: {
    comment_data: {
      type: Array,
      default: []
    }
  },
  data () {
    return {
      default_img: require('@/assets/images/user.png'),
    }
  },
  computed: {
    user_intro () {
      return this.$store.state.user.header_user_intro || {}
    }
  },
  methods: {
    send_container (text) { // 发送消息
      let date = this.date_filter(new Date())
      let data = {
        id:1,
        name: this.user_intro.name,
        time: date,
        main: text,
        img: this.user_intro.avatar
      }
      this.$emit('send_talk',data)
    },
    date_filter (date) {
      let year = date.getFullYear(),
          month = (date.getMonth() + 1),
          dat = date.getDate(),
          hours = date.getHours(),
          seconds = date.getSeconds(),
          minutes = date.getUTCMinutes();
      return  year + '-' + month + '-' + dat + ' ' + hours +':' + minutes + ':' + seconds
    }
  }
}
</script>

<style lang="stylus" scoped>
  .talk_box {
    background: white
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
    .promt{
      text-align: center
      font-size: .5rem
      padding-bottom: .5rem
      color: #333
    }
  }
</style>
