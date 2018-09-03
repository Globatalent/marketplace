<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Connect data to the backend
      -->
    <masonry :cols="{default: 3, 750: 2, 500: 1}" :gutter="{default: '15px', 750: '15px'}">
      <el-card :body-style="{ padding: '0px' }" v-for="(athlete, index) in athletes" :key="index"
               style="margin-bottom:15px;">
        <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}"><img
          v-bind:src="getPicture(athlete)" class="image"></router-link>
        <div style="padding: 14px;">
          <div class="top clearfix">
            <el-row>
              <el-col :span="20">
                <router-link :to="{ name: 'athlete.details', params: { athleteId: athlete.id }}">
                  <span class="athlete-name">{{athlete.firstName}} {{athlete.lastName}}</span>
                </router-link>
                <div class="athlete-sport">
                  <i class="fas fa-mars" v-if="athlete.sex==='MALE'"></i>
                  <i class="fas fa-venus" v-else></i>
                  {{athlete.sport}}
                </div>
              </el-col>
              <el-col :span="4">
                <div class="likeButton" v-if="isSupporter()" @click="setFollowingAthlete(index,athlete)">
                  <i class="fas fa-eye likeIcon is-following" v-if="athlete.following"></i>
                  <i class="far fa-eye likeIcon" v-else></i>
                </div>
              </el-col>
            </el-row>
          </div>
          <el-progress :text-inside="true" :stroke-width="18" :percentage="progress(athlete)"
                       v-if="progress(athlete) < 100"></el-progress>
          <el-progress :text-inside="true" :stroke-width="18" :percentage="progress(athlete)" status="success"
                       v-if="progress(athlete) >= 100"></el-progress>
          <div class="float-right">
            <span class="goal">Goal: {{ athlete.token.price }}</span>
          </div>
          <div class="bottom clearfix">
            <div>
              <el-button type="primary" class="is-full-width m-t-20" @click="goToDetails(athlete)">See details</el-button>
            </div>
          </div>
        </div>
      </el-card>
    </masonry>
  </gb-base-layout>
</template>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
  import router from '@/router.js'

  export default {
    name: 'AthleteProfile',
    components: {
      'gb-base-layout': BaseLayout
    },
    data () {
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
    created () {
      this.initial()
    },
    methods: {
      initial () {
        // Load initial page of athletes
        this.$store.dispatch('athletes/list', {filters: {state: 'APPROVED'}})
      },
      scroll () {
        // Gets a new page of athletes and push them to the current list
        if (!!this.pagination.next) {
          this.$store.dispatch('athletes/list', {url: this.pagination.next, push: true})
        }
      },
      goToDetails(athlete) {
        router.push({ name: 'athlete.details', params: { athleteId: athlete.id }})
      },
      isSupporter () {
        return !!this.user && !!this.user.supporter
      },
      progress (athlete) {
        if (!!athlete.token) {
          return Math.round(athlete.token.progression * 100)
        }
        return 0
      },
      setFollowingAthlete (index, athlete) {
        if (this.isSupporter()) {
          athlete.following = !athlete.following
          this.$store.dispatch('athletes/follow', athlete.id)
            .catch(error => {
              console.log(error)
            })
        }
      },
      likeIconClass (following) {
        if (following) {
          return 'heart'
        } else {
          return 'thumbs-up'
        }
      },
      getPicture (athlete) {
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
    color: #aaa;
    &.is-following {
      transform: scale(1.2);
      color: #4e87b1;
    }
  }

  .athlete-name {
    font-size: 1.2em;
    line-height: 1em;
  }

  .athlete-sport {
    color: #999;
    font-size: .8em;
    line-height: 1em;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 15px;
  }

  .goal {
    color: #999;
    font-size: 1em;
    line-height: 1em;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: 15px;
  }
</style>
