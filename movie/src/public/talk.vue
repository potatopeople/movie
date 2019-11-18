<template functional>
  <section class="talk_box">
    <div class="talk" v-for="item of props.comment_data" :key="item.id">
      <div class="img">
        <img :src="item.img">
      </div>
      <div class="intro">
        <span class="name">{{item.name}}</span>
        <div class="container" v-html="item.main"></div>
        <div class="footer">
          <span class="time">{{item.time}}</span>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="stylus" scoped>
  #text_active{
    background: white
    border-color: #00b5e5
    position: relative
  }
  .talk_box{
    padding: 20px 1rem 0 1rem
    .talk{
      display: flex
      .img{
        img{
          width: 48px
          margin-top: 24px
          height: 48px
          border-radius: 50%
        }
      }
      .intro{
        font-family: Microsoft YaHei,Arial,Helvetica,sans-serif
        font-size: .27rem
        border-top: 1px solid #e5e9ef
        flex: 1
        margin-left: 37px
        padding: 22px 0 14px
        .name{
          font-weight: 600
          display: inline-block
          color: #6d757a
          margin: .1rem 0 .25rem 0
        }
        .name:hover{
          color: #00a1d6
          cursor: default
        }
        .container{
          color: #222
        }
        .footer{
          user-select: none
          margin: .2rem 0 .25rem 0
          color: #99a2aa
          .text{
            font-size: 12px
            font-style: normal
            margin-left: .1rem
            color: #99a2aa
          }
          .time{
          }
          span + span{
            margin-left: .5rem
          }
          .iconfont:hover{
            color: #00a1d6!important
            cursor: pointer
          }
          .Reply{
            cursor: pointer
            padding: .1rem .1rem
            border-radius: 5px
          }
          .Reply:hover{
            color: #00a1d6
            background: #e5e9ef
          }
        }
      }
    }
  }
</style>

