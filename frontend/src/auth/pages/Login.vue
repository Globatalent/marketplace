<template>
  <gb-minimal-layout>

    <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required
        - submit button

     It should be centered (horizontally and vertically) and not be too wide
    -->
    <el-row>
      <el-col :span="12" :offset="6">
        <h2>Sign In</h2>
        <el-form ref="form">
          <el-form-item prop="email" required>
            <el-input placeholder="Email" type="email"></el-input>
          </el-form-item>
          <el-form-item prop="password" required>
            <el-input placeholder="Password" type="password" auto-complete="off"></el-input>
          </el-form-item>
        </el-form>
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
    }
  }
</script>

<style scoped>
</style>
