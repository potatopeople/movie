<template>
  <div class="register_box">
    <login-header/>
    <div class="register">
      <register-step
        :steps="steps" :stepsc="stepsc"
        :stepsT="stepsT" :stepscT="stepscT"
      />
    </div>
    <div class="intro">
      <router-view @steptwo="step_two" @step="step"></router-view>
    </div>
      <login-footer/>
  </div>
</template>

<script>
import LoginHeader from '../login/components/header'
import RegisterStep from './components/step'
import LoginFooter from '../login/components/footer'
export default {
  name: 'Register',
  data () {
    return {
      steps: '',
      stepsc: '',
      stepsT: '',
      stepscT: ''
    }
  },
  components: {
    LoginHeader,
    RegisterStep,
    LoginFooter
  },
  methods: {
    step (val,val2) {
      this.steps = val
      this.stepsc = val2
    },
    step_two (val,val2) {
      this.stepsT = val
      this.stepscT = val2
    }
  }
}
</script>

<style lang="stylus" scoped>
  .register_box{
    background: white
    min-height: 100vh
    margin: auto
    display: flex
    flex-direction: column
    .register{
      margin: 1.5rem auto
      margin-bottom: .8rem
      width: 600px
    }
    .intro{
      flex: 1
      margin: auto
      width: 600px
    }
  }
</style>
