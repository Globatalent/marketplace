<template>
  <gb-base-layout>
    <el-row type="flex" justify="center" class="profile-info">
      <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
        <h2 class="form-lined-title">{{ $tc('message.Profile') }}</h2>
        <div class="form-lined">
          <gb-profile-info-row :field-name=" $tc('message.Email')" :value="user.email"></gb-profile-info-row>
          <gb-profile-info-row :field-name=" $tc('message.FirstName')" :value="user.firstName"></gb-profile-info-row>
          <gb-profile-info-row :field-name=" $tc('message.LastName')" :value="user.lastName"></gb-profile-info-row>
          <gb-profile-info-row :field-name=" $tc('message.DateFormat')" :value="user.birthDate"></gb-profile-info-row>
          <gb-profile-info-row :field-name=" $tc('message.CountryResidence')"
                               :value="countries[user.country]"></gb-profile-info-row>
          <gb-profile-info-row :field-name=" $tc('message.Citizenship')"
                               :value="user.citizenship"></gb-profile-info-row>

          <el-row>
            <el-col><h3 class="m-t-15">Change your password</h3></el-col>
          </el-row>
          <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
            <el-row :gutter="20">
              <el-col :xs="24">
                <el-form-item prop="password">
                  <el-input v-bind:placeholder="$tc('message.Password')" type="password"
                            v-model="form.password"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="repeatPassword">
                  <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password"
                            v-model="form.repeatPassword"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-form-item class="text-center">
              <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc('message.Save')
                }}
              </el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24" class="">
        <el-tabs type="border-card">
          <el-tab-pane :label="$tc('message.Following')">
            <el-table :data="campaigns" style="width: 100%">
              <el-table-column prop="id" label="ID"></el-table-column>
              <el-table-column prop="title" label="Title"></el-table-column>
              <el-table-column prop="sport.name" label="Sport"></el-table-column>
              <el-table-column fixed="right" label="Operaciones">
                <template slot-scope="scope">
                  <el-button @click="unfollow(scope)" type="text" size="small">{{$tc('message.Unfollow')}}</el-button>
                </template>
              </el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane :label="$tc('message.Alert',2)">
            <el-table :data="alerts" style="width: 100%">
              <el-table-column prop="id" label="ID"></el-table-column>
              <el-table-column prop="rule" label="Rule"></el-table-column>
              <el-table-column prop="amount" label="Amount"></el-table-column>
              <el-table-column prop="athlete.firstName" label="Athlete"></el-table-column>
            </el-table>
          </el-tab-pane>
          <el-tab-pane :label="$tc('message.purchases',3)">
            <el-table :data="purchases" style="width: 100%">
              <el-table-column prop="id" label="ID"></el-table-column>
              <!-- <el-table-column prop="rule" label="Rule"></el-table-column> -->
              <el-table-column prop="amount" label="Amount"></el-table-column>
              <el-table-column prop="status" label="Status"></el-table-column>
            </el-table>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
  import Vue from 'vue'
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
  import countries from '@/base/helpers/countries'
  import ProfileInfoRow from '@/users/components/ProfileInfoRow.vue'
  import { Message } from 'element-ui'

  export default {
    name: 'Profile',
    components: {
      'gb-base-layout': BaseLayout,
      'gb-profile-info-row': ProfileInfoRow
    },
    data () {
      return {
        countries: countries,
        purchases: undefined,
        form: {
          password: '',
          repeatPassword: '',
        },
        rules: {
          password: [{required: true, message: 'Please enter a new password', trigger: 'blur'}],
          repeatPassword: [
            {required: true, message: 'Please confirm your password', trigger: 'blur'},
            {validator: this.validateRepeatPassword, trigger: 'blur'}
          ],
        }
      }
    },
    computed: {
      ...mapGetters({
        alerts: 'alerts/alerts',
        campaigns: 'campaigns/campaigns',
        pagination: 'campaigns/pagination',
        user: 'users/user'
      })
    },
    created () {
      this.initial()
    },
    methods: {
      initial () {
        this.$store.commit('campaigns/campaigns', [])
        this.$store.dispatch('alerts/alerts')
        this.$store.dispatch('users/fetchUser').then(user => {
          this.$store.dispatch('campaigns/list', {
            filters: {followed_by: user.id}
          })
        })
        Vue.axios.get('https://staging.globatalent.com/api/v1/purchases/')
          .then(response => {
            console.log(response)
            this.purchases = response.data.results
        })
      },
      unfollow (scope) {
        const id = scope.row.id
        this.$store
          .dispatch('athletes/follow', id)
          .then(() => {
            this.$store.dispatch('athletes/list', {
              filters: {followed_by: this.user.id}
            })
          })
          .catch(error => {
            console.log(error)
          })
      },
      validateRepeatPassword (rule, value, callback) {
        if (value === '') {
          callback(new Error('Please input the password again'))
        } else if (value !== this.form.password) {
          callback(new Error('Two inputs don\'t match!'))
        } else {
          callback()
        }
      },
      onSubmit (form) {
        this.$refs[form].validate(valid => {
          if (valid) {
            const dataForm = Object.assign({}, this.form)
            this.saveUserProfile(dataForm)
          } else {
            return false
          }
        })
      },
      saveUserProfile (data) {
        this.$store
          .dispatch('users/update', data)
          .then(response => {

            Message.success('Password updated')
            this.form = {
              password: '',
              repeatPassword: '',
            }
          })
          .catch(error => {
            console.error(error)
          })
      }
    }
  }
</script>

<style type="scss" scoped>
  .profile-info {
    margin-bottom: 20px;
  }
</style>
