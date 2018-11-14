<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc("message.WeBringTheTalent") }}</h3>
          <h4 class="beginBlock-subTitle" v-html="$t('message.TheFirstSportsCryptoExchange')"></h4>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24">
        <ul class="campaignsFilter">
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">54</span><span class="campaignsFilter-item-text">{{ $tc("message.AllCampaigns") }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">21</span><span class="campaignsFilter-item-text">{{ $tc("message.LaunchingSoon") }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">44</span><span class="campaignsFilter-item-text">{{ $tc("message.New") }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">11</span><span class="campaignsFilter-item-text">{{ $tc("message.Ending") }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">11</span><span class="campaignsFilter-item-text">{{ $tc("message.Hot") }}</span></li>
        </ul>
      </el-col>
    </el-row>
    <el-row>
      <el-col :xs="24">
        <div class="searchList">
          <el-input :placeholder='$tc("message.Search")' class="searchList-input" v-model="search" @keyup.native="onSearch">
            <i slot="suffix" class="el-input__icon el-icon-search"></i>
          </el-input>
          <el-select :placeholder='$tc("message.BySport")' class="searchList-option" v-model="sport" @change="filter()">
            <el-option :label="$tc('message.BySport')" :value="null"></el-option>
            <el-option v-for="(sport, index) in sports" :key="index" :label="sport.name" :value="sport.id">
            </el-option>
          </el-select>
          <el-select :placeholder='$tc("message.ByCountry")' class="searchList-option" v-model="country" @change="filter()">
            <el-option :label="$tc('message.ByCountry')" :value="null"></el-option>
            <el-option v-for="(item, index) in countries" :key="index" :label="allCountries[item]" :value="item">
            </el-option>
          </el-select>
          <el-select :placeholder='$tc("message.AllTypes")' class="searchList-option" v-model="kind" @change="filter()">
            <el-option :label="$tc('message.AllTypes')" :value="null"></el-option>
            <el-option :label="$tc('message.Athletes')" :value="'athlete'"></el-option>
            <el-option :label="$tc('message.Clubs')" :value="'club'"></el-option>
          </el-select>
        </div>
      </el-col>
    </el-row>
    <masonry :cols="{default: 4, 992: 3, 750: 2, 500: 1}" :gutter="{default: '40px', 750: '20px'}" v-if="campaigns.length > 0">
      <el-card :body-style="{ padding: '0px', display: 'flex', 'flex-direction': 'column' }" v-for="(campaign, index) in campaigns" :key="index">
        <router-link :to="{ name: 'campaign.details', params: { campaignId: campaign.id }}">
          <div class="campaign-image" v-if="campaign.image" :style="{backgroundImage:'url('+campaign.image+')'}">
            <div class="campaign-sport" v-if="campaign.sport" :style="'background-color:'+getRandomSportColor(campaign.sport.id)">{{campaign.sport.name}}</div>
          </div>
          <div class="campaign-image is-placeholder-image" v-else>
            <div class="campaign-sport" v-if="campaign.sport" :style="'background-color:'+getRandomSportColor(campaign.sport.id)">{{campaign.sport.name}}</div>
          </div>
        </router-link>
        <div class="campaign-info">
          <div class="clearfix campaign-nameBlock">
            <el-row>
              <el-col :span="24">
                <router-link :to="{ name: 'campaign.details', params: { campaignId: campaign.id }}">
                  <span class="campaign-name">{{campaign.title}}</span>
                </router-link>
              </el-col>
              <!-- <el-col :span="4" class="text-right">
                <img src="~@/assets/img/bandera.png" alt="" class="image campaign-flag">
              </el-col> -->
            </el-row>
            <el-row>
              <el-col>
                <div class="campaign-subtitle"><span v-if="campaign.giveBack">{{campaign.giveBack.length > 50 ? campaign.giveBack.substring(0,50)+" ..." : campaign.giveBack}}</span></div>
              </el-col>
            </el-row>
          </div>

          <div class="campaign-progress">
            <div>
              <div class="campaign-progress-info">
                <div class="campaign-progress-info-funding">
                  <div v-if="!!campaign.token" class="campaign-progress-info-funding-text">{{$tc('message.Funding')}}:<span class="campaign-progress-info-funding-qty"> $ {{ $n(campaign.funds) }}</span></div>
                  <div v-if="!!campaign.token" class="campaign-progress-info-funding-text">{{$tc('message.SoftCapt')}}:<span class="campaign-progress-info-funding-qty"> $ {{ $n(campaign.funds) }}</span></div>
                </div>
                <div class="campaign-progress-rating">
                  <star-rating :rating="campaign.rating" inline read-only :show-rating="false" :star-size="15" :round-start-rating="false"></star-rating>
                </div>
              </div>
              <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress(campaign)" v-if="progress(campaign) < 100"></el-progress>
              <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress(campaign)" status="success" v-if="progress(campaign) >= 100"></el-progress>
            </div>
          </div>
          <div class="clearfix campaign-footer">
            <!-- <router-link :to="{ name: 'campaign.details', params: { campaignId: campaign.id }}">
                <el-button type="primary" class="is-full-width m-t-20">See details</el-button>
              </router-link> -->
            <div class="timeLeft">
              <i class="far fa-clock"></i><span class="timeLeft-text">{{campaign.remaining}} days left</span>
            </div>
            <div class="likeButton" v-if="isLogged" @click="setFollowingCampaign(index, campaign)">
              <el-tooltip class="item" effect="dark" :content="$tc('message.AddFavorites')" placement="bottom">
                <i class="fas fa-heart likeIcon is-following" v-if="campaign.following"></i>
                <i class="far fa-heart likeIcon" v-else></i>
              </el-tooltip>
            </div>
          </div>
        </div>
      </el-card>
    </masonry>
    <div class="campaignList-noResults text-center" v-else>
      <h2>{{ $tc('message.NoResults') }}</h2>
    </div>
    <div class="campaignList-startBlock">
      <div class="campaignList-startBlock-container">
        <div class="campaignList-startBlock-sentence">
          <router-link :to="{ name: 'campaign.create'}" class="is-main-color">
            <h4 class="campaignList-startBlock-sentence1" v-html="$t('message.StartCampaignNow')"></h4>
          </router-link>
          <h5 class="campaignList-startBlock-sentence2">{{$t('message.AlsoGift')}}</h5>
        </div>
        <el-button type="primary" class="startFreeButton" size="big">{{$tc('message.StartFreeTrial')}}</el-button>
      </div>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'
import StarRating from 'vue-star-rating'
import countries from '@/base/helpers/countries'


export default {
  name: 'CampaignList',
  components: {
    'gb-base-layout': BaseLayout,
    StarRating
  },
  data() {
    return {
      allCountries: countries,
      search: null,
      sport: null,
      country: null,
      kind: null,
      errorMessage: ''
    }
  },
  computed: {
    ...mapGetters({
      sports: 'campaigns/sports',
      campaigns: 'campaigns/campaigns',
      countries: 'campaigns/countries',
      pagination: 'campaigns/pagination',
      user: 'users/user'
    }),
    isLogged() {
      return !!this.user
    }
  },
  created() {
    this.$store.commit('campaigns/sports', [])
    this.$store.dispatch('campaigns/sports')
    this.$store.dispatch('campaigns/countries')
    this.initial()
  },
  methods: {
    initial() {
      // Load initial page of campaigns
      this.$store.commit('campaigns/campaigns', [])
      if (!!this.user) {
        this.$store.dispatch('users/fetchUser').then(() => {
          this.$store.dispatch('campaigns/list', {
            filters: { active: 'True' }
          })
        })
      } else {
        this.$store.dispatch('campaigns/list', {
          filters: {
            active: 'True'
          }
        })
        // .then(() => {
        //   console.log(this.campaigns)
        // })
      }
    },
    onSearch(event) {
      // Update the campaign list using the search
      if (event.keyCode === 13) {
        this.filter()
      }
    },
    filter() {
      let filters = {
        active: 'True'
      }
      if (!!this.search && this.search !== "") filters.search = this.search
      if (!!this.sport && this.sport !== "") filters.sport = this.sport
      if (!!this.country && this.country !== "") filters.country = this.country
      if (!!this.kind && this.kind !== "") filters.kind = this.kind
      this.$store.dispatch('campaigns/list', {filters: filters})
    },
    scroll() {
      // Gets a new page of campaigns and push them to the current list
      if (!!this.pagination.next) {
        this.$store.dispatch('campaigns/list', {
          url: this.pagination.next,
          push: true
        })
      }
    },
    getPrice(campaign) {
      return campaign.funds
    },
    progress(campaign) {
      if (!!campaign.token) {
        return Math.round(campaign.token.progression * 100)
      }
      return 0
    },
    setFollowingCampaigns(index, campaign) {
      campaign.following = !campaign.following
      this.$store.dispatch('campaign/follow', campaign.id).catch(error => {
        console.log(error)
      })
    },
    getRandomRating() {
      const precision = 10 // 1 decimals
      let randomResult = 0
      while (randomResult < 4 || randomResult > 5) {
        randomResult =
          Math.floor(
            Math.random() * (10 * precision - 1 * precision) + 1 * precision
          ) /
          (1 * precision)
      }
      return randomResult
    },
    getRandomSportColor(sport) {
      let randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16)
      let localSportsColors
      if (localStorage.sportsColors === undefined) {
        localSportsColors = []
        localStorage.setItem('sportsColors', JSON.stringify(localSportsColors))
      }
      localSportsColors = JSON.parse(localStorage.getItem('sportsColors'))
      if (!localSportsColors[sport]) {
        localSportsColors[sport] = randomColor
      }
      localStorage.setItem('sportsColors', JSON.stringify(localSportsColors))
      return localSportsColors[sport]
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../scss/variables.scss';
.el-card {
  border-radius: 8px;
  height: 470px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  margin-bottom: 35px;
  &:hover {
    box-shadow: 0 5px 16px 0 rgba(0, 0, 0, 0.2);
  }
  a:hover {
    text-decoration: none;
  }
}

.beginBlock {
  background: url('../../assets/img/background-list-title.png');
  background-repeat: no-repeat;
  background-position: center;
}
.likeButton {
  margin-left: 15px;
  float: right;
  cursor: pointer;
}

.likeIcon {
  font-size: 18px;
  transition: all 0.2s ease-in;
  color: #aaa;
  position: relative;
  top: 2px;
  &.is-following {
    transform: scale(1.2);
    color: #a0a8ab;
  }
}

.campaign-image {
  height: 200px;
  overflow: hidden;
  position: relative;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center top;
  &.is-placeholder-image {
    background-image: url('../../assets/img/user-placeholder-circle.png');
    background-size: 60%;
    background-position: center;
  }
}

.campaign-progress {
  overflow: hidden;
  flex-grow: 1;
}

.el-progress {
  margin-top: 10px;
}

.goal {
  color: #999;
  font-size: 1em;
  line-height: 1em;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 15px;
}

.timeLeft {
  display: inline-block;
  font-size: 13px;
  .far {
    margin-right: 10px;
  }
}

.campaign-subtitle {
  font-family: 'OpenSans Regular';
  height: 50px;
}
.campaign-info {
  color: #687173;
  font-size: 13px;
  display: flex;
  flex-direction: column;
}
.campaign-nameBlock {
  padding: 25px 20px 15px 20px;
  border-bottom: 1px solid #f0f0f0;
  min-height: 130px;
}
.campaign-progress {
  padding: 12px 20px 12px 20px;
  border-bottom: 1px solid #f0f0f0;
}
.campaign-footer {
  padding: 10px 20px 10px 20px;
}
.campaign-flag {
  width: 30px;
  height: auto;
  display: inline-block;
}
.campaign-progress-info {
  display: flex;
  flex-direction: row;
}
.campaign-progress-info-funding {
  width: 65%;
}
.campaign-progress-rating {
  width: 35%;
  text-align: right;
}
.campaign-progress-info-funding-text {
  font-family: 'OpenSans Bold';
}
.campaign-progress-info-funding-qty {
  font-family: 'OpenSans Regular';
}
.searchList {
  display: flex;
  flex-direction: row;
  margin-bottom: 35px;
}
.searchList-option {
  margin-left: 30px;
}

.campaignList-startBlock {
  margin: 30px auto;
  border-top: 1px solid $--grey-detailCampaign-border;
  padding-top: 40px;
  display: block;
  width: 100%;
  max-width: 895px;
  font-size: 0px;
}

.campaignList-startBlock-container {
  max-width: 585px;
  display: block;
  margin: 0 auto;
}

.campaignList-startBlock-sentence {
  display: inline-block;
  vertical-align: top;
  text-align: right;
  padding-right: 20px;
  padding-right: 0px;
  width: 70%;
  width: 100%;
  text-align: center;
}

.campaignList-startBlock-sentence1 {
  font-weight: normal;
  font-family: 'OpenSans Regular';
  font-size: 36px;
  line-height: 36px;
  margin: 0;
}

.campaignList-startBlock-sentence2 {
  font-size: 14px;
}

.startFreeButton {
  display: inline-block;
  vertical-align: top;
  width: 30%;
  font-size: 14px;
  font-family: 'OpenSans SemiBold';
  position: relative;
  top: 6px;
  display: none;
}
</style>
