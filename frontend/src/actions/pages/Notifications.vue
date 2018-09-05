<template>
  <gb-base-layout>
    <div class="notifications">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" class="text-center">
          <el-button-group>
            <el-button type="primary" @click="getUnreadNotifications()">{{ $tc("message.Unread") }}</el-button>
            <el-button type="primary" @click="getReadNotifications()">{{ $tc("message.Read") }}</el-button>
          </el-button-group>
        </el-col>
      </el-row>
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="18" :md="18" :lg="12" class="text-left">
          <ul class="notifications-list">
            <li class="notifications-list-item">
              <div class="notifications-list-item-subtitle">Notification subtitle</div>
            </li>
            <li class="notifications-list-item">
              <div class="notifications-list-item-subtitle">Notification subtitle</div>
            </li>
            <li class="notifications-list-item">
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
  computed: {
    ...mapGetters({
      notifications: 'actions/notifications',
      pagination: 'actions/pagination'
    }),
  },
  created() {
    this.getUnreadNotifications()
  },
  methods: {
    setAsRead(notification) {
      const updatedNotification = {...notification, read: true}
      this.$store.dispatch('actions/updateNotification', updatedNotification)
    },
    getReadNotifications() {
      this.$store.dispatch('actions/notifications', {filters: {read: "True"}})
    },
    getUnreadNotifications() {
      this.$store.dispatch('actions/notifications', {filters: {read: "False"}})
    },
    getNext() {
      if (this.pagination.next) {
        this.$store.dispatch('actions/notifications', {url: this.pagination.next})
      }
    },
    getPrevious() {
      if (this.pagination.previous) {
        this.$store.dispatch('actions/notifications', {url: this.pagination.previous})
      }
    }
  }
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
