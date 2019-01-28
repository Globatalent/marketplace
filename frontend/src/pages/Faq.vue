<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.WeBringTheTalent") }}</h3>
          <h3 class="beginBlock-subTitle">Faq</h3>
        </div>
      </el-col>
    </el-row>
<el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
        <!-- <div class="beginBlock text-center"> -->
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.whatAreTheBasicsTitle')}}</h4>
          <div v-html="$t('message.whatAreTheBasics')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.whatIsGlobatalentTitle')}}</h4>
          <div v-html="$t('message.whatIsGlobatalent')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.howDoesGlobatalentPlatformWorkTitle')}}</h4>
          <div v-html="$t('message.howDoesGlobatalentPlatformWork')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.howDoesGlobatalentExchangeWorkTitle')}}</h4>
          <div v-html="$t('message.howDoesGlobatalentExchangeWork')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.howToContributeToACampaignAndBuyTokensTitle')}}</h4>
          <div v-html="$t('message.howToContributeToACampaignAndBuyTokens')"></div>
          <br>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.canYouBuyWithCreditCardTitle')}}</h4>
          <div v-html="$t('message.canYouBuyWithCreditCard')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.canITradeTokensTitle')}}</h4>
          <div v-html="$t('message.canITradeTokens')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.whoCanStartTitle')}}</h4>
          <div v-html="$t('message.whoCanStart')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.canITradeTokensTitle')}}</h4>
          <div v-html="$t('message.canITradeTokens')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.whyDoPeopleSupportCampaignsTitle')}}</h4>
          <div v-html="$t('message.whyDoPeopleSupportCampaigns')"></div>
          <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.howDoIAskTitle')}}</h4>
          <div v-html="$t('message.howDoIAsk')"></div>
           <h4 class="campaign-name" style="color:	#0375B2">{{$tc('message.campaignFailTitle')}}</h4>
          <div v-html="$t('message.campaignFail')"></div>

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
