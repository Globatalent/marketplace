<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Connect data to the backend
      -->
    <masonry :cols="{default: 3, 750: 2, 500: 1}" :gutter="{default: '15px', 750: '15px'}">
      <el-card :body-style="{ padding: '0px' }" v-for="(athlete, index) in athletes" :key="index" style="margin-bottom:15px;">
        <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}"><img v-bind:src="getPicture(athlete)" class="image"></router-link>
        <div style="padding: 14px;">
          <div class="top clearfix">
            <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}">
              <span>{{athlete.firstName}} {{athlete.lastName}}</span>
            </router-link>
            <div class="likeButton" v-if="isSupporter()" @click="setFollowingAthlete(index,athlete)">
              <i class="fas fa-heart likeIcon is-following" v-if="athlete.following"></i>
              <i class="far fa-heart likeIcon" v-else></i>
            </div>
          </div>
          <div>{{athlete.sport}}</div>
          <div>{{Math.round(athlete.progression * 100)}}%</div>
          <div class="bottom clearfix">
          </div>
        </div>
      </el-card>
    </masonry>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'


export default {
  name: 'AthleteProfile',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      errorMessage: '',
    }
  },
  computed: {
    ...mapGetters({
      athletes: 'athletes/athletes',
      pagination: 'athletes/pagination',
      user: 'users/user',
    }),
  },
  created() {
    this.initial();
  },
  methods: {
    initial() {
      // Load initial page of athletes
      this.$store.dispatch('athletes/list');
    },
    scroll() {
      // Gets a new page of athletes and push them to the current list
      if (!!this.pagination.next) {
        this.$store.dispatch('athletes/list', {url: this.pagination.next, push: true});
      }
    },
    isSupporter() {
      return !!this.user && !!this.user.supporter
    },
    setFollowingAthlete(index, athlete) {
      if (this.isSupporter()) {
        athlete.following = !athlete.following
        this.$store.dispatch('athletes/follow', athlete.id)
          .catch(error => {
            console.log(error)
          })
      }
    },
    likeIconClass(following) {
      console.log(`This following: ${following}`)
      if (following) {
        return 'heart'
      } else {
        return 'thumbs-up'
      }
    },
    getPicture(athlete) {
      const picture = athlete.pictures[0]
      if (picture) {
        return picture.image
      } else {
        return null
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
