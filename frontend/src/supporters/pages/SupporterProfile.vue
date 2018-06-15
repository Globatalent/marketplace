<template>
  <gb-base-layout>
    <!--
      TODO @kike: Supporters must see a list of the athletes they are following and the alerts they have set up
      - We will have 2 tables, one of the following athletes and one with all
      -->
    <el-col :xs="24" class="">
      <el-tabs type="border-card">
        <el-tab-pane :label="$tc('message.Following')">
          <h3>{{$tc('message.Following')}}</h3>
          <el-table :data="athletes" style="width: 100%">
            <el-table-column prop="id" label="id"></el-table-column>
            <el-table-column prop="firstName" label="firstName"></el-table-column>
            <el-table-column prop="lastName" label="lastName"></el-table-column>
            <el-table-column prop="sport" label="sport"></el-table-column>
            <el-table-column prop="country" label="country"></el-table-column>
            <el-table-column fixed="right" label="Operaciones">
              <template slot-scope="scope">
                <el-button @click="handleClick" type="text" size="small">{{$tc('message.Unfollow')}}</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-tab-pane>
        <el-tab-pane :label="$tc('message.Alert',2)">
          <h3>{{$tc('message.Alert',1)}}</h3>
          <el-table :data="athletes" style="width: 100%">
            <el-table-column prop="id" label="id"></el-table-column>
            <el-table-column prop="firstName" label="firstName"></el-table-column>
            <el-table-column prop="lastName" label="lastName"></el-table-column>
          </el-table>
        </el-tab-pane>
      </el-tabs>
    </el-col>
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
  methods: {
    handleClick() {
      console.log('click')
    }
  }
}
</script>

<style scoped>
</style>
