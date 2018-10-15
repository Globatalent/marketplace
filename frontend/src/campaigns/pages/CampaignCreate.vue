<template>
  <gb-base-layout>
    <div v-if="!!kind">
      <component :is="forms[kind]"></component>
    </div>
    <div v-else>
      <el-button-group>
          <el-button type="primary" @click="kind = 'athlete'">{{ $tc("message.Athlete",1) }}</el-button>
          <el-button type="primary" @click="kind = 'club'">{{ $tc("message.Club") }}</el-button>
        </el-button-group>
    </div>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapGetters } from 'vuex'

import AthleteForm from "../components/AthleteForm";
import ClubForm from "../components/ClubForm";

export default {
  name: 'CampaignForm',
  components: {
    'gb-base-layout': BaseLayout,
    'gb-athlete-form': AthleteForm,
    'gb-club-form': ClubForm,
    vueDropzone: vue2Dropzone,
  },
  computed: {
    ...mapGetters({
      user: 'users/user'
    })
  },
  data() {
    return {
      forms: {
        athlete: 'gb-athlete-form',
        club: 'gb-club-form',
      },
      kind: null,
    }
  },
  created() {
  },
  methods: {
  }
}
</script>

<style scoped>
</style>
