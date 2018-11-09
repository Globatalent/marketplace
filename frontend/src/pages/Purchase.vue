<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}" :lg="{span: 8, offset: 8}">
        <h1 class="text-center">{{ $tc("message.PurchaseGBTTokens") }}</h1>
        <div id="bestrate-widget"></div>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'Purchase',
  components: {
    'gb-base-layout': BaseLayout
  },
  computed: {},
  data() {
    return {}
  },
  created() {},
  async mounted() {
    await this.addBestrateWidget()
    let BRWidget = window.BRWidget
    console.log(BRWidget)

    BRWidget.init(
      'bestrate-widget',
      '8cafc531570ace4e1618d2cf8383fb32',
      '0x74070fc80eB6845FdcFE812A77a3296a0e96132F'
    )
  },
  methods: {
    addBestrateWidget() {
      let bestratewidget = document.getElementById('bestrate-widget')
      if (!bestratewidget) {
        bestratewidget = document.createElement('script')
        bestratewidget.type = 'text/javascript'
        bestratewidget.src = `https://bestrate.org/brw_v2/widget.bestrate.js`
        bestratewidget.id = 'bestrate-widget'
        document.getElementsByTagName('head')[0].appendChild(bestratewidget)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../scss/variables.scss';
</style>
