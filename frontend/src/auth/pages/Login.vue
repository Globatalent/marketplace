<template>
  <gb-minimal-layout>

    <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required
        - submit button

     It should be centered (horizontally and vertically) and not be too wide
    -->
    <div class="is-vertical-center">
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" class="loginBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2>Sign In</h2>
        <el-form ref="form">
          <el-form-item prop="email" required>
            <el-input placeholder="Email" type="email"></el-input>
          </el-form-item>
          <el-form-item prop="password" required>
            <el-input placeholder="Password" type="password"></el-input>
          </el-form-item>
          <el-form-item class="text-left">
            <el-checkbox label="Remember me"></el-checkbox>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" class="is-uppercase">Log in</el-button>
          </el-form-item>
          <el-form-item>
            <a href=""><i class="el-icon-setting"></i> Forgot your password?</a>
          </el-form-item>
        </el-form>
        <div>Dont't have an account? <a href="" class="is-main-color">Sign Up</a></div>
      </el-col>
    </el-row>
    </div>
  </gb-minimal-layout>
</template>

<script>
  import MinimalLayout from '@/layout/MinimalLayout.vue'

  export default {
    name: 'Login',
    components: {
      'gb-minimal-layout': MinimalLayout
    }
  }
</script>

<style type="scss" scoped>
  .logo {
    display: block;
    margin: 0 auto 20px auto;
  }
  .loginBox{
  }
</style>
