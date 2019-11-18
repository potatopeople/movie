<template>
    <section class="header">
      <div class="content_box">
        <div class="img_box">
          <img :src="cinemas_img || 'https://p1.meituan.net/deal/201208/22/1_0822151022.jpg@292w_292h_1e_1c'">
        </div>
        <div class="intro_box">
          <p class="name">{{cinemas.name}}</p>
          <p class="address">{{cinemas.address | address_filter}}</p>
          <p class="phone">电话：{{'028-86586269' | phone_filter}}</p>
          <div class="xian">影院服务</div>
          <div class="service">
            <p>
              <span>3D眼镜</span>
              <span>免押金</span>
            </p>
            <p>
              <span>儿童优惠</span>
              <span>1.3米以下小朋友可享受无座免票</span>
            </p>
            <p>
              <span>可停车</span>
              <span>目前免费，详请现场咨询影城</span>
            </p>
          </div>
        </div>
      </div>
    </section>
</template>

<script>
export default {
  name: 'MovieHeader',
  data () {
    return {
      intro: '',
      cinemas_img: '',
    }
  },
  computed: {
    cinemas () {
      return JSON.parse(this.$route.query.cinemas)
    }
  },
  filters: {
    address_filter (value) {
      return value
    },
    phone_filter (value) {
      return value
    }
  },
  methods: {
    async get_cinemas_intro (cid,nid) {
      var data = {
        city_id: cid,
        cinemas_id: nid,
        money: this.cinemas.money
      }
      try {
        var response = await this.$http.postHttp('api/cinemas/cinemasList/movie', data)
        if (response.data.code === 200) {
          this.cinemas_img = response.data.data.cinemas_img
          this.$emit('cinemas_movie', response.data.data.data)
        }
        this.$emit('success_data')
      } catch (error) {
        this.$emit('success_data')
        console.log('cinemas_intro', error)
      }
    }
  },
  created () {
    this.$nextTick(() => {
      var pater = this.cinemas
      this.get_cinemas_intro(pater.cid,pater.nid)
    })
  }
}
</script>

<style lang="stylus" scoped>
  .header{
    position: relative
    height: 320px
    width: 100%
    background: rgb(15,153,213) url('../../../../static/images/cinemas_intro_bac.png')
    .content_box{
      position: relative
      top: 70px
      display: flex
      .img_box{
        position: relative
        width: 292px
        left: 240px
        height: 292px
        box-sizing: content-box
        padding-bottom: 40px
        img{
          width: 100%
          height: 100%
          border: 5px solid white
        }
        background: url('../../../../static/images/cinemas_intro_shadow.png') no-repeat bottom
        background-size: 300px 50px
      }
      .intro_box{
        position: relative
        left: 300px
        color: white
        font-size: .3rem
        .service{
          p{
            span:first-child{
              display: inline-block
              font-size: 12px
              height: 22px
              border-radius: 2px
              min-width: 60px
              line-height: 23px
              text-align: center
              border: 1px solid hsla(0,0%,100%,.6)
            }
            span:nth-child(2){
              font-size: 8px
              margin-left: 5px
            }
            margin-bottom: .04rem
          }
        }
        .name{
          font-size: .52rem
          margin-bottom: .18rem
        }
        .address{
          margin-bottom: .12rem
        }
        .phone{
          margin-bottom: .4rem
        }
        .xian{
          position: relative
          margin-bottom: .1rem
        }
        .xian:after{
          content: ''
          position: relative
          display: block
          top: -11px
          left: 70px
          border-top: 1px solid white
        }
      }
    }
  }
</style>
