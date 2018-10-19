<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2 class="form-lined-title">{{ $tc("message.RestorePassword") }}</h2>
        <div class="form-lined">
          <el-form ref="restorePasswordForm" :model="form" :rules="rules">
            <el-form-item prop="password">
              <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item prop="repeat_password">
              <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeat_password"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" native-type="submit" class="is-uppercase is-full-width" @click.prevent="onSubmit('restorePasswordForm')">{{ $tc("message.RestorePassword") }}</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
import router from '@/router.js'
import MinimalLayout from '@/layout/MinimalLayout.vue'

export default {
  name: 'RestorePassword',
  props: ['restorePasswordCode'],
  components: {
    'gb-minimal-layout': MinimalLayout
  },
  data() {
    return {
      form: {
        password: null,
        repeat_password: null,
      },
      rules: {
        password: [
          {
            required: true,
            message: 'Please enter your password',
            trigger: 'blur'
          }
        ],
        repeat_password: [
          {
            required: true,
            message: 'Please repeat your password',
            trigger: 'change'
          }
        ]
      }
    }
  },
  methods: {
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataRestorePassword = {
            restore_password_code: this.restorePasswordCode,
            ...this.form,
          }
          this.logUser(dataRestorePassword)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    logUser(data) {
      this.$store
        .dispatch('auth/restorePassword', data)
        .then(response => {
          router.push({ name: 'login' })
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style type="scss" scoped>
.logo {
  display: block;
  margin: 0 auto 20px auto;
  max-width: 400px;
}
</style>
