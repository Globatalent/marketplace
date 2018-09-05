<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" class="">
        <el-tabs type="border-card">
          <el-tab-pane :label="$tc('message.Unread')">
            <el-table :data="unreadNotifications" style="width: 100%">
              <el-table-column fixed="left" label="Operaciones" width="135" class="text-left">
                <template slot-scope="scope">
                  <el-button @click="setAsRead(scope,unreadNotifications)" type="primary" size="mini" round>Mark as read</el-button>
                </template>
              </el-table-column>
              <el-table-column prop="action.text" label="Notifications"></el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane :label="$tc('message.Read')">
            <el-table :data="readNotifications" style="width: 100%">
              <el-table-column prop="action.text" label="Notifications"></el-table-column>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
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
    return {
      unreadNotifications: [],
      readNotifications: []
    }
  },
  computed: {
    ...mapGetters({
      notifications: 'actions/notifications',
      pagination: 'actions/pagination'
    })
  },
  created() {
    this.getUnreadNotifications()
    this.getReadNotifications()
  },
  methods: {
    setAsRead(notification) {
      debugger
      const updatedNotification = { ...notification, read: true }
      this.$store.dispatch('actions/updateNotification', updatedNotification)
    },
    getReadNotifications() {
      this.$store
        .dispatch('actions/notifications', {
          filters: { read: 'True' }
        })
        .then(response => {
          this.readNotifications = response
          console.log(this.readNotifications)
        })
        .catch(error => {
          console.error(error)
        })
    },
    getUnreadNotifications() {
      this.$store
        .dispatch('actions/notifications', { filters: { read: 'False' } })
        .then(response => {
          this.unreadNotifications = response
          console.log(this.unreadNotifications)
        })
        .catch(error => {
          console.error(error)
        })
    },
    getNext() {
      if (this.pagination.next) {
        this.$store.dispatch('actions/notifications', {
          url: this.pagination.next
        })
      }
    },
    getPrevious() {
      if (this.pagination.previous) {
        this.$store.dispatch('actions/notifications', {
          url: this.pagination.previous
        })
      }
    }
  }
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
