<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <component :is="form"></component>
    </el-row>
  </gb-minimal-layout>
</template>

<script>
import MinimalLayout from '@/layout/MinimalLayout.vue'
import RegistrationForm from '../components/RegistrationForm.vue'

export default {
  name: 'Registration',
  data() {
    return {
      form: 'gb-registration',
      userType: 'supporter'
    }
  },
  components: {
    'gb-minimal-layout': MinimalLayout,
    'gb-registration': RegistrationForm
  }
}
</script>

<style type="scss" scoped>
.registrationBox {
  margin-bottom: 20px;
}
</style>
