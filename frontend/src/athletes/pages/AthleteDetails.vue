<template>
  <gb-base-layout>
    <div class="container">
      <el-row type="flex" justify="center">
        <el-col :xs="24">
          <el-carousel :interval="4000" trigger="click" height="400px" indicator-position="outside">
            <el-carousel-item v-for="(item, itemIndex) in athlete.pictures" :key="itemIndex">
              <img :src="item.image" alt="">
            </el-carousel-item>
          </el-carousel>
          <div class="title">
            <span class="athlete-sport">{{athlete.sport}}</span>
            <!-- <h4>
              <i class="fas fa-globe-africa"></i> {{athlete.country}}
              <i class="fas fa-mars m-l-15" v-if="athlete.sex === 'MALE'"></i>
              <i class="fas fa-venus" v-else></i>
              {{athlete.sport}}
            </h4> -->
          </div>
        </el-col>
      </el-row>
      <div>
        <h1 class="athlete-name">{{athlete.firstName}} {{athlete.lastName}}</h1>
        <div class="athlete-details-container">
          <div class="athlete-actions-column">
            <div v-if="isSupporter()">
              <el-button v-if="athlete.following" type="primary" class="m-b-15" @click="setFollowingAthlete()">
                <i class="fas fa-heart"></i> {{$tc('message.Following')}}
              </el-button>
              <el-button v-else class="m-b-15" @click="setFollowingAthlete()">
                <i class="far fa-heart"></i> {{$tc('message.Follow')}}
              </el-button>
            </div>
            <div v-if="!!token.code">
              <h3>{{$tc('message.Token')}}: {{ token.code }}</h3>
              <el-row>
                <el-col :span="12">
                  <h4 class="small-title">{{$tc('message.Price')}}</h4>
                  <p>{{ token.unitPrice }} {{ token.currency }}</p>
                </el-col>
                <el-col :span="12">
                  <h4 class="small-title text-right">{{$tc('message.Collected')}}</h4>
                  <p class="text-right">{{collected()}} GBT</p>
                </el-col>
              </el-row>
              <div class="progress m-b-15 clearfix">
                <el-progress text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress" v-if="progress < 100"></el-progress>
                <el-progress text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress" status="success" v-if="progress >= 100"></el-progress>
                <div class="float-right">
                  <span class="small-title">Goal: {{ token.amount }} GBT</span>
                </div>
              </div>
              <el-button type="primary" class="is-full-width" size="big" v-if="isSupporter()" @click="goToInvest(athlete)">
                <i class="fas fa-money-bill"></i> {{$tc('message.Invest')}}
              </el-button>
            </div>
          </div>
          <div class="athlete-info-column">
            <!-- <div>{{$tc('message.Age')}}: {{athlete.age}}</div> -->
            <p>{{athlete.biography}}</p>

            <h4>{{$tc('message.Link',2)}}</h4>
            <p v-for="(link, linkIndex) in athlete.links" :key="linkIndex">
              <a :href="link.url" :title="link.name" target="_blank">
                {{link.name}} <i class="fas fa-external-link-alt"></i>
              </a>
            </p>
          </div>
        </div>
      </div>

    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'

export default {
  name: 'AthleteDetails',
  components: {
    'gb-base-layout': BaseLayout
  },
  data() {
    return {
      token: {}
    }
  },
  computed: {
    ...mapGetters({
      athlete: 'athletes/athlete',
      user: 'users/user'
    }),
    progress() {
      if (!!this.token) {
        return Math.round(this.token.progression * 100)
      }
      return 0
    }
  },
  created() {
    const id = this.$route.params.athleteId
    this.$store.dispatch('athletes/fetch', id).then(() => {
      this.token = this.athlete.token ? this.athlete.token : {}
    })
  },
  methods: {
    isSupporter() {
      return !!this.user && !!this.user.supporter
    },
    setFollowingAthlete() {
      if (this.isSupporter()) {
        this.athlete.following = !this.athlete.following
        this.$store
          .dispatch('athletes/follow', this.athlete.id)
          .catch(error => {
            console.log(error)
          })
      }
    },
    collected() {
      if (!!this.token) {
        return this.token.amount - this.token.remaining
      }
      return 0
    },
    goToInvest(athlete) {
      router.push({ name: 'athlete.invest', params: { athleteId: athlete.id } })
    }
  }
}
</script>

<style scoped>
@import '../../scss/variables.scss';

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

.container {
  margin-top: -20px;
}

.title {
  margin: -110px 20px 0;
  color: #fff;
  text-shadow: 0 2px 5px black;
  position: relative;
  z-index: 200;
  height: 110px;
}

h1 {
  font-size: 3em;
  margin-bottom: 0;
  line-height: 1em;
  padding: 0;
}

.el-carousel__indicators {
  z-index: 300;
  float: right;
}

.athlete-details-container {
  display: flex;
  justify-content: flex-start;
  flex-flow: row;
}

.athlete-actions-container {
  flex: 1 1 auto;
  min-width: 320px;
  position: relative;
  order: 2;
  padding-left: 20px;
  padding-top: 35px;
}

.small-title {
  color: #999;
  font-size: 0.9em;
  line-height: 0.9em;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 0;
}

.el-button {
  font-size: initial;
}

a:hover {
  text-decoration: none;
}

@media screen and (min-width: 800px) {
  .athlete-details-container {
    display: flex;
    justify-content: flex-start;
    flex-flow: row;
  }

  .athlete-actions-column {
    flex: 1 1 auto;
    min-width: 320px;
    position: relative;
    order: 2;
    padding-left: 20px;
    padding-top: 25px;
  }

  .athlete-info-column {
    flex: 2 1 auto;
    order: 1;
    padding: 20px 0;
  }

  .athlete-actions {
    width: 300px;
    position: fixed;
    padding: 20px;
    box-sizing: border-box;
    border: 1px solid #eee;
    border-radius: 10px;
  }
}
</style>
