<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2>{{ $tc("message.SignIn") }}</h2>
        <el-form ref="loginForm" :model="form" :rules="rules">
          <el-form-item prop="email" :error="loginErrors.email">
            <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
          </el-form-item>
          <el-form-item prop="password" :error="loginErrors.password">
            <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item class="text-left">
            <el-checkbox v-bind:label="$tc('message.RememberMe')"></el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" native-type="submit" class="is-uppercase" @click.prevent="onSubmit('loginForm')">{{ $tc("message.LogIn") }}</el-button>
          </el-form-item>
          <el-form-item class="forgotPassword">
            <a href="">
              <i class="fa fa-lock"></i> {{ $tc("message.ForgotYourPassword") }}</a>
          </el-form-item>
        </el-form>
        <div>{{ $tc("message.DontHaveAccount") }}
          <router-link :to="{ name: 'registration'}" class="is-main-color">{{ $tc("message.SignUp") }}</router-link>
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
      errorMessage: '',
      form: {
        email: null,
        password: null
      },
      loginErrors: {
        non_field_errors: '',
        email: '',
        password: ''
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
            trigger: 'change'
          },
          { validator: this.validatePassword, trigger: 'blur' }
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
          router.push({ name: 'athlete.list' })
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
