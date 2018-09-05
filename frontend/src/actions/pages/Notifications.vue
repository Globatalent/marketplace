<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24" class="">
        <el-tabs type="border-card" @tab-click="handleTabClick" value="unread">
          <el-tab-pane :label="$tc('message.Unread')" name="unread">
            <el-table :data="notifications" style="width: 100%" v-loading="loadingNotifications">
              <el-table-column fixed="left" label="Operations" width="135" class="text-left">
                <template slot-scope="scope">
                  <el-button @click="setAsRead(scope)" type="primary" size="mini" round>Mark as read</el-button>
                </template>
              </el-table-column>
              <el-table-column prop="action.text" label="Notifications"></el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane :label="$tc('message.Read')" name="read">
            <el-table :data="notifications" style="width: 100%" v-loading="loadingNotifications">
              <el-table-column prop="action.text" label="Notifications"></el-table-column>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
    <el-row v-if="pagination.count > 0">
      <el-col :xs="24" class="text-center">
        <el-pagination
          layout="prev, next"
          :total="pagination.count"
          :disabled="loadingNotifications"
          @prev-click="getPrevious()"
          @next-click="getNext()">
        </el-pagination>
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
    }
  },
  computed: {
    ...mapGetters({
      unread: 'actions/unread',
      notifications: 'actions/notifications',
      loadingNotifications: 'actions/loadingNotifications',
      pagination: 'actions/pagination'
    })
  },
  created() {
    this.getUnreadNotifications()
  },
  methods: {
    handleTabClick(tab, event) {
      if (tab.name == 'read') {
        this.getReadNotifications()
      } else if (tab.name == 'unread') {
        this.getUnreadNotifications()
      }
    },
    setAsRead(scope) {
      const updatedNotification = { ...scope.row, read: true }
      this.$store.dispatch('actions/updateNotification', updatedNotification)
        .then( () => {
          this.getUnreadNotifications()
        })
    },
    getReadNotifications() {
      this.$store
        .dispatch('actions/notifications', {
          filters: { read: 'True' }
        })
    },
    getUnreadNotifications() {
      this.$store
        .dispatch('actions/notifications', {
          filters: { read: 'False' }
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
