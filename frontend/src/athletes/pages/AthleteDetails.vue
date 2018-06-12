<template>
  <gb-base-layout>
    <!--
      TODO @kike: Show athlete details with the following order:
        - Carousel with the images of the athlete
        - Name of the athlete with an edit button (will add hide/show logic)
        - Other athlete data: Country, age and sport
        - List of links: name and url
      -->
    <el-row type="flex" justify="center">
      <el-col :xs="24" :sm="12" :md="24" class="text-center">
        <h2>Athlete Id:{{athlete.id}} Details</h2>
        <el-carousel :interval="4000" type="card" height="200px">
          <el-carousel-item v-for="item in 6" :key="item">
            <h3>{{ item }}</h3>
          </el-carousel-item>
        </el-carousel>
        <h3>{{athlete.firstName}} {{athlete.lastName}}</h3>
        <el-button type="primary">Edit</el-button>
        <div>Country: {{athlete.country}}</div>
        <div>Age: {{athlete.age}}</div>
        <div>Sport: {{athlete.sport}}</div>
        <h4>Links</h4>
        <ul>
          <li v-for="(link, index) in athlete.links" :key="index">
            <a :href="link.link" :title="link.linkTitle" target="_blank">{{link.linkTitle}}</a>
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
        id: '',
        firstName: 'Jon',
        lastName: 'Snow',
        country: 'Winterfell',
        date: '01/01/2000',
        sport: 'destroy white walkers',
        sex: 'male',
        age: '33',
        links: [
          {
            linkTitle: 'YouTube',
            link: 'https://www.youtube.com/?gl=ES&hl=es'
          },
          {
            linkTitle: 'Facebook',
            link: 'https://www.facebook.com/'
          },
          {
            linkTitle: 'Twitter',
            link: 'http://twitter.com/'
          },
          {
            linkTitle: 'Instagram',
            link: 'https://www.instagram.com/?hl=es'
          }
        ]
      }
    }
  },
  created() {
    console.log('athlete id:' + this.$route.params.athleteId)
    this.athlete.id = this.$route.params.athleteId
  }
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
