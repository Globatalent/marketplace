<template>
  <gb-base-layout>
<el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
        <!-- <div class="beginBlock text-center"> -->
          <!-- <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.whatAreTheBasicsTitle')}}</h4>
          <div v-html="$t('message.whatAreTheBasics')"></div> -->
          <h1>Globatalent is in scheduled manteinance mode. We are working hard to improve our site, and we will be back soon!!</h1>

        <!-- </div> -->
      </el-col>
    </el-row>

    <div class="campaignList-startBlock">
      <div class="campaignList-startBlock-container">
        <div class="campaignList-startBlock-sentence">
          <router-link :to="{ name: 'campaign.create'}" class="is-main-color">
            <el-button type="primary" class="startFreeButton" size="big" v-html="$tc('message.StartCampaignNow')"></el-button>
          </router-link>
        </div>
        <!-- <el-button type="primary" class="startFreeButton" size="big">{{$tc('message.StartFreeTrial')}}</el-button> -->
      </div>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'FaqPage',
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

  .startFreeButton {
    display: inline-block;
    vertical-align: top;
    width: auto;
    font-size: 14px;
    font-family: 'Aller';
    font-weight: bold;
    position: relative;
    top: 6px;
  }
</style>
