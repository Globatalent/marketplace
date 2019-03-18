<template>
  <el-card :body-style="{ padding: '0px', display: 'flex', 'flex-direction': 'column' }">
    <router-link :to="{ name: 'campaign.details', params: { campaignId: campaign.id }}">
      <div :class="['campaign-image', {'is-placeholder-image': !campaign.image}]" :style="campaign.image ? {backgroundImage:'url('+campaign.image+')'} : {}">
        <div class="campaign-sport" v-if="campaign.sport"
             :style="'background-color:#'+campaign.sport.color">{{campaign.sport.name}}
        </div>
        <img :src="countryFlag" alt="" class="image campaign-flag">
      </div>
    </router-link>
    <div class="campaign-info">
      <div class="clearfix campaign-nameBlock">
        <el-row>
          <el-col :span="24">
            <router-link :to="{ name: 'campaign.details', params: { campaignId: campaign.id }}">
            <span class="campaign-name" v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.title}}</span>
            <span class="campaign-name" v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.title}}</span>
            <span class="campaign-name" v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.title}}</span>
            <span class="campaign-name" v-else>{{campaign.title}}</span>
            </router-link>
          </el-col>
        </el-row>
        <el-row>
          <el-col>
            <div class="campaign-subtitle show-more-container" :class="{ extended: isExtended }">
            <span v-if="campaign.id == 5 && locale == 'es-ES'">{{getDescription(epfc.description)}}</span>
            <span v-else-if="campaign.id == 4 && locale == 'es-ES'">{{getDescription(zentro.description)}}</span>
            <span v-else-if="campaign.id == 126 && locale == 'es-ES'">{{getDescription(vega.description)}}</span>
            <span v-else>{{getDescription(campaign.description)}}</span>
            <a class="show-more-msg" @click="showMore()" v-if="campaign.id == 5 && locale == 'es-ES' && epfc.description.length > 50">{{showMoreMsg()}}</a>
            <a class="show-more-msg" @click="showMore()" v-else-if="campaign.id == 4 && locale == 'es-ES' && zentro.description.length > 50">{{showMoreMsg()}}</a>
            <a class="show-more-msg" @click="showMore()" v-else-if="campaign.id == 126 && locale == 'es-ES' && vega.description.length > 50">{{showMoreMsg()}}</a>
            <a class="show-more-msg" @click="showMore()" v-else-if="campaign.description && campaign.description.length > 50">{{showMoreMsg()}}</a>
            </div>
          </el-col>
        </el-row>
      </div>

      <div class="campaign-progress">
        <div>
          <div class="campaign-progress-info">
            <div class="campaign-progress-info-funding">
              <div v-if="!!campaign.token" class="campaign-progress-info-funding-text">{{$tc('message.Funding')}}:<span
                class="campaign-progress-info-funding-qty"> $ {{ $n(campaign.funds) }}</span></div>
              <div v-if="!!campaign.token" class="campaign-progress-info-funding-text">{{$tc('message.SoftCapt')}}:<span
                class="campaign-progress-info-funding-qty"> $ {{ $n(campaign.softCap) }}</span></div>
            </div>
            <div class="campaign-progress-rating">
              <star-rating :rating="campaign.rating" inline read-only :show-rating="false" :star-size="15"
                           :round-start-rating="false"></star-rating>
            </div>
          </div>
          <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694"
                       :percentage="progress" v-if="progress < 100"></el-progress>
          <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694"
                       :percentage="progress" status="success" v-if="progress >= 100"></el-progress>
        </div>
      </div>
      <div class="clearfix campaign-footer">
          <div>
        <template v-if="campaign.started < new Date()">
        <el-button class="buy-tokens" type="primary" size="big" v-if="isLogged" v-html="$tc('message.BuyTokens')" @click="goToInvest(campaign)"></el-button>
        <el-button class="buy-tokens" type="primary" size="big" v-else @click="goToLogin()" v-html="$tc('message.BuyTokens')"></el-button>
        </template>
        <div class="timeLeft">
          <i class="far fa-clock"></i>
          <span v-if="campaign.started < new Date()" class="timeLeft-text">{{campaign.remaining}} days left</span>
          <span class="timeLeft-text is-uppercase" v-else>{{ $tc('message.ComingSoon') }}</span>
        </div>
        <div class="likeButton" v-if="isLogged" @click="setFollowingCampaign()">
          <el-tooltip class="item" effect="dark" :content="$tc('message.AddFavorites')" placement="bottom">
            <i class="fas fa-heart likeIcon is-following" v-if="campaign.following"></i>
            <i class="far fa-heart likeIcon" v-else></i>
          </el-tooltip>
        </div>
        </div>
      </div>
    </div>
  </el-card>
