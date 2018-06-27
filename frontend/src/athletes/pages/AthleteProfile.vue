<template>
  <gb-base-layout>
    <!--
      TODO @victor:
      - Handle form data and send it to the backend
      -->
    <div class="athleteProfileEdit">
      <el-row type="flex" justify="center">
        <el-col :xs="24" :sm="12" :md="24" :lg="6" :xl="4" class="text-center">
          <h2>{{ $tc("message.AthleteProfileEditPage") }}</h2>
        </el-col>
      </el-row>
      <el-form ref="form">
        <el-row justify="center" :gutter="20">
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item required v-bind:label="$tc('message.FirstName')">
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.first_name"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$tc('message.LastName')">
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.last_name"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$tc('message.Date')">
              <el-date-picker type="date" v-bind:placeholder="$tc('message.PickADate')" style="width: 100%;" v-model="form.date"></el-date-picker>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item required v-bind:label="$tc('message.Country')">
              <el-input v-bind:placeholder="$tc('message.Country')" type="text" v-model="form.country"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$tc('message.Sport')">
              <el-input v-bind:placeholder="$tc('message.Sport')" type="text" v-model="form.sport"></el-input>
            </el-form-item>
            <el-form-item v-bind:label="$tc('message.Sex')" class="text-left sexFormElement">
              <el-radio-group>
                <el-radio label="MALE" v-model="form.sex">{{ $tc("message.Male") }}</el-radio>
                <el-radio label="FEMALE" v-model="form.sex">{{ $tc("message.Female") }}</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
        <el-row type="flex" justify="left" :gutter="20" v-for="(link, index) in links" :key="index">
          <el-col :xs="24" :sm="12" :md="12" class="text-center">
            <el-form-item required v-bind:label="$tc('message.LinkTitle')+' '+(index+1)">
              <el-input v-bind:placeholder="$tc('message.LinkTitle')" type="text" v-model="link.name"></el-input>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="11" :md="11" class="text-center">
            <el-form-item required v-bind:label="$tc('message.Link')+' '+(index+1)">
              <el-input v-bind:placeholder="$tc('message.Link')" type="text" v-model="link.url"></el-input>
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="1" :md="1" class="text-center removeButtonCol">
            <div @click="deleteRow(index)" class="circleButton">
              <i class="fa fa-minus-circle addButtonCircle"></i>
            </div>
          </el-col>
        </el-row>
        <el-row type="flex" justify="center" :gutter="20">
          <el-col :xs="24" class="text-center">
            <el-button type="primary" class="is-uppercase" @click="addRow">{{ $tc("message.addLink") }}</el-button>
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
              <el-button type="primary" class="is-uppercase" @click="onSubmit">{{ $tc("message.Save") }}</el-button>
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
    vueDropzone: vue2Dropzone
  },
  created() {
    this.axios
      .get('/api/v1/users/me/')
      .then(response => {
        console.log(response)
        this.form.first_name = response.data.athlete.first_name
        this.form.last_name = response.data.athlete.last_name
        this.form.country = response.data.athlete.country
        this.form.date = response.data.athlete.date_of_birth
        this.form.sport = response.data.athlete.sport
        this.form.sex = response.data.athlete.sex
        this.links = response.data.athlete.links
        this.pictures = response.data.athlete.pictures
      })
      .catch(error => {
        console.log(error)
      })
  },
  data() {
    return {
      errorMessage: '',
      form: {
        // password: '123456',
        // repeatPassword: '123456',
        // first_name: 'Jon',
        // last_name: 'Snow',
        // country: 'Winterfell',
        // date: '01/01/2000',
        // sport: 'destroy white walkers',
        // sex: 'male'
      },
      links: [{}],
      pictures: [{}],
      /*
      TODO @victor:
      vue-dropzone Docs  https://rowanwins.github.io/vue-dropzone/docs/dist/#/manual
      - Send images to the backend
      - Remove images action
      */
      dropzoneOptions: {
        url: '/api/v1/pictures/',
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: { 'Content-Type': 'multipart/form-data' }
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
      var testLink = {
        name: 'Twitter',
        url: 'http://twitter.com'
      }
      this.axios
        .post('/api/v1/link/', { body: testLink })
        .then(response => {
          console.log('Added link',response)
        })
        .catch(error => {
          console.log(error)
        })
    },
    addRow() {
      this.links.push({
        name: '',
        url: ''
      })
    },
    deleteRow(index) {
      this.links.splice(index, 1)
    }
  }
}
</script>

<style scoped>
</style>
