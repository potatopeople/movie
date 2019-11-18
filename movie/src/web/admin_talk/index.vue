<template>
  <section>
    <table-data @look_main="look_main" @drop_talk="drop_talk" @pointr="pointr" :user_talk="user_talk" />
    <look-mask @close_mask="close_mask" v-if="main_tf" :main="main" />
  </section>
</template>

<script>
import LookMask from './components/mask'
import TableData from './components/table'
export default {
  name: 'UserTalk',
  components: {
    TableData,
    LookMask
  },
  data () {
    return {
      user_talk: [],
      main: {},
      main_tf: false
    }
  },
  computed: {
    token () {
      return window.sessionStorage.getItem('admin_token')
    }
  },
  methods: {
    close_mask () {
      this.main_tf = false
    },
    look_main (main) {
      this.main = main
      this.main_tf = true
      console.log(main)
    },
    pointr (ids) {
      for (let i = 0; i < this.user_talk.length; i++) {
        this.user_talk[i].active = ''
        if (parseInt(ids) === this.user_talk[i].id) {
          this.user_talk[i]['active'] = 'active'
        }
      }
    },
    async drop_talk (id, index) {
      try {
        let response = await this.$http.del_http_auth('api/admin/talk/drop/' + id,'',this.token)
        if (response.data.code === 200) {
          this.user_talk.splice(index,1)
          alert('删除成功')
        } else {
          alert('删除失败')
        }
      } catch (error) {
        alert('删除失败')
        console.log(error)
      }
    },
    async get_user_talk () {
      try {
        let response = await this.$http.get_http_auth('api/admin/data_query/talk','',this.token)
        if (response.data.code === 200) {
          this.data_handel(response.data.data)
        }
      } catch (error) {
        alert(error)
      }
    },
    data_handel (datas) {
      for(let i = 0; i < datas.length; i++) {
        datas[i]['active'] = ''
      }
      this.user_talk = datas
    }
  },
  created () {
    this.$nextTick(this.get_user_talk)
  }
}
</script>

<style lang="stylus" scoped>

</style>
