<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Connect data with the backend
      -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" class="text-center">
        <!-- <h2>Athlete Id:{{athlete.id}} Details</h2> -->
        <el-carousel :interval="4000" type="card" height="200px">
          <el-carousel-item v-for="item in athlete.pictures" :key="item">
            <img :src="item.image" alt="">
          </el-carousel-item>
        </el-carousel>
        <h3>{{athlete.first_name}} {{athlete.last_name}}</h3>
        <el-button type="primary">{{$tc('message.Edit')}}</el-button>
        <div>{{$tc('message.Country')}}: {{athlete.country}}</div>
        <!-- <div>{{$tc('message.Age')}}: {{athlete.age}}</div> -->
        <div>{{$tc('message.Sport')}}: {{athlete.sport}}</div>
        <h4>{{$tc('message.Link',2)}}</h4>
        <ul>
          <li v-for="(link, index) in athlete.links" :key="index">
            <a :href="link.url" :title="link.name" target="_blank">{{link.name}}</a>
          </li>
        </ul>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'AthleteDetails',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      athlete: {
        // id: '',
        // first_name: 'Jon',
        // last_name: 'Snow',
        // country: 'Winterfell',
        // date: '01/01/2000',
        // sport: 'destroy white walkers',
        // sex: 'male',
        // age: '33',
        // links: [
        //   {
        //     linkTitle: 'YouTube',
        //     link: 'https://www.youtube.com/?gl=ES&hl=es'
        //   },
        //   {
        //     linkTitle: 'Facebook',
        //     link: 'https://www.facebook.com/'
        //   },
        //   {
        //     linkTitle: 'Twitter',
        //     link: 'http://twitter.com/'
        //   },
        //   {
        //     linkTitle: 'Instagram',
        //     link: 'https://www.instagram.com/?hl=es'
        //   }
        // ]
      }
    }
  },
  created() {
    this.athlete.id = this.$route.params.athleteId
    this.axios.get('http://localhost:8000/api/v1/athletes/'+this.athlete.id).then((response) => {
      this.athlete = response.data
      }).catch((error) => {
        console.log(error)
      })
  },
}
</script>

<style scoped>
ul {
  margin: 0;
  padding: 0;
  list-style: none;
}
.el-carousel__item h3 {
  color: #475669;
  font-size: 14px;
  opacity: 0.75;
  line-height: 200px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
</style>
