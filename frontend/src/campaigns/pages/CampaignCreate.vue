<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.SoLetsBegin") }}</h3>
          <h4 class="beginBlock-subTitle">{{ $tc("message.Im") }}<span class="is-bold">{{ $tc("message.raising") }}</span>{{ $tc("message.forDots") }}</h4>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="30" type="flex">
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12" class="campaignProfile-col">
        <div class="campaignProfile text-center">
          <a @click="create('athlete')" class="campaignProfile-box"><img src="~@/assets/img/athlete-profile.png" alt="" class="campaignProfile-box-img"></a>
        </div>
      </el-col>
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12" class="campaignProfile-col">
        <div class="campaignProfile text-center">
          <a @click="create('club')" class="campaignProfile-box"><img src="~@/assets/img/organization-profile.png" alt="" class="campaignProfile-box-img"></a>
        </div>
      </el-col>
    </el-row>
    <el-row :gutter="30">
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12" class="campaignProfile-boxCol">
        <a @click="create('athlete')" class="campaignProfile-box-linkText">
          <div class="campaignProfile-box-linkText-title">{{ $tc("message.AnAthlete") }}</div>
        </a>
      </el-col>
      <el-col :xs="12" :sm="12" :md="12" :lg="12" :xl="12" class="campaignProfile-boxCol">
        <a @click="create('club')" class="campaignProfile-box-linkText">
          <div class="campaignProfile-box-linkText-title">{{ $tc("message.AClubOrganization") }}</div>
        </a>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center footerBottom">
        <div class="campaignProfile-box-linkText-subTitle">{{$t("message.AllSportsText")}}</div>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'

export default {
  name: 'CampaignForm',
  components: {
    'gb-base-layout': BaseLayout
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
      kind: null
    }
  },
  created() {
    this.$store
      .dispatch('campaigns/list', {
        filters: {
          user: this.user.id,
          is_draft: 'True'
        }
      })
      .then(campaigns => {
        // There is no draft campaign
        if (campaigns.length === 0) {
          this.allow = true
          // There is a draft campaign, so we load it to edit
        } else {
          const campaign = campaigns[0]
          this.$store.commit('campaigns/campaign', campaign)
          // Show modal to load draft or discard it
          this.$confirm(
            'There is a draft campaign, please select:',
            'Warning',
            {
              confirmButtonText: 'Continue',
              cancelButtonText: 'Discard draft',
              type: 'warning'
            }
          )
            .then(() => {
              router.push({
                name: 'campaign.edit',
                params: {
                  campaignId: campaign.id,
                  step: 'card'
                }
              })
            })
            .catch(() => {
              const payload = { id: campaign.id }
              this.$store.dispatch('campaigns/delete', payload).then(() => {
                this.$message({
                  type: 'info',
                  message: 'Draft deleted'
                })
              })
            })
        }
      })
  },
  methods: {
    draftConfirm() {},
    create(kind) {
      this.$store
        .dispatch('campaigns/create', { kind: kind })
        .then(campaign => {
          router.push({
            name: 'campaign.edit',
            params: {
              campaignId: campaign.id,
              step: 'card'
            }
          })
        })
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../scss/variables.scss';

.campaignProfile {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  max-width: 360px;
  max-height: 360px;
}

.campaignProfile-col {
  &:nth-child(1) {
    justify-content: flex-end;
    display: flex;
  }
}

.campaignProfile-box {
  display: block;
  background: $--green-light-background;
  border: 1px solid $--grey-border;
  border-radius: 2px;
  padding: 50px;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.campaignProfile-box-img {
  width: 100%;
  max-width: 233px;
  display: block;
  margin: 0 auto;
}

.campaignProfile-boxCol {
  display: flex;
  justify-content: flex-end;
  &:nth-child(2) {
    justify-content: flex-start;
  }
}

.campaignProfile-box-linkText {
  max-width: 360px;
  width: 100%;
  text-align: center;
  cursor: pointer;
}

.campaignProfile-box-linkText-title {
  font-size: 31px;
  margin: 20px 0;
  font-family: 'Aller Bold';
  color: $--black-subtitle;
}

.campaignProfile-box-linkText-subTitle {
  font-size: 14px;
  color: $--black-subtitle;
  font-family: 'Aller Regular';
}
</style>
