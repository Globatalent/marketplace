<template>
  <gb-base-layout>
    <div>
      <el-button-group v-if="allow">
          <el-button type="primary" @click="create('athlete')">{{ $tc("message.Athlete",1) }}</el-button>
          <el-button type="primary" @click="create('club')">{{ $tc("message.Club") }}</el-button>
        </el-button-group>
    </div>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapGetters } from 'vuex'
import router from '@/router.js'


export default {
  name: 'CampaignForm',
  components: {
    'gb-base-layout': BaseLayout,
  },
  computed: {
    ...mapGetters({
      user: 'users/user',
      campaigns: 'campaigns/campaigns',
      campaign: 'campaigns/campaign',
      user: 'users/user'
    })
  },
  data() {
    return {
      allow: false,
      kind: null,
    }
  },
  created() {
    this.$store.dispatch('campaigns/list', {filters: {
      user: this.user.id,
      is_draft: 'True',
    }}).then( campaigns => {
      // There is no draft campaign
      if (campaigns.length === 0) {
        this.allow = true
      // There is a draft campaign, so we load it to edit
      } else {
        const campaign = campaigns[0]
        this.$store.commit('campaigns/campaign', campaign)
        router.push({ name: 'campaign.edit', params: {
          campaignId: campaign.id ,
          step: 'card',
        }})
      }
    })
  },
  methods: {
    create(kind) {
      this.$store.dispatch('campaigns/create', {kind: kind}).then( () => {
        this.kind = kind
      })
    }
  }
}
</script>

<style scoped>
</style>
