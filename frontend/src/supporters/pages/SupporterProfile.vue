<template>
  <gb-base-layout>
    <!--
      TODO @kike: Supporters must see a list of the athletes they are following and the alerts they have set up
      - We will have 2 tables, one of the following athletes and one with all 
      -->
  </gb-base-layout>
</template>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'

  export default {
    name: 'SupporterProfile',
    components: {
      'gb-base-layout': BaseLayout
    },
    data() {
    return {
      athletes: [
        {
          id: '1',
          firstName: 'Jon',
          lastName: 'Snow',
          image: 'https://cde.laprensa.e3.pe/ima/0/0/1/3/9/139652.jpg',
          sport: 'destroy white walkers',
          country: 'Winterfell',
          following: false
        },
        {
          id: '2',
          firstName: 'Daenerys',
          lastName: 'Targaryen',
          image: 'https://i.ytimg.com/vi/PC-Z2ZU66jc/maxresdefault.jpg',
          sport: 'play with fire',
          country: 'The Crownlands',
          following: true
        },
        {
          id: '3',
          firstName: 'Tyrion',
          lastName: 'Lannister',
          image: 'https://media.giphy.com/media/idhHzlOqNA7Sw/giphy.gif',
          sport: 'drink',
          country: 'The Crownlands',
          following: true
        },
        {
          id: '4',
          firstName: 'Daenerys',
          lastName: 'Targaryen',
          image: 'https://i.ytimg.com/vi/PC-Z2ZU66jc/maxresdefault.jpg',
          sport: 'play with fire',
          country: 'The Crownlands',
          following: true
        },
        {
          id: '5',
          firstName: 'Tyrion',
          lastName: 'Lannister',
          image: 'https://media.giphy.com/media/idhHzlOqNA7Sw/giphy.gif',
          sport: 'drink',
          country: 'The Crownlands',
          following: true
        },
        {
          id: '6',
          firstName: 'Jon',
          lastName: 'Snow',
          image: 'https://cde.laprensa.e3.pe/ima/0/0/1/3/9/139652.jpg',
          sport: 'destroy white walkers',
          country: 'Winterfell',
          following: false
        }
      ]
    }
  },
  }
</script>

<style scoped>
</style>
