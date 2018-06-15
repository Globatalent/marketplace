<template>
  <gb-minimal-layout>
    <!--
      TODO @victor:
      - Submit form.
    -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2>{{ $tc("message.SignIn") }}</h2>
        <el-form ref="form">
          <el-form-item required>
            <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
          </el-form-item>
          <el-form-item required>
            <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item class="text-left">
            <el-checkbox v-bind:label="$tc('message.RememberMe')"></el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $tc("message.LogIn") }}</el-button>
          </el-form-item>
          <el-form-item class="forgotPassword">
            <a href="">
              <i class="fa fa-lock"></i> {{ $tc("message.ForgotYourPassword") }}</a>
          </el-form-item>
        </el-form>
        <div>{{ $tc("message.DontHaveAccount") }}
          <a href="" class="is-main-color">{{ $tc("message.SignUp") }}</a>
        </div>
      </el-col>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
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
          email: '',
          password: ''
        },
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault();
        const dataLogin = Object.assign({}, this.form);
        // Pasamos el objeto con logUser
        this.logUser(dataLogin);
      },
      logUser(data) {
        console.log('TODO @victor: Login user action ...');
        console.log('logUser',this.$store);
        console.log('logUser form',this.form);

        this.$store.dispatch('auth/login', this.form).then((data) => {
          console.log('AuthLogin', data);
          // this.$store.dispatch('users/fetchUser').then(() => {
          //   this.hide()
          // }).catch(() => {
          //   this.hide()
          // })
        }).catch(() => {
          this.hide()
        })
      },
    },
  }
</script>

<style type="scss" scoped>
  .logo {
    display: block;
    margin: 0 auto 20px auto;
    max-width: 400px;
  }
</style>
