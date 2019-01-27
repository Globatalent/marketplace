<template>
  <gb-base-layout>
    <div class="message-container">
      <h1 class="title">Success</h1>
      <p class="subtitle">Your campaign is now live!</p>
      <img src="@/assets/img/success.png" alt="" class="success-icon">
      <el-button type="success" class="button" @click="editCampaign()">Edit Campaign</el-button>
      <p class="bottom-links text-center">
        <router-link :to="{name: 'campaign.details', params: {campaignId: campaignId}}">Preview</router-link>
        <span class="m-l-15 m-r-15">|</span>
        <router-link :to="{name:'faq'}">{{ $tc('message.Faq') }}</router-link>
      </p>
    </div>
  </gb-base-layout>
</template>

<script>
  import BaseLayout from '@/layout/BaseLayout.vue'
  import { mapGetters } from 'vuex'
  import router from '@/router.js'
  import StarRating from 'vue-star-rating'

  export default {
    name: 'CampaignSuccess',
    props: ['campaignId'],
    components: {
      'gb-base-layout': BaseLayout,
      StarRating
    },
    methods: {
      editCampaign () {
        this.$router.push({
          name: 'campaign.edit',
          params: {
            campaignId: this.campaignId,
            step: 'card'
          }
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
  @import "@/scss/variables.scss";

  .message-container {
    max-width: 500px;
    border: 1px solid $--grey-border;
    border-radius: 10px;
    background: url("../../assets/img/background_success.png") top center no-repeat $--grey-detailCampaign-box;
    background-position-y: 30px;
    display: block;
    margin: 20px auto;
    padding: 20px;
    text-align: center;
    font-family: 'Aller', Arial, SansSerif;
  }

  .title {
    color: $--color-success;
    font-size: 3em;
    font-weight: 300;
    margin-top: 50px;
    line-height: 1.3;
  }

  .success-icon {
    width: 100%;
    height: auto;
    max-width: 130px;
    margin: 10px auto 30px;
  }

  .button {
    width: 200px;
    text-transform: capitalize;
    margin-bottom: 10px;
    font-size: 1em;
    font-weight: bold;
  }

  .bottom-links {
    margin-bottom: 20px;
    a {
      color: $--grey-text;
    }
  }
</style>
