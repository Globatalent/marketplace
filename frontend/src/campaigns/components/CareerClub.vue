<template>
  <el-col :xs="24" class="formSteps-container">
    <div class="infoTag">Draft Campaign</div>
    <el-breadcrumb separator=">">
      <el-breadcrumb-item :to="{ path: '/campaigns' }">Campaign</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/campaigns/create">Card campaign</a></el-breadcrumb-item>
    </el-breadcrumb>
    <div class="formSteps-actions">
      <el-button type="danger" class="" @click.prevent="onDiscard()">{{ $tc("message.DiscardCampaign") }}</el-button>
      <el-button type="secondary" class="" @click.prevent="onSaveAndContinue()">{{ $tc("message.ReviewLaunch") }}</el-button>
    </div>
    <div class="formSteps">
      <div v-if="campaign.kind == 'athlete'">
        <h2 class="formSteps-title">{{ $tc("message.Career") }}</h2>
        <p class="formSteps-text">Introduce your Career and entice people to learn more.</p>
        <el-form-item required :label="$tc('message.Ranking')">
          <p class="formSteps-inputText">Enter your actual ranking. (If is applicable)</p>
          <el-input type="text" v-model="form.ranking"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Biography')">
          <p class="formSteps-inputText">Tell potential contributors more about your campaign. Provide details that will motivate people
to contribute. A good pitch is compelling, informative, and easy to digest. Learn more.</p>
          <el-input type="text" v-model="form.biography"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Achievements')">
          <p class="formSteps-inputText">List your sport career achievements (year, titles or position) as well as participation in different
tournaments, etc.</p>
          <el-input type="text" v-model="form.achievements"></el-input>
        </el-form-item>
        <el-form-item>
        <div class="formSteps-lineButton"></div>
        <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinue") }}</el-button>
      </el-form-item>
      </div>
      <div v-if="campaign.kind == 'club'">
        <h2 class="formSteps-title">{{ $tc("message.Club") }}</h2>
        <p class="formSteps-text">Introduce your Career and entice people to learn more.</p>
        <el-form-item required :label="$tc('message.ClubHistory')">
          <p class="formSteps-inputText">Tell potential contributors more about your campaign. Provide details that will motivate people to
contribute. A good pitch is compelling, informative, and easy to digest. Learn more.</p>
          <el-input type="text" v-model="form.history"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Achievements')">
          <p class="formSteps-inputText">List your sport career achievements (year, titles or position) as well as participation in different
tournaments, etc.</p>
          <el-input type="text" v-model="form.achievements"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.ExpectedSportsAchievements')">
          <p class="formSteps-inputText">(titles, ranking position, etc)</p>
          <el-input type="text" v-model="form.expected"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Players')">
          <p class="formSteps-inputText">List all team players</p>
          <el-input type="text" v-model="form.players"></el-input>
        </el-form-item>
        <el-form-item>
        <div class="formSteps-lineButton"></div>
        <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinue") }}</el-button>
      </el-form-item>
      </div>
    </div>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'

export default {
  name: 'CareerClub',
  components: {},
  data() {
    return {
      // Form
      form: {
        ranking: null,
        biography: null,
        achievements: null,
        history: null,
        expected: null,
        players: null
      }
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
          this.form = { ...this.campaign }
        }
      })
  },
  methods: {
    onDiscard() {
      const payload = { id: this.campaign.id }
      this.$store.dispatch('campaigns/delete', payload)
    },
    onSaveAndContinue() {
      const payload = {
        id: this.campaign.id,
        ranking: this.form.ranking,
        biography: this.form.biography,
        achievements: this.form.achievements,
        history: this.form.history,
        expected: this.form.expected,
        players: this.form.players
      }
      this.$store.dispatch('campaigns/update', payload).then(() => {
        router.push({
          name: 'campaign.edit',
          params: {
            campaignId: this.campaign.id,
            step: 'funding'
          }
        })
      })
    }
  }
}
</script>

<style type="scss" scoped>
</style>
