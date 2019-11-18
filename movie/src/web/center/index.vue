<template>
  <section class="center_box">
    <div class="list">
      <p class="title">个人中心</p>
      <div @click="chose_option(item.ticps,item.path)" :class="[item.active,'option']" v-for="item of ticps" :key="item.id">{{item.text}}</div>
    </div>
    <div class="body">
      <p class="bo_title">{{cat_text}}</p>
      <router-view @error_ticps="error_ticps" />
    </div>
    <screen-mask @error_ticps="error_ticps" :ticps="ticpsx" v-if="ticps_mask" />
  </section>
</template>

<script>
import ScreenMask from '@/public/mask'
export default {
  name: 'UserCenter',
  components: {
    ScreenMask
  },
  data () {
    return {
      ticps: [
        {id:1,text:'基本信息',ticps:'intro',path:'/center/intro',active:'active'},
        {id:2,text:'我的订单',ticps:'order',path:'/center/order',active:''},
      ],
      ticpsx: '',
      ticps_mask: false
    }
  },
  watch: {
    cat: {
      handler (o,n) {
        this.ticps.forEach(item => {
          item.active = ''
          if (item.ticps === o) {
            item.active = 'active'
          }
        })
      },
      immediate: true
    }
  },
  computed: {
    cat () {
      return this.$route.query.cat
    },
    cat_text () {
      for (let i = 0; this.ticps.length; i++) {
        if (this.ticps[i].ticps === this.cat) {
          return this.ticps[i].text
        }
      }
    }
  },
  methods: {
    error_ticps (value,ticps='') { // 錯誤提示
      if (value === 'close') {
        this.ticpsx = ''
        this.ticps_mask = false
      } else if (value === 'error') {
        this.ticpsx = ticps
        this.ticps_mask = true
      }
    },
    chose_option (ticps,path) {
      this.$router.push({
        path,
        query: {
          cat:ticps
        }
      })
    }
  }
}
</script>

<style lang="stylus" scoped>
  .center_box{
    display: flex
    margin-top: 30px
    border: 1px solid rgb(200,200,200)
    min-height: 800px
    .list{
      flex: 1
      background: rgb(245,245,245)
      color: #222
      font-weight: 400
      .title{
        margin: 40px 0 30px 0
        font-size: 22px
        text-align: center
      }
      .option{
        height: 40px
        line-height: 40px
        font-size: 18px
        text-align: center
        cursor: pointer
      }
      .active{
        background: rgb(15,230,230)
      }
    }
    .body{
      flex: 5
      background: white
      .bo_title{
        color: rgb(15,180,230)
        padding: 26px 0
        font-size: 18px
        border-bottom: 1px solid #e1e1e1
        margin-left: 40px
      }
    }
  }
</style>
