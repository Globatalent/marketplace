<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.WeBringTheTalent") }}</h3>
          <h4 class="beginBlock-subTitle">News</h4>
        </div>
      </el-col>
    </el-row>

    <el-row>
      <el-col :xs="24" :sm="{span: 12, offset: 6}" :lg="{span: 8, offset: 8}">
        <p>Coming soon!</p>
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
  name: 'NewsPage',
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
