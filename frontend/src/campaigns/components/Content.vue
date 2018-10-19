<template>
  <el-col :xs="24" class="formSteps-container">
    <div class="infoTag">Draft Campaign</div>
    <el-breadcrumb separator=">">
      <el-breadcrumb-item :to="{ path: '/campaigns' }">Campaign</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/campaigns/create">Content</a></el-breadcrumb-item>
    </el-breadcrumb>
    <div class="formSteps-actions">
      <el-button type="danger" class="" @click.prevent="onDiscard()">{{ $tc("message.DiscardCampaign") }}</el-button>
      <el-button type="secondary" class="" @click.prevent="onSaveAndContinue()">{{ $tc("message.ReviewLaunch") }}</el-button>
    </div>
    <div class="formSteps">
      <h2 class="formSteps-title">{{ $tc("message.Content") }}</h2>
      <p class="formSteps-text">Make a good first impression: introduce your campaign objectives and entice people to learn more. This basic information will represent your campaign on your campaign page, on your campaign card, and in searches.</p>
      <el-form-item :label="$tc('message.SocialMedia')">
        <div v-for="(link, index) in form.links" :key="index" class="socialLinks">
          <span :class="link.network+' socialLinks-icon'"></span>
          <el-input type="text" v-model="link.url" placeholder="http://"></el-input>
        </div>
      </el-form-item>
      <el-form-item required :label="$tc('message.BasicInformation')">
        <el-input type="text" :placeholder="$tc('message.Height')" v-model="form.height"></el-input>
        <el-input type="text" :placeholder="$tc('message.Weight')" v-model="form.weight"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.ActualClub')" v-if="form.kind==='athlete'">
        <el-input type="text" v-model="form.club"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.ActualCoach')" v-if="form.kind==='athlete'">
        <el-input type="text" v-model="form.coach"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.PitchVideoorImage')">
        <p class="formSteps-inputText">Add a video or image to appear on the top of your campaign page. Campaigns with videos
          raise 2000% more then campaigns without videos. Keep your video 2-3 minutes. </p>
        <el-tabs v-model="activePitch" @tab-click="handleClick">
          <el-tab-pane label="Add Video" name="video">
            <div class="tabTitle">Video URL</div>
            <p class="formSteps-inputText">Enter a YouTube or Vimeo URL to appear at the top of your campaign pages.</p>
            <el-input type="text" v-model="form.pitchUrl" placeholder="Video url"></el-input>
          </el-tab-pane>
          <el-tab-pane label="Add Image" name="image">
            <div class="tabTitle">Add Image</div>
            <el-upload drag thumbnail-mode :limit="1" :action="options.action" :headers="options.headers" :name="options.name" :http-request="options.httpRequest" :file-list="!!form.pitchImage ? [{name: form.pitchImage.substring(form.pitchImage.lastIndexOf('/') + 1), url: form.pitchImage}] : []">
              <i class="el-icon-upload" style="padding: 0"></i>
              <div class="el-upload__text">Upload Image</div>
            </el-upload>
          </el-tab-pane>
        </el-tabs>
      </el-form-item>
      <el-form-item>
        <div class="formSteps-lineButton"></div>
        <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinue") }}</el-button>
      </el-form-item>
    </div>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'
import ajax from '@/base/helpers/ajax'

export default {
  name: 'Content',
  components: {},
  data() {
    return {
      // Form
      form: {
        links: [],
        height: null,
        weight: null,
        club: null,
        coach: null,
        pitchUrl: null,
        pitchImage: null
      },
      // Card Image
      options: {
        name: 'pitch_image',
        headers: {
          Authorization: this.$store.getters['auth/header']
        },
        httpRequest: ajax,
        action: ''
      },
      activePitch: 'video'
    }
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
      user: 'users/user'
    })
  },
  created() {
    this.$store
      .dispatch('campaigns/fetch', this.$route.params.campaignId)
      .then(() => {
        if (!!this.campaign && !!this.campaign.id) {
          this.options.action = `${
            Vue.axios.defaults.baseURL
          }/api/v1/campaigns/${this.campaign.id}/`
          this.form = { ...this.campaign }
          this.form.links = this.initialSocialLinks(this.campaign)
        }
      }).catch(()=> router.push({name: 'campaign.create'}))
  },
  methods: {
    handleClick(tab, event) {
      // console.log(tab, event)
    },
    initialSocialLinks(campaign) {
      const networks = [
        'facebook',
        'instagram',
        'twitter',
        'youtube',
        'linkedin',
        'whatsapp',
        'flickr'
      ]
      const socialLinks = networks.map(network => {
        const links = campaign.links.filter(item => item.network == network)
        if (links.length > 0) {
          return links[0]
        }
        return { id: null, campaign: campaign.id, network: network, url: null }
      })
      return socialLinks
    },
    onDiscard() {
      const payload = { id: this.campaign.id }
      this.$store.dispatch('campaigns/delete', payload).then( () => {
        router.push({name: 'campaign.create'})
      })
    },
    onSaveAndContinue() {
      const payload = {
        id: this.campaign.id,
        links: this.form.links,
        height: this.form.height,
        weight: this.form.weight,
        club: this.form.club,
        coach: this.form.coach,
        pitchUrl: this.form.pitchUrl,
        pitchImage: this.form.pitchImage
      }
      this.$store.dispatch('campaigns/update', payload).then(() => {
        router.push({
          name: 'campaign.edit',
          params: {
            campaignId: this.campaign.id,
            step: 'career'
          }
        })
      })
    }
  }
}
</script>

<style type="scss" scoped>
</style>
