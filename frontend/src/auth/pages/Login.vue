<template>
  <gb-minimal-layout>
    <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required
        - submit button

     It should be centered (horizontally and vertically) and not be too wide


     - Add font-awesome
     - Add internationalitation
    -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2>{{ $t("message.signIn") }}</h2>
        <el-form ref="form">
          <el-form-item required>
            <el-input placeholder="Email" type="email" v-model="form.email"></el-input>
          </el-form-item>
          <el-form-item required>
            <el-input placeholder="Password" type="password" v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item class="text-left">
            <el-checkbox label="Remember me"></el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="is-uppercase" @click="onSubmit">Log in</el-button>
          </el-form-item>
          <el-form-item>
            <a href="">
              <i class="el-icon-setting"></i> Forgot your password?</a>
          </el-form-item>
        </el-form>
        <div>Dont't have an account?
          <a href="" class="is-main-color">Sign Up</a>
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
      console.log('TODO: Login user action ...');
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
