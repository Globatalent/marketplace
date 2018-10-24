<template>
  <gb-base-layout>
    <div class="is-padding-boxed">
      <el-row>
        <el-col>
          <el-breadcrumb separator=">" class="breadcrumbCampaignDetail">
            <el-breadcrumb-item :to="{ path: '/' }">Sports</el-breadcrumb-item>
            <el-breadcrumb-item><a href="/">Football</a></el-breadcrumb-item>
          </el-breadcrumb>
        </el-col>
      </el-row>
    </div>
    <div class="campaignDetails-detailBox">
      <div class="is-padding-boxed">
        <el-row :gutter="40">
          <el-col :xs="24" :md="16" class="campaignDetails-col">
            <div class="campaignDetails-title">
              <h1 class="campaign-name">{{campaign.title}}</h1>
              <img src="~@/assets/img/bandera.png" alt="" class="image campaign-flag">
              <div class="campaign-sport">{{campaign.sport.name}}</div>
              <div class="campaignDetails-timeRemaining">
                <i class="el-icon-time"></i>
                <span class="campaignDetails-timeRemaining-text">30 days left</span>
              </div>
            </div>
            <el-carousel :interval="4000" trigger="click" height="400px" indicator-position="outside">
              <el-carousel-item>
                <img :src="campaign.image" alt="">
              </el-carousel-item>
            </el-carousel>
          </el-col>
          <el-col :xs="24" :md="8" class="campaignDetails-col">
            <div class="campaignDetails-collected">{{collected()}} <span class="campaignDetails-collected-currency">GBT</span><span class="campaignDetails-collected-text">{{$tc('message.Raised')}}</span></div>
            <div class="progress m-b-15 clearfix">
              <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress" v-if="progress < 100"></el-progress>
              <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694" :percentage="progress" status="success" v-if="progress >= 100"></el-progress>
            </div>
            <div class="campaignDetails-invest">Invest in {{campaign.title}}</div>
            <p class="campaignDetails-description">{{campaign.description}}</p>
            <div class="campaignDetails-fundingDetails">
              <div class="campaignDetails-fundingDetails-numbers">
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">Funding:</span>
                    <span class="campaignDetails-fundingDetails-numbers-row-number">$500,000</span>
                  </div>
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">1 M10 token =</span>
                    <span class="campaignDetails-fundingDetails-numbers-row-number">$5</span>
                  </div>
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">Soft Capt:</span>
                    <span class="campaignDetails-fundingDetails-numbers-row-number">$150,000</span>
                  </div>
              </div>
              <div class="campaignDetails-fundingDetails-rating">
                <div class="campaignDetails-fundingDetails-rating-experts"><span class="is-marked is-mark-down">73</span><span class="campaignDetails-fundingDetails-rating-experts-text"> Experts Rating</span></div>
                  <star-rating :rating="getRandomRating()" inline read-only :show-rating="false" star-size="15" :round-start-rating="false" active-color="#419ce1"></star-rating>
              </div>
            </div>

            <el-button type="primary" class="is-full-width" size="big" v-if="!!this.user" @click="goToInvest(campaign)">
              <i class="fas fa-money-bill"></i> {{$tc('message.BuyTokens')}}
            </el-button>
          </el-col>
        </el-row>
      </div>
    </div>
    <div>
      <div class="campaign-details-container">
        <div class="campaign-actions-column">
          <div v-if="!!this.user">
            <el-button v-if="campaign.following" type="primary" class="m-b-15" @click="setFollowingCampaign()">
              <i class="fas fa-heart"></i> {{$tc('message.Following')}}
            </el-button>
            <el-button v-else class="m-b-15" @click="setFollowingCampaign()">
              <i class="far fa-heart"></i> {{$tc('message.Follow')}}
            </el-button>
          </div>

        </div>
        <div class="campaign-info-column">
          <p>{{campaign.description}}</p>

          <h4>{{$tc('message.Link', 2)}}</h4>
          <p v-for="(link, linkIndex) in campaign.links" :key="linkIndex">
            <a :href="link.url" :title="link.url" target="_blank" v-if="!!link.url">
              {{link.url}} <i class="fas fa-external-link-alt"></i>
            </a>
          </p>
        </div>
      </div>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import { mapGetters } from 'vuex'
import router from '@/router.js'
import StarRating from 'vue-star-rating'

