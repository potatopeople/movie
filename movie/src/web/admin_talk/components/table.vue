<template>
  <section class="table_box">
    <table class="box">
      <tr class="title">
        <th
          class="title tfd"
          v-for="(item, index) of title"
          :key="index"
        >
          {{item.name}}
        </th>
      </tr>
      <tr
        v-for="item of user_talk"
        :class="['main',item.active]"
        :key="item.id"
      >
        <td :key="index" v-for="(citem,index) of intro_attribute">
          {{item[citem]}}
        </td>
      </tr>
    </table>
    <div class="edit_box">
      <div @mouseout="point_tr" @mouseover="point_tr(item.id)" class="edit" v-for="(item,index) of user_talk" :key="item.id">
        <span @click="look_main(item)">查看</span>
        <span @click="drop_talk(item.id,index)">删除</span>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'TableData',
  props: {
    user_talk: {
      type: Array,
      default: []
    }
  },
  data () {
    return {
      title: [
        {name:'编号'},
        {name:'电影'},
        {name:'昵称'},
        {name:'用户名'},
        {name:'内容'}
      ]
    }
  },
  computed: {
    intro_attribute () {
      let anchor = []
      for (let attribute in this.user_talk[0]) {
        if (attribute !== 'main' && attribute !== 'active') {
          anchor.push(attribute)
        }
      }
      anchor.push('main')
      return anchor
    }
  },
  methods: {
    look_main (item) {
      this.$emit('look_main',item)
    },
    drop_talk (id,index) {
      this.$emit('drop_talk',id,index)
      console.log(id)
    },
    point_tr (id='0') {
      this.$emit('pointr',id)
    }
  }
}
</script>

<style lang="stylus" scoped>
  .table_box{
    margin-top: .3rem
    position: relative
    font-size: .3rem
    color: rgb(150,150,150)
    width: calc(100vw - 315px)
    min-width: calc(1090px - 315px)
    overflow-x: auto    
    .box{
      border-collapse: collapse
		  border: none
      width: 100%
      .title{
        background: rgb(15,183,213)
        color: white
        th:nth-child(1){
          font-weight:normal
        }
      }
      .input{
        position: relative
      }
      tr{
        position: relative
      }
      td,th{
        text-align: center
        vertical-align: middle
        white-space: nowrap
        padding: .1rem .2rem
        max-width: 200px
        overflow: hidden
      }
      .active{
        background: rgb(240,255,247)!important
      }
      th{
        border-top: 1px solid rgb(220,220,220)
        border-left: 1px solid rgb(220,220,220)
        border-bottom: 1px solid rgb(220,220,220)
      }
      td{
        border-left: 1px solid rgb(220,220,220)
        border-bottom: 1px solid rgb(220,220,220)
      }
      td:last-child,th:last-child{
        border-right: 1px solid rgb(220,220,220)
      }
      tr + tr:nth-child(odd){
        background: rgb(250,250,250)
      }
      tr + tr:hover{
        background: rgb(240,255,247)
        cursor: default
      }
    }
    .edit_box{
      position: fixed
      right: 51px
      background: white
      display: flex
      flex-direction: column
      top: 207px
      border-left: 1px solid rgb(220,220,220)
      border-right: 1px solid rgb(220,220,220)
      border-bottom: 1px solid rgb(220,220,220)
      .edit{
        height: 33px
        display: flex
        align-items: center
        justify-content: center
        padding: 0 .1rem
        span{
          color: rgb(255,255,255)
          font-size: 12px
          user-select: none
          padding: .06rem .2rem
          cursor: pointer
          margin: 0 .2rem
          display: inline-block
          background: rgb(64,159,255) linear-gradient(
                        rgba(255,255,255,.3),
                        transparent
          )
        }
        span:active{
          background:rgb(64,159,255)
        }
        span + span {
          background: red linear-gradient(
                        rgba(255,255,255,.3),
                        transparent
          )
        }
        span + span:active{
          background:red
        }
      }
    }
  }
</style>
