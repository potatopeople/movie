import Vue from 'vue';

Vue.component('DataMask',{
    props: {
        tf: {
            type: Boolean,
            default: true
        }
    },
    template: `
        <section style="position:fixed;left:0;right:0;bottom:0;top:0;z-index:999;background:white url('../../static/images/loading.gif') no-repeat;background-position: center">
        </section>
    `
})