export default {
  name: 'CampaignDetails',
  components: {
    'gb-base-layout': BaseLayout,
    StarRating
  },
  data() {
    return {
      token: {}
    }
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
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
    const id = this.$route.params.campaignId
    this.$store.dispatch('campaigns/fetch', id).then(() => {
      this.token = !!this.campaign.token ? this.campaign.token : {}
    })
  },
  methods: {
    setFollowingCampaign() {
      if (!!this.user) {
        this.campaign.following = !this.campaign.following
        this.$store
          .dispatch('campaigns/follow', this.campaign.id)
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
    goToInvest(campaign) {
      router.push({
        name: 'campaign.invest',
        params: { campaigneId: campaign.id }
      })
    },
    getRandomRating(){
      const precision = 10; // 1 decimals
      return Math.floor(Math.random() * (10 * precision - 1 * precision) + 1 * precision) / (1*precision);
    }
  }
}
</script>

<style lang="scss" scoped>
@import '../../scss/variables.scss';

ul {
  margin: 0;
  padding: 0;
  list-style: none;
}

a:hover {
  text-decoration: none;
}

.is-marked{
  display: inline-block;
  border-radius: 5px;
  background-color: $--pink;
  color: white;
  font-family: 'OpenSans Regular';
  font-size: 12px;
}
.is-mark-down{
  &::after{
    content: "<";
    transform: rotate(-90deg);
  }
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

.campaignDetails-detailBox {
  background-color: $--grey-detailCampaign-box;
  border-top: 2px solid $--grey-detailCampaign-border;
  border-bottom: 2px solid $--grey-detailCampaign-border;
  margin-top: 100px;
  .campaignDetails-col {
    position: relative;
    top: -100px;
  }
}
.campaignDetails-title {
  margin-bottom: 20px;
}
.campaign-name {
  display: inline-block;
  font-size: 28px;
  font-family: 'OpenSans Regular';
  color: $--black;
  vertical-align: middle;
}

.campaign-flag {
  max-width: 30px;
  display: inline-block;
  margin-left: 20px;
}

.campaign-sport {
  position: relative;
  left: inherit;
  bottom: inherit;
  margin-left: 20px;
}

.campaignDetails-timeRemaining {
  font-size: 14px;
  color: $--black;
  display: inline-block;
  float: right;
  font-family: 'OpenSans Regular';
}

.el-carousel__indicators {
  z-index: 300;
  float: right;
}

.campaignDetails-collected{
  font-size: 32px;
  line-height: 32px;
  color: $--black;
  font-family: 'OpenSans SemiBold';
  margin-bottom: 20px;
}

.campaignDetails-collected-currency,
.campaignDetails-collected-text{
  font-size: 14px;
  font-family: 'OpenSans Regular';
  color: $--black;
}

.campaignDetails-collected-currency{
  margin-right: 5px;
}

.campaign-details-container {
  display: flex;
  justify-content: flex-start;
  flex-flow: row;
}

.campaign-actions-container {
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

.campaignDetails-invest{
  font-size: 20px;
  font-family: 'OpenSans Regular';
  color: $--black;
  margin-bottom: 10px;
}

.campaignDetails-description{
  font-family: 'OpenSans Regular';
  color: $--grey-title;
  font-size: 14px;
}

.progress{
  margin-bottom: 50px;
}

.campaignDetails-fundingDetails{
  border-top: 1px solid $--grey-detailCampaign-border;
  padding-top: 20px;
  font-family: 'OpenSans Regular';
  font-size: 0;
}

.campaignDetails-fundingDetails-numbers-row-title{
  font-size: 15px;
  color: $--grey-title;
}
.campaignDetails-fundingDetails-numbers{
  display: inline-block;
  width: 60%;
  padding-right: 5px;
}
.campaignDetails-fundingDetails-numbers-row-number{
  font-size: 15px;
  color: $--green-numbers;
}

.campaignDetails-fundingDetails-rating{
  display: inline-block;
  width: 40%;
  border: 1px solid $--grey-detailCampaign-border;
  background: white;
  padding: 5px 10px;
  border-radius: 5px;
}

.campaignDetails-fundingDetails-rating-text{

}

@media screen and (min-width: 800px) {
  .campaign-details-container {
    display: flex;
    justify-content: flex-start;
    flex-flow: row;
  }

  .campaign-actions-column {
    flex: 1 1 auto;
    min-width: 320px;
    position: relative;
    order: 2;
    padding-left: 20px;
    padding-top: 25px;
  }

  .campaign-info-column {
    flex: 2 1 auto;
    order: 1;
    padding: 20px 0;
  }

  .campaign-actions {
    width: 300px;
    position: fixed;
    padding: 20px;
    box-sizing: border-box;
    border: 1px solid #eee;
    border-radius: 10px;
  }
}
</style>
