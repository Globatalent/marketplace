<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24">
        <div class="beginBlock text-center">
          <h4 class="beginBlock-subTitle">{{ $tc("message.About") }}</h4>
        </div>
      </el-col>
    </el-row>

    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}">
      <p>Globatalent is a global marketplace that allows people all over the world to fund and trade in their favorite athletes, clubs and sports idols.</p>
      <p>We give everyone the chance to have a stake in athletes and idols, and even bet on future talent. We have made it our goal to bring the best sports idols in the world to this platform.</p>
      <p>We’ve created an ecosystem based on blockchain technology that allows people to seamlessly and transparently trade and exchange tokens. Our revolutionary product is available and it is backed by some of the greatest sporting talent in the world.</p>
      <p><b>Athletes</b> can get funds to focus on developing their career and give back to supporters part of their revenues. </p>
      <p><b>Clubs and sports institutions</b> can obtain ﬁnance in exchange to a percentage of their ticketing, sponsorship, TV rights and more, in a transparent way. We also provide tools to notably increase fan engagement.</p>
      </el-col>
    </el-row>

    <div class="campaignList-startBlock">
      <div class="campaignList-startBlock-container">
        <div class="campaignList-startBlock-sentence">
          <router-link :to="{ name: 'campaign.create'}" class="is-main-color">
            <h4 class="campaignList-startBlock-sentence1" v-html="$t('message.StartCampaignNow')"></h4>
          </router-link>
          <h5 class="campaignList-startBlock-sentence2">{{$t('message.AlsoGift')}}</h5>
        </div>
        <!-- <el-button type="primary" class="startFreeButton" size="big">{{$tc('message.StartFreeTrial')}}</el-button> -->
      </div>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'AboutPage',
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
</style>
