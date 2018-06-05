<template>
  <gb-minimal-layout>
    Login page
    <!--
      TODO @kike: Show a form with the following fields:
        - email: input type email, required
        - password: input type password, required
        - submit button

     It should be centered (horizontally and vertically) and not be too wide
    -->
  </gb-minimal-layout>
</template>

<script>
  import MinimalLayout from '@/layouts/MinimalLayout.vue'

  export default {
    name: 'Login',
    components: {
      'gb-minimal-layout': MinimalLayout
    }
  }
</script>

<style scoped>
</style>
