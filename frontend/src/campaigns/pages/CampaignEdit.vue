<template>
  <gb-aside-layout>
    <el-col :xs="24" v-loading.fullscreen="loading">
      <el-form ref="form" label-position="top" class="text-left">
        <component :is="steps[$route.params.step]" @discard="isDiscardDialogVisible = true"></component>
      </el-form>
    </el-col>
    <el-dialog
      :title="$tc('message.DiscardCampaign')"
      :visible.sync="isDiscardDialogVisible">
      <span>{{$tc('message.ConfirmDiscardCampaign')}}</span>
      <span slot="footer" class="dialog-footer">
    <el-button @click="isDiscardDialogVisible = false">{{$tc('message.Cancel')}}</el-button>
    <el-button type="primary" @click="onDiscard">Confirm</el-button>
  </span>
    </el-dialog>
  </gb-aside-layout>
</template>

<script>
  import Vue from 'vue'
  import { mapGetters } from 'vuex'

  import AsideLayout from '@/layout/AsideLayout.vue'
  import CardCampaign from '../components/CardCampaign'
  import Content from '../components/Content'
  import CareerClub from '../components/CareerClub'
  import Funding from '../components/Funding'

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
    data () {
      return {
        steps: {
          card: 'gb-card-campaign',
          content: 'gb-content',
          career: 'gb-career-club',
          funding: 'gb-funding',
        },
        isDiscardDialogVisible: false,
        loading: false
      }
    },
    methods: {
      onDiscard () {
        this.loading = true
        const payload = {id: this.campaign.id}
        this.$store.dispatch('campaigns/delete', payload).then(() => {
          this.loading = false
          this.$router.push({name: 'campaign.create'})
        })
      },
    }
  }
</script>

<style type="scss" scoped>
</style>
