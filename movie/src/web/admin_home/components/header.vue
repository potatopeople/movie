<template>
  <section class="header_box">
    <div class="header_back">
      <p class="name">土豆电影后台管理</p>
      <p class="user">
        <span>{{user_name || '用户'}}</span>
        <img @click.stop="user_center" :src="user_img">
      </p>
      <div class="user_center" v-if="show_center">
        <ul class="user_option">
          <li
            v-for="(item, index) of user"
            :key="item.id"
            @click="chose_option(item.text,index)"
            :class="['option']"
          >
            {{item.text}}
          </li>
        </ul>
      </div> 
      <message-box
        :option="option"
        @sure_btn="sure_btn"
        @close_btn="close_btn"
      />
    </div>
  </section>
</template>

<script>
import MessageBox from '@/public/message'
export default {
  name: 'HomeHeader',
  components: {
    MessageBox
  },
  data () {
    return {
      option: {
        show: false,
        position: 'absolute',
        btn_show: true,
        tiSize: '.35rem',
        messSize: '.3rem',
        message: '是否注销用户？',
        catgory: 'tips',
        animatedIn: 'animated fadeInRight',
        animatedOut: 'animated fadeOutRight',
        top: '90px',
        right: '1rem',
        enterTime: 800, // 进入动画时间
        leaveTime: 600 // 离开动画时间
      },
      user_img: require('../../../assets/images/user.png'),
      dom_height: '',
      user: [
        {id:1,text:'个人中心',active:''},
        {id:2,text:'设置',active:''},
        {id:3,text:'注销',active:''}
      ],
      show_center: false
    }
  },
  computed: {
    user_name () {
      return window.sessionStorage.getItem('admin_name')
    }
  },
  methods: {
    sure_btn () {
      this.$router.replace('/admin')
    },
    close_btn () {
      this.option.show = false
    },
    user_center () {
      this.show_center = this.show_center == false ? true:false
    },
    chose_option () {
      document.documentElement.style.overflow = 'hidden'
      this.option.show = true
      this.disappear()
    },
    disappear () {
      this.show_center = false
    } 
  },
  mounted () {
    this.bus.$on('screen_click',this.disappear)
  }
}
</script>

<style lang="stylus" scoped>
  .header_box{
    flex: 0.5
    min-height: 70px
    max-height: 80px
    display: flex
    .header_back{
      position: relative
      flex: 1
      background: rgb(32,160,255)
      display: flex
      color: white
      justify-content: space-between
      align-items: center
      p{
        padding: 0
        margin: 0
      }
      .name{
        margin-left: .65rem
        font-size: .7rem
      }
      .user{
        margin-right: 1rem
        font-size: .35rem
        align-items: center
        display: flex
        position: relative
        span{
          margin-right: 1.5rem
          user-select: none
        }
        img{
          cursor: pointer
          position: absolute
          right: 0
          width: 60px
          height: 60px
        }
      }
      .user_center:before{
        content: ''
        top: -12px
        left: 25%
        position: absolute
        border: 6px solid white
        border-color: transparent transparent white transparent
      }
      .user_center{
        position: absolute
        z-index: 5
        right: 1rem
        top: 90px
        background: white
        filter: drop-shadow(0rem 0rem .05rem rgb(150,150,150))
        border-radius: 5px
        .user_option{
          padding: 0
          margin: 0
          list-style: none
          .option{
            font-size: .35rem
            padding: .3rem .35rem
            color: rgb(80,80,80)
          }
          .option:last-child{
            border-top: 1px solid rgb(220,220,220)
          }
          .option:hover{
            background: rgb(240,240,240)
            cursor: pointer
          }
        }
      }
    }
  }
</style>
