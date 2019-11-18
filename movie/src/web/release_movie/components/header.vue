<template>
    <section class="header">
      <div class="content_box">
        <div class="img_box">
          <img :src="movie_data.img">
        </div>
        <div class="intro_box">
          <p class="name">{{movie_data.name}}</p>
          <p class="elname">{{movie_data.elname}}</p>
          <p class="cat">{{movie_data.catgory}}</p>
          <p class="address">
              {{movie_data.address}}
              &nbsp;/&nbsp;
              {{movie_data.playTime}}
          </p>
          <p class="time">{{movie_data.releaseTime | time_filter}}上映</p>
          <div class="box">
              <div class="save"><i></i>收藏</div>
              <div class="score"><i></i>评分</div>
          </div>
          <div class="information" @click="look_mvie">{{ticps}}</div>
        </div>
        <div class="evaluate">
          <div class="score_box">
            <p>用户评分</p>
            <div class="box">
              <div class="score">{{movie_data.score}}</div>
              <div class="img">
                <div ref="score" class="img_s"></div>
              </div>
            </div>
          </div>
          <div class="ticket_box">
            <p>累计票房</p>
            <div class="ticket">{{movie_data.ticketRank}}</div>
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
      movie_information: [], // 电影基本数据
      ticps: '查看电影详情'
    }
  },
  props: {
    movie_data: {
      type: Object,
      default: {}
    }
  },
  filters: {
    time_filter (time) {
      var len = time.split('')
      if (len.length > 10) {
        return time.substring(0,10) + '  '+ time.substring(10,12) +':00'
      }
      return time
    }
  },
  methods: {
    look_mvie () {
      this.ticps = this.ticps === '查看电影详情' ? '购票':'查看电影详情'
      this.$emit('look_intro')
    },
    computer_score () {
      var len = parseFloat(this.movie_data.score) / 10 * 100
      this.$refs.score.style.width = len + '%'
    }
  },
  mounted () {
    this.computer_score()
  }
}
</script>

<style lang="stylus" scoped>
  .header{
    position: relative
    height: 376px
    width: 100%
    background: rgb(15,153,213) url('../../../../static/images/cinemas_intro_bac.png')
    .content_box{
      position: relative
      top: 70px
      display: flex
      .img_box{
        position: relative
        width: 240px
        left: 240px
        height: 330px
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
        left: 270px
        color: white
        font-size: .3rem
        .name{
          font-size: .52rem
          font-weight: 700
        }
        .elname{
          font-size: 18px
          line-height: 1.3
          margin-bottom: .28rem
        }
        .cat{
          margin-bottom: .15rem
        }
        .address{
          margin-bottom: .15rem
        }
        .box{
          display: flex
          margin-top: 1rem
          div{
            width: 120px
            text-align: center
            height: 36px
            line-height: 36px
            margin-right: .2rem
            background: #756189
            border-radius: .04rem
            cursor: pointer
          }
          i{
            height: .32rem
            width: .32rem
            display: inline-block
            vertical-align: middle
            margin-right: .15rem
            margin-top: -.04rem
          }
          .score{
            i{
              background: url('../../../../static/images/score_bac.png')
            }
          }
          i{
            background: url('../../../../static/images/save.png')
          }
        }
        .information{
          width: 250px
          cursor: pointer
          height: 40px
          background: rgb(15,153,213)
          line-height: 40px
          text-align: center
          font-size: 16px
          margin-top: 10px
          border-radius: .04rem
        }
      }
      .evaluate{
        position: relative
        left: 370px
        color: white
        .score_box{
          p{
            margin: 0
          }
          .box{
            display: flex
            .score{
              color: #ffc600
              font-size: 30px
            }
            .img{
              width: 70px
              background: url('../../../../static/images/score_bac.png')
              background-repeat: repeat-x
              background-size: 14px
              background-origin: content-box
              padding: .28rem 0
              box-sizing: border-box
              margin-left: .3rem
              .img_s{
                height: 100%
                background: url('../../../../static/images/score_bac2.png')
                background-repeat: repeat-x
                background-size: 14px
              }
            }
          }
          margin-top: 175px
        }
        .ticket_box{
          .ticket{
            color: #fff
            font-size: 30px
          }
        }
      }
    }
  }
</style>
