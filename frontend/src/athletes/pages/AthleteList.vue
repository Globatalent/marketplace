<template>
    <gb-base-layout>
      Athlete List Page
      <!--
      TODO @kike: Show a list of athletes. You can use the card component (el-card).

      The data you'll get from an athlete is:
        - firstName - string
        - lastName - string
        - image - string (url to the athlete image)
        - sport - string
        - country - string
        - following: boolean

      The name and the image must be a link to the athlete details page (TBD)
      There must be a button for the follow/unfollow functionality

      - Use Masonry
      - Use Element cards
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
