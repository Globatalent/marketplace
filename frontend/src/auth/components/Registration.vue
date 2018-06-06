<template>
  <gb-minimal-layout>
    <!--
      TODO @kike: Ask user if they are an athlete or a supporter, then show the appropriate form. Show the supporter one by default
    -->
    Select your user type:
    <el-button @click="userType = 'athlete'">Athlete</el-button>
    <el-button @click="userType = 'supporter'">Supporter</el-button>
    <component :is="forms[userType]"></component>
  </gb-minimal-layout>
</template>

<script>
  import MinimalLayout from '@/layouts/MinimalLayout.vue'
  import AthleteRegistrationForm from './AthleteRegistrationForm.vue'
  import SupporterRegistrationForm from './SupporterRegistrationForm.vue'

  export default {
    name: 'Registration',
    data () {
      return {
        forms: {
          athlete: 'gb-athlete-registration',
          supporter: 'gb-supporter-registration',
        },
        userType: 'supporter'
      }
    },
    components: {
      'gb-minimal-layout': MinimalLayout,
      'gb-athlete-registration': AthleteRegistrationForm,
      'gb-supporter-registration': SupporterRegistrationForm,
    }
  }
</script>

<style scoped>
</style>
