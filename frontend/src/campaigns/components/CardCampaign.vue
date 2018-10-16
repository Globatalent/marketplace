<template>
  <el-col :xs="24">
    <h2 class="form-lined-title text-center">{{ $tc("message.CardCampaign") }}</h2>
    <div class="form-lined">
      <el-form-item required :label="$tc('message.CampaignTitle')">
        <el-input v-bind:placeholder="$tc('message.EnterExcitingTitle')" type="text" v-model="form.title"></el-input>
      </el-form-item>
      <el-form-item required :label="$tc('message.CampaignTagline')">
        <el-input v-bind:placeholder="$tc('message.ShortDescription')" type="text" v-model="form.description"></el-input>
      </el-form-item>
      <el-form-item :label="$tc('message.CampaignCardImage')">
        <el-upload
          drag
          thumbnail-mode
          :limit="1"
          :action="options.action"
          :headers="options.headers"
          :name="options.name"
          :http-request="options.httpRequest"
          :file-list="!!form.image ? [{name: form.image.substring(form.image.lastIndexOf('/') + 1), url: form.image}] : []"
          >
          <i class="el-icon-upload" style="padding: 0"></i>
          <div class="el-upload__text">Upload Image</div>
        </el-upload>
      </el-form-item>
      <el-form-item v-bind:label="$tc('message.Gender')" class="text-left sexFormElement" v-if="form.kind==='athlete'">
        <el-radio-group>
          <el-radio label="male" v-model="form.gender">{{ $tc("message.Male") }}</el-radio>
          <el-radio label="female" v-model="form.gender">{{ $tc("message.Female") }}</el-radio>
        </el-radio-group>
      </el-form-item>
      <el-form-item :label="$tc('message.Sport')">
        <el-select v-model="form.sport" placeholder="Select">
          <el-option
            v-for="sport in sports"
            :key="sport.id"
            :label="sport.name"
            :value="sport.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item :label="$tc('message.Tags')">
        <el-tag
          :key="tag"
          v-for="tag in form.tags"
          closable
          :disable-transitions="false"
          @close="handleTagClose(tag)">
          {{tag}}
        </el-tag>
        <el-input
          class="input-new-tag"
          v-if="tagInputVisible"
          v-model="tagInput"
          ref="saveTagInput"
          size="mini"
          @keyup.enter.native="handleTagInputConfirm"
          @blur="handleTagInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small" @click="showTagInput">Add +</el-button>
      </el-form-item>
    </div>
    <el-form-item>
      <el-button type="primary" class="is-uppercase" @click.prevent="onSaveAndContinue()">{{ $tc("message.SaveContinute") }}</el-button>
    </el-form-item>
  </el-col>
</template>

<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'
import Campaign from '@/campaigns/models/Campaign'
import ajax from '@/base/helpers/ajax'
import router from '@/router.js'


export default {
  name: 'CardCampaign',
  components: {
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
        tags: [],
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
        action: "",
      },
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
    this.$store.dispatch('campaigns/sports')
    this.$store.dispatch('campaigns/fetch', this.$route.params.campaignId).then( () => {
      if (!!this.campaign && !!this.campaign.id) {
        this.options.action = `${Vue.axios.defaults.baseURL}/api/v1/campaigns/${this.campaign.id}/`
        this.form = { ... this.campaign }
      }
    })
  },
  methods: {
      handleTagClose(tag) {
        this.campaign.tags.splice(this.campaign.tags.indexOf(tag), 1);
      },
      showTagInput() {
        this.tagInputVisible = true;
        this.$nextTick(_ => {
          this.$refs.saveTagInput.$refs.input.focus();
        });
      },
      handleTagInputConfirm() {
        let tagInput = this.tagInput;
        if (tagInput) {
          this.campaign.tags.push(tagInput);
        }
        this.tagInputVisible = false;
        this.tagInput = '';
      },
      onSaveAndContinue() {
        const payload = {
          id: this.campaign.id,
          title: this.form.title,
          description: this.form.description,
          gender: this.form.gender,
          sport: this.form.sport.id,
          tags: this.form.tags,
        }
        this.$store.dispatch('campaigns/update', payload).then( () => {
          router.push({ name: 'campaign.edit', params: {
            campaignId: this.campaign.id ,
            step: 'content',
          }})
        })
      }
  }
}
</script>

<style type="scss" scoped>
</style>
