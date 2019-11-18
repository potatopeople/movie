<template>
  <section class="page_box">
    <div id="pageBox" v-show="this.$store.state.movieList.movie_list.page > 1">
      <div class="pageBtnStyle item currentPage">1</div>
      <div class="pageBtnStyle item">2</div>
      <div class="pageBtnStyle item">3</div>
      <div class="pageBtnStyle item">4</div>
      <div class="pageBtnStyle item">5</div>
      <div class="pageBtnStyle item">6</div>
      <div class="pageBtnStyle item">7</div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'MoviePage',
  data () {
    return {
      option: {
        currentPage: 1,
        //count: 7,
        showPageBtnCount: 6,//该项暂时无法修改
        bLast: false,
        bFirst: true
      },
      catgorys: '',
      order: ''
    }
  },
  watch: {
    page () {
      this.option.count = this.page
      this.updateLastPage()
      this.addEllipsis()
    }
  },
  computed: {
    oItem () {
      return document.getElementsByClassName("item")
    },
    oBox () {
      return document.getElementById('pageBox')
    },
    catgory () {
      return this.$store.state.movieList.movie_list.catgory
    },
    page () {
      return this.$store.state.movieList.movie_list.pageSum
    }
  },
  methods: {
    addEllipsis () {
      let oMoreLeft = document.getElementsByClassName("left")
      let oMoreRight = document.getElementsByClassName("right")
      if (this.option.currentPage < this.page - Math.ceil(this.option.showPageBtnCount / 2) - 1) {
        oMoreRight.length > 0 ? "" : this.oItem[this.option.showPageBtnCount].insertAdjacentHTML('beforebegin', `<div class="pageBtnStyle more right" style="transform: rotate(180deg);font-size:.4rem">.....</div>`)
      } else {
        oMoreRight[0] ? this.oBox.removeChild(oMoreRight[0]) : ''
      }
      if (this.option.currentPage >= this.option.showPageBtnCount - 1) {
        oMoreLeft.length > 0 ? '' : this.oItem[0].insertAdjacentHTML('afterend', `<div class="pageBtnStyle more left" style="transform: rotate(180deg);font-size:.4rem">.....</div>`)

      } else {
        oMoreLeft[0] ? this.oBox.removeChild(oMoreLeft[0]) : ''
      }
    },
    updateLastPage() {
      this.oItem[this.option.showPageBtnCount].innerHTML = this.page
    },
    updatePage(target) {
      let oAdd = document.getElementsByClassName("add")
      // 忘了 querySelectorAll的dom不是实时的
      if (this.option.currentPage > (this.page - (this.option.showPageBtnCount - 1))
        || this.option.currentPage < (this.option.showPageBtnCount - 1)) {
        // 删除增加的
        for (let item of this.oItem) {
          item.className = 'pageBtnStyle item'
        }
        if (this.option.currentPage > this.page - this.option.showPageBtnCount) {
          if (this.option.currentPage <= this.page - Math.ceil(this.option.showPageBtnCount)) {
          }
          // 最后几页
          if (!this.option.bLast) {
            this.option.bLast = true;
            for (let ind = 1; ind < this.option.showPageBtnCount; ind++) {
              this.oItem[ind].innerHTML = parseInt(this.page) - this.option.showPageBtnCount + ind
            }
          } else {
          }
          for (let item of this.oItem) {
            if (item.innerHTML == this.option.currentPage) {
              item.className = "pageBtnStyle item currentPage"
              break
            }
          }
        } else if (this.option.currentPage < (this.option.showPageBtnCount - 1)) {
          if (!this.option.bFirst) {
            this.option.bFirst = true;
            for (let ind = 1; ind < this.option.showPageBtnCount; ind++) {
              this.oItem[ind].innerHTML = 1 + ind
            }
          } else { }
          for (let item of this.oItem) {
            if (item.innerHTML == this.option.currentPage) {
              item.className = "pageBtnStyle item currentPage"
              break
            }
          }
        } else { }
      } else {
        this.option.bLast = false;
        this.option.bFirst = false;
        for (let ind = 1; ind < this.option.showPageBtnCount; ind++) {
          this.oItem[ind].innerHTML = parseInt(this.option.currentPage - 3) + ind
        }
        for (let item of this.oItem) {
          item.className = 'pageBtnStyle item'
        }
        this.oItem[3].className = 'pageBtnStyle item currentPage'
      }
    },
    addClick () {
      this.oBox.addEventListener('click',(e) => {
        let target = event.target || e.target
        if (target.className.indexOf("item") > -1) {
          if (this.option.currentPage === target.innerText) {
            return 0
          } else {
            this.option.currentPage = target.innerText || '1';
            this.http(0,this.catgory,this.option.currentPage, 30)
            this.addEllipsis()
            this.updatePage(target)
            window.scroll(0,0)
          }
        }
      }, false)
    },
    async http (orderBy='0',type='release', page=1, size=30) {
      let data = {
        orderBy:this.order || '0', // 排序类型
        showType: type, // 电影数据类型
        page, // 页数
        pageSize: size, // 每页数据量
        catgory: this.catgorys.catgorys || 'all',
        years: this.catgorys.years || 'all',
        region: this.catgorys.region || 'all'
      }
      try {
        let response = await this.$http.postHttp('api/movie', data)
        if (response.data.code === 200) {
          this.$store.dispatch('get_movie_list', [response.data.data,this.catgory])
        }
      } catch (error) {
        console.log('电影数据请求出错：', error)
      }
    },
    redict () {
      this.option.currentPage = '1'
      this.addEllipsis()
      this.updatePage(document.getElementsByClassName('pageBtnStyle')[0])
    }
  },
  mounted () {
    this.updateLastPage()
    this.addEllipsis()
    this.addClick()
    this.bus.$on('movie_catgory', (value) => {
      this.catgorys = value
      this.redict()
    })
    this.bus.$on('movie_orderby', (value) => {
      this.order = value
      this.redict()
    })
    this.bus.$on('catgory', this.redict)
  }
}
</script>

<style lang="stylus" scoped>
  .page_box{
    margin-top: .7rem
    #pageBox{
      margin: auto
      width: 440px
      display: flex
      .pageBtnStyle{
        font-size: .35rem
        margin: auto
        cursor: pointer
        padding: 3px 12px
        border: 1px solid rgb(150,150,150)
        background: white
        color: black
        text-align: center
      }
      .currentPage{
        background: rgb(15,153,213)
        color: white
      }
    } 
  }
</style>

