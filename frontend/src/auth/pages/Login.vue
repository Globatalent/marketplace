<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4" class="loginBox text-center">
        <router-link :to="{ name: 'athlete.list'}">
          <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        </router-link>
        <h2 class="form-lined-title">{{ $tc("message.SignIn") }}</h2>
        <div class="form-lined">
          <el-form ref="loginForm" :model="form" :rules="rules">
            <el-form-item prop="email">
              <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item prop="password">
              <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item class="text-left">
              <el-checkbox v-bind:label="$tc('message.RememberMe')"></el-checkbox>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" native-type="submit" class="is-uppercase is-full-width" @click.prevent="onSubmit('loginForm')">{{ $tc("message.LogIn") }}</el-button>
            </el-form-item>
            <el-form-item class="forgotPassword">
              <router-link :to="{ name: 'forgot'}" class="is-main-color">
                <i class="fa fa-lock"></i> {{ $tc("message.ForgotYourPassword") }}
              </router-link>
            </el-form-item>
          </el-form>
          <div class="form-reminderBlock">{{ $tc("message.DontHaveAccount") }}
            <router-link :to="{ name: 'registration'}" class="is-main-color">{{ $tc("message.SignUp") }}</router-link>
          </div>
        </div>
      </el-col>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
import router from '@/router.js'
import MinimalLayout from '@/layout/MinimalLayout.vue'

export default {
  name: 'Login',
  components: {
    'gb-minimal-layout': MinimalLayout
  },
  data() {
    return {
      form: {
        email: null,
        password: null
      },
      rules: {
        email: [
          {
            required: true,
            message: 'Please enter a valid email',
            trigger: 'blur'
          },
          {
            type: 'email',
            message: 'Please enter a valid email',
            trigger: ['blur', 'change']
          }
        ],
        password: [
          {
            required: true,
            message: 'Please enter your password',
            trigger: 'blur'
          }
        ]
      }
    }
  },
  methods: {
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataLogin = Object.assign({}, this.form)
          this.logUser(dataLogin)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    logUser(data) {
      this.$store
        .dispatch('auth/login', this.form)
        .then(data => {
          this.$router.push({ name: 'campaign.list' })
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
