<template>
  <el-col :xs="24">
    <h2 class="form-lined-title text-center">{{ $tc("message.Career") }}</h2>
    <div class="form-lined">
        <el-form-item :label="$tc('message.Ranking')">
          <el-input type="text" v-model="form.ranking"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Biography')">
          <el-input type="text" v-model="form.biography"></el-input>
        </el-form-item>
        <el-form-item :label="$tc('message.Achievements')">
          <el-input type="text" v-model="form.achievements"></el-input>
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
  name: 'Career',
  components: {
  },
  data() {
    return {
      // Form
      form: {
        ranking: null,
        biography: null,
        achievements: null,
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
      }
    })
  },
  methods: {
      onSaveAndContinue() {
        const payload = {
          id: this.campaign.id,
          ranking: this.form.ranking,
          biography: this.form.biography,
          achievements: this.form.achievements,
        }
        this.$store.dispatch('campaigns/update', payload).then( () => {
          router.push({ name: 'campaign.edit', params: {
            campaignId: this.campaign.id ,
            step: 'funding',
          }})
        })
      }
  }
}
</script>

<style type="scss" scoped>
</style>
