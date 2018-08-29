<template>
  <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
    <h2 class="form-lined-title">{{ $tc("message.Supporter") }}</h2>
    <div class="form-lined">
      <el-form ref="form" label-position="top" class="text-left">
        <el-row :gutter="20">
          <el-col :xs="24" :md="12">
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :md="12">
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item class="text-center">
          <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $tc("message.Register") }}</el-button>
        </el-form-item>
      </el-form>
      <el-row>
        <div class="form-reminderBlock text-center">{{ $tc("message.AlreadyAccount") }}
          <router-link :to="{ name: 'login'}" class="is-main-color">{{ $tc("message.LogIn") }}</router-link>
        </div>
      </el-row>
    </div>
  </el-col>
</template>

<script>
import router from '@/router.js'

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
      this.$store
        .dispatch('auth/registerSupporter', data)
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
</style>
