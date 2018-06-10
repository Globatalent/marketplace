<template>
    <gb-base-layout>
      Athlete Details Page
      <!--
      TODO @kike: Show athlete details with the following order:
        - Carousel with the images of the athlete
        - Name of the athlete with an edit button (will add hide/show logic)
        - Other athlete data: Country, age and sport
        - List of links: name and url
      -->
    </gb-base-layout>
</template>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'

  export default {
    name: 'AthleteDetails',
    components: {
      'gb-base-layout': BaseLayout
    }
  }
</script>

<style scoped>

</style>
