<template>
  <gb-base-layout>
    <div class="notifications">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" class="text-center">
          <el-button-group>
            <el-button type="primary" @click="userType = 'athlete'">{{ $tc("message.Unread") }}</el-button>
            <el-button type="primary" @click="userType = 'supporter'">{{ $tc("message.Read") }}</el-button>
          </el-button-group>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" class="text-left">
          <ul class="notifications-list">
            <li class="notifications-list-item">
              <div class="notifications-list-item-title">Notification title</div>
              <div class="notifications-list-item-subtitle">Notification subtitle</div>
            </li>
            <li class="notifications-list-item">
              <div class="notifications-list-item-title">Notification title</div>
              <div class="notifications-list-item-subtitle">Notification subtitle</div>
            </li>
            <li class="notifications-list-item">
              <div class="notifications-list-item-title">Notification title</div>
              <div class="notifications-list-item-subtitle">Notification subtitle</div>
            </li>
          </ul>
        </el-col>
      </el-row>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'

export default {
  name: 'Notifications',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {}
  },
  computed: {},
  created() {},
  methods: {}
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
