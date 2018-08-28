<template>
  <gb-base-layout>
    <!--
      TODO @kike: Supporters must see a list of the athletes they are following and the alerts they have set up
      - We will have 2 tables, one of the following athletes and one with all
      -->
    <el-col :xs="24" class="">
      <el-tabs type="border-card">
        <el-tab-pane :label="$tc('message.Following')">
          <h3>{{$tc('message.Following')}}</h3>
          <el-table :data="athletes" style="width: 100%">
            <el-table-column prop="id" label="id"></el-table-column>
            <el-table-column prop="firstName" label="firstName"></el-table-column>
            <el-table-column prop="lastName" label="lastName"></el-table-column>
            <el-table-column prop="sport" label="sport"></el-table-column>
            <el-table-column prop="country" label="country"></el-table-column>
            <el-table-column fixed="right" label="Operaciones">
              <template slot-scope="scope">
                <el-button @click="unfollow(scope)" type="text" size="small" >{{$tc('message.Unfollow')}}</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
        <el-tab-pane :label="$tc('message.Alert',2)">
          <h3>{{$tc('message.Alert',1)}}</h3>
          <el-table :data="alerts" style="width: 100%">
            <el-table-column prop="id" label="id"></el-table-column>
            <el-table-column prop="rule" label="rule"></el-table-column>
            <el-table-column prop="amount" label="amount"></el-table-column>
            <el-table-column prop="athlete.first_name" label="athlete"></el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-col>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'

export default {
  name: 'SupporterProfile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {}
  },
  computed: {
    ...mapGetters({
      alerts: 'supporters/alerts',
      athletes: 'athletes/athletes',
      pagination: 'athletes/pagination',
      user: 'users/user',
    }),
  },
  created() {
    this.initial();
  },
  methods: {
    initial() {
      this.$store.dispatch('supporters/alerts')
      this.$store.dispatch('users/fetchUser').then( user => {
        this.$store.dispatch('athletes/list', {filters: {'followed_by': user.id}});
      })
    },
    unfollow(scope) {
      const id = scope.row.id
      this.$store.dispatch('athletes/follow', id).then( () => {
        this.$store.dispatch('athletes/list', {filters: {'followed_by': this.user.id}});
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
</style>
