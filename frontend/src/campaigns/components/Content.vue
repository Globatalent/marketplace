<template>
  <el-col :xs="24">
    <h2 class="form-lined-title text-center">{{ $tc("message.Content") }}</h2>
    <div class="form-lined">
        <el-form-item :label="$tc('message.SocialMedia')">
          <el-input type="text" v-for="(link, index) in form.links" :key="index" v-model="link.url"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.BasicInformation')">
          <el-input type="text" :placeholder="$tc('message.Height')" v-model="form.height"></el-input>
          <el-input type="text" :placeholder="$tc('message.Weight')" v-model="form.weight"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.ActualClub')" v-if="form.kind==='athlete'">
          <el-input type="text" v-model="form.club"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.ActualCoach')" v-if="form.kind==='athlete'">
          <el-input type="text" v-model="form.coach"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.PitchVideoorImage')">
          <el-input type="text" v-model="form.pitchUrl"></el-input>
          <el-input type="text" v-model="form.pitchImage"></el-input>
        </el-form-item>
    </div>
    <el-form-item>
      <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinute") }}</el-button>
    </el-form-item>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'


export default {
  name: 'Content',
  components: {
  },
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
        pitchImage: null,
      },
    }
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
      user: 'users/user'
    })
  },
  created() {
    this.$store.dispatch('campaigns/fetch', this.$route.params.campaignId).then( () => {
      if (!!this.campaign && !!this.campaign.id) {
        this.form = { ... this.campaign }
        this.form.links = this.initialSocialLinks(this.campaign)
      }
    })
  },
  methods: {
      initialSocialLinks(campaign) {
        const networks = ["facebook", "instagram", "twitter", "youtube", "linkedin", "whatsapp", "flickr"]
        const socialLinks = networks.map( network => {
          const links = campaign.links.filter( item => item.network == network)
          if (links.length > 0 ) {
            return links[0]
          }
          return {id: null, campaign: campaign.id, network: network, url: null}
        })
        return socialLinks
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
          pitchImage: this.form.pitchImage,
        }
        this.$store.dispatch('campaigns/update', payload).then( () => {
          router.push({ name: 'campaign.edit', params: {
            campaignId: this.campaign.id ,
            step: 'career',
          }})
        })
      }
  }
}
</script>

<style type="scss" scoped>
</style>
