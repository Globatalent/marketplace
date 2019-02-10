<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.WeBringTheTalent") }}</h3>
          <h3 class="beginBlock-subTitle">Page not found</h3>
        </div>
      </el-col>
    </el-row>
<el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'not-found',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {}
  },

  created() {},
  methods: {}
}
</script>

<style lang="scss" scoped>
  @import '../scss/variables.scss';

  .beginBlock {
    background: url('../assets/img/background-list-title.png');
    background-repeat: no-repeat;
    background-position: center;
  }

  .campaignList-startBlock {
    margin: 30px auto;
    border-top: 1px solid $--grey-detailCampaign-border;
    padding-top: 40px;
    display: block;
    width: 100%;
    max-width: 895px;
    font-size: 0px;
  }

  .campaignList-startBlock-container {
    max-width: 585px;
    display: block;
    margin: 0 auto;
  }

  .campaignList-startBlock-sentence {
    display: inline-block;
    vertical-align: top;
    text-align: right;
    padding-right: 20px;
    padding-right: 0px;
    width: 70%;
    width: 100%;
    text-align: center;
  }

  .campaignList-startBlock-sentence1 {
    font-weight: normal;
    font-family: 'Aller';
    font-size: 36px;
    line-height: 36px;
    margin: 0;
  }

  .campaignList-startBlock-sentence2 {
    font-size: 14px;
  }

  strong {
    font-weight: bold;
  }
</style>

