<template>
  <gb-base-layout>
    <!--
      TODO @kike: Supporters must see a list of the athletes they are following and the alerts they have set up
      - We will have 2 tables, one of the following athletes and one with all
      -->
    <datatable v-bind:columns="columns" v-bind:data="athletes" v-bind:total="total" v-bind:query="query" />
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
// import mockData from '@/_mockData'

export default {
  name: 'SupporterProfile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      columns: [
        { title: 'User ID', field: 'id', sortable: true },
        { title: 'First Name', field: 'firstName' },
        { title: 'Last Name', field: 'lastName', sortable: true },
        { title: 'Sport', field: 'sport' },
        { title: 'Country', field: 'country' }
      ],
      data: [],
      total: 6,
      query: { "limit": 10, "offset": 0, "sort": "id", "order": "asc" },
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
  watch: {
    query: {
      handler (query) {
        // mockData(query).then(({ rows, total }) => {
        //   this.data = rows
        //   this.total = total
        // })
      },
      deep: true
    }
  }
}
</script>

<style scoped>
</style>
