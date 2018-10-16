<template>
  <gb-base-layout>
    <el-col :xs="24">
        <el-form ref="form" label-position="top" class="text-left">
          <component :is="steps[$route.params.step]"></component>
        </el-form>
    </el-col>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'

import BaseLayout from '@/layout/BaseLayout.vue'
import CardCampaign from "../components/CardCampaign";
import Content from "../components/Content";
import Career from "../components/Career";
import Funding from "../components/Funding";


export default {
  name: 'CampaignForm',
  components: {
    'gb-base-layout': BaseLayout,
    'gb-card-campaign': CardCampaign,
    'gb-content': Content,
    'gb-career': Career,
    'gb-funding': Funding,
  },
    computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
    })
  },
  data() {
    return {
      steps: {
        card: 'gb-card-campaign',
        content: 'gb-content',
        career: 'gb-career',
        funding: 'gb-funding',
      }
    }
  },
  methods: {
  }
}
</script>

<style type="scss" scoped>
</style>
