<template>
  <gb-base-layout>
    <el-row type="flex" justify="center" class="profile-info">
      <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
        <h2 class="form-lined-title">{{ $tc("message.Profile") }}</h2>
        <div class="form-lined">
          <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
            <el-row :gutter="20">
              <el-col :xs="24">
                <el-form-item required prop="email">
                  <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email" :disabled='true'></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="password">
                  <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="repeatPassword">
                  <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="firstName">
                  <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="lastName">
                  <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="birthDate">
                  <el-date-picker v-bind:placeholder="$tc('message.DateFormat')" type="date" class="datepicker" v-model="form.birthDate"></el-date-picker>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="country">
                  <el-select v-model="form.country" filterable v-bind:placeholder="$tc('message.CountryResidence')">
                    <el-option
                      v-for="(code, index) in Object.keys(countries)"
                      :key="index"
                      :label="countries[code]"
                      :value="code">
                    </el-option>
                  </el-select>
                </el-form-item>
              </el-col>
              <el-col :xs="24">
                <el-form-item prop="citizenship">
                  <el-input v-bind:placeholder="$tc('message.Citizenship')" type="text" v-model="form.citizenship"></el-input>
                </el-form-item>
              </el-col>
            </el-row>
            <el-form-item class="text-center">
              <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Save") }}</el-button>
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
        </el-tabs>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import countries from '@/base/helpers/countries'


export default {
  name: 'Profile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      countries: countries,
      form: {
        email: '',
        password: '',
        firstName: '',
        lastName: '',
        country: '',
        citizenship: '',
        birthDate: '',
      },
      rules: {
        repeatPassword: [{ validator: this.validateRepeatPassword, trigger: 'change' }],
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
  created() {
    this.initial()
  },
  methods: {
    initial() {
      this.$store.commit('campaigns/campaigns', [])
      this.$store.dispatch('alerts/alerts')
      this.$store.dispatch('users/fetchUser').then(user => {
        this.form = { ...this.user}
        this.$store.dispatch('campaigns/list', {
          filters: { followed_by: user.id }
        })
      })
    },
    unfollow(scope) {
      const id = scope.row.id
      this.$store
        .dispatch('athletes/follow', id)
        .then(() => {
          this.$store.dispatch('athletes/list', {
            filters: { followed_by: this.user.id }
          })
        })
        .catch(error => {
          console.log(error)
        })
    },
    validateRepeatPassword(rule, value, callback) {
      if (value === '') {
        callback(new Error('Please input the password again'))
      } else if (value !== this.form.password) {
        callback(new Error("Two inputs don't match!"))
      } else {
        callback()
      }
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          if (!!this.form.birthDate) {
            this.form.birthDate = this.form.birthDate.toISOString().split('T')[0]
          }
          const dataForm = Object.assign({}, this.form)
          this.saveUserProfile(dataForm)
        } else {
          return false
        }
      })
    },
    saveUserProfile(data) {
      this.$store
        .dispatch('users/update', data)
        .then(response => {
          console.log('User updated')
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
