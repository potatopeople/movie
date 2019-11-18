<template>
  <section class="look_mask" @click.stop="close">
    <div class="input_box">
        <p class="id">
            编号<span>： </span><span class="sp">{{main.id}}</span>
        </p>
        <p class="movie">
            电影<span>： </span><span class="sp">《{{main.movie}}》</span>
        </p>
        <p class="username">用户名<span class=" ma">：</span><span class="sp">{{main.username}}</span>
        </p>
        <p>
            用户昵称<span class="mao">： </span><span class="sp">{{main.name}}</span>
        </p>
        <div class="main">
            <p>评论内容</p>
            <span class="po">： </span>
            <p class="box" v-html="main.main"></p>
        </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'LookMask',
  props: {
    main: {
      type: Object,
      default: {}
    }
  },
  computed: {
    expression_data () {
      var i = 1,
          img_title= ['微笑','嫌弃','喜欢','呆','大哭','害羞','无语','委屈','尴尬','生气','奸笑','大笑','惊讶','囧','捂脸','灵魂出窍','吐','抠鼻','惊喜','傲娇','疼','阴险','画风突变','妙啊','doge','滑稽','吃瓜','笑哭','支持','吓','点赞'],
          img_obj = []
      for (i;i <= 31; i++) {
        img_obj.push(
          {
            id:i,url:'../../../static/images/expression_'+i+'.webp',
            title: img_title[i - 1]
          }
        )
      }
      return img_obj
    }
  },
  filters: {
    main_filter (main) {
      text = text.replace(/\[.*?\]/g, function () {
        return this.filter_expression(arguments[0])
      }.bind(this))
      text = text.replace(/\n/g,'<br />')
      text = text.replace(/<[a-zA-Z]>/g,' ')
      text = text.replace(/<\/[a-zA-Z]>/g,' ')
      return text
    }
  },
  methods: {
    close () {
      this.$emit('close_mask')
    },
    filter_expression (text) { // 匹配表情
      let reg = text.replace(/[\[\]]/g, '')
      for (var item of this.expression_data) {
        if (reg === item.title) {
          return `<img style="display:inline-block;height:20px;width:20px" src=${item.url} />`
        }
      }
      return text
    }
  }
}
</script>

<style lang="stylus" scoped>
  .look_mask{
    position: fixed
    left: 0
    right: 0
    bottom: 0
    top: 0
    background: rgba(150,150,150,.7)
    display: flex
    .input_box{
      padding: .5rem .5rem .3rem .8rem
      width: 600px
      min-height: 400px
      background: white
      color: rgb(0,0,0)
      margin: auto
      border-radius: 5px
      box-shadow: 0 0 .1rem rgb(150,150,150)
      .sp{
        margin-left: 0rem
      }
      .ma{
        margin-left: .55rem
      }
      .mao{
        margin-left: .66rem
      }
      p{
        font-size: .35rem
        margin-bottom: .2rem
        span{
          letter-spacing: 1px
        }
      }
      .id{
        letter-spacing: .68rem
      }
      .movie{
        letter-spacing: .68rem
      }
      .username{
        letter-spacing: .16rem
      }
      .po{
        position: absolute
        left: 2.08rem
        top: 0
      }
      .main{
        font-size: .35rem
        margin-bottom: .2rem
        position: relative
        display: flex
        .box{
          margin-left: 1.1rem
          color: rgb(100,100,100)
        }
      }
    }
  }
</style>
