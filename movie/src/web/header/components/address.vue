<template>
  <section class="address_box">
    <div class="box" ref="box">
      <div class="header">
        <span class="chose">请选择城市</span>
        <div class="search">
          <input v-model="search" placeholder="搜索城市" type="text" class="input">
        </div>
        <span @click="close_box" class="iconfont">&#xe60d;</span>
      </div>
      <div class="address">
        <ul class="list">
          <li v-if="tf" class="search_list active">搜索</li>
          <li
            :class="['option',item.active]"
            v-for="(item,index) of spin"
            :key="item.id"
            @click="chose_spin(item.name,index)"
          >
            {{item.name}}
          </li>
        </ul>
        <div class="name">
          <span
            class="city"
            v-for="item of curren_address"
            :key="item.id"
            @click="chose_city(item)"
          >
            {{item.name}}
          </span>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import remoteLoad from '@/public/remoload'
export default {
  name: 'NavAddress',
  data () {
    return {
      address: [], // 城市数据
      spin: [], // 城市分类
      curren_address: [], // 当前城市分类数据
      search: '', // 搜索城市
      tf: false,
      location: '' // 定位的地点
    }
  },
  watch: {
    search () {
      if (this.search) {
        this.search_city()
      } else {
        this.curren_address = []
      }
    }
  },
  computed: {
    all_address () { // 所有城市数据
      return this.address['all']
    }
  },
  methods: {
    get_user_navtar () { // 开始定位
      var mapObj = new AMap.Map('iCenter');
      var _this = this
      mapObj.plugin('AMap.Geolocation', function () {
        var geolocation = new AMap.Geolocation({
          enableHighAccuracy: true, // 是否使用高精度定位，默认:true
          timeout: 10000, // 超过10秒后停止定位，默认：无穷大
          maximumAge: 0 // 定位结果缓存0毫秒，默认：0
        })
        mapObj.addControl(geolocation)
        geolocation.getCurrentPosition()
        AMap.event.addListener(geolocation, 'complete', _this.onComplete) // 返回定位信息
        AMap.event.addListener(geolocation, 'error', _this.onError) // 返回定位出错信息
      })
    },
    onError(obj) { // 定位失败
      this.refine_address('北京')
      console.log('定位失败：',JSON.stringify(obj.info + '--' + obj.message))
    },
    onComplete(obj){ // 定位成功
      this.location = obj.addressComponent.city || '北京'
      this.refine_address(this.location)
    },
    refine_address (address) {
      var data = ''
      var index = this.all_address.findIndex(item => {
        var tf = new RegExp(item.name)
        return tf.exec(address)
      })
      if (index > -1) {
        data = this.all_address[index]
      } else {
        data = this.all_address[18]
      }
      this.$store.dispatch('get_user_address', data)
      this.get_city_id()
    },
    close_box () { // 关闭菜单
      this.$emit('close_address', false)
    },
    search_city () { // 搜索城市
      this.spin.forEach((item) => {
        item.active = ''
      })
      this.tf = true
      let reg = new RegExp(this.search)
      let search_city_data = this.address['all'].filter((item) => {
        return reg.test(item.name)
      })
      if (search_city_data.length) {
        this.curren_address = search_city_data
      } else {
        this.curren_address = [{id:1,name:'没有搜索到城市'}]
      } 
    },
    chose_spin (catgory,index) { // 选择城市分类
      this.tf = false
      this.curren_address = this.address[catgory]
      this.spin.forEach((item,indexs) => {
        if (index === indexs) {
          item.active = 'active'
        } else {
          item.active = ''
        }
      })
    },
    chose_city (city) { // 选择城市
      this.$store.dispatch('get_user_address', city)
      this.$emit('close_address', false)
      this.get_cinemas_list_data(city.id)
    },
    get_city_id () {
      var city_id = window.localStorage.getItem('userAddress')
      city_id = JSON.parse(city_id)
      this.get_cinemas_list_data(city_id.id)
    },
    async get_cinemas_list_data (id) {
      try{
        let response = await this.$http.getHttp(`api/cinemas/cinemasList/${id}`)
        if (response.data.code === 200) {
          this.$store.dispatch('get_cinemas_data', response.data.data)
        }
      } catch (error) {
        console.log('电影院请求错误:',error)
      }
    },
    async addressHttp () {
      try {
        let response = await this.$http.getHttp('api/address')
        if (response.data.code = 200) {
          this.address = response.data.data
          this.data_filter(this.address)
        }
      } catch (error) {
        console.log('地址请求错误：',error)
      }
    },
    data_filter (data) { // 数据整理
      let anchor = [],
          i = 0;
      for (let item in data) {
        anchor.push({id:i,name: item,active: ''})
        i ++
      }
      anchor[0].active = 'active'
      anchor.pop() // 删除最后一项
      this.curren_address = this.address['A']
      this.spin = anchor
    },
    async initMap() {
      try{
        await remoteLoad(`http://webapi.amap.com/maps?v=1.3&key=a55652fb4e2c77556cd4f1234d849eaa`),
        this.get_user_navtar()
      } catch (error) {
        console.log('高德数据获取失败',error)
      }
    }
  },
  created () {
    this.$nextTick(() => {
      this.addressHttp()
      this.initMap()
    })
  }
}
</script>

<style lang="stylus" scoped>
  .address_box{
    position: absolute
    width: 100%
    height: 100%
    background: rgba(100,100,100,.6)
    z-index: 100
    .box{
      position: fixed
      width: 900px
      top: 15%
      left: calc(50% - 400px)
      background: rgb(255,255,255)
      .header{
        font-size: .35rem
        padding: .3rem
        margin: 0
        display: flex
        justify-content: space-between
        align-items: center
        .iconfont{
          font-size: .5rem
          cursor: pointer
        }
        .search{
          .input{
            border: 1px solid rgb(200,200,200)
            outline: none
            font-size: .3rem
            color: rgb(120,120,120)
            padding: .1rem .1rem
          }
        }
      }
      .address{
        display: flex
        height: 400px
        overflow: auto
        .list{
          background: rgb(240,240,240)
          overflow: auto
          height: 400px
          list-style: none
          padding: .2rem 0 0 0
          margin: 0
          .search_list{
            width: 2rem
            position: relative
            cursor: pointer
            text-align: center
            font-size: .3rem
            padding: .2rem .2rem .2rem .3rem
            color: rgb(15,153,213)
            background: rgb(255,255,255)
          }
          .option{
            position: relative
            width: 2rem
            cursor: pointer
            text-align: center
            font-size: .3rem
            padding: .2rem .2rem .2rem .3rem
          }
          .option:hover{
            color: rgb(15,153,213)
            text-shadow: 0 0 .1rem rgb(100,100,100)
          }
          .active{
            color: rgb(15,153,213)!important
            text-shadow: 0 0 0 rgb(100,100,100)!important
            background: rgb(255,255,255)
          }
          .active:before{
            content: ''
            position: absolute
            top: 0
            left: 0
            height: 100%
            width: 5px
            background: rgb(15,153,213)
          }
        }
        .name{
          flex: 1
          display: flex
          overflow: auto
          flex-wrap: wrap
          padding: .25rem .4rem
          font-size: .31rem
          align-content: flex-start
          .city{
            cursor: pointer
            margin: 0 .8rem .7rem 0
            height: min-content
          }
          .city:hover{
            color: rgb(15,133,213)
          }
        }
      }
    }
  }
</style>
