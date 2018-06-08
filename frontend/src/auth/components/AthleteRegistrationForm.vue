<template>
  <!--
      TODO @victor:
        - Fix Sex radio option
        - submit form
    -->
  <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="text-center">
    <h2>{{ $t("message.Athlete") }}</h2>
    <el-form ref="form" label-position="top" class="text-left">
      <el-form-item required v-bind:label="$t('message.Email')">
        <el-input v-bind:placeholder="$t('message.Email')" type="email" v-model="form.email"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.Password')">
        <el-input v-bind:placeholder="$t('message.Password')" type="password" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.RepeatPassword')">
        <el-input v-bind:placeholder="$t('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.FirstName')">
        <el-input v-bind:placeholder="$t('message.FirstName')" type="text" v-model="form.firstName"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.LastName')">
        <el-input v-bind:placeholder="$t('message.LastName')" type="text" v-model="form.lastName"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.Country')">
        <el-input v-bind:placeholder="$t('message.Country')" type="text" v-model="form.country"></el-input>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.Date')">
        <el-date-picker type="date" v-bind:placeholder="$t('message.PickADate')" style="width: 100%;" v-model="form.date"></el-date-picker>
      </el-form-item>
      <el-form-item required v-bind:label="$t('message.Sport')">
        <el-input v-bind:placeholder="$t('message.Sport')" type="text" v-model="form.sport"></el-input>
      </el-form-item>
      <el-form-item v-bind:label="$t('message.Sex')" class="text-left sexFormElement">
        <el-radio-group>
          <el-radio label="male" v-model="form.sex">{{ $t("message.Male") }}</el-radio>
          <el-radio label="female" v-model="form.sex">{{ $t("message.Female") }}</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item class="text-center">
        <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $t("message.Register") }}</el-button>
      </el-form-item>
    </el-form>
  </el-col>
</template>

<script>
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
        sex: 'male',
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
      console.log('TODO @victor: Register athlete user action ...', this.form)
    }
  }
}
</script>

<style type="scss" scoped>
</style>
