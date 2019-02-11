<template>
  <gb-base-layout>
    <el-row>
      <el-col :xs="24">
        <div class="beginBlock text-center">
          <h3 class="beginBlock-title">{{ $tc('message.WeBringTheTalent') }}</h3>
          <h4 class="beginBlock-subTitle" v-html="$t('message.TheFirstSportsCryptoExchange')"></h4>
        </div>
      </el-col>
    </el-row>
        <div class="campaignList-startBlock" style="padding-top:0px;border-top:hidden;">
      <div class="campaignList-startBlock-container">
        <div class="campaignList-startBlock-sentence">
          <router-link :to="{ name: 'campaign.create'}" class="is-main-color">
            <el-button type="primary" class="startFreeButton" size="big" v-html="$tc('message.StartCampaignNow')"></el-button>
          </router-link>
        </div>
      </div>
    </div>
    <!-- <el-row>
      <el-col :xs="24">
        <ul class="campaignsFilter">
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">54</span><span
            class="campaignsFilter-item-text">{{ $tc('message.AllCampaigns') }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">21</span><span
            class="campaignsFilter-item-text">{{ $tc('message.LaunchingSoon') }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">44</span><span
            class="campaignsFilter-item-text">{{ $tc('message.New') }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">11</span><span
            class="campaignsFilter-item-text">{{ $tc('message.Ending') }}</span></li>
          <li class="campaignsFilter-item"><span class="campaignsFilter-item-number">11</span><span
            class="campaignsFilter-item-text">{{ $tc('message.Hot') }}</span></li>
        </ul>
      </el-col>
    </el-row> -->
    <!--<el-row class="el-row--flex" type="flex">-->
    <el-row>
      <!--<el-col :xm="12">
          <el-input :placeholder='$tc("message.Search")' class="searchList-input" v-model="search"
                    @keyup.native="onSearch">
            <i slot="suffix" class="el-input__icon el-icon-search"></i>
          </el-input>
      </el-col>
      <el-col :xm="4">
          <el-select :placeholder='$tc("message.BySport")' class="searchList-option" v-model="sport" @change="filter()">
            <el-option :label="$tc('message.BySport')" :value="null"></el-option>
            <el-option v-for="(sport, index) in sports" :key="index" :label="sport.name" :value="sport.id">
            </el-option>
          </el-select>
      </el-col>
      <el-col :xm="4">
          <el-select :placeholder='$tc("message.ByCountry")' class="searchList-option" v-model="country"
                     @change="filter()">
            <el-option :label="$tc('message.ByCountry')" :value="null"></el-option>
            <el-option v-for="item in countries" :label="item.name" :value="item.code" :key="item.code">
            </el-option>
          </el-select>
      </el-col>
      <el-col :xm="4">
          <el-select :placeholder='$tc("message.AllTypes")' class="searchList-option" v-model="kind" @change="filter()">
            <el-option :label="$tc('message.AllTypes')" :value="null"></el-option>
            <el-option :label="$tc('message.Athletes')" :value="'athlete'"></el-option>
            <el-option :label="$tc('message.Clubs')" :value="'club'"></el-option>
          </el-select>
      </el-col>-->
      <el-col>
        <masonry :cols="{default: 4, 750: 2, 500: 1}" :gutter="{default: '40px', 750: '20px'}">
          <div class="filter-box">
            <el-input :placeholder='$tc("message.Search")' class="searchList-input" v-model="search"
                      @keyup.native="onSearch">
              <i slot="suffix" class="el-input__icon el-icon-search"></i>
            </el-input>
          </div>
          <div class="filter-box">
            <el-select :placeholder='$tc("message.BySport")' class="searchList-option" v-model="sport" @change="filter()">
              <el-option :label="$tc('message.BySport')" :value="null"></el-option>
              <el-option v-for="(sport, index) in sports" :key="index" :label="sport.name" :value="sport.id">
              </el-option>
            </el-select>
          </div>
          <div class="filter-box">
            <el-select :placeholder='$tc("message.ByCountry")' class="searchList-option" v-model="country"
                      @change="filter()">
              <el-option :label="$tc('message.ByCountry')" :value="null"></el-option>
              <el-option v-for="item in countries" :label="item.name" :value="item.code" :key="item.code">
              </el-option>
            </el-select>
          </div>
          <div class="filter-box">
            <!-- <el-select :placeholder='$tc("message.ByCountry")' class="searchList-option" v-model="country"
                      @change="filter()">
              <el-option :label="$tc('message.ByCountry')" :value="null"></el-option>
              <el-option v-for="item in countries" :label="item.name" :value="item.code" :key="item.code">
              </el-option>
            </el-select> -->
              <el-select :placeholder='$tc("message.AllTypes")' class="searchList-option" v-model="kind" @change="filter()">
            <el-option :label="$tc('message.AllTypes')" :value="null"></el-option>
            <el-option :label="$tc('message.Athletes')" :value="'athlete'"></el-option>
            <el-option :label="$tc('message.Clubs')" :value="'club'"></el-option>
          </el-select>
          </div>
        </masonry>
      </el-col>
    </el-row>
    <el-row v-loading.fullscreen="loadingCampaigns" v-if="campaigns.length > 0">
      <el-col>
        <masonry :cols="{default: 4, 992: 3, 750: 2, 500: 1}" :gutter="{default: '40px', 750: '20px'}">
          <gb-campaign-list-card v-for="campaign in campaigns" :key="campaign.id"
                                 :campaign="campaign"></gb-campaign-list-card>
        </masonry>
      </el-col>
    </el-row>
    <div class="campaignList-noResults text-center" v-else>
      <h2>{{ $tc('message.NoResults') }}</h2>
    </div>
    <div class="campaignList-startBlock">
      <div class="campaignList-startBlock-container">
        <div class="campaignList-startBlock-sentence">
          <router-link :to="{ name: 'campaign.create'}" class="is-main-color">
            <el-button type="primary" class="startFreeButton" size="big" v-html="$tc('message.StartCampaignNow')"></el-button>
          </router-link>
        </div>
      </div>
    </div>
    <el-row>
      <el-col class="news-title">
        <div class="beginBlock text-center">
          <h3 id="news" class="beginBlock-subTitle">{{$tc('message.campaignNewsTitle')}}</h3>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col>
        <carousel :autoplay="true" :loop="true" :scroll-per-page="false" :per-page-custom="[[1280, 4], [992, 3], [750, 2], [320, 1]]" :autoplay-timeout=6000>
          <slide v-for="article in news" :key="article[0]">
            <el-card :body-style="{ padding: '0px', display: 'flex', 'flex-direction': 'column' }">
              <div :class="['campaign-image', {'is-placeholder-image': !article[3]}]" :style="article[3] ? {backgroundImage:'url('+article[3]+')'} : {}">
              </div>
              <div class="campaign-info">
                <div class="clearfix campaign-nameBlock">
                  <el-row>
                    <el-col :span="24">
                        <span class="campaign-name">{{article[1]}}</span>
                    </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                      <div class="campaign-subtitle news-content show-more-container" :class="{ extended: isExtended }">
                        <span v-if="article[2]" v-html="getDescription(article[0], article[2])"></span>
                        <a class="show-more-msg" @click="showMore(article[0])" v-if="article[2] && article[2].length > 140"> {{showMoreMsg(article[0])}}</a>
                      </div>
                    </el-col>
                  </el-row>
                </div>
              </div>
            </el-card>
          </slide>
        </carousel>
      </el-col>
    </el-row>
  </gb-base-layout>
</template>

<script>
import Vue from 'vue'
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
import CampaignListCard from '@/campaigns/components/CampaignListCard.vue'
  import countries from '@/base/helpers/countries'
  import VueI18n from 'vue-i18n'
  import { Carousel, Slide } from 'vue-carousel';

  export default {
    name: 'CampaignList',
    components: {
      'gb-base-layout': BaseLayout,
      'gb-campaign-list-card': CampaignListCard,
       Carousel,
        Slide
    },
    data () {
      return {
        allCountries: countries,
        search: null,
        sport: null,
        country: null,
        kind: null,
        errorMessage: '',
        loadingCampaigns: false,
        news: null,
        isExtended: ''
      }
    },
    computed: {
      ...mapGetters({
        sports: 'campaigns/sports',
        campaigns: 'campaigns/campaigns',
        countryCodes: 'campaigns/countries',
        pagination: 'campaigns/pagination',
        user: 'users/user'
      }),
      countries () {
        let countriesWithLabels = []
        this.countryCodes.forEach(country => {
          countriesWithLabels.push({
            code: country,
            name: this.allCountries[country]
          })
        })
        return countriesWithLabels.sort((a, b) => (a.name > b.name ? 1 : (b.name > a.name) ? -1 : 0))
      }
    },
    created () {
      this.$store.commit('campaigns/sports', [])
      this.$store.dispatch('campaigns/sports')
      this.$store.dispatch('campaigns/countries')
      this.initial()
    },
    mounted () {
      this.checkScroll()
      Vue.axios
      .get('https://web.globatalent.com/wp-json/wp/v2/posts?_embed')
      .then(response => (
        this.news = response.data.map( 
          post => [
            post.id, 
            post.title.rendered, 
            post.content.rendered, 
            post._embedded['wp:featuredmedia'][0]['source_url'], 
          ]
        )
      ))
    },
    methods: {
      initial () {
        // Load initial page of campaigns
        this.$store.commit('campaigns/campaigns', [])
        if (!!this.user) {
          this.$store.dispatch('users/fetchUser').then(() => {
            this.$store.dispatch('campaigns/list', {
              filters: {active: 'True'}
            })
          })
        } else {
          this.$store.dispatch('campaigns/list', {
            filters: {
              active: 'True'
            }
          })
          .then(() => {
            console.log(this.campaigns.sort((a,b) => b.rating - a.rating))
          })
        }
      },
      onSearch (event) {
        // Update the campaign list using the search
        if (event.keyCode === 13) {
          this.filter()
        }
      },
      filter () {
        let filters = {
          active: 'True'
        }
        if (!!this.search && this.search !== '') filters.search = this.search
        if (!!this.sport && this.sport !== '') filters.sport = this.sport
        if (!!this.country && this.country !== '') filters.country = this.country
        if (!!this.kind && this.kind !== '') filters.kind = this.kind
        this.$store.dispatch('campaigns/list', {filters: filters})
      },
      checkScroll () {
        window.onscroll = () => {
          let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight >= document.documentElement.offsetHeight - 500

          // if (bottomOfWindow && !this.loadingCampaigns) {
          if (!this.loadingCampaigns) {
            // this.loadingCampaigns = true
            // Gets a new page of campaigns and push them to the current list
            if (!!this.pagination.next) {
              this.$store.dispatch('campaigns/list', {
                filters: {active: 'True'},
                url: this.pagination.next,
                push: true
              }).then(() => {this.loadingCampaigns = false})
            } else {
              this.loadingCampaigns = false
            }
          }
        }
      },
      showMore(id) {
        this.isExtended == id ? this.isExtended = '' : this.isExtended = id
      },
      showMoreMsg(id) {
        return this.isExtended == id ? this.$tc("message.showLess") : this.$tc("message.showMore");
      },
      getDescription(id, desc) {
        return this.isExtended == id ? desc : (desc.length > 140 ? desc.substring(0,140)+' ...' : desc);
      }
    }
  }

</script>

<style lang="scss" scoped>
  @import '../../scss/variables.scss';

  .beginBlock {
    background: url('../../assets/img/background-list-title.png');
    background-repeat: no-repeat;
    background-position: center;
  }

  .filter-box {
    margin-bottom: 15px;
  }

  .searchList-option {
    width: 100%;
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
    font-family: 'Aller';
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
    width: auto;
    font-size: 14px;
    font-family: 'Aller';
    font-weight: bold;
    position: relative;
    top: 6px;
  }

  .el-card {
    border-radius: 8px;
    //height: 470px;
    margin: 0 20px;
    margin-bottom: 35px;
    box-shadow: none !important;


    a:hover {
      text-decoration: none;
    }
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

  .show-more-msg{
    color: $--color-primary !important;
    background: white;
    position: absolute;
    bottom: 0;
    left: 0;
    cursor: pointer;
  }
  .show-more-container {
    overflow: hidden;
    transition: all .3s ease-out;
  }
  .show-more-container.extended {
    max-height: 100%;
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
    font-family: 'Aller Regular';
    padding-bottom: 30px;
  }

  .campaign-info {
    color: #687173;
    font-size: 13px;
    display: flex;
    flex-direction: column;
    min-height: 220px;
  }

  .campaign-nameBlock {
    padding: 25px 20px 15px 20px;
    min-height: 170px;
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
    float: right;
    position: absolute;
    right: 10px;
    bottom: 10px;
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
    font-family: 'Aller Bold';
  }

  .campaign-progress-info-funding-qty {
    font-family: 'Aller Regular';
  }

  .fulltext p,
.less {
	display: none;
}

.fulltext:target p,
.fulltext:target .less {
	display: block;
}

.fulltext:target .more {
	display: none;
}
.news-title {
  padding-top: 60px;
}
.news-content {
  min-height: 120px;
}
</style>
