<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="registrationBox text-center">
        <div>{{ $tc("message.SelectYourUserType") }}</div>
        <el-button-group>
          <el-button type="primary" @click="userType = 'athlete'">{{ $tc("message.Athlete",1) }}</el-button>
          <el-button type="primary" @click="userType = 'supporter'">{{ $tc("message.Supporter") }}</el-button>
        </el-button-group>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <component :is="forms[userType]"></component>
    </el-row>
    <el-row>
      <div class="text-center">{{ $tc("message.AlreadyAccount") }}
        <router-link :to="{ name: 'login'}" class="is-main-color">{{ $tc("message.LogIn") }}</router-link>
      </div>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
import MinimalLayout from '@/layout/MinimalLayout.vue'
import AthleteRegistrationForm from '../components/AthleteRegistrationForm.vue'
import SupporterRegistrationForm from '../components/SupporterRegistrationForm.vue'

export default {
  name: 'Registration',
  data() {
    return {
      forms: {
        athlete: 'gb-athlete-registration',
        supporter: 'gb-supporter-registration'
      },
      userType: 'supporter'
    }
  },
  components: {
    'gb-minimal-layout': MinimalLayout,
    'gb-athlete-registration': AthleteRegistrationForm,
    'gb-supporter-registration': SupporterRegistrationForm
  }
}
</script>

<style type="scss" scoped>
.registrationBox {
  margin-bottom: 20px;
}
</style>
