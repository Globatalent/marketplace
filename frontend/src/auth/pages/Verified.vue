<template>
  <gb-minimal-layout>
  </gb-minimal-layout>
</template>

<script>
import router from '@/router.js'
import MinimalLayout from '@/layout/MinimalLayout.vue'

export default {
  name: 'Verified',
  props: ['verificationCode'],
  data() {
    return {}
  },
  components: {
    'gb-minimal-layout': MinimalLayout
  },
  methods: {
    verifyEmail() {
      this.$store.dispatch('users/verify', this.verificationCode).then( () => {
        router.push({ name: 'login' })
      }).catch( error => {
        router.push({name: 'not-found'})
      })
    }
  },
  mounted() {
    this.verifyEmail();
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
