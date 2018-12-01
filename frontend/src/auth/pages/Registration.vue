<template>
  <gb-minimal-layout>
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="12" class="text-center loginBox">
      <router-link :to="{ name: 'campaign.list'}">
          <img class="logo" src="~@/assets/img/Globatalent-logo-vert.png" />
        </router-link>
      <component :is="form"></component>
      </el-col>
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
