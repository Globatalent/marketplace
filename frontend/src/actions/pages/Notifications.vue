<template>
  <gb-base-layout>
    <div class="notifications">
      <el-row>
        <el-col :xs="24" class="">
          <el-tabs type="border-card">
            <el-tab-pane :label="$tc('message.Unread')">
              <el-table :data="unreadNotifications.action" style="width: 100%">
                <el-table-column prop="text" label="Notifications"></el-table-column>
              </el-table>
            </el-tab-pane>
            <el-tab-pane :label="$tc('message.Read',2)">
              <el-table :data="readNotifications.action" style="width: 100%">
                <el-table-column prop="text" label="Notifications"></el-table-column>
              </el-table>
            </el-tab-pane>
          </el-tabs>
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
    return {
      unreadNotifications: [],
      readNotifications: []
    }
  },
  computed: {
    ...mapGetters({
      notifications: 'actions/notifications'
    })
  },
  created() {
    // this.$store.dispatch('actions/notifications')
    this.$store
      .dispatch('actions/notifications', {
        filters: { read: 'False' }
      })
      .then(response => {
        this.unreadNotifications = response
      })
      .catch(error => {
        console.error(error)
      })
    this.$store
      .dispatch('actions/notifications', {
        filters: { read: 'True' }
      })
      .then(response => {
        this.readNotifications = response
      })
      .catch(error => {
        console.error(error)
      })
  },
  methods: {}
}
</script>

<style scoped>
@import '../../scss/variables.scss';
</style>
