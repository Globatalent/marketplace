<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4" class="forgotBox text-center">
        <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        <h2 class="form-lined-title">{{ $tc("message.RecoverPassword") }}</h2>
        <div class="form-lined">
          <el-form ref="forgotForm" :model="form" :rules="rules">
            <el-form-item prop="email" :error="formErrors.email">
              <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item>
              <el-button type="primary" native-type="submit" class="is-uppercase is-full-width" @click.prevent="onSubmit('forgotForm')">{{ $tc("message.Recover") }}</el-button>
            </el-form-item>
          </el-form>
        </div>
      </el-col>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
import router from '@/router.js'
import MinimalLayout from '@/layout/MinimalLayout.vue'

export default {
  name: 'Forgot',
  components: {
    'gb-minimal-layout': MinimalLayout
  },
  data() {
    return {
      errorMessage: '',
      form: {
        email: null,
      },
      formErrors: {
        non_field_errors: '',
        email: '',
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
      }
    }
  },
  methods: {
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form)
          this.forgotUser(dataForm)
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    forgotUser(data) {
      this.$store
        .dispatch('auth/forgot', this.form)
        .then(data => {
          router.push({ name: 'login' })
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
