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
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce iaculis urna eu venenatis feugiat. Curabitur eu leo condimentum, posuere velit id, volutpat quam. Nulla vitae metus suscipit, elementum ligula eget, finibus mauris. Duis egestas tortor quis iaculis auctor. Suspendisse sit amet laoreet dui. Cras venenatis neque a venenatis euismod. Proin vitae sagittis elit. Vestibulum feugiat est non mauris accumsan ornare. Donec euismod in eros id ullamcorper. Aliquam at augue risus.</p>
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
