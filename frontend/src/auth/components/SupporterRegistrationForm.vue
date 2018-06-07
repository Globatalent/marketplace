<template>
  <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required, min 8 chars
        - repeat_password: input type password, required, must be the same as field password
        - first_name: input type text, required
        - last_name: input type text, required
        - Add labels
        - submit button
    -->
  <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="text-left">
    <h2>Supporter</h2>
    <el-form ref="form" label-position="top">
      <el-form-item required label="Email">
        <el-input placeholder="Email" type="email" v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Password" type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Repeat password" type="password" v-model="form.repeatPassword"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="First name" type="text" v-model="form.firstName"></el-input>
      </el-form-item>
      <el-form-item required>
        <el-input placeholder="Last name" type="text" v-model="form.lastName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" class="is-uppercase" @click="onSubmit">Register</el-button>
      </el-form-item>
    </el-form>
  </el-col>
</template>

<script>
export default {
  name: 'SupporterRegistrationForm',
  components: {},
  data() {
    return {
      errorMessage: '',
      form: {
        email: '',
        password: '',
        repeatPassword: '',
        firstName: '',
        lastName: ''
      }
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      const dataForm = Object.assign({}, this.form)
      // Pasamos el objeto con registerUser
      this.registerUser(dataForm)
    },
    registerUser(data) {
      console.log('TODO: Register supporter user action ...', this.form)
    }
  }
}
</script>

<style type="scss" scoped>
</style>
