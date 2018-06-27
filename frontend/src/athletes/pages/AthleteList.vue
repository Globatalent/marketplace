<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Connect data to the backend
      -->
    <masonry :cols="{default: 3, 750: 2, 500: 1}" :gutter="{default: '15px', 750: '15px'}">
      <el-card :body-style="{ padding: '0px' }" v-for="(athlete, index) in athletes" :key="index" style="margin-bottom:15px;">
        <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}"><img v-bind:src="athlete.image" class="image"></router-link>
        <div style="padding: 14px;">
          <div class="top clearfix">
            <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}">
              <span>{{athlete.first_name}} {{athlete.last_name}}</span>
            </router-link>
            <div class="likeButton" @click="setFollowingAthlete(index,athlete)">
              <i class="fas fa-heart likeIcon is-following" v-if="athlete.following"></i>
              <i class="far fa-heart likeIcon" v-else></i>
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
  created() {
    this.axios.get('http://localhost:8000/api/v1/athletes/').then((response) => {
      this.athletes = response.data.results
        // commit('setUser', UserTransformer.fetch(response.data))
        // resolve(response)
      }).catch((error) => {
        // reject(error)
        console.log(error)
      })
  },
  data() {
    return {
      errorMessage: '',
      athletes: []
    }
  },
  methods: {
    setFollowingAthlete(index, athlete) {
      athlete.following = !athlete.following
      this.axios
        .post('http://localhost:8000/api/v1/athlete/'+athlete.id+'/following/')
        .then(response => {
          console.log('Favorited athlete',response)
          // this.$set(this.athletes, index, athlete)
        })
        .catch(error => {
          console.log(error)
        })
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

<style lang="scss" scoped>
.likeButton {
  margin-left: 15px;
  float: right;
  cursor: pointer;
}
.likeIcon {
  font-size: 20px;
  transition: all 0.2s ease-in;
  &.is-following {
    transform: scale(1.2);
    color: red;
  }
}
</style>
