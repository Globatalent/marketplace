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
              <el-input v-bind:placeholder="$tc('message.FirstName')" type="text" v-model="form.firstName"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$tc('message.LastName')">
              <el-input v-bind:placeholder="$tc('message.LastName')" type="text" v-model="form.lastName"></el-input>
            </el-form-item>
            <el-form-item required v-bind:label="$tc('message.Date')">
              <el-date-picker type="date" v-bind:placeholder="$tc('message.PickADate')" style="width: 100%;" v-model="form.birthDate"></el-date-picker>
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
                <el-radio label="male" v-model="form.sex">{{ $tc("message.Male") }}</el-radio>
                <el-radio label="female" v-model="form.sex">{{ $tc("message.Female") }}</el-radio>
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
import Vue from 'vue'
import BaseLayout from '@/layout/BaseLayout.vue'
import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import { mapGetters } from 'vuex'


export default {
  name: 'AthleteProfile',
  components: {
    'gb-base-layout': BaseLayout,
    vueDropzone: vue2Dropzone
  },
  computed: {
    ...mapGetters({
      user: 'users/user',
    }),
  },
  data() {
    return {
      errorMessage: '',
      form: {
      },
      links: [],
      linksToDelete: [],
      pictures: [],
      picturesToDelete: [],
      /*
      TODO @victor:
      vue-dropzone Docs  https://rowanwins.github.io/vue-dropzone/docs/dist/#/manual
      - Send images to the backend
      - Remove images action
      */
      dropzoneOptions: {
        url: `${Vue.axios.defaults.baseURL}/api/v1/pictures/`,
        paramName: 'image',
        maxFilesize: 2,
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: {
          'Authorization': this.$store.getters['auth/header']
        }
      }
    }
  },
  created() {
    this.$store.dispatch('users/fetchUser').then( () => {
      this.form = { ...this.user.athlete }
      this.links = this.user.athlete.links
      this.pictures = this.user.athlete.pictures
      if (this.links.length == 0 ) {
        this.addRow()
      }
      this.loadPictures()
    })
    .catch(error => {
      console.log(error)
    })
  },
  methods: {
    loadPictures() {
      this.pictures.forEach(picture => {
        const url = picture.image
        const name = url.substring(url.lastIndexOf('/') + 1);
        const file = { size: 123, name: name };
      this.$refs.myVueDropzone.manuallyAddFile(file, url);
      })
    },
    onSubmit(evt) {
      evt.preventDefault()
      const dataForm = Object.assign({}, this.form)
      this.saveUserProfile(dataForm)
    },
    saveUserProfile(data) {
      const linksToCreate = this.links.filter(link => !link.id)
      const linksToUpdate = this.links.filter(link => !!link.id)
      const payload = {
        linksToCreate: linksToCreate,
        linksToUpdate: linksToUpdate,
        linksToDelete: this.linksToDelete,
        ...data
      }
      this.$store.dispatch('athletes/update', data).then(response => {
        Promise.all(
          linksToCreate.map(link => {
            return this.$store.dispatch('athletes/createLink', link)
          }).concat(
            linksToUpdate.map(link => {
              return this.$store.dispatch('athletes/updateLink', link)
            })
          ).concat(
            this.linksToDelete.map(link => {
              return this.$store.dispatch('athletes/deleteLink', link)
            })
          ).then(() => {
            console.log("Links saved!")
          }).catch(() => {
            console.error("Error saving links!")
          })
        )
      }).catch(error => {

      })
    },
    addRow() {
      this.links.push({name: '', url: ''})
    },
    deleteRow(index) {
      const link = this.links[index]
      if (!!link.id) {
        this.linksToDelete.push(link)
      }
      this.links.splice(index, 1)
    }
  }
}
</script>

<style scoped>
</style>
