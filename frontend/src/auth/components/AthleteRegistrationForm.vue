<template>
  <!--
      TODO @victor:
        - Fix Sex radio option
    -->
  <el-col :xs="24" :sm="12" :md="12" :lg="10" :xl="6" class="text-center">
    <h2 class="form-lined-title">{{ $tc("message.Athlete",1) }}</h2>
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
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.Sport')" type="text" v-model="form.sport"></el-input>
            </el-form-item>
            <el-form-item v-bind:label="$tc('message.Sex')" class="text-left sexFormElement">
              <el-radio-group>
                <el-radio label="male" v-model="form.sex">{{ $tc("message.Male") }}</el-radio>
                <el-radio label="female" v-model="form.sex">{{ $tc("message.Female") }}</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :md="12">
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-input v-bind:placeholder="$tc('message.Country')" type="text" v-model="form.country"></el-input>
            </el-form-item>
            <el-form-item required>
              <el-date-picker type="date" v-bind:placeholder="$tc('message.DateOfBirth')" style="width: 100%;" v-model="form.date"></el-date-picker>
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
  name: 'AthleteRegistrationForm',
  components: {},
  data() {
    return {
      errorMessage: '',
      form: {
        email: '',
        password: '',
        repeatPassword: '',
        firstName: '',
        lastName: '',
        country: '',
        date: '',
        sport: '',
        sex: 'male'
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
      this.$store
        .dispatch('auth/registerAthlete', data)
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
