<template>
  <section class="list_box">
    <div class="list_option">
      <ul class="option">
        <li
          class="options"
          v-for="(item,pindex) of option"
          :key="item.id"
        >
          <div class="parent" @click="chose_option(item.text,pindex)">
            <span class="parents">
              <span class="iconfont font" v-html="item.catgory"></span>
              <span>{{item.text}}</span>
            </span>
            <span :class="['bottom','iconfont',item.tran]">&#xe6ec;</span>
          </div>
          <ul ref="children" :class="['children_option']">
            <li
              v-for="(child,cindex) of item.children"
              :class="['option',child.active]"
              :key="child.id"
              @click="chose_children(child.text,cindex,pindex,item.text,child.path)"
            >
              <div class="child">
                <span class="parents">{{child.text}}</span>
              </div>
            </li>
          </ul>
        </li>
      </ul>
    </div>
    <div class="main">
      <list-nav
        :curren_list="curren_list"
        :curren_chlid="curren_chlid"
      />
      <div class="list_main">
        <router-view />
      </div>
    </div>
  </section>
</template>

<script>
import ListNav from '../components/navigation'
export default {
  name: 'HomeList',
  components: {
    ListNav
  },
  data () {
    return {
      option: [
        {
          id:1,text:'用户信息',tran: '',catgory:'&#xe66b;',
          children:[
            {id:1,text:'基本信息',active:'',name:'用户信息',path:'/admin/home/user'}
          ]
        },
        {
          id:2,text:'电影管理',tran: '',catgory:'&#xe610;',
          children:[
            {id:1,text:'基本信息',active:'',name:'电影信息',path:'/admin/home/user'}
          ]
        },
        {
          id:3,text:'电影院管理',tran: '',catgory:'&#xe6dc;',
          children:[
            {id:1,text:'基本信息',active:'',name:'电影院信息',path:'/admin/home/user'}
          ]
        },
        {
          id:4,text:'评论管理',tran: '',catgory:'&#xe620;',
          children:[
            {id:1,text:'基本信息',active:'',name:'评论信息',path:'/admin/home/talk'}
          ]
        },
      ],
      curren_list: '',
      curren_chlid: ''
    }
  },
  computed: {
    querys () {
      return this.$route.query
    }
  },
  methods: {
    // 父选项点击事件
    chose_option (text,index) {
      this.curren_chlid = ''
      this.option.forEach(item => {
        item.children.forEach(citem => {
          citem.active = ''
        })
      })
      this.option.forEach((item, indexs) => {
        item.show = ''
        item.tran = ''
        this.$refs.children[indexs].style.height = '0px'
        if (parseInt(index) === indexs) {
          if (this.curren_list === text) {
            item.show = ''
            item.tran = ''
            this.curren_list = ''
            this.$refs.children[index].style.height = '0px'
          } else {
            item.show = 'active'
            item.tran = 'tran'
            this.$refs.children[index].style.height = this.option[index].children.length * '60' + 'px'
            this.curren_list = item.text
          }
        }
      })
    },
    // 子选项点击事件
    chose_children (text,cindex,pindex,ptext,path) {
      this.option.forEach((pitem, pindexs) => {
        pitem.children.forEach((citem, cindexs) => {
          if ((pindexs === parseInt(pindex)) && (parseInt(cindex) === cindexs)) {
            if (!(this.curren_chlid === text)){
              citem.active = 'active'
              this.curren_chlid = text
              this.$router.push({
                path: path,
                query: {
                  catgory: citem.name,
                  pindex,
                  cindex,
                  text,
                  ptext
                }
              })
            }
          } else {
            citem.active = ''
          }  
        })
      })
    },
    redict_dom () {
      this.chose_option(this.querys.ptext,this.querys.pindex)
      this.chose_children(
        this.querys.text,this.querys.cindex,
        this.querys.pindex,this.querys.ptext
      )
    }
  },
  created () {
    this.$nextTick(() => {
      this.redict_dom()
    })
  }
}
</script>

<style lang="stylus" scoped>
  .list_box{
    flex: 10
    display: flex
    .list_option{
      border-right: 1px solid rgb(235,235,235)
      flex: 1
      min-width: 239px
      background: rgb(235,235,235)
      .option{
        list-style: none
        padding: 0
        margin: 0
        font-size: .35rem
        .options{
          cursor: pointer
          display: flex
          color: rgb(80,80,80)
          flex-direction: column
          .parent{
            flex: 1
            display: flex
            justify-content: space-between
            .parents{
              display: flex
              align-items: center
              height: 1.3rem
              margin-left: .7rem
            }
            .iconfont{
              display: flex
              align-items: center
              margin-right: .7rem
              color: rgb(150,150,150)
              transition: transform .5s
             }
             .font{
               font-size: .4rem
               color: rgb(15,153,213)
             }
             .tran{
               transform: rotate(90deg)
             }
          }
          .parent:hover{
            background: rgb(220,220,220)
          }
          .children_option{
            padding: 0
            margin: 0
            display: flex
            color: rgb(80,80,80)
            background: white
            height: 0
            flex-direction: column
            transition: height .5s
            overflow: hidden
            .option{
              display: flex
              flex-directin: column
              justify-content: center
              padding-top: .4rem
              padding-bottom: .4rem
              cursor: pointer
            }
            .option:hover{
              background: rgb(245,245,245)
            }
            .active{
              color: rgb(15,153,213)!important
            }
          }
        }
      }
    }
    .main{
      flex: 7
      display: flex
      flex-direction: column
      padding: 0 1rem 0 .5rem
      .list_main{
        flex: 10
      }
    }
  }
</style>
