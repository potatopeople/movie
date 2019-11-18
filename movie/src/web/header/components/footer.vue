<template>
  <section class="footer">
    <p class="link">
      <span>关于 :</span>
      <span class="alink">关于我们</span>
      <span> &nbsp;|&nbsp; </span>
      <span class="alink">管理团队</span>
      <span> &nbsp;|&nbsp; </span>
      <span class="alink">投资者关系</span>
      <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;友情链接 :</span>
      <span class="alink">美团网</span>
      <span> &nbsp;|&nbsp; </span>
      <span class="alink">格瓦拉</span>
      <span> &nbsp;|&nbsp; </span>
      <span class="alink">美团下载</span>
      <span> &nbsp;|&nbsp; </span>
      <span class="alink">欢喜首映</span>
    </p>
    <p class="link">
      商务合作邮箱：v@tudou.com 客服电话：10105335 违法和不良信息举报电话：4006018900
    </p>
    <p class="link">
      用户投诉邮箱：tousujubao@meituan.com 舞弊线索举报邮箱：wubijubao@tudou.com
    </p>
    <p class="link">
      ©2016 土豆电影 maoyan.com 京ICP证160733号 京ICP备16022489号-1 京公网安备 11010102003232号 网络文化经营许可证 电子公告服务规则
    </p>
  </section>
</template>

<script>
export default {
  name: 'MovieFooter'
}
</script>

<style lang="stylus" scoped>
  .footer{
    .link{
      font-size: .28rem
      color: rgb(102,102,102)
      text-align: center
      .alink{
        color: rgb(239,66,56)
      }
      .alink:hover{
        text-decoration: underline
        cursor: pointer
      }
    }
  }
</style>
