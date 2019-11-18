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
        class="main"
        v-for="item of user_intro"
        :key="item.id"
      >
        <td :key="index" v-for="(citem,index) of intro_attribute">
          {{item[citem]}}
        </td>
      </tr>
    </table>
  </section>
</template>

<script>
export default {
  name: 'TableData',
  props: {
    user_intro: {
      type: Array,
      default: []
    }
  },
  data () {
    return {
      title: [
        {name:'编号'},
        {name:'用户名'},
        {name:'姓名'},
        {name:'性别'},
        {name:'头像'}
      ]
    }
  },
  computed: {
    intro_attribute () {
      let anchor = []
      for (let attribute in this.user_intro[0]) {
        if (attribute !== 'avatar') {
          anchor.push(attribute)
        }
      }
      anchor.push('avatar')
      return anchor
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
      .active{
        background: rgb(15,153,213)
        border: 1px solid rgb(15,153,213)
      }
      tr{
        position: relative
      }
      td,th{
        text-align: center
        vertical-align: middle
        white-space: nowrap
        padding: .1rem .2rem
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
  }
</style>
