<template>
  <el-col :xs="24" class="text-center">
    <h2 class="form-lined-title">{{ $tc("message.Athlete",1) }}</h2>
    <div class="form-lined">
      <el-form ref="form" label-position="top" class="text-left">
        <el-form-item required>
          <el-input v-bind:placeholder="$tc('message.CampaignTitle')" type="text" v-model="form.title"></el-input>
        </el-form-item>
        <el-form-item required>
          <el-input v-bind:placeholder="$tc('message.CampaignTagline')" type="text" v-model="form.description"></el-input>
        </el-form-item>
        <el-form-item v-bind:label="$tc('message.Gender')" class="text-left sexFormElement">
          <el-radio-group>
            <el-radio label="male" v-model="form.gender">{{ $tc("message.Male") }}</el-radio>
            <el-radio label="female" v-model="form.gender">{{ $tc("message.Female") }}</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item>
          <el-upload
            drag
            thumbnail-mode
            limit="1"
            :action="options.action"
            :headers="options.headers"
            :name="options.name"
            >
            <i class="el-icon-upload"></i>
          </el-upload>
        </el-form-item>
      </el-form>
    </div>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import Campaign from '@/campaigns/models/Campaign'


export default {
  name: 'AthleteForm',
  components: {
  },
  data() {
    return {
      form: new Campaign({}),
      options: {
        action: `${Vue.axios.defaults.baseURL}/api/v1/pictures/`,
        name: 'image',
        headers: {
          Authorization: this.$store.getters['auth/header']
        }
      },
    }
  },
  computed: {
    ...mapGetters({
      sports: 'campaigns/sports',
      user: 'users/user'
    })
  },
  created() {
    this.$store.dispatch('campaigns/sports')
  },
  methods: {
  }
}
</script>

<style type="scss" scoped>
</style>
