<template>
  <el-col :xs="24" class="formSteps-container">
    <div class="infoTag" v-if="campaign.isDraft">Draft Campaign</div>
    <el-breadcrumb separator=">">
      <el-breadcrumb-item :to="{ path: '/campaigns' }">Campaign</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/campaigns/create">Card campaign</a></el-breadcrumb-item>
    </el-breadcrumb>
    <div class="formSteps-actions">
      <el-button v-if="campaign.isDraft" type="danger" class="" @click.prevent="onDiscard()">{{ $tc("message.DiscardCampaign") }}</el-button>
      <el-button type="secondary" class="" @click.prevent="onSaveAndContinue()">{{ $tc("message.ReviewLaunch") }}</el-button>
    </div>
    <div class="formSteps">
      <h2 class="formSteps-title">{{ $tc('message.CardCampaign') }}</h2>
      <p class="formSteps-text">Make a good first impression: introduce your campaign objectives and entice people to
        learn more. This basic information will represent your campaign on your campaign page, on your campaign card,
        and in searches.</p>
      <el-form-item required :label="$tc('message.CampaignTitle')">
        <p class="formSteps-inputText">What is the title of you campaign?</p>
        <el-input v-bind:placeholder="$tc('message.EnterExcitingTitle')" type="text" v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.CampaignTagline')">
        <p class="formSteps-inputText">Provide a short description that best describes your campaign</p>
        <el-input v-bind:placeholder="$tc('message.ShortDescription')" type="text"
                  v-model="form.description"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.CampaignCardImage')">
        <p class="formSteps-inputText">Upload a square image that represents your campaign.<br/>
          640 x 640 recommended resolution, 220 x 220 minimum resolution.</p>



        <gb-image-upload field-name="image" :campaign-id="campaign.id" v-if="campaign" :image-url="form.image"
                         @image-changed="updateImage">
        </gb-image-upload>




        <!--<el-upload class="campaign-upload" drag :limit="1" :action="options.action" :headers="options.headers"-->
                   <!--:name="options.name" :http-request="options.httpRequest" list-type="picture-card" :multiple="false">-->
          <!--<i class="el-icon-upload" style="padding: 0"></i>-->
          <!--<div class="el-upload__text">Upload Image</div>-->
        <!--</el-upload>-->
      </el-form-item>
      <el-form-item required v-bind:label="$tc('message.Gender')" class="text-left sexFormElement"
                    v-if="form.kind==='athlete'">
        <el-radio-group v-model="form.gender">
          <el-radio label="male">{{ $tc('message.Male') }}</el-radio>
          <el-radio label="female">{{ $tc('message.Female') }}</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item required :label="$tc('message.Sport')">
        <p class="formSteps-inputText">Provide a short description that best describes your campaign to your
          audience.</p>
        <el-select v-model="form.sport" placeholder="Select">
          <el-option v-for="(sport, index) in sports" :key="index" :label="sport.name" :value="sport.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item required :label="$tc('message.Tags')">
        <p class="formSteps-inputText">Enter up to five keywords that best describe your campaign. These tags will help
          with organization and discoverability.</p>
        <el-tag :key="tag" v-for="tag in form.tags" closable :disable-transitions="false" @close="handleTagClose(tag)">
          {{tag}}
        </el-tag>
        <el-input class="input-new-tag" v-if="tagInputVisible" v-model="tagInput" ref="saveTagInput" size="mini"
                  @keyup.enter.native="handleTagInputConfirm" @blur="handleTagInputConfirm">
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showTagInput">Add +</el-button>
      </el-form-item>
      <el-form-item>
        <div class="formSteps-lineButton"></div>
        <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{
          $tc('message.SaveContinue') }}
        </el-button>
      </el-form-item>
    </div>
  </el-col>
</template>

<script>
  import Vue from 'vue'
  import { mapGetters } from 'vuex'
  import ajax from '@/base/helpers/ajax'
  import router from '@/router.js'
  import ImageUpload from '@/campaigns/components/ImageUpload.vue'

export default {
  name: 'CardCampaign',
    components: {
      'gb-image-upload': ImageUpload
    },
  data() {
    return {
      // Form
      form: {
        title: null,
        description: null,
        image: null,
        gender: null,
        sport: null,
        tags: []
      },
      // Tags
      tagInputVisible: false,
      tagInput: '',
      // Card Image
      options: {
        name: 'image',
        headers: {
          Authorization: this.$store.getters['auth/header'],
        },
        httpRequest: ajax,
        action: ''
      }
    }
  },
  computed: {
    ...mapGetters({
      campaign: 'campaigns/campaign',
      sports: 'campaigns/sports',
      user: 'users/user'
    })
  },
  created() {
    this.$store.commit('campaigns/sports', [])
    this.$store.dispatch('campaigns/sports')
    this.$store
      .dispatch('campaigns/fetch', this.$route.params.campaignId)
      .then(() => {
        if (!!this.campaign && !!this.campaign.id) {
          this.options.action = `${
            Vue.axios.defaults.baseURL
          }/api/v1/campaigns/${this.campaign.id}/`
          this.form = { ...this.campaign }
          if (!!this.form.sport) {
            this.form.sport = this.form.sport.id
          }
        }
      }).catch(()=> router.push({name: 'campaign.create'}))
  },
  methods: {
    handleTagClose(tag) {
      this.campaign.tags.splice(this.campaign.tags.indexOf(tag), 1)
    },
    showTagInput() {
      this.tagInputVisible = true
      this.$nextTick(_ => {
        this.$refs.saveTagInput.$refs.input.focus()
      })
    },
    handleTagInputConfirm() {
      let tagInput = this.tagInput
      if (tagInput) {
        this.campaign.tags.push(tagInput)
      }
      this.tagInputVisible = false
      this.tagInput = ''
    },
    onDiscard() {
      const payload = { id: this.campaign.id }
      this.$store.dispatch('campaigns/delete', payload).then( () => {
        router.push({name: 'campaign.create'})
      })
    },
    updateImage (fieldName, newURL) {
      this.form[fieldName] = newURL
    },
    onSaveAndContinue() {
      const payload = {
        id: this.campaign.id,
        title: this.form.title,
        description: this.form.description,
        gender: this.form.gender,
        sport: !!this.form.sport ? this.form.sport : null,
        tags: this.form.tags
      }
      this.$store.dispatch('campaigns/update', payload).then(() => {
        this.form = { ...this.campaign }
        router.push({
          name: 'campaign.edit',
          params: {
            campaignId: this.campaign.id,
            step: 'content'
          }
        })
      })
    }
  }
}
</script>

<style type="scss" scoped>
</style>
