<template>
  <!--
      TODO @victor:
        - submit form
    -->
  <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="text-center">
    <h2>{{ $tc("message.Supporter") }}</h2>
    <el-form ref="form" label-position="top" class="text-left">
      <el-form-item required v-bind:label="$tc('message.Email')">
        <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$tc('message.Password')">
        <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$tc('message.RepeatPassword')">
        <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$tc('message.FirstName')">
        <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$tc('message.LastName')">
        <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
      </el-form-item>
      <el-form-item class="text-center">
        <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $tc("message.Register") }}</el-button>
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
      console.log('TODO @victor: Register supporter user action ...', this.form)
    }
  }
}
</script>

<style type="scss" scoped>
</style>
