<template>
  <gb-aside-layout>
    <el-col :xs="24">
        <el-form ref="form" label-position="top" class="text-left">
          <component :is="steps[$route.params.step]"></component>
        </el-form>
    </el-col>
  </gb-aside-layout>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'

import AsideLayout from '@/layout/AsideLayout.vue'
import CardCampaign from "../components/CardCampaign";
import Content from "../components/Content";
import CareerClub from "../components/CareerClub";
import Funding from "../components/Funding";


export default {
  name: 'CampaignForm',
  components: {
    'gb-aside-layout': AsideLayout,
    'gb-card-campaign': CardCampaign,
    'gb-content': Content,
    'gb-career-club': CareerClub,
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
        career: 'gb-career-club',
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
