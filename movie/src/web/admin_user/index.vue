<template>
  <section>
    <table-data :user_intro="user_intro" />
  </section>
</template>

<script>
import TableData from './components/table'
export default {
  name: 'UserIntro',
  components: {
    TableData
  },
  data () {
    return {
      user_intro: []
    }
  },
  computed: {
    token () {
      return window.sessionStorage.getItem('admin_token')
    }
  },
  methods: {
    async get_user_intro () {
      try {
        let response = await this.$http.get_http_auth('api/admin/data_query/user','',this.token)
        if (response.data.code === 200) {
          this.user_intro = response.data.data
        }
      } catch (error) {
        alert(error)
      }
    }
  },
  created () {
    this.$nextTick(this.get_user_intro)
  }
}
</script>

<style lang="stylus" scoped>

</style>
