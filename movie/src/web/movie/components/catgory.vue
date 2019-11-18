<template>
  <section class="catgory_box" ref="box">
    <ul class="catgory">
      <li class="box">
        <div class="cat">分类：</div>
        <ul>
          <li
            v-for="(item, index) of catgory.catgorys"
            :key="index"
            :class="[item.chose]"
            @click="chose_catgory('catgorys', item.name, index)"
          >
            {{item.name}}
          </li>
        </ul>
      </li>
    </ul>
    <ul class="years">
      <li class="box">
        <div class="cat">地区：</div>
        <ul>
          <li
            v-for="(item, index) of catgory.years"
            :key="index"
            :class="[item.chose]"
            @click="chose_catgory('years', item.name, index)"
          >
            {{item.name}}
          </li>
        </ul>
      </li>
    </ul>
    <ul class="region">
      <li class="box">
        <div class="cat">年代：</div>
        <ul>
          <li
            v-for="(item, index) of catgory.region"
            :key="index"
            :class="[item.chose]"
            @click="chose_catgory('region', item.name, index)"
          >
            {{item.name}}
          </li>
        </ul>
      </li>
    </ul>
  </section>
</template>

<script>
export default {
  name: 'MovieCatgory',
  data () {
    return {
      catgory: [],
      catgorys:'',
      years: '',
      region: ''
    }
  },
  methods: {
    chose_catgory (type, catgory, indexe,i=0) { // 类型点击事件
      if (!(this[type] === catgory)) {
        let chose
        this[type] = catgory
        for (let i  = 0; i < this.catgory[type].length; i++) {
          if (this.catgory[type][i].chose === 'active') {
            this.catgory[type][i].chose = ''
          }
        }
        if (i === 0) {
          this.http_catgory(this.catgorys,this.years,this.region)
        }
        this.catgory[type][indexe].chose = 'active'
      } else {
        return 0
      }
    },
    http_catgory (catgorys,years,region) {
      if (catgorys === '全部') {
        catgorys = 'all'
      }
      if (years === '全部') {
        years = 'all'
      }
      if (region === '全部') {
        region = 'all'
      }
      this.bus.$emit('movie_catgory',{
        catgorys: catgorys || 'all',
        years: years || 'all',
        region: region || 'all'
      })
    },
    handel_data (data) { // 赋值
      let chose
      let cat = data
      for (let item in data) {
        cat[item] = cat[item].map((item, index) => {
          if (index === 0) {
            chose = 'active'
          } else {
            chose = ''
          }
          return {
            name: item,
            chose
          }
        })
      }
      this.catgory = cat
    },
    async getMovieList () { // 请求电影分类列表
      try{
        let response = await this.$http.getHttp('api/movieCatgory')
        if (response.data.code === 200) {                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
          this.handel_data(response.data.data)
        }
        this.$emit('success_data')
      } catch (error) {
        this.$emit('success_data')
        console.log('电影分类失败：', error)
      }
    },
    catgory_redirect () { // 重定向位置
      let cat = ['catgorys', 'years', 'region']
      for (let i = 0; i < 3; i++) {
        this.chose_catgory(cat[i],'all',0,1)
      }
    }
  },
  created () {
    this.$nextTick(() => {
      this.getMovieList()
      this.bus.$on('catgory', this.catgory_redirect)
    })
  }
}
</script>

<style lang="stylus" scoped>
  @import '~style/fontFamily.styl'
  ulContent(){
    margin-top: .2rem
    margin-bottom: .2rem
    list-style: none
    .box{
      font-size: .3rem
      display: flex
      .cat{
        padding-left: .2rem
        text-align: center
        width: 1.5rem
        line-height: .6rem
        color: rgb(120,120,120)
      }
      ul{
        flex: 1
        list-style: none
        li{
          min-width: 50px
          height: 22px
          border-radius: .2rem
          color: black
          text-align: center
          float: left
          margin: .1rem .25rem
        }
        li:hover{
          color: rgb(15,153,213)
          cursor: pointer
        }
      }
    }
    
  }
  .active{
    background: rgb(15,153,213)!important
    color: white!important
  }
  .catgory_box{
    user-select: none
    width: 100%
    display: flex
    flex-direction: column
    back()
    fontFamily()
    .catgory{
      ulContent()
    }
    .years{
      ulContent()
    }
    .region{
      ulContent()
    }
  }
</style>
