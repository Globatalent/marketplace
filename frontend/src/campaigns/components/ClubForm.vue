<template>
  <el-col :xs="24" class="text-center">
    <h2 class="form-lined-title">{{ $tc("message.Club",1) }}</h2>
    <div class="form-lined">
      <el-form ref="form" label-position="top" class="text-left">
        <el-form-item required>
          <el-input v-bind:placeholder="$tc('message.CampaignTitle')" type="text" v-model="form.title"></el-input>
        </el-form-item>
        <el-form-item required>
          <el-input v-bind:placeholder="$tc('message.CampaignTagline')" type="text" v-model="form.description"></el-input>
        </el-form-item>
      </el-form>
    </div>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import Campaign from '@/campaigns/models/Campaign'
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'


export default {
  name: 'AthleteForm',
  components: {
    vueDropzone: vue2Dropzone
  },
  data() {
    return {
      form: new Campaign({})
    }
  },
  computed: {
    ...mapGetters({
      user: 'campaigns/sports'
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
