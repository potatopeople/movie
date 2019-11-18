import Vue from 'vue';

Vue.component('SliderPips', {
  template: `
    <div class="slider-pips">
      <input
        :disabled="disabled"
        class="slider-pips__range"
        :id="mola"
        :class="['slider-pips__range--' + (0 + 1) ]"
        type="range"
        :min="min"
        :max="max"
        ref="input"
        :step="step"
        v-model="lineL"
        @change="leave"
        @input="updateValue( $event, '0' )"
      />
      <div v-if="isRange" class="slider-pips__range-holder">
        <div class="slider-pips__range-selection" :style="{ width: rangeWidth, left: rangeLeft }">
        </div>
      </div>
    </div>
        `,
  data() {
    return {
      mola: '',
      disabled: false,
      vals: this.values,
      lineL: 0,
      reg: new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"),
    };
  },
  props: {
    email: { type: String, default: '' },
    values: { type: Array, default: [0] },
    min: { type: Number, default: 0 },
    max: { type: Number, default: 100 },
    step: { type: Number, default: 1 },
    labels: Boolean,
    range: Boolean,
    floats: Boolean,
  },
  watch: {
    lineL() {
      if (this.lineL === '20') {
        this.disabled = true;
        this.$emit('post_email', true);
      }
    },
    email() {
      this.verify_emails();
    },
  },
  computed: {
    isRange: function isRange() {
      return this.range;
    },
    pipCount: function pipCount() {
      return Math.round((this.fixedMax - this.fixedMin) / this.fixedStep + 1);
    },
    fixedStep: function fixedStep() {
      return this.fixValue(this.step);
    },
    fixedMin: function fixedMin() {
      return this.fixValue(this.min);
    },
    fixedMax: function fixedMax() {
      return this.fixValue(this.max);
    },
    rangeFraction: function rangeFraction() {
      return 100 / (this.fixedMax - this.fixedMin);
    },
    rangeWidth: {
      set() {
        this.lineL = 0;
        this.vals.splice(0, 1, 0);
      },
      get() {
        if (this.vals.length === 1) {
          return (this.vals[0] - this.fixedMin) * this.rangeFraction + "%";
        } else {
          return (this.vals[1] - this.vals[0]) * this.rangeFraction + "%";
        }
      }
    },
    rangeLeft: function rangeLeft() {
      if (this.vals.length === 1) {
        return "0%";
      } else {
        return -(this.fixedMin - this.vals[0]) * this.rangeFraction + "%";
      }
    }
  },
  methods: {
    verify_emails() {
      if (this.email === '') {
        this.disabled = true;
        this.verify('邮箱不能为空！', 'introTwo');
        return false;
      } else if (this.reg.test(this.email)) {
        this.disabled = false;
        this.verify('正确！', 'introFour');
        return true;
      } else {
        this.disabled = true;
        this.verify('邮箱格式错误！', 'introTwo');
        return false;
      }
    },
    verify(text, color) {
      this.$emit('verify_email', text, color);
    },
    fixValue: function fixValue(value) {
      return parseFloat(parseFloat(value).toFixed(2));
    },
    leave() {
      if (parseInt(this.lineL) < 20) {
        this.rangeWidth = '0%';
      }
    },
    post_email_error() {
      this.rangeWidth = '0%';
    },
    new_post_email() {
      setTimeout(() => {
        this.disabled = false
      }, 1500);
    },
    updateValue: function updateValue(ev, handle) {
      if (this.verify_emails()) {
        this.disabled = false;
        const pipValue = this.fixValue(ev.target.value);
        if (this.isRange && this.vals.length > 1) {
          if (handle === 0 && pipValue > this.vals[1]) {
            this.$set(this.vals, 0, this.vals[1]);
          } else if (handle === 1 && pipValue < this.vals[0]) {
            this.$set(this.vals, 1, this.vals[0]);
          } else {
            this.$set(this.vals, handle, pipValue);
          }
        } else {
          this.$set(this.vals, handle, pipValue);
        }
      } else {
        this.verify('请输入正确的邮箱！', 'introTwo');
        this.disabled = true;
      }
    },
    browserCatgory() { // 根据浏览器类型指定样式
      if (this.getBrowserInfo() === 'firefox') {
        this.mola = 'mola';
      } else {
        this.mola = '';
      }
    },
    getBrowserInfo () { // 判断浏览器类型
      let Sys = {};
      let ua = navigator.userAgent.toLowerCase();
      let re =/(msie|firefox|chrome|opera|version).*?([\d.]+)/;
      let m = ua.match(re);
      Sys.browser = m[1].replace(/version/, "'safari"); // 类型
      Sys.ver = m[2]; // 版本
      return Sys.browser;
    },
  },
  mounted() {
    this.bus.$on('post_email_error', this.post_email_error);
    this.bus.$on('new_post_email', this.new_post_email);
    if (this.email === '') {
      this.disabled = true;
    }
    this.browserCatgory();
  },
});