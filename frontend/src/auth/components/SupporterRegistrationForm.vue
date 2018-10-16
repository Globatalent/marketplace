<template>
  <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
    <h2 class="form-lined-title">{{ $tc("message.Supporter") }}</h2>
    <div class="form-lined">
      <el-form ref="form" label-position="top" class="text-left" :model="form" :rules="rules">
        <el-row :gutter="20">
          <el-col :xs="24" :md="12">
            <el-form-item required prop="email">
              <el-input v-bind:placeholder="$tc('message.Email')" type="email" v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item required prop="password">
              <el-input v-bind:placeholder="$tc('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item required prop="repeatPassword">
              <el-input v-bind:placeholder="$tc('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :md="12">
            <el-form-item required prop="firstName">
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required prop="lastName">
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item class="text-center">
          <el-button type="primary" class="is-uppercase" @click.prevent="onSubmit('form')">{{ $tc("message.Register") }}</el-button>
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
import { Message } from 'element-ui'

export default {
  name: 'SupporterRegistrationForm',
  components: {},
  data() {
    return {
      form: {
        email: '',
        password: '',
        repeatPassword: '',
        firstName: '',
        lastName: ''
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
        password: [{ validator: this.validatePass, trigger: 'change' }],
        repeatPassword: [{ validator: this.validatePass2, trigger: 'change' }],
        firstName: [
          {
            required: true,
            message: 'Please input first name',
            trigger: 'blur'
          }
        ],
        lastName: [
          { required: true, message: 'Please input last name', trigger: 'blur' }
        ],
      }
    }
  },
  methods: {
    validatePass(rule, value, callback) {
      if (value === '') {
        callback(new Error('Please input the password'))
      } else {
        callback()
      }
    },
    validatePass2(rule, value, callback) {
      if (value === '') {
        callback(new Error('Please input the password again'))
      } else if (value !== this.form.password) {
        callback(new Error("Two inputs don't match!"))
      } else {
        callback()
      }
    },
    onSubmit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          const dataForm = Object.assign({}, this.form)
          this.$store
            .dispatch('auth/registerSupporter', dataForm)
            .then(data => {
              router.push({ name: 'campaing.list' })
            })
            .catch(error => {
              if (!!error.response) {
                Message.error({ message: error.response.data.error, center: true })
              } else {
                console.error(error)
              }
            })
        } else {
          console.error('error submit!!')
          return false
        }
      })
    }
  }
}
</script>

<style type="scss" scoped>
</style>