</template>


<script>
  import { mapGetters } from 'vuex'
  import Vuex from 'vuex'
  import router from '@/router.js'
  import StarRating from 'vue-star-rating'
  import VueI18n from 'vue-i18n'

  export default {
    name: 'CampaignListCard',
    props: ['campaign'],
    components: {
      StarRating
    },
    data () {
      return {
        isExtended: false,
        redirecting: false,
        locale: this.$i18n.locale,
        zentro: {
          title: 'Zentro Basket Madrid',
          description: 'Accede 6% de la facturación de la academia desde el año 3 hasta el 10\n💰 * 24% de los beneficios de la academia desde el año 3 hasta el 10\n* Previsión de retorno al fan : 225% -275% (10 años)\n* ¡¡Las futuras estrellas del baloncesto están aquí !!'
        },
        epfc: {
          title: 'Llevemos al Europa Point a la UEFA!!!!',
          description: 'Accede al 20% del dinero de los premios de Liga de Campeones o Europa league y al 20% de los ingresos por derechos de traspasos de jugadores. ¡Grandes posibilidades de clasificarse para la UEFA! ⚽'
        },
        vega: {
          title: 'David Vega, Futuro campeón de tenis',
          description: 'Accede al 18 % de los premios ATP  desde Enero de 2021 a Diciembre de 2030. ¡¡Multiplica tu apoyo por 5!!'
        }
      }
    },
    created () {
      this.locale = this.$i18n.locale;
    },
    computed: {
      ...mapGetters({
        user: 'users/user'
      }),
      isLogged () {
        return !!this.user
      },
      progress () {
        if (!!this.campaign.token) {
          return Math.round(this.campaign.token.progression * 100)
        }
        return 0
      },
          goToLogin() {
      router.push({
        name: 'login'
      })
    },
      countryFlag () {
        try {
          return require(`../../assets/img/flags/${this.campaign.country.toLowerCase()}.png`)
        } catch(error) {
          return null
        }
      },
    },
    methods: {
      setFollowingCampaign() {
        this.campaign.following = !this.campaign.following;
        this.$store.dispatch('campaigns/follow', this.campaign.id).catch(error => {
          console.log(error)
        })
      },
      goToInvest (campaign) {
        router.push({
          name: 'campaign.details',
          params: {campaignId: campaign.id}
        })
      },
      showMore() {
        this.isExtended = !this.isExtended;
      },
      showMoreMsg() {
        return this.isExtended ? this.$tc("message.showLess") : this.$tc("message.showMore");
      },
      getDescription(description) {
        return this.isExtended ? description : (description.length > 50 ? description.substring(0,50)+' ...' : description);
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import '../../scss/variables.scss';

  .el-card {
    border-radius: 8px;
    //height: 470px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    margin-bottom: 35px;

    &:hover {
      box-shadow: 0 5px 16px 0 rgba(0, 0, 0, 0.2);
    }

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
  }

  .campaign-nameBlock {
    padding: 25px 20px 15px 20px;
    border-bottom: 1px solid #f0f0f0;
    min-height: 170px;
  }

  .campaign-progress {
    padding: 12px 20px 12px 20px;
    border-bottom: 1px solid #f0f0f0;
  }

  .campaign-footer {
    padding: 10px 20px 10px 20px;
    min-height: 80px;
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

.buy-tokens {
  margin-right: 15px;
}
</style>
