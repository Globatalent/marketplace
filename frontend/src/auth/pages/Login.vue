<template>
  <gb-minimal-layout>
    <!--
      TODO @victor:
      - Submit form.
    -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2>{{ $t("message.SignIn") }}</h2>
        <el-form ref="form">
          <el-form-item required>
            <el-input v-bind:placeholder="$t('message.Email')" type="email" v-model="form.email"></el-input>
          </el-form-item>
          <el-form-item required>
            <el-input v-bind:placeholder="$t('message.Password')" type="password" v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item class="text-left">
            <el-checkbox v-bind:label="$t('message.RememberMe')"></el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $t("message.LogIn") }}</el-button>
          </el-form-item>
          <el-form-item class="forgotPassword">
            <a href="">
              <icon name="lock"></icon> {{ $t("message.ForgotYourPassword") }}</a>
          </el-form-item>
        </el-form>
        <div>{{ $t("message.DontHaveAccount") }}
          <a href="" class="is-main-color">{{ $t("message.SignUp") }}</a>
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
