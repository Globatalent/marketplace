<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Handle form data and send it to the backend
      -->
    <div class="athleteProfileEdit">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" :md="24" :lg="6" :xl="4" class="text-center">
          <h2>{{ $t("message.AthleteProfileEditPage") }}</h2>
        </el-col>
      </el-row>
      <el-form ref="form">
        <el-row justify="center" :gutter="20">
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item required v-bind:label="$t('message.Password')">
              <el-input v-bind:placeholder="$t('message.Password')" type="password" v-model="form.password"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$t('message.RepeatPassword')">
              <el-input v-bind:placeholder="$t('message.RepeatPassword')" type="password" v-model="form.repeatPassword"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$t('message.FirstName')">
              <el-input v-bind:placeholder="$t('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$t('message.LastName')">
              <el-input v-bind:placeholder="$t('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item required v-bind:label="$t('message.Country')">
              <el-input v-bind:placeholder="$t('message.Country')" type="text" v-model="form.country"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$t('message.Date')">
              <el-date-picker type="date" v-bind:placeholder="$t('message.PickADate')" style="width: 100%;" v-model="form.date"></el-date-picker>
            </el-form-item>
            <el-form-item required v-bind:label="$t('message.Sport')">
              <el-input v-bind:placeholder="$t('message.Sport')" type="text" v-model="form.sport"></el-input>
            </el-form-item>
            <el-form-item v-bind:label="$t('message.Sex')" class="text-left sexFormElement">
              <el-radio-group>
                <el-radio label="male" v-model="form.sex">{{ $t("message.Male") }}</el-radio>
                <el-radio label="female" v-model="form.sex">{{ $t("message.Female") }}</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row type="flex" justify="left" :gutter="20" v-for="(link, index) in links" :key="index">
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
          <el-form-item required v-bind:label="$t('message.LinkTitle')+' '+(index+1)">
            <el-input v-bind:placeholder="$t('message.LinkTitle')" type="text" v-model="link.linkTitle"></el-input>
          </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="11" :md="11" class="text-center">
          <el-form-item required v-bind:label="$t('message.Link')+' '+(index+1)">
            <el-input v-bind:placeholder="$t('message.Link')" type="text" v-model="link.link"></el-input>
          </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="1" :md="1" class="text-center removeButtonCol">
            <div @click="deleteRow(index)" class="circleButton">
              <icon name="minus-circle" class="addButtonCircle" scale="2" ></icon>
            </div>
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" :gutter="20">
          <el-col :xs="24" class="text-center">
            <el-button type="primary" class="is-uppercase" @click="addRow">{{ $t("message.addLink") }}</el-button>
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" :gutter="20">
          <el-col :xs="24" :sm="18" :md="18" class="text-center">
            <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" :gutter="20">
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item class="text-center">
              <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $t("message.Save") }}</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>
  </gb-base-layout>
</template>

<script>
import BaseLayout from '@/layout/BaseLayout.vue'
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

export default {
  name: 'AthleteProfile',
  components: {
    'gb-base-layout': BaseLayout,
    'vueDropzone': vue2Dropzone
  },
  data() {
    return {
      errorMessage: '',
      form: {
        password: '123456',
        repeatPassword: '123456',
        firstName: 'Jon',
        lastName: 'Snow',
        country: 'Winterfell',
        date: '01/01/2000',
        sport: 'destroy white walkers',
        sex: 'male'
      },
      links: [{}],
      /*
      TODO @victor:
      vue-dropzone Docs  https://rowanwins.github.io/vue-dropzone/docs/dist/#/manual
      - Send images to the backend
      - Remove images action
      */
      dropzoneOptions: {
          url: 'https://httpbin.org/post',
          thumbnailWidth: 150,
          maxFilesize: 0.5,
          headers: { "My-Awesome-Header": "header value" }
      }
    }
  },
  methods: {
    onSubmit(evt) {
      evt.preventDefault()
      const dataForm = Object.assign({}, this.form)
      this.saveUserProfile(dataForm)
    },
    saveUserProfile(data) {
      console.log('TODO @victor: Save athlete profile ...', this.form)
    },
    addRow() {
      this.links.push({
        linkTitle: '',
        link: ''
      })
    },
    deleteRow(index) {
      this.links.splice(index,1)
    }
  }
}
</script>

<style scoped>
</style>
