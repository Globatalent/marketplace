<template>
  <gb-base-layout>
    <div v-if="!!campaign.isDraft">
      <div class="is-padding-boxed">
        <el-row>
          <el-col :xs="24">
        <div class="beginBlock text-center">
          <h4 class="beginBlock-subTitle" v-html="$t('message.campaignDraft')"></h4>
        </div>
      </el-col>
        </el-row>
      </div>  
    </div>
    <div v-else>
      <div class="is-padding-boxed">
        <el-row>
          <el-col>
            <el-breadcrumb separator=">" class="breadcrumbCampaignDetail">
              <el-breadcrumb-item :to="{ path: '/' }">Sports</el-breadcrumb-item>
              <el-breadcrumb-item><a href="/">{{!!campaign.sport ? campaign.sport.name : ''}}</a></el-breadcrumb-item>
            </el-breadcrumb>
          </el-col>
        </el-row>
      </div>
      <div class="campaignDetails-detailBox" v-if="campaign">
      <modal name="payment" height="auto" adaptive="true" scrollable="true">
      <header>
        <h2 class="text-center">
          How many tokens do you want to buy?
        </h2>
      </header>
      <div class="payInfo">
        <div>
        <span v-if="readyToPay" class="is-bold">Amount to buy</span>
        <vue-numeric class="autonumeric" v-if="readyToPay" read-only="true" :currency="token.code" separator="," v-model.number="pledged" v-bind:minus="false"></vue-numeric>
        <vue-numeric class="autonumeric" v-else :currency="token.code" separator="," :min="minimumPledge" :max="token.remaining" v-model.number="pledged" v-bind:minus="false"></vue-numeric>
        </div>
      <ul>
        <li>
          <span class="is-bold">{{token.code}} price per unit:</span> {{token.unitPrice}}$
        </li>
        <li>
          <span class="is-bold">Fees:</span>
            <ul>
              <li style="margin-left: 1rem">
                With Credit Card or Paypal: {{(((pledged * token.unitPrice * paymentFee) + 0.3)/ (1-paymentFee)).toFixed(2)}}$
              </li>
              <li style="margin-left: 1rem">
                With BTC/ETH: 0$
              </li>
            </ul>
        </li>
        <li>
          <span class="is-bold">Total to pay:</span>
            <ul>
              <li style="margin-left: 1rem">
                With Credit Card or Paypal: ${{ ((pledged * token.unitPrice + 0.3) / (1 - paymentFee)).toFixed(2) }} USD
              </li>
              <li style="margin-left: 1rem">
                With BTC/ETH: ${{(pledged * token.unitPrice).toFixed(2)}} USD
              </li>
            </ul>
        </li>
        <!-- <li>
          <span class="is-bold">Estimated date of release:</span> {{campaign.finished}}
        </li> -->
      </ul>
      </div>
      <div class="payFooter">
      <button class="crypto-link" v-if="readyToPay === false" v-on:click="payment(campaign.title,campaign.description, token.id, pledged,((pledged * token.unitPrice + 0.3) / (1 - paymentFee)).toFixed(2), pledged * token.unitPrice )">Buy {{token.code}}</button>
      </div>
      <div v-show="readyToPay" class="payment__parent">
        <div class="payment__container">
          <div id="paypal-button-container"></div>
          <div style="margin-top: 0.3rem">
            <a class="crypto-link" :href="coinbaseCheckoutURL" target="_blank"> Coinbase Commerce (BTC/ETH)</a>
          </div>
        </div>
      </div>
    </modal>
        <div class="is-padding-boxed">
          <el-row :gutter="40">
            <el-col :xs="24" :md="16" class="campaignDetails-col">
              <div class="campaignDetails-title">
                <h1 class="campaign-name">{{campaign.title}}</h1>
                <img :src="countryFlag" alt="" class="image campaign-flag" v-if="campaign.country">
                <div class="campaign-sport" :style="`background-color:#${campaign.sport.color}`" v-if="campaign.sport">
                  {{!!campaign.sport ? campaign.sport.name : ''}}
                </div>
                <div class="campaignDetails-timeRemaining">
                  <i class="el-icon-time"></i>
                  <span v-if="hasStarted"
                        class="campaignDetails-timeRemaining-text">{{campaign.remaining}} {{$tc('message.DaysLeft')}}</span>
                  <span v-else
                        class="campaignDetails-timeRemaining-text is-uppercase">{{$tc('message.ComingSoon')}}</span>
                </div>

              </div>
              <el-carousel :interval="4000" trigger="click" height="400px" indicator-position="outside" v-if="campaign">
                <el-carousel-item v-for="(picture, index) in carouselImages" :key="index">
                  <img :src="picture" alt="">
                </el-carousel-item>
              </el-carousel>
            </el-col>
            <el-col :xs="24" :md="8" class="campaignDetails-col">
              <div class="campaignDetails-collected"><span
                class="campaignDetails-collected-currency">$</span> {{((token.amount - token.remaining) * token.unitPrice).toFixed(2)}} <span
                class="campaignDetails-collected-text">{{$tc('message.Raised')}}</span>
              </div>
              <div class="progress m-b-15 clearfix">
                <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694"
                            :percentage="progress" v-if="progress < 100"></el-progress>
                <el-progress :text-inside="false" :show-text="false" :stroke-width="7" color="#32c694"
                            :percentage="progress" status="success" v-if="progress >= 100"></el-progress>
              </div>
              <div class="campaignDetails-invest"> {{campaign.title}}</div>
              <p class="campaignDetails-description">{{campaign.description}}</p>
              <div class="campaignDetails-fundingDetails">
                <div class="campaignDetails-fundingDetails-numbers">
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">{{ $tc('message.Funding')}}: </span>
                    <span
                      class="campaignDetails-fundingDetails-numbers-row-number"> {{ $n(campaign.funds, 'currency') }}</span>
                  </div>
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">1 {{ !!campaign.token ? campaign.token.code : '' }} token = </span>
                    <span class="campaignDetails-fundingDetails-numbers-row-number">{{ $n(!!campaign.token ? campaign.token.unitPrice: 0, 'currency') }}</span>
                  </div>
                  <div class="campaignDetails-fundingDetails-numbers-row">
                    <span class="campaignDetails-fundingDetails-numbers-row-title">{{$tc('message.SoftCapt')}}: </span>
                    <span
                      class="campaignDetails-fundingDetails-numbers-row-number"> {{ $n(campaign.softCap, 'currency') }}</span>
                  </div>
                </div>
                <div class="campaignDetails-fundingDetails-rating">
                  <div class="campaignDetails-fundingDetails-rating-experts"><span
                    class="is-marked is-mark-down">73</span><span
                    class="campaignDetails-fundingDetails-rating-experts-text"> {{$tc('message.ExpertsRating')}}</span>
                  </div>
                  <star-rating :rating="campaign.rating" inline read-only :show-rating="false" :star-size="16"
                              :padding="1" :round-start-rating="false" active-color="#419ce1"></star-rating>
                </div>
              </div>
              <template v-if="hasStarted">
                <el-button type="primary" class="is-full-width buyTokensButton" size="big" @click="show('payment')" v-if="isVerified">
                  {{$tc('message.BuyTokens')}}
                </el-button>
                <el-button type="primary" class="is-full-width buyTokensButton" v-html="$tc('message.BuyTokens')" @click="goToLogin(campaign)" size="big" v-else>
                </el-button>
              </template>
              <el-button type="primary" class="is-full-width buyTokensButton" disabled size="big" @click="goToInvest(campaign)" v-else>
                {{$tc('message.ComingSoon')}}
              </el-button>
              <div class="campaignDetails-favoriteSocial">
                <div class="favoriteLink" v-if="campaign.following" type="primary" @click="setFollowingCampaign()">
                  <i class="fas fa-heart"></i> {{$tc('message.Favorite')}}
                </div>
                <div class="favoriteLink" v-else @click="setFollowingCampaign()">
                  <i class="far fa-heart"></i> {{$tc('message.Favorite')}}
                </div>
                <div class="socialLinksDetail">
                  <social-sharing :url="addSharingUrl"
                      :title="addSharingTitle"
                      :description="addSharingDescription"
                      quote=""
                      hashtags="globatalent"
                      twitter-user="globatalent"
                      inline-template>
                    <div>
                        <network network="email">
                            <i class="fa fa-envelope"></i>
                        </network>
                        <network network="facebook">
                          <i class="fab fa-facebook"></i>
                        </network>
                        <network network="linkedin">
                          <i class="fab fa-linkedin"></i>
                        </network>
                        <network network="twitter">
                          <i class="fab fa-twitter"></i>
                        </network>
                    </div>
                  </social-sharing>
                </div>
              </div>
            </el-col>
          </el-row>
        </div>
      </div>
      <div class="campaignDetails-infoContainer is-padding-boxed">
        <vue-tabs>
          <v-tab title="Campaign insights">
        <div class="campaignDetails-infoContainer-data">
          <ul class="campaignDetails-infoContainer-data-miniMenu">
            <li class="campaignDetails-infoContainer-data-miniMenu-item" v-if="campaign.description">
              <a href="#" v-scroll-to="'#storySection'">
                <span class="menuLine"></span>
                <span class="campaignDetails-infoContainer-data-miniMenu-item-text">{{ $tc('message.Story') }}</span>
              </a>
            </li>
            <li class="campaignDetails-infoContainer-data-miniMenu-item" v-if="campaign.biography">
              <a href="#" v-scroll-to="'#biographySection'">
                <span class="menuLine"></span>
                <span class="campaignDetails-infoContainer-data-miniMenu-item-text">{{ $tc('message.Biography') }}</span>
              </a>
            <li class="campaignDetails-infoContainer-data-miniMenu-item" v-if="campaign.funds">
              <a href="#" v-scroll-to="'#fundsSection'">
                <span class="menuLine"></span>
                <span
                  class="campaignDetails-infoContainer-data-miniMenu-item-text">{{ $tc('message.FundsRequierement') }}</span>
              </a>
            </li>
            <li class="campaignDetails-infoContainer-data-miniMenu-item">
              <a href="#" v-scroll-to="'#buyTokenSection'">
                <span class="menuLine"></span>
                <span class="campaignDetails-infoContainer-data-miniMenu-item-text">{{$tc('message.BuyTokens')}}</span>
              </a>
            </li>
          </ul>
          <el-row :gutter="50">
            <el-col :xs="24" :md="8" class="campaignDetails-infoContainer-data-title">&nbsp;</el-col>
            <el-col :xs="24" :md="16" class="campaignDetails-infoContainer-data-text"><span
              class="campaignDetails-infoContainer-data-text-title">{{campaign.title}}</span></el-col>
          </el-row>

          <gb-campaign-info-row v-if="campaign.biography" id="storySection" :title="$tc('message.Story')">
            <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.description}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.description}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.description}}</pre>
            <pre v-else>{{campaign.description}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.ranking" :title="$tc('message.Ranking')">
            <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.ranking}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.ranking}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.ranking}}</pre>
            <pre v-else>{{campaign.ranking}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.biography" id="biographySection" :title="$tc('message.Biography')">
            <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.biography}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.biography}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.biography}}</pre>
            <pre v-else>{{campaign.biography}}</pre>
          </gb-campaign-info-row>
          <gb-campaign-info-row v-if="campaign.history" id="storySection" :title="$tc('message.History')">
            <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.history}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.history}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.history}}</pre>
            <pre v-else>{{campaign.history}}</pre>
          </gb-campaign-info-row>
          <gb-campaign-info-row v-if="campaign.pitchUrl" id="pitchUrlSection" :title="$tc('message.Video')">
            <div v-if="campaign.pitchUrl.includes('youtube')" class="videoWrapper">
              <iframe width="560" height="315" v-bind:src="'https://www.youtube.com/embed/' + campaign.pitchUrl.split('?').slice(-1)[0].split('&').filter(param => param.includes('v=')).slice(-1)[0].split('v=').slice(-1)[0]" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div v-if="campaign.pitchUrl.includes('vimeo')" class="videoWrapper">
              <iframe v-bind:src="'https://player.vimeo.com/video/' + campaign.pitchUrl.split('/').slice(-1)[0]" width="640" height="360" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
            </div>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.height" :title="$tc('message.Height')">
            {{campaign.height}} cm
          </gb-campaign-info-row>
          <gb-campaign-info-row v-if="campaign.weight" :title="$tc('message.Weight')">
            {{campaign.weight}} kg
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.club" :title="$tc('message.CurrentClub')">
            {{campaign.club}}
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.coach" :title="$tc('message.CurrentCoach')">
            {{campaign.coach}}
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.funds" id="fundsSection" :title="$tc('message.FundsRequierement')">
            <div class="fundsQty"><span class="fundsQty-currency">$</span>{{ $n(campaign.funds) }}</div>
            {{ $tc('message.LookingToRaise') }}
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.achievements" :title="$tc('message.Achievements')">
                        <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.achievements}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.achievements}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.achievements}}</pre>
            <pre v-else>{{campaign.achievements}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.expected" id="expectedSection"
                                :title="$tc('message.ExpectedSportAchievements')">
            <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.expected}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.expected}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.expected}}</pre>
            <pre v-else>{{campaign.expected}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.players" id="playersSection"
                                :title="$tc('message.Players')">
                        <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.players}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.players}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.players}}</pre>
            <pre v-else>{{campaign.players}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.use" id="useSection" :title="$tc('message.HowYouWillUse')">
                        <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.use}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.use}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.use}}</pre>
            <pre v-else>{{campaign.use}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="campaign.giveBack" id="giveBackSection" :title="$tc('message.WhatWillYou')">
                        <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.giveBack}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.giveBack}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.giveBack}}</pre>
            <pre v-else>{{campaign.giveBack}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="!!campaign.revenues && campaign.revenues.length > 0" id="revenueSection"
                                :title="$tc('message.Revenue3years')">
            <div class="incomeRow" v-for="item in campaign.revenues" :key="item.id">
              {{item.year}} - {{item.currencySymbol}} <span class="is-bold">{{$n(item.amount)}}</span>
            </div>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="!!campaign.incomes && campaign.incomes.length > 0" id="incomeForecastSection"
                                :title="$tc('message.IncomeForecastFor5')">
            <div class="incomeRow" v-for="item in campaign.incomes" :key="item.id">
              {{item.year}} - {{item.currencySymbol}} <span class="is-bold">{{$n(item.amount)}}</span>
            </div>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="!!campaign.examples && campaign.examples.length > 0" id="examplesSection"
                                :title="$tc('message.ExamplesIncomeSimilar')">
                        <pre v-if="campaign.id == 5 && locale == 'es-ES'">{{epfc.examples}}</pre>
            <pre v-else-if="campaign.id == 4 && locale == 'es-ES'">{{zentro.examples}}</pre>
            <pre v-else-if="campaign.id == 126 && locale == 'es-ES'">{{vega.examples}}</pre>
            <pre v-else>{{campaign.examples}}</pre>
          </gb-campaign-info-row>

          <gb-campaign-info-row v-if="!!campaign.recommendations && campaign.recommendations.length > 0"
                                id="recommendationsSection"
                                :title="$tc('message.Recommendations')">
            <el-row v-for="recommendation in campaign.recommendations" :key="recommendation.id">
              <el-col>
                <video v-if="recommendation.file.includes('mp4')" width="100%" controls>
                  <source :src="recommendation.file" type="video/mp4">
                </video>
                <a v-else :href="recommendation.file" target="_blank"><i class="el-icon-document"></i> {{ $tc('message.Download')
                  }}</a>
              </el-col>
            </el-row>
          </gb-campaign-info-row>


          <el-row :gutter="50">
            <el-col :xs="24" :md="8" class="campaignDetails-infoContainer-data-title text-right">&nbsp;</el-col>
            <el-col :xs="24" :md="16" id="buyTokenSection"
                    class="campaignDetails-infoContainer-data-text is-last-block">
            <template v-if="hasStarted">
              <el-button type="primary" class="is-full-width buyTokensButton" size="big" @click="show('payment')" v-if="isVerified">
                {{$tc('message.BuyTokens')}}
              </el-button>
              <el-button type="primary" class="is-full-width buyTokensButton" size="big" v-else>
                Verify your account
              </el-button>
            </template>
            <el-button type="primary" class="is-full-width buyTokensButton" disabled size="big" @click="goToInvest(campaign)" v-else>
              {{$tc('message.ComingSoon')}}
            </el-button>
              <div class="campaignDetails-infoContainer-campaignCopyright">
                <img src="~@/assets/img/logo-only.png" alt=""
                    class="campaignDetails-infoContainer-campaignCopyright-img">
                <div class="campaignDetails-infoContainer-campaignCopyright-text">{{ $tc('message.PlayerPoweredBy') }}
                  <span class="campaignDetails-infoContainer-campaignCopyright-text-name">Globatalent</span></div>
              </div>
            </el-col>
          </el-row>
        </div>
          </v-tab>
          <v-tab title="Social Feed">
            <div class="campaignDetails-infoContainer-data" v-if="twitterUrl != '' ">
              <div style="max-width: 300px">
              <Timeline :id="twitterUrl" :sourceType="'profile'" :options="{ tweetLimit: '5'}"/>
              </div>
            </div>
            <div class="campaignDetails-infoContainer-data" v-else>
              No news avaliable!!
            </div>
          </v-tab>
        </vue-tabs>
      </div>
    </div>
  </gb-base-layout>
</template>

<script>
  import Vue from 'vue'
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
  import router from '@/router.js'
  import StarRating from 'vue-star-rating'
  import CampaignInfoRow from '@/campaigns/components/CampaignInfoRow.vue'
  import {VueTabs, VTab} from 'vue-nav-tabs'
  import 'vue-nav-tabs/themes/vue-tabs.css'
  import { Timeline } from 'vue-tweet-embed'
  import VueNumeric from 'vue-numeric'

  Vue.use(window["vue-js-modal"].default); 
  // Vue.use(VueNumeric);
  
  export default {
    name: 'CampaignDetails',
    components: {
       VueTabs,
       VTab,
      'gb-base-layout': BaseLayout,
      'gb-campaign-info-row': CampaignInfoRow,
      StarRating,
      Timeline,
      VueNumeric
    },
    data () {
      return {
        token: {},
        pictures: [],
        redirecting: false,
        paymentFee: 0.054,
        pledged: 0,
        minimumPledge: 1,
        readyToPay: false,
        coinbaseCheckoutURL: '',
        urlCampaing: '',
        titleCampaing: '',
        descriptionCampaing: '',
        waiting: false,
        locale: '',
        epfc: {
          description: 'test'
        },
        zentro: {

        },
        vega: {
          description: "Accede al 18 % de los premios ATP  desde Enero de 2021 a Diciembre de 2030. ¡¡Multiplica tu apoyo por 5!!",
          ranking: "116 ATP Dobles",
          giveBack:'David está dispuesto a ofrecer el 18% de sus ingresos de "premio de ATP" desde el 1 de enero de 2021 hasta diciembre de 2030.\n\n🔰1.Porcentaje de ingresos💰:\n✔ Reciba el 18% de sus ganancias en dinero del Premio ATP. (que se publican en ATP.COM)\n\n🔰2. Otros beneficios🎁:\n✔ Participa en un sorteo anual para 10 clases magistrales con él en España.\n✔ Participa en un sorteo de un día con David. Esto incluye estar con él durante 3 días para seguirlo día a día. Esto incluye el transporte interno y un regalo de bienvenida.\n✔ Sorteo de dos entradas VIP por año en un torneo ATP por definir.\n\n🔰3. Duración de los derechos 📅\n✔ Desde el 1 de enero de 2021 hasta diciembre de 2030.\n\n📝Notas:\n✔  9,000 tokens\n✔ Precio por token 20 USD\n\nEntonces, si David logra sus objetivos además de ayudar a un joven talento, los fans que compren su token arecibirán una ganancia.\n\nSi David genera 4M en 10 años, significa que se distribuirán 800,000 USD y por cada token de David comprado, se recibirá un total de $ 106.60, que es un beneficio de más de 5 veces lo que se aportó. Por cada 1 USD  aportado recibirás un poco más de 5 USD de vuelta.\n\nEn todo momento, los titulares de los tokens  de David pueden vender sus tokens en el Exchange de GBT a otra persona interesada en comprar.\n\nEl valor del Token aumentará o disminuirá dependiendo del rendimiento del atleta, pero siempre mantendrá los derechos establecidos.\n\nAl final del primer año, si el atleta ha logrado más del 89% de los objetivos, recibirá la cantidad liberada del segundo año. Si no logran sus objetivos, los poseedores de tokens votarán si desean continuar o no ,necesitan una mayoría del 51% y el dinero depositado en la cuenta continuará en depósito y luego se transferirá a David. De lo contrario, los poseedores de tokens de David serán reembolsados.',
          expected: "🏆 - 2019 top 100 ATP dobles\n🏆 - 2020 top 80 ATP dobles\n🏆 - 2021 (Enero) - 2030 (Diciembre) Alcanzar entre el top 50 y 1 del ranking de dobles ATP",
          use: "Para este proceso de 3 años, David necesita 180,000 USD para cubrir los gastos de su entrenador de tenis, así como el equipo de profesionales y sus gastos de viaje. La financiación se entregará en 3 años.",
          achievements: "David ha alcanzado en el pasado los siguientes logros:\n🏆 -2018 doubles champion Challenger Blois, Marburg, Biella y Barcelona. 111 ATP dobles.\n🏆 -2017 Finalista dobles Challenger Segovia and Sevilla. Campeóndobles 6 Futures ITF. 175 ATP dobles\n🏆 -2016 Campeón dobles 7 Futures ITF. 255 ATP dobles\n🏆 -2015 Campeón dobles 2 Futures ITF, 510 ATP dobles",
          biography: "David es un tenista de 24 años que tiene una gran proyección en la modalidad de dobles. Necesita continuar con su dedicación y entrenamiento en un 150% para lograr sus objetivos a medio plazo (en 2 años) para alcanzar el top 50 en el mundo en dobles ATP y a largo plazo para situarse en  el top 10 en el mundo en dobles ATP.\nPara lograr sus objetivos, necesita continuar con el trabajo integral que ha estado desarrollando durante los últimos 6 años junto con su Entrenador de tenis, Toni Colom y su equipo de profesionales a través de Passion Talent Group",
          examples: "Estos son los diferentes  niveles de ingresos que un jugador de dobles de tenis puede obtener en función de su ranking:\n💰 $100,000 en top 50\n💰 $150,000 en top 40\n💰 $300,000 en top 30\n💰 $500,000 en top 20\n💰 $1,000,000 en top 10"
        }
      }
    },
    computed: {
      ...mapGetters({
        campaign: 'campaigns/campaign',
        user: 'users/user'
      }),
      progress () {
        if (!!this.token) {
          return Math.round(this.token.progression * 100)
        }
        return 0
      },
      hasStarted () {
        return this.campaign.started < new Date()
      },
      addSharingUrl() {
        return 'https://market.globatalent.com' + this.$route.fullPath
      },
      addSharingTitle() {
        return this.campaign.title
      },
      addSharingDescription() {
        return this.campaign.description
      },
      isVerified () {
        if (!!this.user) {
          return true
        }
        else {
          return false
        }
      },
      twitterUrl () {
        this.$forceUpdate();
        return (
          this.campaign.links != undefined && 
          this.campaign.links.filter(site => site.network == 'twitter') != undefined && 
          this.campaign.links.filter(site => site.network == 'twitter')[0] != undefined && 
          this.campaign.links.filter(site => site.network == 'twitter')[0].url != undefined && 
          this.campaign.links.filter(site => site.network == 'twitter')[0].url.split('/')[3] != undefined
          ) ? this.campaign.links.filter(site => site.network == 'twitter')[0].url.split('/')[3].split('?')[0] : '';
      },
      countryFlag () {
        try {
          return require(`../../assets/img/flags/${this.campaign.country.toLowerCase()}.png`)
        } catch(error) {
          return null
        }
      },
      carouselImages () {
        let initialImages = [this.campaign.image]
        if (this.campaign.pitchImage){
          initialImages.push(this.campaign.pitchImage)
        }
        return initialImages.concat(this.pictures)
      }
    },
    created () {
      const id = this.$route.params.campaignId
      this.locale = this.$i18n.locale;


      this.$store.dispatch('campaigns/fetch', id).then(() => {
        this.token = !!this.campaign.token ? this.campaign.token : {}
        this.campaign.incomes.sort((x, y) => x.year - y.year)
        this.campaign.revenues.sort((x, y) => x.year - y.year)
      })
      .catch(() => {
        router.push({
           name: 'not-found',
           params: {}
         })
      })
      this.$store.dispatch('campaigns/listPictures', {campaign: id}).then((pictures) => {
        this.pictures = pictures.map(picture => picture.image)
      })
    },
    methods: {
      show (id) {
        this.$modal.show(id)
      },
      setFollowingCampaign () {
        if (!!this.user) {
          this.campaign.following = !this.campaign.following
          this.$store
            .dispatch('campaigns/follow', this.campaign.id)
            .catch(error => {
              console.log(error)
            })
        }
      },
    goToLogin() {
      router.push({
        name: 'login'
      })
    },
    payment (name, description,token, amount, amountCredit, amountCrypto) {
      let sender = this.$store

      Vue.axios({
        method: 'post',
        url:'https://api.commerce.coinbase.com/charges',
        headers: {
          'Content-Type': 'application/json',
          'X-CC-Api-Key': '74038429-1376-4218-86b5-94c88c1f454f',
          'X-CC-Version': '2018-03-22'
        },
        data: {
          "name": name,
          "description": description,
          "local_price": {
            "amount": amountCrypto,
            "currency": "USD"
          },
        "metadata": {
         "customer_id": this.user.id,
       },
          "pricing_type": "fixed_price",
          "redirect_url": "https://market.globatalent.com",
          "cancel_url": "https://market.globatalent.com"
        }
      })
      .then(response => {
        this.coinbaseCheckoutURL = response.data.data.hosted_url
      })

      .then(this.readyToPay = true)
      paypal.Buttons({
          createOrder: function(data, actions) {
          // Set up the transaction
          return actions.order.create({
            purchase_units: [{
              amount: {
                value: amountCredit
              }
            }]
          });
          },
          onApprove: function(data, actions) {
            return actions.order
            .capture()
            .then(details => {
            const dataForm = {
              token: token,
              amount: amount,
            }
          sender
          .dispatch('tokens/purchase', dataForm)
          .then( purchase => {
          console.log(purchase)
          router.push({
            name: 'campaign.list'
          })
        })
        .catch(error => {})
            });
          }
        })
      .render('#paypal-button-container');
      
      },
      collected () {
        if (!!this.token) {
          return parseFloat(((this.token.amount - this.token.remaining) * this.token.unit_price).toFixed(2))
        }
        return 0
      },
      goToInvest (campaign) {
        console.log(this.token)
      },
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

  pre {
    font-family: inherit;
    font-size: inherit;
    white-space: pre-wrap;
  }

  a:hover {
    text-decoration: none;
  }

  .is-marked {
    display: inline-block;
    border-radius: 5px;
    background-color: $--pink;
    color: white;
    font-family: 'Aller Regular';
    font-size: 12px;
    padding: 0 3px;
  }

  .is-mark-down {
    &::after {
      content: '<';
      transform: rotate(-90deg);
      position: relative;
      display: inline-block;
      margin-left: 3px;
    }
  }

  .el-carousel__item {
    border-radius: 5px;

    img {
      object-fit: cover;
      height: 100%;
      object-position: top;
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
    padding-bottom: 50px;

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
    font-family: 'Aller Regular';
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
    font-family: 'Aller Bold';
  }

  .el-carousel__indicators {
    z-index: 300;
    float: right;
  }

  .campaignDetails-collected {
    font-size: 32px;
    line-height: 32px;
    color: $--black;
    font-family: 'Aller Bold';
    margin-bottom: 20px;
  }

  .campaignDetails-collected-currency,
  .campaignDetails-collected-text {
    font-size: 14px;
    font-family: 'Aller Regular';
    color: $--black;
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

  .campaignDetails-invest {
    font-size: 20px;
    font-family: 'Aller Regular';
    color: $--black;
    margin-bottom: 10px;
  }

  .campaignDetails-description {
    font-family: 'Aller Regular';
    color: $--grey-title;
    font-size: 14px;
  }

  .progress {
    margin-bottom: 50px;
  }

.videoWrapper {
	position: relative;
	padding-bottom: 56.25%; /* 16:9 */
	padding-top: 25px;
	height: 0;
}
.videoWrapper iframe {
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
}

  .campaignDetails-fundingDetails {
    border-top: 1px solid $--grey-detailCampaign-border;
    padding-top: 20px;
    font-family: 'Aller Regular';
    font-size: 0;
  }

  .campaignDetails-fundingDetails-numbers {
    display: inline-block;
    width: 48%;
    padding-right: 5px;
  }

  .campaignDetails-fundingDetails-numbers-row-title {
    font-size: 14px;
    color: $--grey-title;
  }

  .campaignDetails-fundingDetails-numbers-row-number {
    font-size: 14px;
    color: $--green-numbers;
  }

  .campaignDetails-fundingDetails-rating {
    display: inline-block;
    vertical-align: top;
    width: 52%;
    border: 1px solid $--grey-detailCampaign-border;
    background: white;
    padding: 5px 10px;
    border-radius: 5px;
    max-width: 180px;
  }

  .campaignDetails-fundingDetails-rating-experts {
    margin-bottom: 5px;
  }

  .campaignDetails-fundingDetails-rating-experts-text {
    color: $--pink;
    text-decoration: underline;
    font-size: 14px;
    font-family: 'Aller Regular';
    display: inline-block;
    margin-left: 10px;
  }

  .vue-star-rating {
    padding-left: 10px;
    margin-bottom: 5px;
  }

  .buyTokensButton {
    font-weight: bold;
    margin-top: 30px;
  }

  .campaignDetails-infoContainer {
    position: relative;
    top: -44px;
  }

  .campaignDetails-infoContainer-data {
    position: relative;
    padding: 40px 85px;
    background-color: white;
    border: 2px solid $--grey-detailCampaign-border;
    background-image: url('~@/assets/img/logo-translucent.png');
    background-repeat: no-repeat;
    background-position: right 50px bottom 50px;
    border-top: none;
  }

  .campaignDetails-infoContainer-data-text-title {
    font-size: 25px;
    font-family: 'Aller Regular';
    color: $--black;
    margin-bottom: 20px;
  }

  .campaignDetails-infoContainer-data-title {
    color: black;
    font-size: 20px;
    line-height: 25px;
    font-family: 'Aller Regular';
  }

  .campaignDetails-infoContainer-data-text {
    font-size: 14px;
    color: $--grey-text;
    font-family: 'Aller Regular';
    margin-bottom: 40px;

    .line {
      margin-top: 20px;
      display: block;
      width: 100%;
      max-width: 400px;
      border-top: 1px solid $--grey-detailCampaign-border;
    }

    &.is-last-block {
      max-width: 383px;
      text-align: center;
    }
  }

  .fundsQty {
    font-family: 'Aller Bold';
    font-size: 28px;
    line-height: 28px;
    color: $--green-numbers;
    display: inline-block;

    // .fundsQty-currency {
    //   font-size: 18px;
    //   position: relative;
    //   top: -13px;
    //   margin-right: 3px;
    // }
  }

  .campaignDetails-infoContainer-campaignCopyright {
    text-align: center;
    margin: 30px auto 0 auto;
  }

  .campaignDetails-infoContainer-campaignCopyright-img {
    max-width: 23px;
    display: inline-block;
    margin-right: 10px;
  }

  .campaignDetails-infoContainer-campaignCopyright-text {
    display: inline-block;
    color: black;
  }

  .campaignDetails-infoContainer-campaignCopyright-text-name {
    font-weight: bold;
    color: $--blue-dark;
  }

  .campaignDetails-infoContainer-logoTranslucent {
    position: absolute;
    bottom: 50px;
    right: 50px;
    max-width: 130px;
  }

  .campaignDetails-favoriteSocial {
    margin-top: 30px;
  }

  .favoriteLink {
    font-size: 14px;
    font-family: 'Aller Regular';
    cursor: pointer;
    display: inline-block;
    width: auto;
    margin-right: 20px;
  }

  .socialLinksDetail {
    display: inline-block;
    width: auto;

    a {
      color: $--grey-text;
    }
  }

  .socialLinks-icon {
    width: 20px;
    height: 20px;
    margin: 0 10px 0 0;
  }

  .campaignsFilter-item {
    position: relative;

    &.is-active {
      &::after {
        content: '';
        display: block;
        width: 70%;
        position: absolute;
        bottom: -32px;
        left: 15%;
        border: 1px solid $--blue;
      }
    }
  }

  .campaignDetails-infoContainer-data-miniMenu {
    width: 200px;
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

    .autonumeric {
    -webkit-appearance: none;
    background-color: #fff;
    background-image: none;
    border-radius: 4px;
    border: 1px solid #dcdfe6;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    color: #606266;
    display: inline-block;
    font-size: inherit;
    height: 40px;
    line-height: 40px;
    outline: none;
    padding: 0 15px;
    -webkit-transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    transition: border-color 0.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    max-width: 210px;
  }

  .payInfo {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
  }
  
  .payFooter {
    display: flex;
    justify-content: space-around;
    padding: 1rem;
  }

  .payment__parent {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .payment__container {
    padding: 2rem;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-content: space-around;
    align-items: top;
  }
  
  .crypto-link {
    color: white;

    border: 1px solid #5584b0;

    background-color: #5584b0;

    padding: 0.6rem;

    border-radius: 4px;

    font-weight: bold;
  }

  @media screen and (max-width: 768px) {

    .campaignDetails-infoContainer-data {
        background: none;
    }
  }
</style>
