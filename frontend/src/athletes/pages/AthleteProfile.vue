<template>
    <gb-base-layout>
      Athlete Profile Page
      <!--
      TODO @kike: Here the athlete must be able to upload their data and add pictures and links (to videos, social networks, etc)
      A picture has only the image. We can send them one by one or in bulk
      A link has a name and a url, and they can add as much as they want

      They must also be able to edit the data they submitted in the registration form (except the email for now)
      -->
    </gb-base-layout>
</template>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'

  export default {
    name: 'AthleteProfile',
    components: {
      'gb-base-layout': BaseLayout
    }
  }
</script>

<style scoped>

</style>
