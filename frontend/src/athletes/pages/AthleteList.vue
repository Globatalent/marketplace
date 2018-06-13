<template>
  <gb-base-layout>
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
    <masonry :cols="{default: 3, 750: 2, 500: 1}" :gutter="{default: '15px', 750: '15px'}">
      <el-card :body-style="{ padding: '0px' }" v-for="(athlete, index) in athletes" :key="index" style="margin-bottom:15px;">
        <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}"><img v-bind:src="athlete.image" class="image"></router-link>
        <div style="padding: 14px;">
          <div class="top clearfix">
            <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}">
              <span>{{athlete.firstName}} {{athlete.lastName}}</span>
            </router-link>
            <div class="likeButton" @click="setFollowingAthlete(index,athlete)">
              <icon name="heart" class="likeIcon is-following" scale="2" v-if="athlete.following"></icon>
              <icon name="thumbs-up" class="likeIcon" scale="2" v-else></icon>
              <!-- <icon v-bind:name="likeIconClass(athlete.following)" class="likeIcon" scale="2"></icon> -->
              <div>Following: {{athlete.following}}</div>
            </div>

          </div>
          <div>{{athlete.sport}}</div>
          <div class="bottom clearfix">
          </div>
        </div>
      </el-card>
    </masonry>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'

export default {
  name: 'AthleteProfile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      errorMessage: '',
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
    setFollowingAthlete(index,athlete) {
      athlete.following = !athlete.following;
      this.$set(this.athletes, index, athlete)
    },
    likeIconClass(following) {
      console.log(`This following: ${following}`)
      if (following) {
        return 'heart'
      } else {
        return 'thumbs-up'
      }
    }
  }
}
</script>

<style scoped>
.likeButton {
  margin-left: 15px;
  float: right;
  cursor: pointer;
}
.is-following {
  font-style: regular;
}
</style>
