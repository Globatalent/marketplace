<template>
  <gb-base-layout>
<el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">

          <h1>Globatalent is in scheduled manteinance mode. We are working hard to improve our site, and we will be back soon!!</h1>

        <!-- </div> -->
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'FaqPage',
  components: {
    'gb-base-layout': BaseLayout
  }
}
</script>

<style lang="scss" scoped>
  @import '../scss/variables.scss';

  .beginBlock {
    background: url('../assets/img/background-list-title.png');
    background-repeat: no-repeat;
    background-position: center;
  }

</style>
