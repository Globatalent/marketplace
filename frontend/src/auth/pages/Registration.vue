<template>
  <gb-minimal-layout>
    <!--
      TODO @kike: Ask user if they are an athlete or a supporter, then show the appropriate form. Show the supporter one by default
    -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="6" :xl="4" class="loginBox text-center">
        <span>Select your user type:</span>
        <el-button @click="userType = 'athlete'">Athlete</el-button>
        <el-button @click="userType = 'supporter'">Supporter</el-button>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <component :is="forms[userType]"></component>
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
</style>
